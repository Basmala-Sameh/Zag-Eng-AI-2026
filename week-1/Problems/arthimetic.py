# x, y = float(input("Enter the 2 numbers "))
# float could not convert string to float 
# x, y = float(input("Enter the 2 numbers ").split())
# float take one number , couldn't take list

x ,y = map(float,input("Enter the 2 numbers").split())
sum = x+y
subtract = x-y
product = x*y

big = max(x,y)
small = min(x,y)
divission = None

if small==0:
    divission = "can't divde by zero"
else:
    divission = x/y


print (f"Summition of your 2 numbers is : {sum}") 
print (f"Subtraction of your 2 numbers is : {subtract}") 
print (f"Division of your 2 numbers is : {divission}") 
print (f"Product of your 2 numbers is : {product}") 
