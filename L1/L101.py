print(" *** Wind classification ***")
a = float(input("Enter wind speed (km/h) : "))
if a < 0 :
    print("!!!Wrong value can't classify.")
elif a < 52 and a >= 0 :
    print("Wind classification is Breeze.")
elif a < 56 and a >= 52 :
    print("Wind classification is Depression.")
elif a < 102 and a >= 56 :
    print("Wind classification is Tropical Storm.")
elif a < 209 and a >= 102 :
    print("Wind classification is Typhoon.")
else :
    print("Wind classification is Super Typhoon.")