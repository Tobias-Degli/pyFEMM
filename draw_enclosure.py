import femm

from req import *

def draw_enclosure():
    
    # Draw outside contour
    femm.hi_drawline(x1,y1,x2,y2)
    femm.hi_drawarc(x2,y2,x3,y3,angle_2_3,1)
    femm.hi_drawline(x3,y3,x4,y4)
    femm.hi_drawline(x4,y4,x5,y5)
    femm.hi_drawline(x5,y5,x6,y6)
    femm.hi_drawline(x6,y6,x7,y7)
    femm.hi_drawline(x7,y7,x8,y8)
    femm.hi_drawarc(x8,y8,x1,y1,angle_8_1,1)
    
    # Draw heater element
    femm.hi_drawrectangle(x9,y9,x11,y11)
    #femm.hi_drawarc(-x1_a,y1_a,x2_a,y2_a,angle_a,1)
    return()