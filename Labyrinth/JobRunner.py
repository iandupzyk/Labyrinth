from flask_restful import Resource

class JobRunner(Resource) :
    def parseJobSpec(self, spec) :
        try :
            self.command = spec['command']

