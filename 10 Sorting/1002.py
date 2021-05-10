###################
# Disclaimer part #
###################
'''
Lab#10 | Sorting
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
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def buble(l):
    for last in range(len(l)-1,-1,-1):
        swaped = False
        for i in range(last):
            a1,a2 = i,i+1
            if l[a1] < 0 and l[a2] < 0:
                continue
            if l[a2] < 0:
                a2 += 1
                if a2 > last: break
            if l[a1] > l[a2]:
                l[a1], l[a2] = l[a2], l[a1]
                swaped = True
        if not swaped: break

inp = [int(i) for i in input('Enter Input : ').split()]
buble(inp)
print(' '.join(str(i) for i in inp))