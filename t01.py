# coding:utf-8
import sys
from time import sleep


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(stream=sys.stdout)

# now it works
print('print something')
print("output")

sleep(50)
print("end")
