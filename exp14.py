
# Open the file in write mode
with open("MyFile.txt", "w") as file:
    # Ask the user to input three lines
    #for i in range(3):
        #line = input(f"Enter line {i + 1}: ")
        #file.write(line + "\n")
    line = input(f"Enter line one: ")
    file.write(line + "\n")
    line = input(f"Enter line two: ")
    file.write(line + "\n")
    line = input(f"Enter line three: ")
    file.write(line + "\n")
print("Three lines have been written to MyFile.txt.")
