from students.students import students
from teachers.teachers import teachers
from course.course import course

s1 = students(78,"Sama" , "CS")
t1 = teachers(40 , "Dr.Kareem" , "IT")

c1 = course(3 , "Computer vision", t1)
s1.enroll(c1)

print(f"{s1.name} enrolled in {s1.course.title}")