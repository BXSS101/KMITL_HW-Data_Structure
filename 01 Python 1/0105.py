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
n = int(input("Enter Input : "))
for i in range(n + 2) :
    #first row
    if i == 0 :
        for j in range((n + 2) * 2) :
#            print(j, end='')
            #first half
            if j < (((n + 2) * 2) / 2) :
                #print('0', end='')
                if j < (((n + 2) * 2) / 2) - (i + 1) :
                    print('.', end='')
                else :
                    print('#', end='')
            #second half
            else :
                print('+', end='')
        print('')
    #last row
    elif i == n + 1 :
        for j in range((n + 2) * 2) :
            #print('E', end='')
            if j < (((n + 2) * 2) / 2) :
                print('#', end='')
            else :
                print('+', end='')
        print('')
    #other row
    else :
        for j in range((n + 2) * 2) :
            #print('*', end='')
            if j < (((n + 2) * 2) / 2) :
                if j < (((n + 2) * 2) / 2) - (i + 1) :
                    print('.', end='')
                else :
                    print('#', end='')
            else :
                if j == (((n + 2) * 2) / 2) :
                    print('+', end='')
                elif j == ((n + 2) * 2) - 1 :
                    print('+', end='')
                else :
                    print('#', end='')
        print('')
for i in range(n + 2) :
    if i == 0 :
        for j in range((n + 2) * 2) :
            #print('E', end='')
            if j < (((n + 2) * 2) / 2) :
                print('#', end='')
            else :
                print('+', end='')
        print('')
    elif i == n + 1 :
        for j in range((n + 2) * 2) :
#            print(j, end='')
            #first half
            if j < (((n + 2) * 2) / 2) :
                print('#', end='')
            #second half
            else :
                #print('0', end='')
                if j < ((n + 2) * 2) - i :
                    print('+', end='')
                else :
                    print('.', end='')
        print('')
    else :
        for j in range((n + 2) * 2) :
            #print('*', end='')
            if j < (((n + 2) * 2) / 2) :
                if j == 0 :
                    print('#', end='')
                elif j == (((n + 2) * 2) / 2) - 1 :
                    print('#', end='')
                else :
                    print('+', end='')
            else :
                if j < ((n + 2) * 2) - i :
                    print('+', end='')
                else :
                    print('.', end='')
        print('')