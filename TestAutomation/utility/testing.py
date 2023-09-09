from configparser import ConfigParser
config=ConfigParser()
config.read(".\inputfiles\testing.cfg")
print(config.get("hello","username"))