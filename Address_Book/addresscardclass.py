class AddressCard:
    def __init__(self, theName='None', thePhone='None', theEmail='None'):
        self.name=theName
        self.email=theEmail
        self.phone=thePhone
    
    def setName(self, theName):
        self.name=theName
        
    def setEmail(self, theEmail):
        self.email=theEmail
        
    def setPhone(self, thePhone):
        self.phone=thePhone
    
    def setboth(self, theName, theEmail):
        self.name=theName
        self.email=theEmail    
                
    def name(self):
        return self.name
    
    def email(self):
        return self.email
        
    def printit(self):
        print "==================================================================="
        print "|                                                                 |"
        print self.name
        print self.email
        print "|                                                                 |"
        print "==================================================================="
        