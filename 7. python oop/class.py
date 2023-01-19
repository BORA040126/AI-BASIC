class Note(object):
    def __init__(self, content=None):
        self.content=content

    def write_content(self, content):
        self.content=content

    def remove_all(self):
        self.content=""
    
    def __add__(self,other):
        return self.content+other.content

    def __str__(self):
        return self.content