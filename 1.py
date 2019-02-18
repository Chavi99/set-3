def airthmetic_progression_sum(n,k,a):
    s=int((n/2)*(2*a+(n-1)*k))
    print(s)
y=list(map(int,input().split()))
airthmetic_progression_sum(y[0],y[1],y[2])
