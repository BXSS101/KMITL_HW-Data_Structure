###################
# Disclaimer part #
###################
'''
Lab#4 | Queue
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
class Queue:
    def __init__(self):
        self.items = list()
    def enqueue(self, value):
        self.items.append(value)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() <= 0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return -1
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output

inputs = input('Enter Input : ').split(',')
q = Queue()
for iter in inputs:
    if len(iter) == 1:
        if not q.is_empty():
            print(q.dequeue(), 0)
        else:
            print(-1)
    else:
        text = iter.split()
        val = text[1]
        q.enqueue(val)
        print(q.size())
print(q)