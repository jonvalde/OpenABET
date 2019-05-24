class Student():
    def __init__(self, first_name, last_name, studentID, gpa, sectionID):
        self.first_name = first_name
        self.last_name = last_name
        self.studentID = studentID
        self.gpa = gpa
        self.sectionID = sectionID

    def setFirstname(self, first_name):
        self.first_name = first_name

    def setLastname(self, last_name):
        self.last_name = last_name

    def setId(self, studentID):
        self.studentID = studentID

    def setGPA(self, gpa):
        self.gpa = gpa

    def getFirstname(self):
        return self.first_name

    def getLastname(self):
        return self.last_name

    def getId(self):
        return self.studentID

    def getGPA(self):
        return self.gpa

    def setSectionID(self, sectionID):
        self.sectionID = sectionID

    def getSectionID(self):
        return self.sectionID

    def __str__(self):
        return (self.first_name, self.last_name, self.studentID, self.gpa, self.sectionID)