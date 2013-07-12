width=10
height=3
x=0
y=0

def printwidth(width, x):
    if (width==0):
        pass

    else:
        for k in range (x-1):
            print ' ',
        for i in range(width-1):
            print '-',
        print '-'
    
def printheight(height, x):
    if (height==0):
        pass

    else:
        for j in range(height):
            
            for k in range (x-1):
                print ' ',
                
            print '|',
    
            for i in range (width-2):
                print ' ',
            
            print '|'


    
if (y<0):
    if ((y+height)==0):
        pass
    else
    for L in range(y+height):
        print ' '
            
    printwidth(width,x)

    printheight(height,x)
    
    printwidth(width,x)
            
elif(gap>0):
    printwidth(width,x)

    printheight(height,x)
    
    printwidth(width,x)
    
    for L in range(y-height):
        print ' '