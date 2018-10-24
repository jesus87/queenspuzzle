from sqlalchemy import create_engine


class Storage:
    #Constructor
    def __init__(self,readYaml):
        self.__dbString="postgres://"+readYaml.user+":"+readYaml.password+"@"+readYaml.host+":"+readYaml.port+"/"+readYaml.dbName
        self.__db=create_engine(self.__dbString)
        self.__createTable()
    #if table does not exist , we create it
    def __createTable(self):
        self.__db.execute("CREATE TABLE IF NOT EXISTS solution (queens integer, responses text, xvalues text,yvalues text,runedat timestamp with time zone DEFAULT now())")  
    #insert the values on postgress
    def insert(self,queens,responses,xvalues,yvalues):
        self.__db.execute("INSERT INTO solution (queens, responses, xvalues,yvalues) VALUES ("+str(queens)
        +", '"+str(responses)+"','"+str(xvalues)+"','"+str(yvalues)+"')")