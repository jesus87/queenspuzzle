

import random
import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

class GeneticAlgorithm:
    
    #   Constructor
    def __init__(self,queens):
        self.__queens = queens
        self.__toolbox = base.Toolbox()
        self.__problemDefinition()
        self.__toolboxDefinition()
        self.__initPoblation()
        self.__evaluationPoblation()
        self.__geneticOperators()
        self.__run()

        
     #   Problem definition
    def __problemDefinition(self):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

    #   registration of function -- this is going to be our toolbox
    def __toolboxDefinition(self):
        self.__toolbox.register("permutation", random.sample, range(self.__queens), self.__queens)

    #   Individual and Poblation Initialization
    def __initPoblation(self):
       self.__toolbox.register("individual", tools.initIterate, creator.Individual, self.__toolbox.permutation)
       self.__toolbox.register("population", tools.initRepeat, list, self.__toolbox.individual)
     #   Evaluation function
    def __evaluationPoblation(self):
        self.__toolbox.register("evaluate", self.__qualificateQueens)
      #   Genetic Operators
    def __geneticOperators(self):
        self.__toolbox.register("mate", tools.cxPartialyMatched)
        self.__toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/self.__queens)
        self.__toolbox.register("select", tools.selTournament, tournsize=3)

    #   Qualification Function
    def __qualificateQueens(self,particular):
        #    The first step is to evaluate the problem.
        #    In this function of evaluation let's calculate the numbers of queens on the diagonal.
        #    This is calculated like R-1
        #
        #############################################################################
        definedSize = len(particular)
        left_right_diagonal = [0] * (2*definedSize-1)
        right_left_diagonal = [0] * (2*definedSize-1)
        
        # this is the numbers of queens in each diagonal
        for value in range(definedSize): # iterate the rows
            left_right_diagonal[value+particular[value]] += 1 
            right_left_diagonal[definedSize-1-value+particular[value]] += 1
        
        # this is the numbers of attacks in each diagonal
        total = 0
        for value in range(2*definedSize-1): # iterate the diagonals
            if left_right_diagonal[value] > 1: # are there attacks?
                total += left_right_diagonal[value] - 1 # atttacks n-1
            if right_left_diagonal[value] > 1:
                total += right_left_diagonal[value] - 1
        return total,
    #   Run Process 
    def __run(self):
        seed=0
        random.seed(seed)
        pop = self.__toolbox.population(n=300)
        hof = tools.HallOfFame(1) # storage the best individual
        stats = tools.Statistics(lambda ind: ind.fitness.values) # statics calculation
        stats.register("Avg", numpy.mean)
        stats.register("Std", numpy.std)
        stats.register("Min", numpy.min)
        stats.register("Max", numpy.max)
        algorithms.eaSimple(pop, self.__toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True) # genetic algorithm "black box"
        self.__population=pop
        self.__stats= stats
        self.__hof= hof
    @property
    def population(self):
        return self.__population
    @property
    def theBest(self):
        return self.__hof
    @property
    def stats(self):
        return self.__stats
    @property
    def queens(self):
        return self.__queens

        


        
        