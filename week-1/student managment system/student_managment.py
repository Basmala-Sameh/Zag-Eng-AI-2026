students_data = {}

def save_to_file(name , age , scores):
    with open ("students.txt" , "a") as file :
        scores_str = " ".join( map(str,scores) )
        file.write( f"{name},{age},{scores_str}\n")

def read_from_file():
    with open("students.txt" , "r") as file:
        data = file.read()
        print(data)

def add_student():
    try:
        name = input("Enter the student name : ")
    except:
        print("Please enter a text")

    try :
        age  = int(input("Enter the age : "))
    except:
        print("Invalid age")

    try:
        scores = list(map (int ,input("Enter the scores (seprated by space): ").split())) 
    except:
        print("Score must be between (0-100)")
    
    info = (age , scores)

    students_data.update( { name : info} )
    save_to_file(name,age,scores)

    print(f"{name} added and saved successfully")









