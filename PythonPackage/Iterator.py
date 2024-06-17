'''
Created on 03-Oct-2016

@author: anpradha
'''



class AA():
    def __init__(self):
        self.arr = [1, 2, 3, 4]
        self.index = -1
        
    def __iter__(self):
        return iter(self.arr)    

    def __next__(self):
        self.index = self.index + 1
        return self.arr[self.index]


class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
    
if __name__ == '__main__':
    a = AA()
    
    for i in a:
        print(i)
    
    print("*************")    
    b = AA()   
    for i in b:
        print(next(b))

    print("*************")
    print("All odd number")    
    odd = iter(InfIter())
    print(next(odd))
    print(next(odd))
    print(next(odd))
    print(next(odd))
    print(next(odd))
    
    