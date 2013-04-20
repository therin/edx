# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
   Runs simulations and make histograms for problem 1.
 
   Runs numTrials simulations to show the relationship between delayed
   treatment and patient outcome using a histogram.
 
   Histograms of final total virus populations are displayed for delays of 300,
   150, 75, 0 timesteps (followed by an additional 150 timesteps of
   simulation).
 
   numTrials: number of simulation runs to execute (an integer)
   """
 
    # TODO
 
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
 
    delays = [300,150,75,0]
    results = []
 
    for delay in delays:
        for i in range(numTrials):
            virusList = []
            virusPop = 0
            for j in range(numViruses):
                virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            my_patient = TreatedPatient(virusList, maxPop)
 
            for step in range(delay + 150):
                if step == delay:
                    my_patient.addPrescription('guttagonol')
                virusPop = my_patient.update()
            results.append(virusPop)
 
    toPlot = []
    for i in range(0,len(results),numTrials):
        toPlot.append(results[i:i+numTrials])
    print toPlot
 
    for i in range(len(delays)):
        pylab.subplot(2,2,i+1)
        pylab.hist(toPlot[i])
    pylab.show()


simulationDelayedTreatment(300)
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
