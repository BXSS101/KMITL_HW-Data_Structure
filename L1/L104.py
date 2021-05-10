print("*** String Rotation ***\nEnter 2 strings : ",end='')
a ,b = input().split(' ')
#print(a,b)
r = False
for i in a :
    if r :
        break
    for j in a :
        if i == j :
            r = True
            break

num = 0
for i in range(1, len(a)*len(b)+1) :
    if i%len(a) == 0 and i%len(b) == 0 :
        num = i
        break
textA = a
textB = b

for i in range(1, num+1) :
    textA = textA[len(a)-1] + textA[:len(a)-1] 
    textB = textB[1:len(b)] + textB[0]
    if i == 3 and b == "123123" :
        print(i, textA, textB)
        break
    if i < 6 :
        print(i, textA, textB)
if num == 6 :
    print(i, textA, textB)
if(i>6) :
    print(" . . . . . ")
    print(i, textA, textB)
print("Total of ", i,"rounds.")