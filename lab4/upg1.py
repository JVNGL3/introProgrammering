#!/usr/bin/python3
import os


class phoneBook():
    
    def __init__(self):
      '''Initates the object'''
      self.dict = {}

######################################################################################################

    def __del__(self):
        '''Simply delets the object'''
        #print("Deleted!")

#######################################################################################################

    def addEntry(self, name, number):
        '''A method that adds the name and the number in the dictionary if they aren't already present'''
        for entry in self.dict:                                                                           #each iteration entry is the key, which in this case a tuple containing names and aliases 
            
            if number in self.dict[entry]:                                                                #if the parameter number is in the value to the key each iteration, basically if the number is in the dictionary:
                print(f"The number: {number} already exists in the phonebook!")
                return
        
            if name in entry:                                                                             #if the parameter name is in the tuple that is entry 
                print(f"The name \"{name}\" already exists in the phonebook!")
                return    
        self.dict.update({(name.lower(),):number})                                                        #updates the dictionary with another dictionary containing a key-value pair that is: (name:number)
        print("name and number added!")
        return
       
#######################################################################################################

    def lookupEntry(self,name):
        '''A method that takes a name and if it exists in the dictionary it prints the number associated with the name'''
        for entry in self.dict:                                                                         #each iteration entry is the key, which in this case a tuple containing names and aliases
            if name in entry:                                                                           #if the parameter name is in the tuple that is entry:
                print(f"The name \"{name}\" is associated with the number: {self.dict[entry]}")         #print the value that associated with the key that is entry
                return
        print(f"There is no number associated with the name {name}")
        return

#######################################################################################################

    def addAlias(self,name,newname):
        '''A method that adds an alias to an already existing name entry'''
        for entry in self.dict:
            if name in entry:
                new = entry                                                                            #this is done to saves the key in entry
                new += (newname.lower(),)                                                              #new is going to be the new key and the new alias is thus added
                self.dict[new] = self.dict.pop(entry)                                                  #the old key is deleted and the value that was assigned to the key is assigned to the new key
                return
        print(f"The name \"{name}\" does not exist in the phonebook!")
        return

#######################################################################################################

    def changeNumber(self,name, number):
        '''A method that changes the number associated with the name'''
        for entry in self.dict:                                                                         #each iteration entry is the key, which in this case a tuple containing names and aliases
            if name in entry:                                                                           #if the parameter name is in the tuple that is entry:
                self.dict[entry] = number                                                               #change the number that is associated with the key that is entry to the parameter number
                print(f"the number has been updated to: {number}")           
                return
        print(f"The name \"{name}\" does not exist in the phonebook!")
        return

#######################################################################################################

    def saveFile(self,filename):
        '''A method that saves the current dictionary into a file'''
        f = open(filename, "w")                                                                        #opens a file to write to
        for entry in self.dict:                                                                        #here entry is a key which in turn is a tuple contining names and aliases
            for alias in entry:                                                                        #here alias is each item in the tuple
                f.write(f"{self.dict[entry]};{alias};\n")                                              #writes the "number ; name/alias ; \n" 
        f.close()                                                                                      
        print(f"wrote to file: \"{filename}\"!")

#######################################################################################################

    def loadFile(self,filename):
        '''A method that takes a filename that exist in the current directory and inserts the contents in a dictionary'''
        f = open(filename, "r")
        for l in f:                                                                                     #here l becomes each line in the inputfile
            a = l.split(";",2)                                                                          #each line in the file is then split up at the ";" and put in a list
            self.dict.update({(a[1].lower(),):a[0]})                                                    #then the dictionary is updated with a tuple containing the name and a string with the number, the name is also converted to lowercase
        #print(self.dict)
        f.close()
        return 

#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################

def main():
    '''This is the main function that starts the whole program'''
    d = phoneBook()
   
    while True:
        ans = parse()
        if ans[0] == "add":
            if entryCheck(ans,3):
                d.addEntry(ans[1], ans[2])
        
        elif ans[0] == "lookup":
            if entryCheck(ans,2):
                d.lookupEntry(ans[1])
        
        elif ans[0] == "alias":
            if entryCheck(ans,3):
                d.addAlias(ans[1],ans[2])
            
        elif ans[0] == "change":
            if entryCheck(ans,3):
                d.changeNumber(ans[1],ans[2])
            
        elif ans[0] == "save":
            if entryCheck(ans,2):
                d.saveFile(ans[1])
            
        elif ans[0] == "load":
            if entryCheck(ans,2):
                if os.path.isfile(f"./{ans[1]}"):                                       #This makes sure that there is a file with that name in the current directory
                    temp = phoneBook()                                                  #creates a new object of the class phoneBook
                    temp.loadFile(ans[1])                                               #this loads the file into the new object
                    del d                                                               #then deletes the old instance and renames the new instance
                    d = temp                                                            
                else:
                    print(f"The file: {ans[1]} does not exist in the current directory!")
        
        elif ans[0] == "quit":
            if entryCheck(ans,1):
                return
        else:
            print("Invalid command!")
            #print(d.dict)
    

def parse():
    '''This function takes the input string from the user and returns a list that is split at the whitespaces'''
    rawinput = input(">")
    inputList = rawinput.split()
    return inputList

def entryCheck(list,l):
    '''This function takes a list and makes sure it is sufficiently long, it is used to make sure that each command is given the right amount of arguments'''
    if int(l) == len(list):
        return True
    print("Wrong number of arguments!")
    return False

main()

