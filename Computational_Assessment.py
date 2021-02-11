#Refactored the data to be easier to work with
#Removed the headings because they are useless

########################################################################################################################################################################################################

#FIX ERRORS OUT THE ASS 
#DISPLAU REGRESSION ON GRAPH

import math
import numpy
from numpy.core.fromnumeric import amax, amin
from scipy.sparse.bsr import bsr_matrix
from sklearn.linear_model import LinearRegression #Shit
import matplotlib.pyplot as plt # Graph plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.optimize as optimization

class program:  
  def func(self, x, a, b):
    return a + b*b*x

  def regression(self, fCoerc, fMag): # Regression Method
    # Create toy data for curve_fit.
    xdata = numpy.array([0.0,1.0,2.0,3.0,4.0,5.0])
    ydata = numpy.array([0.1,0.9,2.2,2.8,3.9,5.1])
    sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])

    # Compute chi-square manifold.
    Steps = 101  # grid size
    Chi2Manifold = numpy.zeros([Steps,Steps])  # allocate grid
    amin = -7.0  # minimal value of a covered by grid
    amax = +5.0  # maximal value of a covered by grid
    bmin = -4.0  # minimal value of b covered by grid
    bmax = +4.0  # maximal value of b covered by grid
    for s1 in range(Steps):
        for s2 in range(Steps):
            # Current values of (a,b) at grid position (s1,s2).
            a = amin + (amax - amin)*float(s1)/(Steps-1)
            b = bmin + (bmax - bmin)*float(s2)/(Steps-1)
            # Evaluate chi-squared.
            chi2 = 0.0
            for n in range(len(xdata)):
                residual = (ydata[n] - func(xdata[n], a, b))/sigma[n]
                chi2 = chi2 + residual*residual
            Chi2Manifold[Steps-1-s2,s1] = chi2  # write result to grid.

    # Plot grid.
    plt.figure(1, figsize=(8,4.5))
    plt.subplots_adjust(left=0.09, bottom=0.09, top=0.97, right=0.99)
    # Plot chi-square manifold.
    image = plt.imshow(Chi2Manifold, vmax=50.0,
              extent=[amin, amax, bmin, bmax])
    # Plot where curve-fit is going to for a couple of initial guesses.
    for a_initial in -6.0, -4.0, -2.0, 0.0, 2.0, 4.0:
        # Initial guess.
        x0   = numpy.array([a_initial, -3.5])
        xFit = optimization.curve_fit(func, xdata, ydata, x0, sigma)[0]
        plt.plot([x0[0], xFit[0]], [x0[1], xFit[1]], 'o-', ms=4,
                 markeredgewidth=0, lw=2, color='orange')
    plt.colorbar(image)  # make colorbar
    plt.xlim(amin, amax)
    plt.ylim(bmin, bmax)
    plt.xlabel(r'$a$', fontsize=24)
    plt.ylabel(r'$b$', fontsize=24)
    plt.savefig('demo-robustness-curve-fit.png')
    plt.show()

  def readFile(self): # File reading method
    string_without_line_breaks = ""
    a_file = open("Coercivity_Mag_Data.dat", 'r')

    for line in a_file: # Goes through each line in the file and removes the /n
      stripped_line = line.rstrip()
      string_without_line_breaks += stripped_line

    a_file.close() # Closes the file

    NewData = string_without_line_breaks.split(":") #Splits the string into an array
    NewData.pop() # Removes the last empty value which appeared for some reason

    Coercivity = [] # Declares 2 arrays for Coercivity and Magnetisation
    Magnetisation = []
    Coercivity = NewData[::2] # Starts at the first element and does every other element after
    Magnetisation = NewData[1::2] # Starts at the second element, then every other

    self.regression(Coercivity, Magnetisation) #Calls the regression method

newProgram = program()
newProgram.readFile()