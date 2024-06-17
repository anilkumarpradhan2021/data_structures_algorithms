'''
Created on 12-Sep-2016

@author: anpradha
'''


 
def print_dict(dict_element):    
    for key in dict_element:
        print("Key : " + str(key), end=" ")
        print("Count : " + str(dict_element[key].count), end=" ")
        print("index : " + str(dict_element[key].index), end=" ")
        print()

class Element:
    def __init__(self, count=1, index=0):
        self.count = count
        self.index = index

        
if __name__ == '__main__':
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    print(arr)
    dict_element = {}
    ''' Just add all element to dict '''
    
    for i in range(len(arr)):
        if arr[i] in dict_element:
            element = dict_element[arr[i]]
            element.count = element.count + 1
        else:
            element = Element(1, i)
            dict_element[arr[i]] = element
            
    print_dict(dict_element)
    
    final_key = list(dict_element.keys())
    ''' I am using selection sort '''
    for i in range(len(final_key)):
        for j in range(i + 1, len(final_key)):
            ''' if entry having count more next entry then swap'''
            if (dict_element[final_key[i]].count > dict_element[final_key[j]].count):
                final_key[i], final_key[j] = final_key[j], final_key[i]
            ''' if both entry have same count then check for index/order of the entry and swap '''
            if (dict_element[final_key[i]].count == dict_element[final_key[j]].count) and (dict_element[final_key[i]].index < dict_element[final_key[j]].index):
                final_key[i], final_key[j] = final_key[j], final_key[i]
        
    print("After sorted") 
    print_dict(dict_element)
    for i in range(len(final_key) - 1, -1, -1):
        count = dict_element[final_key[i]].count
        value = final_key[i]
        for i in range(count):
            print(value, end=" ")
    
    
