'''
Created on 02-Sep-2016

@author: anpradha
gksfor
'''


def remove_adjacent_pair(string):
    a = list(string)
    print(a)
      
    i = 1
    while i < len(a) :
        if a[i] == a[i - 1]:
            a.pop(i - 1)
            a.pop(i - 1)
            i = i - 2
        i = i + 1    
    print(a)


def remove_all_adjacent(string):
    a = list(string)
    print("Before Remove : " , a)
      
    i = 1
    while i < len(a) :
        if a[i] == a[i - 1] and a[i] == a[i + 1]:
            a.pop(i - 1)
            a.pop(i - 1)
            a.pop(i - 1)
            i = i - 2
        elif a[i] == a[i - 1]:
            a.pop(i - 1)
            a.pop(i - 1)
            i = i - 2   
        i = i + 1    
    print("After Remove : " , a)


def remove_all_adjacent2(string):
    a = list(string)
    print("Before Remove : " , a)
    i = 0
    while i < len(a):

        j = i
        while j < len(a) - 1  and a[j] == a[j + 1]:
            j = j + 1        
            # print("j : " , j)
            # print("i : ", i)
            
        if j > i:
            while j >= i:
                a.pop(j)
                j = j - 1
                # print(a)
            i = i - 2   
    
        i = i + 1
    print("After Remove : " , a)


def removeAdjacentDuplicate(string):
    count = 0
    string = list(string)
    for i in range(1, len(string)):
        if string[count] != string[i]:
            count = count + 1
            string[count] = string[i]
    print(string[:count + 1])        





if __name__ == '__main__':
    remove_all_adjacent2("ABCCCBCBA")
    # remove_all_adjacent("ABCCCCBCBA")
    # remove_adjacent_pair("ABCCCBCBA")
    removeAdjacentDuplicate("ABCCBCBA")

