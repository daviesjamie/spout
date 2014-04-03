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
        self.output.write(obj + '\n')

    def __del__(self):
        self.output.flush()
        self.output.close()


class JSONFileOutputOperation(FileOutputOperation):
    """
    Operation that writes all items it receives as JSON objects on separate lines in a file.
    """
    def __init__(self, filename):
        super(JSONFileOutputOperation, self).__init__(filename)


    def perform(self, obj):
        self.output.write(json.dumps(obj) + '\n')

    def __del__(self):
        super(JSONFileOutputOperation, self).__del__()
