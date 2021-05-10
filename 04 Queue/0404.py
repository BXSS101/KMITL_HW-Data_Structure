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
    def is_in_dep(self, dep):
        for item in self.items:
            if dep == item[0]:
                return True
        return False
    def cut_in(self, value):
        if self.is_empty() or not self.is_in_dep(value[0]):
            self.enqueue(value)
        else:
            for i in range(self.size()-1, -1, -1):
                if self.items[i][0] == value[0]:
                    self.items.insert(i+1, value)
                    return
            self.enqueue(value)
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output

inp = input('Enter Input : ').split('/')
raw_employees = inp[0].split(',')
employees = dict()
for raw in raw_employees:
    dep, idd = raw.split()
    employees[idd] = dep
actions = inp[1].split(',')
q = Queue()
for cmd in actions:
    if len(cmd) == 1:
        if not q.is_empty():
            print(q.dequeue()[1])
        else:
            print('Empty')
    else:
        line = cmd.split()
        val = line[1]
        q.cut_in((employees[val], val))