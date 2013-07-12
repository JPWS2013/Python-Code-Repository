from Graphic_Object_Class_Def import *

class Rectangle(GraphicObject):
    def __init__(self, w=0, h=0):
        GraphicObject.__init__(self, filcol=0, fild=0, lincol=0, origX=0, origY=0)
        w=float(w)
        h=float(h)
        self.width=w
        self.height=h
        
    def setwidthandheight (self, w, h):
        self.width=w
        self.height=h
        
        print "You have set the width to %f and the height to %f" % (self.width, self.height)
        
    def specs(self):
        print 'Width is: ', self.width
        print 'Height is: ', self.height
        
    def area(self):
        self.area=self.width*self.height
        
        print 'The area of this ', self.__class__.__name__, ' is: ', self.area
        
        