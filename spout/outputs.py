from structs import Operation
import json


class PrintOperation(Operation):
    """
    Simple operation to print whatever input is supplied.
    """
    def perform(self, obj):
        print obj


class FileOutputOperation(Operation):
    """
    Operation that writes each input item onto a separate line in a file.
    """
    def __init__(self, filename):
        self.output = open(filename, 'w')

    def perform(self, obj):
        self.output.write(obj)

    def __del__(self):
        self.output.flush()
        self.output.close()
