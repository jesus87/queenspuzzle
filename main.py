# Eight Queens Puzzle
#   The solution was made it using Genetics Alogorithm with python library DEAP
#   Printing was made it using Pyplot library
#   Storage was made it using SQLAlchemy
#Resources: 
# Deap, Creating Individuals:  https://deap.readthedocs.io/en/master/tutorials/basic/part2.html
# Deap, Permutation and Populations :  https://deap.readthedocs.io/en/master/tutorials/basic/part1.html#permutation
# Deap, Permutation and Populations :  https://deap.readthedocs.io/en/master/tutorials/basic/part1.html#permutation
# Pyplot,How to Use Pyplot  https://matplotlib.org/users/pyplot_tutorial.html
# SqlAlchemy, How to Create and Insert data in postgress with sqlalchemy https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
#Dependencies:
#   Dependencies for this project were added on requierements.txt
#############################################################################


import container as container
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
if __name__ == "__main__":
    inputFromBoard = input('Please Type the Numbers of Board/Queens: ')
    numberOfQueens,ok=intTryParse(inputFromBoard)
    if ok:
        print('We are working on ', numberOfQueens, ' Queens')
        _container= container.Container(numberOfQueens)
        _container.run()
    else:
        print('Please type a correct Int Number')    

