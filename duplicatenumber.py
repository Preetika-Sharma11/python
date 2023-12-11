a=[1,4,2,3,2,1,7,7,7,3,6,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)

    else:
        print(i)
        a.remove(i)
