a=10
b=0
# Zero division error
try:
    print(a/b)
    print("division successful")
except ZeroDivisionError as e :
    print(f"Error: {e}")
#print("success")
finally:
    pass
    print("success")   # why are you still working

# Value error 
try:
    v=int("A")        # any number will do so an alphabet will be an error
except ValueError as b:
    print(b)

# Type error
try:
    r="10"+5
except TypeError as c:
    print(c)

# File not found error
# Raised when a file or directory is requested but cannot be found
try:
    with open("nonexistentfile.txt","r") as file:
        con=file.read()
except FileNotFoundError as f:
    print(f)


# Index error
# Raised when a sequence subscript is out of range
try:
    lis=[1,2,3]
    ele=lis[10]
except IndexError as i:
    print(i)