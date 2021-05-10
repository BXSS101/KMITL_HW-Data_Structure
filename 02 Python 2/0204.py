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
lst = list(map(int, input("Enter Your List : ").split(' ')))
if len(lst) < 3 :
    print("Array Input Length Must More Than 2")
    quit()
#print(lst)
uList = []
for i in range(len(lst)) :
    for j in range(i+1, len(lst)) :
        for k in range(j+1, len(lst)) :
            if lst[i] + lst[j] + lst[k] == 0 :
                tList = [lst[i], lst[j], lst[k]]
                #print(tList)
                uList.append(tList)
res = []
for i in uList :
    if i not in res :
        res.append(i)
print(res)