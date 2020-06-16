from classRoom import ClassRoom

class School:
    def __init__(self):
        self.classRooms = {}

    def createClassRoom(self, classId=None):
        if classId == None:
            print('Enter class standard (1-10) :')
            standard = input()
            while(standard not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
                print('Enter valid class standard (1-10) :')
                standard = input()
            print('Enter section name (A-E) :')
            section = input()
            while(section not in ['A', 'B', 'C', 'D', 'E']):
                print('Enter valid section name (A-E) :')
                section = input()
            classId = standard+section
        if(classId not in self.classRooms.keys()):
            standard = classId[:-1]
            section = classId[-1]
            self.classRooms[classId] = ClassRoom(standard, section)
        else:
            print('Class already exists with that name')
        return True

    def getClassRoom(self):
        print('Enter class standard (1-10) :')
        standard = input()
        print('Enter section name (A-E) :')
        section = input()
        classId = standard+section
        try:
            return self.classRooms[classId]
        except KeyError:
            print('Class Room does not exist with that name')
            return None

    def addStudent(self):
        '''Take in student details and add it to respective class'''
        print('Enter student particulars')
        print('Name:')
        name = input()
        print('Roll No:')
        rollNo = input()
        print('Standard(1-10):')
        standard = input()
        print('Section(A-E):')
        section = input()
        classId = standard+section
        while(classId not in self.classRooms.keys()):
            print('Class Room does not exist with that name')
            print('Do you want to create a new class room with that name? Enter (y/n)')
            ch = input()
            while(True):
                if(ch == 'y'):
                    self.createClassRoom(classId)
                    break
                elif(ch == 'n'):
                    print('Then enter valid class details')
                    print('Vaild standard(1-10):')
                    standard = input()
                    print('valid section(A-E):')
                    section = input()
                    classId = standard+section
                    break
                else:
                    print('Enter (y/n)')
                    ch = input()
                    continue
        classRoom = self.classRooms[classId]
        classRoom.addStudent(name, rollNo)
