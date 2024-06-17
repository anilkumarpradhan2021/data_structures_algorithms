import logging
import inspect
import itertools
import collections

# BEGIN DEPRECATING CODE
import warnings
# END DEPRECATING CODE

import unittest

# module level logger
logger = logging.getLogger(__name__)

# named tuple used to store iteration information
Iteration = collections.namedtuple('Iteration', ['uid', 'parameters'])

class DefaultLooper(object):
    '''Default Loop Generation Class

    The default loop generation iterator that generates testable `Iterations`. 
        
        - provide new uids for each iteration
        - default uids to number generator
        - provide fixed argument/values input
        - provides kwargs argument/values input
        - auto-fills missing loop argument positions
        - last-minute generation of iteration (yield)

    Behaviors:

        - missing argument positions will be filled with filler, regardless of
          if it's kwargs mismatching or argvs mismatching
        - if user provided UIDs, then it doesn't matter how many argument 
          values are provided, the iterations end when we run out of uids
        - if using default uid generation, the loop ends when we exhaust all
          arguments

    Example
    -------
        >>> iterations = DefaultLooper(a = [1, 2, 3]
        >>> iterations = DefaultLooper(args = ['a'], argvs = ((1,), (2,), (3,)))
    '''

    def __init__(self, 
                 uids = None,
                 *,
                 loopee = None,
                 args = None,
                 argvs = None,
                 filler = None,
                 **kwargs):
        '''DefaultLooper __init__

        Instanciates the loop iterable. In typical user scripts, this API
        is instanciated when the module (script) is loaded. 

        Arguments
        ---------
            uids (iterable/callable): an iterable or callable returning a
                                      sequence of unique iteration UIDs. 
                                      Defaults to a counter starting from 1 and
                                      auto-increment by 1 per iteration.
            loopee (obj): object getting looped. used only to compute the loop
                          uid default prefix when uids str not provided. if not
                          provided, defaults to prefix "iteration"
            args (iterable/callable): a sequence (or callable returning a 
                                      sequence) of arguments for each iteration
            argvs (iterable/callable): a sequence (or callable returning a 
                                       sequence) of argument values for each 
                                       iteration, each matching in position to
                                       args above.
            filler (obj): a single object that is used to 'fill' missing 
                          argument value positions. Default to None
            kwargs (kwargs): any other key-iterable(callable iterable) argument
                             that is added to the list of argvs

        Examples
        --------
            # iteration with 2 arguments and 3 sets of iterations
            >>> DefaultLooper(args = ('a', 'b'), argvs = ((1,2), (2,3)))

            # iteration with 1 kwarg and 2 iterations
            >>> DefaultLooper(a = [1,2])

            # iteration with custom uids iterating 3 times
            >>> DefaultLooper(uids = ['a', 'b', 'c'])

        '''
        # check arguments
        if uids is args is argvs is None and not kwargs:
            raise TypeError("Must provide an argument to loop on.")

        # set defaults and store internally
        self.uids = uids or itertools.repeat(None)
        self.args = args or ()
        self.argvs = argvs or ()
        self.filler = filler
        self.kwargs = kwargs

        # compute prefix
        if loopee is not None:
            # get the function/class name as prefix
            self.prefix = getattr(loopee, '__name__', type(loopee).__name__)
        else:
            # default if loopee was not provided
            self.prefix = 'iteration'

    def __iter__(self):
        '''DefaultLooper iterator

        Generates each iteration when looped. This is purposely designed to be
        a generator, and all internals are iterators so that each iteration is
        only generated when it is called for, instead of pre-generating.


        See behavior section in DefaultLooper documentation.

        '''
        # expand all callables
        uids = self.uids() if callable(self.uids) else self.uids
        args = self.args() if callable(self.args) else self.args
        argvs = self.argvs() if callable(self.argvs) else self.argvs
        kwargs = {k: v() if callable(v) else v for k, v in self.kwargs.items()}

        # combine kwargs keys with args
        # (args is position sensitive)
        combined_args = list(args)
        combined_args.extend(kwargs.keys())

        # convert kwargs into their respective argvs
        # (vertical slicing, pad when necessary using fillvalue)
        # (maintain kwargs order)
        # handles conditions:
        #   - mismatch between kwargv length
        # eg:
        #       a = [1,  2,  3]
        #       b = [4,  5,  6,  7]
        #            |   |   |   |
        #          (1,4) | (3,6)
        #              (2,5)  (None,7)
        kwargvs = itertools.zip_longest(*kwargs.values(), 
                                        fillvalue = self.filler)
        # generate each iteration
        # each iteration eats away:
        #   - 1x uid
        #   - 1x argvs
        #   - 1x kwargs
        #
        # if the arguments provided are different between argvs and kwargvs
        # then pad them with fillers until we exhaust the loop
        for iter_uid, argv, kwargv in itertools.zip_longest(uids, 
                                                            argvs, 
                                                            kwargvs, 
                                                            fillvalue = ()):
            # typecast all to tuple
            argv = tuple(argv)
            kwargv = tuple(kwargv)

            if iter_uid == () or \
               (argv == kwargv == () and type(uids) is itertools.repeat): 
                # exit condition:
                #    - user supplied UIDs and it ran out
                #    - user didn't supply UID, and ran out of arguments
                break

            # pad argv with filler
            # handles condition:
            #   - when the # of argv in each argvs is not the same as args
            # eg:
            #   (1, 2) -> (1, 2, None) if filler was None and len(args) is 3
            argv += tuple(itertools.repeat(self.filler, len(args) - len(argv)))

            # pad kwargv with filler (same as argv)
            # handles condition:
            #   - when there's more argvs than kwargvs
            kwargv += tuple(itertools.repeat(self.filler, 
                                             len(kwargs.keys()) - len(kwargv)))

            # build the kwargs for this iteration
            parameters = dict(zip(combined_args, argv + kwargv))

            # generate uid
            if iter_uid is None:
                iter_uid = self.uid_generator(self.prefix, parameters)

            # give it up
            yield Iteration(uid = iter_uid, parameters = parameters)


    @staticmethod
    def uid_generator(prefix, parameters):
        '''Loop uid generator

        Default loop uid generator, used when a loop iteration uid was not given
        implicitly. The generated uid format is:

            <loopee name>[arg_a=value_a,arg_b=value_b,...]

        where the loopee name is the function/class name.

        Arguments
        ---------
            prefix (string): iteration uid prefix
            parameters (dict): parameters that generates the second uid portion

        Examples
        --------
            Tc_one[a=3]
                test[b=7] 
                test[b=8]
                test[b=9]
        '''
        kwarg_str = []

        for k in sorted(parameters.keys()):
            # callable params
            if callable(parameters[k]):
                kwarg_str.append("%s=%s()" % (str(k), parameters[k].__name__))
            else:
                # replace space with _
                value = '_'.join(str(parameters[k]).split())
                kwarg_str.append("%s=%s" % (str(k), value))

        return prefix + '[' + ','.join(kwarg_str) + ']'


