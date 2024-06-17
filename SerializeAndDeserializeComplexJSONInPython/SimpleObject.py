'''
Created on 06-Apr-2021

@author: anilpradhan

https://yzhong-cs.medium.com/serialize-and-deserialize-complex-json-in-python-205ecc636caa


'''

import json


class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == '__main__':
    student = Student(first_name="Jake", last_name="Doyle")
    # json_data = json.dumps(student,default=lambda o:o.__dict__,indent=4)
    json_data = json.dumps(student.__dict__, indent=4)

    print(json_data)
    # json_data = json.dumps(student)
    
