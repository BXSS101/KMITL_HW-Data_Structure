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
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
ให้เขียน Recursive หาค่า Min ของ Input
'''
minimum = 65000
def min(ls) :
    global minimum
    if not ls :
        #print('Base Case',minimum)
        return 0
    else :
        #print('Now',ls[0])
        if ls[0] < minimum :
            #print(ls[0],'in case')
            minimum = ls[0]
        min(ls[1:])
text = list(map(int, input('Enter Input : ').split(' ')))
min(text)
print('Min :',minimum)
