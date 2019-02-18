def sort_array(n,a):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                t=a[j]
                a[j]=a[i]
                a[i]=t
    if n%2==0:
        x=a[n//2]
        y=a[(n//2)-1]
        z=(x+y)/2
        print(z)
    else:
        print(a[(n//2)])
n=int(input())
ls=list(map(int,input().split()))
sort_array(n,ls)
