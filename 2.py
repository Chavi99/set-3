def maximum_of_array(n,arr):
    s=arr[0]
    for i in arr:
        if i>s:
            s=i
    print(s)
n=int(input())
ls=list(map(int,input().split()))
maximum_of_array(n,ls)
