'''
Created on 25-Aug-2016

@author: anpradha
'''

class End(object):

    def __init__(self, end):
        self.end = end


class SuffixNode(object):
    """Node for Python Trie Implementation"""

    def __init__(self, start, end):
        self.word = None
        self.nodes = {}  # dict of nodes
        self.start = start
        self.end = end
        self.suffix_node = None
        self.index 

class Active(object):
    def __init__(self, node):
        self.activeLength = 0;
        self.activeNode = node;
        self.activeEdge = -1;

        
class SuffixTree(object):
    
    def __init__(self, end):
        self.input = "mississippi#"
        self.remaining_suffix_count = 0
        
        
    def build(self):
        self.root = SuffixNode(1, End(0))
        self.root.index = -1
        self.active = Active(self.root)
        self.end = End(-1)
        
        for i in range(len(self.input)):
            self.start_phase(i)
        
        if self.remaining_suffix_count != 0 :
            print("Something goes wrong ")
            
    def select_node(self, index):
        return self.active.activeNode.nodes[self.input[index]]        

    def select_current_node(self):
        return self.active.activeNode.nodes[self.input[self.active.activeEdge]]        
    
    def length_of_current_node(self,suffix_node):
        return  suffix_node.end - suffix_node.start
    

    def next_char(self,i):
        suffix_node = self.select_current_node()
        
        if self.length_of_current_node(suffix_node) >=self.active.activeLength:
            return self.input[self.active.activeNode.nodes[self.input[self.active.activeEdge]].start + self.active.activeLength]
        
        
    
    def start_phase(self, i):
        
        lastCreatedInternalNode = None
        self.end = self.end + 1 
        
        self.remaining_suffix_count = self.remaining_suffix_count + 1
        
        while self.remaining_suffix_count > 0 :
            if self.active.activeLength == 0:
                '''if current character from root is not None then 
                        increase active length by 1 
                        and 
                        break out of while loop.
                        This is rule 3 extension and trick 2 (show stopper)'''
                # Rule -3 extension 
                if self.select_node(i) != None :
                    self.active.activeLength = self.active.activeLength + 1
                    self.active.activeEdge = self.select_node(i).start
                else:
                    # create a new leaf node with current character from leaf.
                    # Rule -2 extension
                    self.root[self.input[i]] = SuffixNode(i, self.end)   
                    self.remaining_suffix_count = self.remaining_suffix_count - 1 
            else:
                '''
                if active length is not 0 means we are traversing somewhere
                in middle. So check if next character is same as
                current character.
                '''    
                next_char_from_current_active  = self.next_char(i)
                if next_char_from_current_active == self.input[i]:
                    print()
                else:
                    '''
                    next character is not same as current character so create a new internal node as per
                    // rule 2 extension.
                    ''' 
                    suffix_node = self.select_current_node()                   
            
    
