###################
# Disclaimer part #
###################
'''
Lab#7 | Recursion
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
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง
****ห้ามใช้คำสั่ง for, while, do while*****
หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว
Enter Input : 7
______#
_____##
____###
___####
__#####
_######
#######
'''
def rec_row(number, sharps):
    print('_'*(number-sharps), end="")
    print('#'*sharps, end="")
    print()

def rec_pattern(number, row=0):
    if number > 0:
        if row < number:
            row += 1
            rec_row(number, row)
            rec_pattern(number, row)
    elif number == 0:
        print('Not Draw!')
    else:
        if row < abs(number):
            rec_row(abs(number), abs(number)-row)
            row += 1
            rec_pattern(number, row)

number = int(input("Enter Input : "))
rec_pattern(number)