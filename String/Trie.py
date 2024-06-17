'''
Created on 13-Oct-2019

@author: anpradha
'''


class TriNode():

    def __init__(self):
        self.children = {}
        self.endOfWord = False
    

class Trie():

    def __init__(self):
        self.root = TriNode()

    def insert(self, word):
        temp = self.root
        for char_key in word:
            if char_key not in temp.children:
                temp.children[char_key] = TriNode()
            temp = temp.children[char_key]
        
        # end of the word
        temp.endOfWord = True
    
    def search(self, word):
        temp = self.root
        for index in range(len(word)):
            if word[index] not in temp.children:
                return False
            else:
                temp = temp.children[word[index]]
                
        if temp and temp.endOfWord == True:
            return True
        
        return False    
        
                         
if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"] 
    output = ["Not present in trie",
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
    
    print(t.search("there"))
    print(t.search("ther"))
    print(t.root.children)
        
