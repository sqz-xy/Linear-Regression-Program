import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Refactored the data to be easier to work with
#Removed the headings because they are useless

########################################################################################################################################################################################################

#Reads the lines in the file
lines_in_file = open("Coercivity_Mag_Data.dat", 'r').readlines()
number_of_lines = len(lines_in_file)

string_without_line_breaks = ""

a_file = open("Coercivity_Mag_Data.dat", 'r')

#Goes through each line in the file and removes the /n
for line in a_file:

  stripped_line = line.rstrip()

  string_without_line_breaks += stripped_line

a_file.close()

#Prints the string without "/n"
print(string_without_line_breaks)
#Splits the string into an array
NewData = string_without_line_breaks.split(":")
#Removes the last empty value which appeared for some reason
NewData.pop()

#Declares 2 arrays for Coercivity and Magnetisation
Coercivity = []
Magnetisation = []

Coercivity = NewData[::2] #Starts at the first element and does every other element after
Magnetisation = NewData[1::2] #Starts at the second element, then every other

print(Coercivity)
print(Magnetisation)

#Regression time



