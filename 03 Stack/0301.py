###################
# Disclaimer part #
###################
'''
Lab#3 | Stack
Course : Data Structure & Algorithm
Instructor : Kiatnarong Tongprasert, Kanut Tangtisanon
Semester / Academic Year : 1 / 2020
Institute : KMITL, Bangkok, Thailand
Developed By :  BXSS101 (Ackrawin B.)
Github URL : https://github.com/BXSS101
'''
################
# Problem part #
################
class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)
word = input("Enter Input : ")
myStack = Stack()
for i in word :
    if i == '(' or i == '[' :
        myStack.push(i)
        continue
    if i == ')' and myStack.isEmpty() :
        print("Parentheses : Unmatched ! ! !")
        quit()
    if i == ']' and myStack.isEmpty() :
        print("Parentheses : Unmatched ! ! !")
        quit()
    if myStack.isEmpty() :
        continue

    if i == ')' and myStack.peek() == '('  :
        myStack.pop()
        continue
    if i == ']' and myStack.peek() == '['  :
        myStack.pop()
        continue
if myStack.isEmpty() :
    print("Parentheses : Matched ! ! !")
else :
    print("Parentheses : Unmatched ! ! !")