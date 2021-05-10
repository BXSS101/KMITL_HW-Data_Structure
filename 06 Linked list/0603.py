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
    def reverse(self):
        return " ".join(str(i) for i in reversed(self.display()))
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
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
def makeLinkedList(List):
    Linked_list = LinkedList()
    for data in List:
        Linked_list.append(data)
    return Linked_list

text = input('Enter Input (L1,L2) : ').split() 
list01 = text[0].split('->')
list02 = text[1].split('->')
Linked_list_01 = makeLinkedList(list01)
Linked_list_02 = makeLinkedList(list02)
print('L1    :',Linked_list_01)
print('L2    :',Linked_list_02)
print('Merge :',Linked_list_01,Linked_list_02.reverse())