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
n = input("Enter String : ")
vvv = ""
lst = []
for i in range(len(n)) :
    if vvv.find(n[i]) == -1 :
        vvv = vvv + n[i]
    else :
        continue
for i in range(len(n)) :
    lst.append(vvv.find(n[i]))
print(lst)