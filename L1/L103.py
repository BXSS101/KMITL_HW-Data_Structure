print(" *** String count ***")
s = input("Enter message : ")
upper = [], lower = [], Cupper = [], Clower = []
for i in s :
    if i >= 'A' and i <= 'Z' :
        Cupper.append(i)
        if upper.count(i) < 1 :
            upper.append(i)
    if i >= 'a' and i <= 'z' :
        Clower.append(i)
        if lower.count(i) < 1 :
            lower.append(i)
        
lower.sort()
upper.sort()
print("No. of Upper case characters :", len(Cupper))
print("Unique Upper case characters :", end='')
for i in upper :
    print(' ' + i + ' ', end='')
print("\nNo. of Lower case Characters :", len(Clower))
print("Unique Lower case characters :", end='')
for i in lower :
    print(' ' + i + ' ', end='')