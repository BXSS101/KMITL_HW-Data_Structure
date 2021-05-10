print(" *** Divisible number ***")
n = int(input("Enter a positive number : "))
if n < 1 :
    print(n, "is OUT of range !!!")
    quit()
count = 0
print("Output ==> ", end='')
for i in range(1, n+1, 1) :
    if n % i == 0 :
        print(i, end=' ')
        count = count + 1
print("\nTotal ==>", count)