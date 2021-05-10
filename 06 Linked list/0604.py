###################
# Disclaimer part #
###################
'''
Lab#6 | Linked List
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
class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node()
    def __str__(self):
        return " ".join(str(i) for i in self.display())
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node
    def isEmpty(self):
        return self.head.next == None
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems
    def insert(self,index,data):
        if index > self.lenght() or index < 0:
            return None
        elif index == 0:
            self.appendHead(data)
            return self.display()
        elif index == self.lenght():
            self.append(data)
            return self.display()
        cur_idx = 1
        cur_node = self.head
        new_node = node(data)
        while True:
            cur_node = cur_node.next
            if cur_idx == index : 
                new_node.next = cur_node.next
                cur_node.next = new_node
                return new_node.data
            cur_idx += 1
    def appendHead(self,data):
        new_node = node(data)
        new_node.next = self.head.next
        new_head = node()
        new_head.next = new_node
        new_node.prev = new_head
        self.head = new_head
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def erase(self,index):
        if index >= self.lenght():
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx +=1 
    def find(self,data):
        cur = self.head
        inx = 0
        while cur.next != None:
            cur = cur.next
            if cur.data == data:
                return inx
            inx += 1
    def shiftLeft(self):
        inx = self.find('|')
        if inx != 0 :
            self.erase(inx) 
            self.insert(inx - 1,'|')
    def shiftRight(self):
        inx = self.find('|')
        if inx != self.lenght()-1 :
            self.erase(inx) 
            self.insert(inx + 1,'|')

text = input('Enter Input : ').split(',')
LL = LinkedList()
LL.append('|')
for i in text:
    i = i.strip().split()
    if i[0] == 'I':
        LL.insert(LL.find('|'),i[1])
    elif i[0] == 'L':
        LL.shiftLeft()
    elif i[0] == 'R':
        LL.shiftRight()
    elif i[0] == 'B':
        inx = LL.find('|')
        if inx != 0 : LL.erase(inx-1)
    elif i[0] == 'D':
        inx = LL.find('|')
        if inx != LL.lenght()-1 : LL.erase(inx+1)
print(LL)