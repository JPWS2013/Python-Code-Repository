import addresscardclass as addcard
class AddressBook:
    def __init__(self, bookname='noname', thebook=[]  ):
        self.name=bookname
        self.book=thebook
        self.contactnamelist=[]
        
    
    def addcard(self, theCard):
        self.book.append(theCard)
        self.contactnamelist.append(theCard.name)
        
    def entries(self):
        len(self.book)
        
    def list(self):
        for i in range (0, len(self.book)):
            print self.book[i].name
            print self.book[i].email
            print ' '
    
    def listnameonly(self):
        for i in range (0, len(self.book)):
            print self.book[i].name
            print ' '
    
    def search(self, name='0'):
        if (name=='0'):
            print 'You have not entered a name to search for'
        
        for j in range (0, len(self.book)):
            if name.lower()==self.book[j].name.lower():
                print self.book[j].name
                print self.book[j].email
                
        print 'No name found'