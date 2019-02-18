def element_index(n,arr):
    for i in range(0,n):
        print(arr[i],i)
n=int(input())
ls=list(map(int,input().split(" ")))
element_index(n,ls)
        
