'''
Created on 18-Sep-2016

@author: anpradha
'''

from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
@tags("q")
@tags("r")
def get_text(name):
    """returns some text"""
    return "Hello " + name


@tags("r")
def get_text2(name):
    """returns some text"""
    return "Hello " + name


if __name__ == '__main__':
    print(get_text("Anil Kumar Padhan"))
    print(get_text2("Anil Kumar Padhan"))
        
