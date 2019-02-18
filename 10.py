def time(t1,t2):
    hr=abs(t1[0]-t2[0])
    mi=abs(t1[1]-t2[1])
    print(hr,mi)
t1=list(map(int,input().split(" ")))
t2=list(map(int,input().split(" ")))
time(t1,t2)
