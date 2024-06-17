'''
Created on 09-Nov-2019

@author: anpradha

Problem Solution
1. The algorithm work by first creating a loop that will run n! times where n is the length of the string.
2. Each iteration of the loop prints the string and finds its next permutation to be printed in the next iteration.
3. The next higher permutation is found as follows.
4. If our sequence is called seq, then we find the smallest index p such that all elements in seq[p…end] are in descending order.
5. If seq[p…end] is the entire sequence, i.e. p == 0, then seq is the highest permutation. So we simply reverse the entire string to get the smallest permutation which we consider as the next permutation.
6. If p > 0, then we reverse seq[p…end].
7. Then we look for the smallest element in seq[p…end] that is greater than seq[p – 1] and swap its position with seq[p – 1].
8. This is then the next permutation.



https://www.sanfoundry.com/python-program-print-all-permutations-string-lexicographic-order-without-recursion/

'''

from math import factorial

 
def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)
 
    # there are going to be n! permutations where n = len(seq)
    for _ in range(factorial(len(seq))):
        # print permutation
        print(''.join(seq))
 
        '''find the smallest index p such that all elements in seq[p…end] are in decreasing order. 
                               or
           Find the rightmost character which is smaller than its next character. Let us call it 'first char    
           e.g let assume scenario ACB where C > B  , B is the next char                 
        '''
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p = p - 1
 
        '''So we simply reverse the entire  seq[p:] string to get the smallest permutation which we consider as the next permutation '''
        seq[p:] = reversed(seq[p:])
 
        if p > 0:
            '''
                Then we look for the smallest element in seq[p…end] that is greater than seq[p – 1] and swap its position with seq[p – 1].
                                            or
                Ceil of a character is the smallest character greater than seq[p]    
                e.g BAC where B > A , i.e p-1 > q                         
            '''
            q = p
            while seq[p - 1] > seq[q]:
                q = q + 1
 
            # swap seq[p - 1] and seq[q]
            seq[p - 1], seq[q] = seq[q], seq[p - 1]


if __name__ == '__main__':
    print_permutations_lexicographic_order("ABC")
