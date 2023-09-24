#!/usr/bin/python3

class board():

    def __init__(self, message = ""):
        self.message = message
        #this is an attribute

    def write(self, msg):
        self.message = msg       


def main():
    

    board1 = board()
    board2 = board()
    kim = board1
    Chris = board2
    # print(board1.message)
    # print(board2.message)

    print("===Bulletin Board System===")
    
    print("1: Direct Kim to other board")
    print("2: Direct Chris to other board")
    print("3: Tell Kim to post a message ")
    print("4: Tell Chris to post a message")
    print("0: ")

# main()


test = {('Kalle','bosse','nisse'): '123',
        ('Maria',): '123',
        ('Anna',): '321', 
        ('Olle',): '321'
        }
#a = 'filename'

#f = open(a,"w")

# for entry in test:
#     # print("entry:", entry)
#     # print(f"key:{entry}   value:{test[entry]}")
#     for names in entry:
#         print(f"key:{names}   value:{test[entry]}")
#         f.write(f"{test[entry]};{names};\n")

    

# f.write('hello')
# f.write('\nnice to meet you')
# for i in range(2):
#     f.write('\nstopit')


tulp = ('kalle','nisse')

print("before", test)

test[tulp] = test.pop(('Anna',))

print("after", test)

a = test.pop(('Olle',))

print("after", test)
print(a)







