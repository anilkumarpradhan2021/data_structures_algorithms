'''
Created on 06-Apr-2021

@author: anilpradhan
'''

import json

class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_Json(cls,data):
        #return Student(**data)
        return cls(**data)

class Team(object):

    def __init__(self, students):
        self.students = students

    @classmethod
    def from_json(cls, data):
        students = list(map(Student.from_json, data["students"]))
        #return Team(students)
        return cls(students)


if __name__ == '__main__':
    student1 = Student(first_name="Jake", last_name="Foo")
    student2 = Student(first_name="Jason", last_name="Bar")
    team = Team(students=[student1, student2])
    
    # Serializing
    data = json.dumps(team, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print(data)
    # Deserializing
    decoded_team = Team.from_json(json.loads(data))
    print(decoded_team)
    print(decoded_team.students)
