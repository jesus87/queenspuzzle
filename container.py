
import geneticAlgorithm as algorithm
import printer as printer
import readYaml as yamlFile
import storage as dbStorage

class Container:
    #Constructor
    def __init__(self,queens):
        self.__queens=queens

    def run(self):
        #First let's read our config file, in this case a yaml file
        yaml= yamlFile.ReadYaml()
        #Initialization of storage class, passing the configuration
        storage=dbStorage.Storage(yaml)
        #Initialization of the Genetic algorithm for seeking the solution
        genetic= algorithm.GeneticAlgorithm(self.__queens)
        #Finally , print the solution
        myPrinter= printer.Printer(genetic,storage)

        


        
