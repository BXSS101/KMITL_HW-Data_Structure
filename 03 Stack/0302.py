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
        if not self.isEmpty():
            return self.items[-1]
        return (999999999, 0)
    def size(self):
        return len(self.items)
    def count(self, c):
        return self.items.count(c)

dishes = input('Enter Input : ').split(',')
s = Stack()
for i in range(0, len(dishes)):
    weight, frequency = map(int, dishes[i].split())
    if s.isEmpty():
        s.push((weight, frequency))
    else:
        while weight > s.peek()[0]:
            dish = s.pop()
            print(dish[1])
        s.push((weight, frequency))