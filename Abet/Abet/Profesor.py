
class Profesor(Recinto):
    def __init__(self,firstName,lastName):
        self.firstName="Juan"
        self.lastName="Vazquez Del Valle"

    def getFirstName(self):
        return self.firstName
    def getLastname(self):
        return self.lastName
    def setFirstName(self, firstName):
        self.firstName=firstName
    def setLastName(self,lastName):
        self.lastName=lastName

