def prime(n):
    if n==1:
        return False
    else:
        for i in range (2,int((n**0.5)+1)):
            if n%i==0:
                return False
        else:
            return True
y= int(input())
p=0
q=0
if prime(y)==True:
    print('0')
else:
    for j in range(y+1,1000):
        if prime(j)==True:
            p=j
            break
    for t in range(y-1,y-1000,-1):
        if prime(t)==True:
            q=t
            break
    if abs(p-y)<abs(q-y):
        print(abs(p-y))
    elif abs(q-y)<abs(p-y):
        print(abs(q-y))
    else:
        print(abs(p-y))
    