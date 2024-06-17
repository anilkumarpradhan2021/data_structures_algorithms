'''
Created on 24-Nov-2019

@author: anpradha

Word Ladder (Length of shortest chain to reach a target word)
Given a dictionary, and two words ‘start’ and ‘target’ (both of same length). Find length of the smallest chain from ‘start’ to ‘target’ if it exists, such that adjacent words in the chain only differ by one character and each word in the chain is a valid word i.e., it exists in the dictionary. It may be assumed that the ‘target’ word exists in dictionary and length of all dictionary words is same.

Example:

Input:  Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
             start = TOON
             target = PLEA
Output: 7
Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA


'''

# To check if strings differ by  
# exactly one character 

  
def isadjacent(a, b): 
    count = 0
    n = len(a) 
  
    # Iterate through all characters and return false 
    # if there are more than one mismatching characters 
    for i in range(n): 
        if a[i] != b[i]: 
            count += 1
        if count > 1: 
            break
  
    return True if count == 1 else False


from  queue import Queue  


# Returns length of shortest chain to reach  
# 'target' from 'start' using minimum number 
# of adjacent moves.  D is dictionary 
def shortestChainLen(start, target, D): 
  
    # Create a queue for BFS and insert  
    # 'start' as source vertex 
    Q = Queue()
    Q.put((start, 1)) 
  
    while not Q.empty(): 
  
        curr_word , len = Q.get()
  
        # Go through all words of dictionary 
        for it in D.keys(): 
            # Process a dictionary word if it is  
            # adjacent to current word (or vertex) of BFS 
            temp = D[it] 

            if isadjacent(curr_word, temp) == True: 
  
                # Add the dictionary word to Q 
                Q.put((temp, len + 1)) 
  
                # Remove from dictionary so that this  
                # word is not processed again.  This is  
                # like marking visited 
               
                D[temp] = "XXXX"  # i can fix this , this is odd
  
                # If we reached target 
                if temp == target: 
                    return len + 1


if __name__ == '__main__':
    d = {"poon": "poon", "plee": "plee", "same": "same" , "poie": "poie" , "plie": "plie" , "poin": "poin" , "plea": "plea" }
    start = "toon"
    target = "plea"
    print(shortestChainLen(start, target, d))

