###################
# Disclaimer part #
###################
'''
Lab#1 | Basic Python 1
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
print("*** Fun with permute ***")
sList = list(map(int, input("input : ").split(',')))
print("Original Cofllection: ", sList)
sList = sList[::-1] 
print("Collection of distinct numbers:")
print(' ', end='')

def addPermute(pos, tList) :
    return [tList[0:i] + [sList[pos]] + tList[i:] for i in range(len(tList)+1)]
def permute(tList) :
    if len(tList) == 0 :
        return [[]]
    return [x for y in permute(tList[1:])  for x in addPermute(tList[0], y)]
print(permute([i for i in range(len(sList))]))