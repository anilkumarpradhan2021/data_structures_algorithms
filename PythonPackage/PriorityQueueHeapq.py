'''
Created on 03-Oct-2016

@author: anpradha
'''

'''
Created on 09-Sep-2016

@author: anpradha
'''
import heapq


class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        return
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.priority == other.priority
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
   

if __name__ == '__main__':
    print(Skill(1, "Abil") == Skill(1, "Abil"))
    
    h = [12, 43, 51, 2, 1, 1]
    t = [(21, "Anil"), (2, "Uttam")]
    f = [(211, Skill(1, "Abil")), (22, Skill(1, "Abil"))]
    print(f)
    
    heapq.heapify(f)
    print(heapq.heappop(f))
    print(heapq.heappop(f))
    
    test = [(1, "Anil")]
    heapq.heappush(test, (2, "Uttam"))
    heapq.heappush(test, (0, "Sujata"))
    print(test)
    print(heapq.heappop(test))
    

   
