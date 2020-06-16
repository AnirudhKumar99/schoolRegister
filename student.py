class Student:
    def __init__(self, name, standard, section, rollNo, subs):
        self.name = name
        self.standard = standard
        self.section = section
        self.rollNo = rollNo
        self.markList = {}

        self.avg = 0
        self.passStatus = '-'

        self.subs = subs
        for sub in subs:
            self.markList[sub] = None

    def enterMarks(self, markList=None):
        ''' Takes mark list dictionary or enter marks of each sub individually.'''
        if(type(markList) == type({})):
            self.markList = markList
        else:
            for sub in self.subs:
                print(f'Enter marks in {sub}:')
                marks = float(input())
                self.markList[sub] = marks

        self.passStatus = 'Pass'
        for sub in self.subs:
            if(self.markList[sub] <= 35):
                self.passStatus = 'Fail'

        if(self.passStatus == 'Pass'):
            for sub in self.subs:
                self.avg += self.markList[sub]
            self.avg /= len(self.markList)