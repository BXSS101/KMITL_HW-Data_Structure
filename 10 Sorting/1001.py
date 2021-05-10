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
ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def sorted(a) :
    b = list(a)
    for last in range(len(b)-1,-1,-1) :
        swapped = False
        for i in range(last) :
            if b[i] > b[i+1] :
                b[i], b[i+1] = b[i+1], b[i]
                swapped = True
        if not swapped :
            break
    if a == b :
        return True
    else :
        return False

inp = [int(i) for i in input('Enter Input : ').split()]
if sorted(inp) :
    print("Yes")
else :
    print("No")