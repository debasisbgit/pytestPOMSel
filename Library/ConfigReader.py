import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFile/Config.cfg")
    return config.get(section, key)


def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFile/Elements.cfg")
    return config.get(section, key)
