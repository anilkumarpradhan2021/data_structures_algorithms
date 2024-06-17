'''
Created on 10-Oct-2019

@author: anpradha


Shuffle a deck of cards

Given a deck of cards, the task is to shuffle them.

Its very easy

'''
import random


def shuffleCard():
    # let the card be a array
    arr = [i for i in range(52)]
    print("Deck before Shuffle : ")
    print(arr)
    
    for i in arr:
        # find a random number between 0 to 52
        random_index = random.randint(0, 51)
        
        # swap with the radom index
        arr[i], arr[random_index] = arr[random_index] , arr[i]

    print("Deck after Shuffle : ")
    print(arr)

    
def shuffleCardRecursive(cards, i):
    
    if i == 0:
        return cards
    
    shuffleCardRecursive(cards, i - 1)
    
    random_index = random.randint(0, i)
        
        # swap with the radom index
    cards[i], cards[random_index] = cards[random_index] , cards[i]

    return cards

    
if __name__ == '__main__':
    shuffleCard()
    print("&&&&&&&&&&&&&&&& : Recursive : &&&&&&&&&&&&&&&")
    cards = [i for i in range(52)]
    print("Deck before Shuffle : ")
    print(cards)
    cards = shuffleCardRecursive(cards, 51)
    print("Deck after Shuffle : ")
    print(cards)

