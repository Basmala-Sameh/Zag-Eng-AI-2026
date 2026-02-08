#F = (C × 9/5) + 32
def celsius_to_fahrenheit(C):
    F = (C * 1.8) + 32
    return F

def fahrenheit_to_celsius(F):
    C = (F-32) * (5/9)
    return C

def average_temp(temp_list , scale):
    scale = scale.lower()
    if scale not in ("c" , "f"):
        print("Invalid input")
    else:
        return sum(temp_list)/len(temp_list)

def highest_temp(temp_list , scale):
    return max(temp_list)

while True:
    try:
        c = float(input("Enter the celsius temp"))
        break
    except:
        print("Invalid input , please enter an number")

fahr = celsius_to_fahrenheit(c)
print(f"The fahrenheit temp is {fahr} F°")

while True :
    try:
        temp_list = list(map(float ,input("Enter a list of temperatures(seprated by comma)").split(",") ) )
        break
    except:
        print("Invalid input , please enter an number")

scale = input("enter the scale (C/F)")
avg = average_temp(temp_list , scale)
high = highest_temp(temp_list , scale)

if scale.lower() == "c":
    print(f"The average temperatures in celsius : {avg:.2f} C°")
    print(f"The average temperatures in fahrenheit : {celsius_to_fahrenheit(avg):.2f} F°")
    print("===============")
    print(f"The Highest temperature in celsius : {high:.2f} C°")
    print(f"The Highest temperature in fahrenheit : {celsius_to_fahrenheit(high):.2f} F°")
else:
    print(f"The average temperatures in fahrenheit : {avg:.2f} F°")
    print(f"The average temperatures in celsius : {fahrenheit_to_celsius(avg):.2f} C°")
    print("===============")
    print(f"The Highest temperature in fahrenheit : {high:.2f} F°")
    print(f"The Highest temperature in celsius : {fahrenheit_to_celsius(high):.2f} C°")


