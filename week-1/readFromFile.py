#create , write
with open("data.txt" , "w")as f:
    f.write("my name is Basmala\n")
    f.write("I study at Zag university\n")
    f.write("Programing is nice thing and complex in same time\n")
    f.write("Python is intersting\n")

#read
#with open(r"C:\Zag-Eng-AI-2026\week-1\data.txt" , "r") as f:
#read whole file
    #print(f.read())       
# read first line        
    #print(f.readline())           

# read 3rd line
    #lines = f.readlines()
    #print(lines[2].strip())        
    
# another way
    # i = 0
    # for line in f:
    #     if i==2:
    #         print(line.strip())
    #         break
    #     else:
    #         i+=1

#append list to file
hobbies=[]
n = int(input("How many hobbies you have?"))
print("\nWhat's your hoppies?(seperated by new line)\n")
for i in range(n):
    hobbies.append(input().strip())

with open("data.txt","a") as f:
    f.write("My hobbies are : \n")
    for h in hobbies:
        f.write(h +"\n")


