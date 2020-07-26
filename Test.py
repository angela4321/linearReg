from GenerateFile import GenerateFile
from Regression import Regression

dataSize = 1000;
g = GenerateFile(10,1,5,1,5,1,dataSize)
g.makeVariables()
g.makeData()
g.printVariables()
g.printData()

train = g.data[0:dataSize * 6/10]
test = g.data[dataSize * 6/10 : dataSize * 8/10]
validation = g.data[dataSize * 8/10: dataSize]

r = Regression(0.03,train,test,validation,500)
r.learn()
g.printVariables()
r.printTheta()
print("Validation cost: "+r.validate())
