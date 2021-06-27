class Calc:
    def __init__(self,intDataA,intDataB,intWork):
        self.intDataA = intDataA
        self.intDataB = intDataB
        self.intWork = intWork
#        print(self.intWork,self.intDataA,intDataB)
    def main(self):
        if self.intWork == 1:
            result = self.intDataA + self.intDataB
        elif self.intWork == 2:
            result = self.intDataA - self.intDataB
        elif self.intWork == 3:
            result = self.intDataA * self.intDataB
        elif self.intWork == 4:
            result = round(self.intDataA / self.intDataB)
        else:
            result = round(self.intDataA % self.intDataB)
        return result