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
        return " -> ".join(str(i) for i in self.display())
    def addList(self,data):
        self.head = node()
        for i in data:
            self.append(i)
    def append(self,data):
        new_node,cur = node(data),self.head
        while cur.next != None:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node
    def display(self):
        elems,cur = [],self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems
    def lenght(self):
        cur,total = self.head,0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def sort(self):
        cur = self.display()
        ls,strList = [],[]
        for i in cur:
            ls.append(int(i))
        ls = sorted(ls)
        for i in ls:
            strList.append(str(i))
        self.addList(strList)
def getDigit(pos,data):
    pos = pos*-1
    try:
        digit = data[pos]
        return int(digit) if digit != '-' else 0
    except IndexError:
        return 0
def rSort(tempList):
    round,nInput = 0,len(tempList)
    subList = list(LinkedList() for _ in range(10))
    while True:
        round += 1
        for i,data in enumerate(tempList):
            num = getDigit(round,data)
            for j in range(10):
                if num == j:
                    subList[j].append(data)
                    break
        for i in range(10):
            subList[i].sort(reverse=True)
        print('------------------------------------------------------------')
        print('Round :',round)
        
        for i,data in enumerate(subList):
            print(i,':',' '.join(data.display()))
        tempList = []
        for i in subList:                        
            for j in i.display():
                tempList.append(j)
        if subList[0].lenght() == nInput: break
        subList = list(LinkedList() for _ in range(10))
    return round-1,tempList

text = input('Enter Input : ').split()
round,rst = rSort(text)
print('------------------------------------------------------------')
print(round,'Time(s)')
print('Before Radix Sort :',' -> '.join(text))
#rst.reverse()
print('After  Radix Sort :',' -> '.join(rst))