class Idol(object):
    def __init__(self, name, number,color):
        self.name=name
        self.number=number
        self.color=color

    def __str__ (self):
        return "hello, we are %s" %(self.name)


    def __add__(self,other):
        return self.number+other.number

