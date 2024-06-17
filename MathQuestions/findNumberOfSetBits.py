'''
Created on 17-Sep-2019

@author: anpradha
'''


def solution1(num):
    count = 0
    while num > 0:
        if num & 1 == 1:
            count = count + 1
        num = num >> 1
    
    print(count)

    
def solution2(num):
    num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];  
    nibble = 0; 
    if(num == 0): 
        return num_to_bits[0]; 
      
    # Find last nibble , its hex
    nibble = num & 0xf; 
      
    # Use pre-stored values to find count 
    # in last nibble plus recursively add 
    # remaining nibbles. 
      
    return num_to_bits[nibble] + solution2(num >> 4);  
        

if __name__ == '__main__':
    num = 31
    print(solution2(num))
