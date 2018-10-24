import yaml


class ReadYaml:
    #Constructor
    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            self.__user=cfg['database']["user"]
            self.__password=cfg['database']["password"]
            self.__port=cfg['database']["port"]
            self.__dbname=cfg['database']["dbname"]
            self.__host=cfg['database']["host"]    
    @property
    def user(self):
        return self.__user
    @property
    def password(self):
        return self.__password
    @property
    def host(self):
        return self.__host
    @property
    def port(self):
        return self.__port
    @property
    def dbName(self):
        return self.__dbname

    
   