a=int(input())
b=[0,1]
x=0
y=0
for i in range(a):
    b.append(sum(b[-2:]))
for j in b:
    if a<j:
        x=j
        break
for k in b[::-1]:
    if a>k:
        y=k
        break
if abs(x-a)>abs(y-a):
    print(y)
elif abs(x-a)<abs(y-a):
    print(x)
else:
    print(y,x)
