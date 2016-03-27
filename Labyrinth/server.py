
from flask import Flask, request
from flask_restful import Resource, Api
import json
import logging
import subprocess
from .JobManager import JobManager
from .JobRunner import JobRunner

class LabyrinthServer(object) :
    def __init__(self, configFile) :
        self.app = Flask(__name__)
        self.api = Api(self.app)
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

        try :
            for endpoint in self.config['endpoints'] :
                if self.config['endpoints'][endpoint] == "JobRunner" :
                    self.api.add_resource(JobRunner, endpoint)
                    logging.info("Created JobRunner endpoint for "+endpoint)
                elif self.config['endpoints'][endpoint] == "JobManager" :
                    self.api.add_resource(JobManager, endpoint)
                    logging.info("Created JobManager endpoint for "+endpoint)
                else :
                    logging.error("Unknown class for endpoint '%s'.  No Class '%s' exists" % (endpoint,self.config['endpoints'][endpoint]))
        except KeyError :
            logging.critical("There is a configuration problem with the endpoints in the file '%s'" % configFile)
            exit(10)

        try :
            self.app.run(port=self.config['port'])
        except KeyError :
            logging.critical("Server Configuration does not specify a port, defaulting to port 5000")
            self.app.run(port=5000)


