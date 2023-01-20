class fruit(object):
    def __init__(self,name,color):
        self.name=name
        self.color=color

class citrus(fruit):
    def __init__(self, name, color, sugar):
        super().__init__(name,color)
        self.sugar=sugar

    def __str__(self):
        return "이름은 %s 색은 %s색 당도는 %d 입니다" %(self.name, self.color, self.sugar)