#Refactored the data to be easier to work with
#Removed the headings because they are useless

########################################################################################################################################################################################################

#FIX ERRORS OUT THE ASS 
#DISPLAU REGRESSION ON GRAPH

import math as mth
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class program:

  def displayGraph(self):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='beans time (s)', ylabel='bean (mV)',
       title='beans density, beans')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    
  def regression(self, fCoerc, fMag): #Regression Method
    X = fCoerc
    y = fMag

    model = LinearRegression()
    model.fit(X, y)

    X_predict = fMag
    y_precit = model.predict(X_predict)

  def readFile(self): #File reading method
    string_without_line_breaks = ""
    a_file = open("Coercivity_Mag_Data.dat", 'r')

    for line in a_file: #Goes through each line in the file and removes the /n
      stripped_line = line.rstrip()
      string_without_line_breaks += stripped_line

    a_file.close() #Closes the file

    NewData = string_without_line_breaks.split(":") #Splits the string into an array
    NewData.pop() #Removes the last empty value which appeared for some reason

    Coercivity = [] #Declares 2 arrays for Coercivity and Magnetisation
    Magnetisation = []
    Coercivity = NewData[::2] #Starts at the first element and does every other element after
    Magnetisation = NewData[1::2] #Starts at the second element, then every other

    self.regression(Coercivity, Magnetisation) #Calls the regression method

newProgram = program()
newProgram.displayGraph()
newProgram.readFile()
    







