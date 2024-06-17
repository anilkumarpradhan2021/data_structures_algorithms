'''
Created on 01-Oct-2019

@author: anpradha

String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).



'''

if __name__ == '__main__':
    str1 = "aabcccccaaa"
    str_list = list(str1)
    result = ""
    i = 0
    while i < len(str_list):
        c = 1
        result = result + str_list[i]
        while i + 1 < len(str_list)  and str_list[i] == str_list[i + 1]:
            c = c + 1
            i = i + 1
        
        result = result + str(c)
        
        i = i + 1
    print(result)
