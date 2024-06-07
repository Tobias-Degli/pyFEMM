import femm
import math
import numpy as np 
import matplotlib.pyplot as plt 

from req import *
from draw_enclosure import *

# Opens FEMM
femm.openfemm(1)
femm.newdocument(2)



################ ---- FEMM initializaiton ---- ################


# Defines the problem
femm.hi_probdef('meters', 'planar', 1.e-8, problemDepth, 20)
meshsize=5e-4 # A malha tem que ser um pouco menor que o menor componente

draw_enclosure()

#-------------------------------------------------------------------

# Materials
femm.hi_addmaterial('Al',226 ,226 ,0)   #W/(mK) #
femm.hi_addmaterial('Air',0.026,0.026,0)   #W/(mK)
femm.hi_addmaterial('Sylgard',0.39,0.39,0)   #W/(mK) 
femm.hi_addmaterial('Copper',413 ,413 ,0)  # W/(mK)
femm.hi_addmaterial('ThermalPaste',12.8 ,12.8 ,0)  # W/(mK)
femm.hi_addmaterial('Heater',5,5 ,Q_ger) # W/(mK), W/m³

# Boundary conditions
femm.hi_addboundprop('convectionToAmbient',2,0,0,40,7,0); # Ar externo a 40° e h=7
femm.hi_addboundprop('prescribedFixingTemperature',0,40,0,0,0,0); # Ar externo a 40° e h=7

# Apply Materials to regions
# Board
femm.hi_addblocklabel(0.5*(x9+x11),0.5*(y9+y11))
femm.hi_selectlabel(0.5*(x9+x11),0.5*(y9+y11))
femm.hi_setblockprop('Heater',0,meshsize,0)
femm.hi_clearselected()
# Heater
femm.hi_addblocklabel(0.5*(x1+x5),0.5*(y1+y5))
femm.hi_selectlabel(0.5*(x1+x5),0.5*(y1+y5))
femm.hi_setblockprop('Copper',0,meshsize,0)
femm.hi_clearselected()
    
# Apply the boundary conditions to contours
femm.hi_selectsegment(0.5*(x1+x2),y1)
femm.hi_setsegmentprop('prescribedFixingTemperature',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectarcsegment(0.5*(x2+x3),0.5*(y2+y3))
femm.hi_setarcsegmentprop(30,'convectionToAmbient',0,0,'<None>');
femm.hi_clearselected()

femm.hi_selectsegment(0.5*(x3+x4),0.5*(y3+y4))
femm.hi_setsegmentprop('convectionToAmbient',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectsegment(0.5*(x4+x5),0.5*(y4+y5))
femm.hi_setsegmentprop('convectionToAmbient',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectsegment(0.5*(x5+x6),0.5*(y5+y6))
femm.hi_setsegmentprop('convectionToAmbient',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectsegment(0.5*(x6+x7),0.5*(y6+y7))
femm.hi_setsegmentprop('convectionToAmbient',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectsegment(0.5*(x7+x8),0.5*(y7+y8))
femm.hi_setsegmentprop('convectionToAmbient',meshsize,1,0,0,'<None>')
femm.hi_clearselected()

femm.hi_selectarcsegment(0.5*(x8+x1),0.5*(y8+y1))
femm.hi_setarcsegmentprop(30,'convectionToAmbient',0,0,'<None>');
femm.hi_clearselected()

# the file has to be saved before it can be analyzed.
femm.hi_saveas('auto-htutor.feh');

femm.hi_analyze()
# view the results
femm.hi_loadsolution()

femm.closefemm()
