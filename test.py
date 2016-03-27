#!/usr/bin/env python

from Labyrinth import LabyrinthServer
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

server = LabyrinthServer("./test.json")


