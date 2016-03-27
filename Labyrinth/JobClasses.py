import logging

def jobLoader(spec) :
    try :
        jobType = spec['job_type']
        jobName = spec['job_name']
    except KeyError :
        logging.error("There is an error in the job spec, unable to identify the job_type field")

    if jobType == 'HiveJob' :
        retrun HiveJob(jobName, spec)

    elif jobType == 'ShellJob' :
        return ShellJob(jobname, spec)

    elif jobType == 'MySQLJob' :
        return MySQLJob(jobName, spec)

    elif jobType == 'MySQLToHive' :
        return MySQLToHiveJob(jobName, spec)

    elif jobType == 'HiveToMySQL' :
        return HiveToMySQLJob(jobName, spec)

    else :
        logging.error("Unknown job type '%s'! Job will not be added to the schedule" % jobType)
        return None 

class Job(object) :
    def __init__(self, name, spec) :
        logging.info("Initializing object '%s'" % name)
        self.name = name
        self.spec = spec
        self.enabled = True

    def downloadFile(url) :
        pass

    def setName(self, name) :
        self.name = name

    def preRun(self, script) :
        self.prerun = script.split('\n')

    def postRun(self, script) :
        self.postRun = script.split('\n')

    def parseSpec(self) :
        pass

    def run(self) :
        pass

class HiveJob(Job) :
    """
    {
        "job_type" : "HiveJob",
        "script_url" : "Script URL in git",
        "script" : "insert overwrite db.blah select * from other.blah"
        "include" : []
        "owner" : "idupzyk",
        "email" : "ian.dupzyk@gmail.com",
        "email_on_failure" : true,
        "emial_on_success" : false,
        "run_type" : "hiveserver|hivecli",
        "parameters" : {
            "key1" : "val1"
            "key2" : "val2"
        },
        "environment" : {
            "env_var1" : "val1"
            "..." : "..."
        },
        "predecessors" : ["jobs"],
        "successor" : ["jobs"]
    }
    """
    def parseSpec(self) :
        self.jobType = self.spec['job_type']
        if "script_url" in self.spec :
            self.script = self.spec['script_url']
            self.script_type = "url"
        elif "script" in self.spec :
            self.script = self.spec['script']
            self.script_type = "text"
        else :
            self.logging.error("Script information is not found for job: %s" % self.name)

        self.owner = self.spec['owner']
        self.email = self.spec['email']
        self.success_email = self.spec['email_on_success']
        self.failure_email = self.spec['email_on_failure']
        self.run_type = self.spec['run_type']
        if self.run_type not in ['hiveserver', 'hivecli'] :
            logging.error("Unknown type of run_type: %s, must be 'hiveserver' or 'hivecli'" % self.run_type)
            self.enabled = False
        self.parameters = self.spec['parameters']
        self.environ = self.spec['environment']

    def run(self) :
        pass

class ShellJob(Job) :
    def run(self) :
        pass

class MySQLJob(Job) :
    def run(self) :
        pass

class MySQLToHiveJob(Job) :
    def run(self) :
        pass

class HiveToMySQLJob(Job) :
    def run(self) :
        pass


