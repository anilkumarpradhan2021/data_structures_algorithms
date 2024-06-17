'''
Created on 26-Sep-2019

@author: anpradha


Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). 

They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.


'''


class Animal():

    order = 0

    def __init__(self):
        self.dogs = []
        self.cats = []
    
    def enqueueDog(self, dog):
        self.dogs.append((dog, Animal.order))
        Animal.order = Animal.order + 1

    def enqueueCat(self, cat):
        self.cats.append((cat, Animal.order))
        Animal.order = Animal.order + 1

    def dequeueDog(self):
        if len(self.dogs) > 0:
            return self.dogs.pop(0)
        else:
            print("No more dog in shelter")

    def dequeueCat(self):
        if len(self.cats) > 0:
            return self.cats.pop(0)
        else:
            print("No more cat in shelter")
    
    def dequeueAny(self):
        if len(self.cats) == 0:
            return self.dequeueDog()
        elif len(self.dogs) == 0:
            return self.dequeueCat()
        else:
            if self.dogs[0](1) < self.cats[0](1):
                return self.dogs.pop(0)
            else:
                return self.cats.pop(0)


if __name__ == '__main__':
    animal = Animal()
    animal.enqueueCat("cat1")
    animal.enqueueCat("cat2")
    animal.dequeueDog()
    print(animal.dequeueCat())
    print(animal.dequeueAny())
    print(animal.dequeueCat())
    