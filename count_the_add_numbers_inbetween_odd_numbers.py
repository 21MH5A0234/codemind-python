a=int(input())
b=[int(x) for x in input().split()]
c=0
for i in range(a-2):
    if b[i]%2==1 and b[i+1]%2==1 and b[i+2]%2==1:
        c+=1
print(c)