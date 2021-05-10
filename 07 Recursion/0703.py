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
เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว
****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว
บทนิยาม
ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว
'''
def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a%b == 0:
        return b
    else:
        return gcd(b,a%b)


n = list(map(int, input("Enter Input : ").split()))

if n[0] == 0 and n[1] == 0:
    print('Error! must be not all zero.')
    exit()
g = gcd(min(n),max(n))
if g < 0 and n[0] < 0 and n[1] < 0:
    print('The gcd of {} and {} is : {}'.format(min(n),max(n),g*-1))
else:
    print('The gcd of {} and {} is : {}'.format(max(n),min(n),abs(g)))