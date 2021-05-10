def bi_search(l, r, arr, x):
    if l > len(arr)-1 :
        print("Not found")
    if x != arr[l]:
        bi_search(l+1, r-1, arr, x)
    else:
        print("Found")
        
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
bi_search(0, len(arr) - 1, sorted(arr), k)