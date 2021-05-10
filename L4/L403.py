counter = 0
def bSort(ls):
    global counter
    for i in range(len(ls)) :
        swapped = False
        for j in range(len(ls)-i-1) :
            if ls[j] > ls[j+1] :
                ls[j], ls[j+1] = ls[j+1], ls[j]
                swapped = True
            counter = counter + 1 
        if not swapped:
            break
    return ls

print("\n *** Bubble sort ***") 
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bSort(A)
print()
print(A)
print("Data comparison =", counter)