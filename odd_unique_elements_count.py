a=int(input())
b=map(int,input().split())
x=[]
for i in b:
    if i%2==1:
        if i not in x:
            x.append(i)
print(len(x))