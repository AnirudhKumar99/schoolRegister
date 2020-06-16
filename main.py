from school import School


school = School()
while True:
    print('''
    Enter a choice
    1   -   Add a class
    2   -   Add a student
    3   -   Show register of a class
    4   -   Edit student details    
    q   -   Quit
    ''')
    choice = input()
    if(choice == 'q'):
        break
    if(choice == '1'):
        school.createClassRoom()
    if(choice == '2'):
        school.addStudent()
    if(choice == '3'):
        clss = school.getClassRoom()
        if(clss != None):
            clss.displayRegister()
    if(choice == '4'):
        # print('edit student details')
        clss = school.getClassRoom()
        if(clss != None):
            print('Enter rollNo')
            rollNo = input()
            stu = clss.getStudent(rollNo)
            stu.enterMarks()
