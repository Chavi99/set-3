def check_numeric(n):
    x=0
    for i in n:
        if i=="."  or ord(i)>=48 and ord(i)<=57  :
            x+=1
        else:
            x-=1
    if len(n)==x:
        print("yes")
    else:
        print("no")
n=input()
check_numeric(n)

