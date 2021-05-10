###################
# Disclaimer part #
###################
'''
Lab#2 | Basic Python 2
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
def odd_even(m, arr, s):
    if m == "S" :
        sss = " " + arr
        for i in range(1, len(arr) + 1) :
            if s == "Odd" and i % 2 == 1 :
                print(sss[i], end='')
            if s == "Even" and i % 2 == 0 :
                print(sss[i], end='')
    if m == "L" :
        lst = []
        lst2 = []
        if arr.find(' ') != -1 :
            lst = list(arr.split(' '))
        else :
            lst.append(arr)
        for i in range(1, len(lst)+1) :
            if s == "Odd" and i % 2 == 1 :
                lst2.append(lst[i-1])
            if s == "Even" and i % 2 == 0 :
                lst2.append(lst[i-1])
        print(lst2)

print("*** Odd Even ***")
mode, string, oe = input("Enter Input : ").split(',')
odd_even(mode, string, oe)