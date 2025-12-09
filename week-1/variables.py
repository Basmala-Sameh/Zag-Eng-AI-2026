name = input("What's your name?\n")
age = int(input("\nWhat's your age?\n"))
height = float(input("\nWhat's your tall ?\n"))
student = input("\nAre you student? (y/n)\n").lower().strip() in ["y","yes",1]
print("type of name is : " , type(name))
print("type of age is : " , type(age))
print("type of height is : " , type(height))
print("type of student is : " , type(student))
