from student import Student


class ClassRoom:
    def __init__(self, standard, section):
        self.standard = standard
        self.section = section
        self.students = {}
        self.subjects = ['Eng', 'Tel', 'Hin', 'Maths', 'Sci', 'Soc']

    def addStudent(self, name, rollNo):
        if(rollNo not in self.students.keys()):
            self.students[rollNo] = Student(
                name, self.standard, self.section, rollNo, self.subjects)
        else:
            print('A student already exists with that roll number try another number')

    def getStudent(self, rollNo):
        while(rollNo not in self.students.keys()):
            print('Student with that roll number does not exist')
            print('Do you want to create a student with that roll number Enter (y/n)')
            ch = input()
            while(True):
                if(ch == 'y'):
                    print('Enter student name:')
                    name = input()
                    self.addStudent(name, rollNo)
                    break
                elif(ch == 'n'):
                    print('Then enter valid roll number')
                    rollNo = input()
                    break
                else:
                    print('Enter (y/n)')
                    ch = input()
                    continue

        return self.students[rollNo]

    def displayRegister(self):
        print(f'Class of {self.standard}{self.section}')
        print('RollNo', end='\t')

        for sub in self.subjects:
            print(sub, end='\t')
        print('Name', end='\t')
        print('Status', end='\t')
        print('Avg', end='\t')
        print()
        for stu in self.students:
            student = self.students[stu]
            print(student.rollNo, end='\t')
            for sub in self.subjects:
                print(student.markList[sub], end='\t')
            print(student.name, end='\t')
            print(student.passStatus, end='\t')
            print(student.avg, end='\t')
            print()

