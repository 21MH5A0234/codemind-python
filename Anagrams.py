x=input()
y=input()
a=x.lower()
b=y.lower()
if len(a)==len(b):
    for i in a:
        if i not in b:
            print(False)
            break
    else:
        print(True)
else:
    print(False)