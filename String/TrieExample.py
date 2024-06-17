'''
Created on 20-Aug-2016

@author: anpradha
'''
from SuffixPrefix.SuffixPrefixExample import End


# Delete Trie element is pending


class Node:
    """Node for Python Trie Implementation"""
    
    def __init__(self):
        self.word = None
        self.suffix_nodes = {}  # dict of nodes

        
        
    def __get_all__(self):
        """Get all of the words in the trie"""
        x = []
        
        for key, node in self.nodes.items() : 
            if(node.word is not None):
                x.append(node.word)
            x = x + node.__get_all__()

        return x
    
    
    def __insert__(self, word, string_pos=0):
        """Add a word to the node in a Trie"""
        current_letter = word[string_pos]
        
        # Create the Node if it does not already exist
        if current_letter not in self.nodes:
            self.nodes[current_letter] = Node();

        if(string_pos + 1 == len(word)):
            self.nodes[current_letter].word = word
        else:
            self.nodes[current_letter].__insert__(word, string_pos + 1)
            
        return True

    def __is_string_present__(self, string_to_search):
        flag = False
        current_node = self.nodes
        for i in range(len(string_to_search)) : 
            current_char = string_to_search[i]
            if current_char in (current_node) :
                if i + 1 == len(string_to_search) and current_node[current_char].word is not None :
                    return True
                current_node = current_node[current_char].nodes
                
            else:
                return False    
                
        return False
                
    
    def __get_all_with_prefix__(self, prefix, string_pos):
        """Return all nodes in a trie with a given prefix or that are equal to the prefix"""
        x = []
        
        for key, node in self.nodes.items() : 
            # If the current character of the prefix is one of the nodes or we have
            # already satisfied the prefix match, then get the matches
            if(string_pos >= len(prefix) or key == prefix[string_pos]):
                if(node.word is not None):
                    x.append(node.word)
                    
                if(node.nodes != {}):
                    if(string_pos + 1 <= len(prefix)):
                        x = x + node.__get_all_with_prefix__(prefix, string_pos + 1)
                    else:
                        x = x + node.__get_all_with_prefix__(prefix, string_pos)
    
        return x       


class Trie:
   def __init__(self):
        self.root = Node()
        
   def insert(self, word):
        self.root.__insert__(word)
        
   def get_all(self):
        return self.root.__get_all__()

   def get_all_with_prefix(self, prefix, string_pos=0):
        return self.root.__get_all_with_prefix__(prefix, string_pos)

   def is_string_present(self, string_to_search):
        return self.root.__is_string_present__(string_to_search)


if __name__ == '__main__':
    root = Trie()
    root.insert("anil")
    root.insert("abcd")
    print("Print all value")
    print(root.get_all())
    print(root.get_all_with_prefix("an"))
    print(root.is_string_present("anil1"))

    
