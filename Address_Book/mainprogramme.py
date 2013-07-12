import addresscardclass as addcard
import addressbookclass as addbook

#NEXT TASK: COMPARTMENTALIZE EACH MENU OPTION INTO A SEPARATE MODULE

user_select=0
addressbookstoragebin=[]
booknametracker=[]

print 'Welcome to the address book application!'
print ' '

while (user_select !='9'):

    print 'Select what you would like to do from the menu below:'
    print ' '
    print '1. Create new address book'
    print '2. Display all existing address books'
    print '3. Delete an address book'
    print '4. Create a new contact'
    print '5. Display all contacts in an address book'
    print '6. Display all contact info for a contact'
    print ' '
    user_select=raw_input("") 
    
    if (user_select=='1'):
        
        newname=raw_input("Enter a name for this new address book:")
        newbook=addbook.AddressBook(newname)
        booknametracker.append(newname)
        addressbookstoragebin.append(newbook)
        
        print "Your new address book, ", newname, " has been created!"
        print ' '
        
    if (user_select=='2'):
        
        if not addressbookstoragebin:
            print ' '
            print "No address books exist"
            print ' '
            
        else:
            for i in range (0,len(addressbookstoragebin)):
                print addressbookstoragebin[i].name
                
    if (user_select=='3'):
        
        print ' '
        deleteoption=raw_input("Please enter the name of the address book you wish to delete")
        print ' '
        
        if deleteoption in booknametracker:
            positiondetermined=booknametracker.index(deleteoption)
            del addressbookstoragebin[positiondetermined]
            del booknametracker[positiondetermined]
        
        else:
            print ' '
            print "Your selected address book was not found"
            print ' '
            
    if (user_select=='4'):
        
        print ' '
        newname=raw_input("Please enter the name of the new contact you would like to create: ")
        
        newcard=addcard.AddressCard(newname)
        
        print ' '
        print 'We will now proceed to collect contact information from you.'
        print ' '
        
        addcardselector=0
        addcardselector=raw_input("Would you like to add a phone number? Y/N")
        
        if (addcardselector=='Y' or addcardselector=='y'):
            newphonenumber=raw_input("Please enter the phone number: ")
            newcard.setPhone(newphonenumber)
        
        addcardselector=0
        addcardselector=raw_input("Would you like to add an email address? Y/N")
        
        if (addcardselector=='Y' or addcardselector=='y'):
            newemail=raw_input("Please enter the email address: ")
            newcard.setEmail(newemail)
            
        ddcardselector=0
        addcardselector=raw_input("Do you need to change the name? Y/N")
        
        if (addcardselector=='Y' or addcardselector=='y'):
            newname=raw_input("Please enter the new name: ")
            newcard.setName(newname)
            
        print ' '
        selectedaddressbook=raw_input("Finally, which address book would you like to add this new contact to? ")

        if selectedaddressbook in booknametracker:
            positiondetermined=booknametracker.index(selectedaddressbook)
            addressbookstoragebin[positiondetermined].addcard(newcard)
            print "A new contact was created for ", addressbookstoragebin[positiondetermined].book[len(addressbookstoragebin[positiondetermined].book)-1].name
            
        else:
            print "Address book not found"
    
    if (user_select=='5'):
        
        print ' '
        addressbookdisplayselector=raw_input("Please enter the address book which you would like to view all contacts: ")
        print ' '
        
        if addressbookdisplayselector in booknametracker:
            positiondetermined=100000000;
            positiondetermined=booknametracker.index(addressbookdisplayselector)
            addressbookstoragebin[positiondetermined].listnameonly()
            
        else:
            print "Address book not found"
            
    if (user_select=='6'):
        
        print ' '
        addressbookchoice=raw_input("Please tell us which address book this contact is in")
        print ' '
        
        if addressbookchoice in booknametracker:
            positiondetermined=booknametracker.index(addressbookchoice)
            
            contactchoice=raw_input("Please tell us which contact you would like to display")
            print ' '
        
            if contactchoice in addressbookstoragebin[positiondetermined].contactnamelist:
                positiondetermined2=addressbookstoragebin[positiondetermined].contactnamelist.index(contactchoice)
                
                print "Name: ", addressbookstoragebin[positiondetermined].book[positiondetermined2].name
                print "Phone: ", addressbookstoragebin[positiondetermined].book[positiondetermined2].phone
                print "Email: ", addressbookstoragebin[positiondetermined].book[positiondetermined2].email
                
            else:
                print "The contact you entered was not found"
                print ' '
                
        else: 
            print "The address book you entered was not found"
            print ' '
            
            