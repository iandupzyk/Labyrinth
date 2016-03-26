
import subprocess
import logging
from os import environ

class SysComm(object) :
    def __init__(self, cmd=None, stdin=None, environment=None) :
        if cmd is not None :
            self.cmd = cmd.split()
        else :
            self.cmd = cmd

        self.stdin = stdin

        if self.stdin is not None :
            self.stdin_state = subprocess.PIPE
        else :
            self.stdin_state = None

        self.enviornment = environment

    def setStdin(self, stdin) :
        self.stdin = stdin
        self.stdin_state = subprocess.PIPE

        return self

    def setCmd(self, cmd) :
        self.cmd = cmd.split()

        return self

    def setEnv(self, environment) :
        self.environment = environ.copy()

        for key in environment :
            self.environment[key] = environment[key]

        return self

    def execute(self) :
        proc = subprocess.Popen(
                self.cmd
                , stdin=self.stdin_state
                , stdout=subprocess.PIPE
                , stderr=subprocess.PIPE
                , env=self.environment
                )

        self.stdout, self.stderr = proc.communicate(input=self.stdin)

        self.stdout = self.stdout.strip().split('\n')

        i = len(self.stdout)-1 
        while i >= 0 :
            self.stdout[i] = self.stdout[i].strip().replace('\r', '')
            if self.stdout[i] == '' :
                self.stdout.pop(i)

            i-=1
