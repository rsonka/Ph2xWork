'''Rita Sonka
10/24/2016
Ph 20
hw 4
'''

import numericalSpring as nS
import sys

graphicsFolder = sys.argv[1] #"../week3Graphics/"


# Figure 6
nS.plotImplicitEulerErrors(0, 5, .2, 100, graphicsFolder + "implicitEulerErrors1.pdf")

