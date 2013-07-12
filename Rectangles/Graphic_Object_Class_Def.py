class GraphicObject:
    def __init__(self, filcol=0, fild=0, lincol=0, origX=0, origY=0):
        self.fillcolor=filcol
        self.filled=fild
        self.line_color=lincol
        self.originX=origX
        self.originY=origY
        
    def translate(self,x,y):
        x=float(x)
        y=float(y)
        self.originX=self.originX+x
        self.originY=self.originY+y
        print 'This ', self.__class__.__name__, ' is now located at Co-Ordinates X= ', self.originX,', Y= ', self.originY
        
        
    def displaycoord(self):
        print 'This ', self.__class__.__name__, ' is located at Co-Ordinates X= ', self.originX,', Y= ', self.originY