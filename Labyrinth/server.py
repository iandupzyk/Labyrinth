
from flask import Flask, request
from flask_restful import Resource, Api
import json
import logging

api.add_resources(Name, 'endpoint')

class LabyrinthServer(object) :
    def __init__(self, configFile) :
        logging.debug("opening config file %s for reading" % configFile)
        try :
            fp = open(configFile, 'r')
            self.config = json.load(fp)
            fp.close()
        except IOError :
            logging.critical("Unable to open the config file %s for reading" % configFile)
            exit(10)
        except ValueError :
            logging.critical("Unable to read the JSON object in the config file %s" % configFile)
            exit(10)

if __name__ == '__main__' :
    app.run()

def start() :
    app.run()
