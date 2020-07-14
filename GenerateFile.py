import random
class GenerateFile:
    variables = []
    data = []
    numVar = 0
    minVar = 0 #theta
    maxVar = 0
    minX = 0
    maxX = 0
    noise = 0
    m = 0

    def __init__(self,numVar,minVar,maxVar,minX, maxX, noise,m):
        self.numVar = numVar
        self.minVar = minVar
        self.maxVar = maxVar
        self.minX = minX
        self.maxX = maxX
        self.noise = noise
        self.m = m

    def makeVariables(self):    #generates theta
        for i in range(self.numVar):
            self.variables[i] = random.randrange(self.maxVar-self.minVar)+self.minVar


    def makeData(self):
        for i in range(self.m):
            sum = 0
            arr = []
            for j in range(self.numVar):
                temp = random.randrange(self.maxX-self.minX)+self.minX
                sum+=temp*self.variables[j]
                arr.append(temp)

            sum+=random.randrange(self.noise)-self.noise/2
            arr.append(sum)


