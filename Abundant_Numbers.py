a=input()
c=[]
for i in range(1,int(a)):
    if int(a)%i==0:
        c.append(i)
print(sum(c)>int(a))

            