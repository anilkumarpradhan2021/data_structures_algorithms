'''
Created on 17-Sep-2016

@author: anpradha
'''

if __name__ == '__main__':
 
    ''' Assign functions to variables '''
    def greet(name):
        return "hello " + name

    greet_someone = greet
    print (greet_someone("John"))
    # Outputs: hello John

    ''' Define functions inside other functions '''
    
    def greet1(name):
        def get_message():
            return "Hello "
        
        result = get_message() + name
        return result

    print (greet1("John"))
    # Outputs: Hello John
    
    ''' Functions can be passed as parameters to other functions '''
    def greet2(name):
        return "Hello " + name 

    def call_func(func):
        other_name = "John"
        return func(other_name)  
    
    print (call_func(greet2))

    # Outputs: Hello John
    
    ''' Functions can return other functions '''
    
