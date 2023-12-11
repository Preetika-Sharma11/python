
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("_ ",end="")
        else:
            print("* ",end="")
    print()
print("#"*4)
print(4*(4*("_ * ")+"\n"+4*("* _ ")+"\n"))