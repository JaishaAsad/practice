'''
**********************STUDENT MANAGEMENT SYSTEM**************************
**This Program adds, deletes, and searches a student from in-memory list repository
'''
students = []
while True:
    print('Press 1 to add student')
    print('press 2 to find student')
    print('press 3 to delete student')
    print('press 4 to exit!')
    print('press 5 to check num of students enrolled')
    choice = int(input('Enter your choices'))
    if choice == 1:
        student = {}
        student['name']= input ('please enter student name:')
        student['father name']= input ('please enter father name:')
        student['cell number']= input('please enter cell number:')
        students.append(student)
    elif choice == 2:
        a=input('enter name which you wish to find')
        for i in students:
            if 
    elif choice == 4:
        break
    elif choice == 5:
        print('we currently have'+ str(len(students))+'students')
    elif choice == 2:
        name = input('enter the name you want to search for!')
        for student in students:
            if student['name'].lower()== name.lower():
                print('student with name'+name+ 'found and details are as follows')
                print(students)