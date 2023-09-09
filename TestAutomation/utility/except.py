from configparser import ConfigParser
config=ConfigParser()
config.read("./inputfiles/config.cfg")
print(config.get("Hello","username"))