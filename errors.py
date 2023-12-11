def con(a,b):
    try:
        r=a+b
        print(r)
    except TypeError as c:
        print(c)
con("hello","world")
con("hello",123)

def inn(lis,ind):
    try:
        a=lis[ind]
        print(a)
    except IndexError as b:
        print(b)

lis=[1,2,3,4,5]
inn(lis,2)
inn(lis,5)