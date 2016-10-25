'''Rita Sonka
10/24/2016
Ph 20
hw 4
'''

import numericalSpring as nS
import sys

graphicsFolder = sys.argv[1] #"../week3Graphics/"

# Figure 1
nS.plotExplicitEuler(0, 5, .2, 100, graphicsFolder + "explicitEuler1.pdf")

