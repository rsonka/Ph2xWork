'''Rita Sonka
10/24/2016
Ph 20
hw 4
'''

import numericalSpring as nS
import sys

graphicsFolder = sys.argv[1] #"../week3Graphics/"


# Figure 8 (actually two files)
nS.eE_iE_phaseSpace(0, 5, .2, 100, graphicsFolder + "eE_phaseSpace.pdf", graphicsFolder + "iE_phaseSpace.pdf")


