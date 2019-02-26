from llvmlite import ir
from rply.token import BaseBox


class Boolean(BaseBox):
    def __init__(self, value=False):
        self.value = value

    def gettokentype(self):
        return 'BTYPE'


class Double(BaseBox):
    def __init__(self, value=0.0):
        self.value = value

    def gettokentype(self):
        return 'FTYPE'


class Integer(BaseBox):
    def __init__(self, value=0):
        self.value = value

    def gettokentype(self):
        return 'ITYPE'


class Array(BaseBox):
    def __init__(self, _type):
        self._type = _type

    def gettokentype(self):
        return 'ARRAY'


def create(type_name: str):
    if type_name == 'BTYPE':
        return Boolean()
    elif type_name == 'ITYPE':
        return Integer()
    elif type_name == 'FTYPE':
        return Double()


class Pointer(BaseBox):
    def __init__(self, pointee, pt):
        self.pointee = pointee
        self.pointee_type = pt
        self.value = pointee.gettokentype() + pointee.value

    def gettokentype(self):
        return 'POINTER'
