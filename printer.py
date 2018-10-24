

import numpy
import matplotlib.pyplot as plotter
class Printer:
    #   Constructor
    def __init__(self,genetic,storage):
        self.__genetic= genetic
        self.__storage=storage
        self.__print()
    #   function to print and storage the solution
    def __print(self):
        valy = self.__genetic.theBest[0]
        valx= range(self.__genetic.queens)
        valx= numpy.array(valx)
        valy = numpy.array(valy)
        valx = valx + 0.5
        valy = valy + 0.5 
        # Here let's storage de Results
        self.__storage.insert(self.__genetic.queens,self.__genetic.theBest,valx,valy)
        plotter.figure()
        plotter.scatter(valx,valy)
        plotter.xlim(0,self.__genetic.queens)
        plotter.ylim(0,self.__genetic.queens)
        plotter.xticks(valx-0.5)
        plotter.yticks(valx-0.5)
        plotter.grid(True)
        plotter.title(u" Eight Queens Puzzle: Solution for "+str(self.__genetic.queens)+" Queens")
        plotter.show()
          