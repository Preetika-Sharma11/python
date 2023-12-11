a=input()
for i in range(len(a)//2):
    if (a[i]!=a[len(a)-1-i]):
        print("No it is not a palindrome string")
        break
else:
    print("Yes it is a Palindrome string")