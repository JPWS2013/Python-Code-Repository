from Rectangles_Class_Def import *

class square(Rectangle):
        def __init__(self, s=0):
            GraphicObject.__init__(self, filcol=0, fild=0, lincol=0, origX=0, origY=0)
            s=float(s)
            self.width=s
            self.height=s
            
        def setwidthandheight (self, s):
            self.width=s
            self.height=s
            
            print "You have set the width to %f and the height to %f" % (self.width, self.height)