def Sort_array(n,a):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                t=a[j]
                a[j]=a[i]
                a[i]=t
    print(a)
n=int(input())
ls=list(map(int,input().split()))
Sort_array(n,ls)
