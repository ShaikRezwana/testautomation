from configparser import ConfigParser
#created object of configparser class

config=ConfigParser()
#to read data from config file and remember whenever we give path , give /(forward slash))

config.read("./inputfiles/config.cfg")
print(config.get("Hello","username"))