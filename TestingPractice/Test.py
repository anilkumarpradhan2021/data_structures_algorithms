'''
Created on 21-Feb-2018

@author: anpradha
'''


def pow():
    try:
        print("I am try")
        1/0
    except Exception:
        print("Exception happended")
    else:
        print("when no error happen,execute")    

    finally:
        print("I am in finally")
    print("I am after error")    
    

if __name__ == '__main__':
    pow()
