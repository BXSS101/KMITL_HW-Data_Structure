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
print(' *** Wind classification ***')
n = float(input("Enter wind speed (km/h) : "))
if n >= 0 and n <= 51.99 :
    print("Wind classification is Breeze.")
elif n >= 52 and n <= 55.99 :
    print("Wind classification is Depression.")
elif n >= 56 and n <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif n >= 102 and n <= 208.99 :
    print("Wind classification is Typhoon.")
elif n >= 209 :
    print("Wind classification is Super Typhoon.")