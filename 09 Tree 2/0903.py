###################
# Disclaimer part #
###################
'''
Lab#9 | Tree 2
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
'''
จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด เช่น
        5
            4
                3
    2
1
     -2
จากรูป ค่าที่น้อยที่สุดคือ -2 ดังนั้น rank(-2) จะได้ 1 แต่ rank ของค่าที่น้อยกว่า -2 จะเท่ากับ 0
และ rank(0) จะเท่ากับ 1 ส่วน rank(1) จะเท่ากับ 2 เป็นต้น
'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        traversal_path = ''
        if self.root is None:
            self.root = Node(value)
        else:
            buffer = self.root
            while buffer is not None:
                if value < buffer.value:
                    traversal_path += 'L'
                    if buffer.left is None:
                        buffer.left = Node(value)
                        break
                    else:
                        buffer = buffer.left
                else:
                    traversal_path += 'R'
                    if buffer.right is None:
                        buffer.right = Node(value)
                        break
                    else:
                        buffer = buffer.right
        return traversal_path + '*'

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

exp = ''

def inorder(node):
    global exp
    if node is not None:
        inorder(node.left)
        exp += str(node.value) + ' '
        inorder(node.right)

def ranking(lst, to_find):
    rank = 0
    for i in range(len(lst)):
        if to_find >= lst[i]:
            rank += 1
    return rank

inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
tree = BST()
to_find = int(inp[1])
for item in lst:
    tree.add(item)
tree.print_tree(tree.root)
print('--------------------------------------------------')
inorder(tree.root)
rank_list = list(map(int, exp.split()))
print(f'Rank of {to_find} : {ranking(rank_list, to_find)}')