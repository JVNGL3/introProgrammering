#!/usr/bin/python3

def menu():
    #A function used to print out the main menu
    print("\nMain Menu:")
    print("1: Insert word")
    print("2: Lookup word")
    print("3: Exit")

################################################################################################################################################

def wordListOneInsert(wordList, descList):
    word = input("Word to insert:")
    if word in wordList:
        print("The chosen word already exists in the list!")
        return
    else:
        #appends the word and description to the respective list
        wordList.append(word)
        desc = input("Please enter a description of your word:")
        descList.append(desc)
        print("Word successfully added to the list!\n")
        return

def wordListOneLookup(wordList, descList):
    lookup = input("Word to lookup:")    
    if lookup in wordList:
        # if the word that is being looked up is in the list print the description on the respective position using the index
        i = wordList.index(lookup)
        print("Description of", lookup, ":", descList[i])
        return
    else:
        print("The word you're looking for is not in the list!\n") 
        return


def wordListOne():
    #A wordlist implemented by using two separate lists, one for the word and another for the description
    wordList = []
    descList = []
    while True:
        menu()
        ans = int(input("Choose alternative:"))
        if ans == 1:
            wordListOneInsert(wordList,descList)
        elif ans == 2:
            wordListOneLookup(wordList,descList)    
        elif ans == 3:
            return
        else:
            print("Your choice is invalid!\n")


################################################################################################################################################

def wordListTwoInsert(wordList):
    #print("WordlistTwoInsert test!\n")
    word = input("Word to insert:")
    
    for _ in wordList:
        if word in _:
            print("The chosen word already exists in the list!")
            return
    # if the word is not already present in the list appends a tuple of the word and the description to the end of the list
    desc = input("Please enter a description of your word:")
    wordList.append((word,desc))
    print("Word successfully added to the list!\n")
    return


def wordListTwoLookup(wordList):
    lookup = input("\nWord to lookup: ") 
    for _ in wordList:
        if lookup in _:
             #this loop goes through each tuple in the list and checks if the "lookup word" is present in the tuple and then prints the second value in that tuple, which is the description
            print("Description of",lookup, ":", _[1])
            return
        else:
            print("The word you're looking for is not in the list!\n") 
            return


def wordListTwo():
    #A wordlist implemented using a list containing tuples of words and descriptions
    wordList = []    
    
    while True:
        menu()
        ans = int(input("Choose alternative:"))
        if ans == 1:
            wordListTwoInsert(wordList)
        elif ans == 2:
            wordListTwoLookup(wordList)  
        elif ans == 3:
            return
        else:
            print("Your choice is invalid!\n")
    
################################################################################################################################################

def wordListThreeInsert(wordList):
    word = input("Word to insert:")
    if word in wordList:
        print("The chosen word already exists in the list!")
        return
    else:
        #if the input word is not already present in the dicionary, the function updates the dictionary with a new key value pair of the word and the description
        desc = input("Please enter a description of your word:")
        wordList.update({word:desc})
        print("Word successfully added to the list!\n")
        return


def wordListThreeLookup(wordList):
    lookup = input("\nWord to lookup: ")
    if lookup in wordList:
        #if the "lookup word" is present in the dictionary it prints the value to the key that is the "lookup word"
        print("Description of",lookup, ":", wordList[lookup])
    else:
        print("The word you're looking for is not in the list!\n") 
        return


def wordListThree():
    #A wordlist implemented using a dictionary with key value pairs, word and description
    wordList = {}
    
    while True:
        menu()
        ans = int(input("Choose alternative:"))
        if ans == 1:
            wordListThreeInsert(wordList)
        elif ans == 2:
            wordListThreeLookup(wordList)  
        elif ans == 3:
            return
        else:
            print("Your choice is invalid!\n")


################################################################################################################################################

# wordListOne()
# wordListTwo()
# wordListThree()
