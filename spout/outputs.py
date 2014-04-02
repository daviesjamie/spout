from structs import Operation
import json


class PrintOperation(Operation):
    """
    Simple operation to print whatever input is supplied.
    """
    def perform(self, obj):
        print obj
