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
    while True:
            name = input("Enter the student name : ")
            cleaned = name.strip().replace(" ","")
            if cleaned == "" :
                    print("Name couldn't be empty")
            elif not cleaned.isalpha() :
                    print("Name couldn't contain numbers or symbols")
            else:
                    break

    while True:
            try :
                age  = int(input("Enter the age : "))
                break
            except:
                print("Invalid age")

    while True:
            try:
                scores = list(map (int ,input("Enter the scores (seprated by space): ").split())) 
                break 
            except:
                print("Score must be between (0-100)")
    
    info = (age , scores)

    students_data.update( { name : info} )
    save_to_file(name,age,scores)

    print(f"{name} added and saved successfully")

def normalize(n):
    return n.lower().strip().replace(" " , "")

def show_student_info(name):
    search = normalize(name)
    for n , t in students_data.items():
        if normalize(n) == search:
            age = t[0]
            scores = t[1]
            print(f"Name   : {n}\n")
            print(f"Age    : {age}\n")
            print(f"Scores : {scores}\n")
            return

    print(f"{name} Not found")

students_averge = {}
# name , averge

def calc_average():
    for n , t in students_data.items() :
        total = sum(t[1])
        averge = total/len(t[1])
        students_averge[n] = averge

def print_students_averge():
    calc_average()
    print(students_averge.items())

def list_by_average():
    try:
        min_avg = int(input("Enter the minimum averge you want to list the students based on : "))
    except:
        print("Please enter a number ")
        return

    
    calc_average()

    print(f"Students above {min_avg} :\n")
    
    for name , avg in students_averge.items():
        if avg >= min_avg :
            print(f"{name} -> {avg}\n")


def main():
    print("Student Managment System\n".center(60))
    print("========================\n".center(60))

    while True:
        print("1.Add student")
        print("2.Show student info")
        print("3.Show students averge")
        print("4.List students based on certain average")
        print("5.read from file")
        print("6.Exit")
        option = input("Choose an option")

        if option == "1":
            add_student()
        elif option=="2" :
            x = input("Enter the student's name : ")
            show_student_info(x)
        elif option=="3" :
            print_students_averge()
        elif option=="4" :
            list_by_average()
        elif option=="5" :
            read_from_file()
        else:
            break

main()