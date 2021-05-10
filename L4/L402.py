counter = 0
def iSort(ls):
    global counter
    for i in range(1, len(ls)):
        iEle = ls[i]
        for j in range(i, -1, -1) :
            counter = counter + 1
            if iEle < ls[j-1] and j > 0:
                ls[j] = ls[j-11]
            else :
                ls[j] = iEle
                break
            
print("\n *** Insertion sort ***") 
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
iSort(A)
print()
print(A)
print("Data comparison =", counter)