class LoopDecorator(object):
    '''AEtest testable loop decorator

    Defines & uses the AEtest loopable protocol that enables testable (section,
    Testcase etc) looping. This API is the decorator called within the user
    script that marks the testable to be looped during execution.

    Note that this class is not used directly. Rather, users should be calling
    the @loop decorator instead (set below)

    Loop Protocol:

        - testables with attr `__loop__` (and is an iterable) is loopable
        - `__loop__` obj should return `Iteration` objects when iterated, 
          and contains:

            - uid: the uid of the loop iteration
            - kwargs: dict of key-value mapping that are called as funcargs for
                      the looping testable

    Example
    -------
        >>> @aetest.loop(uids = [1, 2])
        ... class Testcase(aetest.Testcase):
        ...     pass
        >>> @aetest.loop(loop_value = ['a', 'b', 'c'])
        ... class Testcase(aetest.Testcase):
        ...     pass

    '''

    def __init__(self, *args, generator = DefaultLooper, **kwargs):
        '''loop __init__

        Arguments
        ---------
            target (obj): target loopable testable
            generator (obj): loop iteration generator object, defaults to 
                             `DefaultLooper`. using this argument enables users
                             to supply a custom `Iteration` generator
            kwargs (kwargs): any arguments to be passed to the generator cls

        '''
        # BEGIN DEPRECATING CODE
        if 'id' in kwargs:
            warnings.warn(message = "Starting v3.0.0, section.id is deprecated "
                                    "and replaced by section.uid. Please "
                                    "modify your scripts. This will be removed "
                                    "next release",
                          category = DeprecationWarning,
                          stacklevel = 3)
            kwargs['uid'] = kwargs.pop('id')
        # END DEPRECATING CODE

        # store until used in __call__
        self.args = args
        self.kwargs = kwargs
        self.generator = generator

    def __call__(self, target):
        '''loop __call__

        class __call__ is called when the testable is passed in as target during
        the last step of decoration

        Returns
        -------
            target, after adding `__loop__` object.

        '''

        # store this loop object into the loop target
        target.__loop__ = self.generator(loopee = target,
                                         *self.args, 
                                         **self.kwargs)

        # return the original target unchanged
        return target

    @classmethod
    def mark(cls, obj, *args, **kwargs):
        '''mark for loops

        classmethod of LoopDecorator. Used within testscript sections to enable 
        post-mortem looping, eg. to mark a testcase or a section that occurs
        after this current section for looping. 
        This is different from typical @loop decorator looking, in the sense 
        that it allows users to configure testcase/section looping dynamically.

        Example
        -------
            >>> class CommonSetup(aetest.CommonSetup):
            ...     @aetest.subsection
            ...     def subsection(self):
            ...         aetest.loop.mark(Testcase, uids = [1,2,3])
            ...
            >>> class Testcase(aetest.Testcase):
            ...     pass

        Arguments
        ---------
            obj (object): the object to be looped on
            args (list args): any argument to be passed to the loop generator
            kwargs (kwargs): any arguments to be passed to the generator cls

        Returns
        -------
            None
        '''

        # get the actual class function object
        # (since methods are immutable)
        if inspect.ismethod(obj):
            obj = obj.__func__

        cls(*args, **kwargs)(obj)


def loopable(obj):
    '''loopable

    determines whether a test object is loopable based on the aetest looping
    protocol.
    
    Arguments
    ---------
        obj (obj): any input object

    Returns
    -------
        True if object is loopable, False otherwise.
    '''

    return  isinstance(getattr(obj, '__loop__', None), collections.Iterable)


def get_iterations(obj):
    '''get_iterations

    returns an iterator/generator of test iterations currently defined for the
    given object. 
    
    Arguments
    ---------
        obj (obj): any input object that is loopable under the loop protocol

    Returns
    -------
        iterator/generator of iterations
    '''

    if not loopable(obj):
        raise TypeError("object '%s' is not loopable" % obj)
    
    return iter(obj.__loop__)


# lowercase Loop clas
# as this is the api user will use
# eg:
#   @loop(uids = [1,2,3])
#   def test(self): pass
loop = LoopDecorator

 
class FooTestCase(unittest.TestCase):
    @loop(value = 3)
    def test_testing(self, value):
        print("Hi")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 
  