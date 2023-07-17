import configparser


# creating object of configparser
config = configparser.ConfigParser()


# creating a section
config.add_section("database")


# adding key-value pairs
config.set("database", "host", "local host")
config.set("database", "admin", "root")
config.set("database", "password", "password")
config.set("database", "database", "studentInfo")
config.set("database", "version", "1.1.0")





with open("conf.ini", 'w') as example:
   config.write(example)