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
จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว
รูปแบบการรับ input จะแบ่งโดย '/'
1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ
2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว
รูปแบบ output 
จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST 
*** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***
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

    def closest_value(self, value):
        if self.root is not None:
            diff = 99999999999999999999999
            to_return = -1
            q = Queue()
            q.enqueue(self.root)
            while not q.is_empty():
                buffer = q.dequeue()
                if value == buffer.value:
                    to_return = buffer.value
                    break
                else:
                    if abs(value-buffer.value) < diff:
                        diff = abs(value-buffer.value)
                        to_return = buffer.value
                if buffer.left is not None:
                    q.enqueue(buffer.left)
                if buffer.right is not None:
                    q.enqueue(buffer.right)
            return to_return

inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
tree = BST()
compare = int(inp[1])
for item in lst:
    tree.add(item)
    tree.print_tree(tree.root)
    print('--------------------------------------------------')
print(f'Closest value of {compare} : {tree.closest_value(compare)}')