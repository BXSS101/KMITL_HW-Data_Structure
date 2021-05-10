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
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return -1
    def cut_in(self, value):
        if self.is_empty():
            self.items.append(value)
        elif self.peek()[0] == 'EN':
            self.items.insert(0, value)
        else:
            for i in range(self.size()):
                if self.items[i][0] == 'EN':
                    self.items.insert(i, value)
                    return
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

text= input('Enter Input : ').split(',')
q = Queue()
for action in text:
    cmd = action.split()
    if len(cmd) == 1:
        if not q.is_empty():
            print(q.dequeue()[1])
        else:
            print('Empty')
    else:
        if cmd[0] == 'EN':
            q.enqueue((cmd[0], cmd[1]))
        elif cmd[0] == 'ES':
            q.cut_in((cmd[0], cmd[1]))