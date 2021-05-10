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
        return self.items[len(self.items)-1],self.items[len(self.items)-2]
    def size(self):
        return len(self.items)
    def count(self, c):
        return self.items.count(c)

word = list(map(str,input('Enter Input : ').split()))
s = Stack()
cb = 0
for i in word:
    if s.isEmpty():
        s.push(i)
    else:
        while True:    
            if  s.size() >= 2:
                p1,p2 = s.peek()
                if i == p1 and i == p2:
                    s.pop()
                    s.pop()
                    cb += 1
                    break
                else:
                    s.push(i)
                    break
            else:
                s.push(i)
                break
print(len(s.items))
ans = reversed(s.items)
print('Empty' if s.size() == 0 else ''.join(ans))
if cb > 1:
    print("Combo : {} ! ! !".format(cb))