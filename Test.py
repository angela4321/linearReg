from GenerateFile import GenerateFile
from Regression import Regression

g = GenerateFile(1,1,5,1,5,1,200)
g.makeVariables()
g.makeData()
g.printVariables()
g.printData()

r = Regression(0.03,g.data,100)
r.learn()
g.printVariables()
r.printTheta()
