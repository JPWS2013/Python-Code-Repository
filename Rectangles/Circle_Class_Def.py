from Graphic_Object_Class_Def import *

class circle(GraphicObject):
        def __init__(self, r=0):
            GraphicObject.__init__(self, filcol=0, fild=0, lincol=0, origX=0, origY=0)
            r=float(r)
            self.radius=r
            
        def setwidthandheight (self, r):
            self.radius=r
        
            print "You have set the rdius to ", self.radius
        
        def specs(self):
            print 'The radius is: ', self.radius
        
        def area(self):
            self.area=3.14159*self.radius*self.radius
        
            print 'The area of this ', self.__class__.__name__, ' is: ', self.area