class Student:
    StudentCount = 0

    def __init__(self,StudentId = 0,StudentName = "",StudentPhone =""):
        self.StudentId = StudentId
        self.StudentName = StudentName
        self.StudentPhone = StudentPhone
        Student.StudentCount += 1

    def showCount(self):
        print("Total instances of Student is:",Student.StudentCount)

    def showData(self):
        print("Student Id is",self.StudentId)
        print("Student Name is", self.StudentName)
        print("Student Phone is", self.StudentPhone)

    def setData(self,StudentId = 0,StudentName = "",StudentPhone =""):
        self.StudentId = StudentId
        self.StudentName = StudentName
        self.StudentPhone = StudentPhone
        #Student.StudentCount += 1

class Science:
    def __init__(self,Physics = 0.0,Chemistry=0.0):
        self.Physics = Physics
        self.Chemistry = Chemistry

    def showData(self):
        print("Physics Marks is : ",self.Physics)
        print("Chemistry Marks is :",self.Chemistry)

    def setData(self,Physics = 0.0,Chemistry=0.0):
        self.Physics = Physics
        self.Chemistry = Chemistry

class Results(Student,Science):
    def __init__(self,StudentId = 0,StudentName = "",StudentPhone = "",Physcis = 0.0,Chemistry = 0.0):
        Student.__init__(self,StudentId,StudentName,StudentPhone)
        Science.__init__(self,Physcis,Chemistry)

        self.total = Physcis + Chemistry
        self.percentage = self.total/200 * 100

    def setData(self,StudentId = 0,StudentName = "",StudentPhone ="",Physics = 0.0,Chemistry = 0.0):
        Student.__init__(self, StudentId, StudentName, StudentPhone)
        Science.__init__(self, Physics, Chemistry)
        self.total = Physics + Chemistry
        self.percentage = self.total / 200 * 100

    def showData(self):
        Student.showData(self)
        Science.showData(self)
        print("Total Marks :",self.total)
        print("Percentage :",self.percentage)

a = Results(1,"Shreyash","344534334",89.9,90.6)
a.showData()
a.showCount()
