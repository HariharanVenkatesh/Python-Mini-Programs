#Excersice no 17 - Students marks to grade Using Dictionary

Students_Marks = {
    'Hariharan':92,
    'Aswin':85,
    'Caleb':73,
    'Abi':65,
    'Shajith':56,
    'Dravid':45,
    'Pradeep':34,
    'Sarvesh':99
}
students_Grades = {}
for Student in Students_Marks:
    Marks = Students_Marks[Student]
    if Marks > 90:
        students_Grades[Student] = "A+"
    elif Marks > 80:
        students_Grades[Student] = "A"
    elif Marks >70:
        students_Grades[Student] = "B+"
    elif Marks >60:
        students_Grades[Student] = "B"
    elif Marks >50:
        students_Grades[Student] = "c"            
    elif Marks >40:
        students_Grades[Student] = "D"  
    else:
        students_Grades[Student] = "F"       
print(students_Grades)                           

