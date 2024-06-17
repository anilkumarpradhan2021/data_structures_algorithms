'''
Created on 26-Oct-2019

@author: anpradha

check Cracking the Coding Interview PDF for explanation . Section Hard 17.9

'''


def KthMinimumNumberWhosePrimeFactorAre3_5_7(k):
    min_element = 1
    queue3 = []
    queue5 = []
    queue7 = []
    
    # initialise the queue
    queue3.append(min_element)
    
    for i in range(k) :
        v3 = queue3[0] if len(queue3) > 0  else float("inf")  # 1st element
        v5 = queue5[0] if len(queue5) > 0  else float("inf")  # 1st element
        v7 = queue7[0] if len(queue7) > 0  else float("inf")  # 1st element

        min_element = min(v3, min(v5, v7))
    
        if min_element == v3:
            queue3.remove(v3)
            queue3.append(3 * min_element)
            queue5.append(5 * min_element)
            queue7.append(7 * min_element)
        elif min_element == v5:
            queue5.remove(v5)
            queue5.append(5 * min_element)
            queue7.append(7 * min_element)
            
        if min_element == v7:
            queue7.remove(v7)
            queue7.append(7 * min_element)

    print(min_element)    

    
if __name__ == '__main__':
    KthMinimumNumberWhosePrimeFactorAre3_5_7(7)
    KthMinimumNumberWhosePrimeFactorAre3_5_7(8)
