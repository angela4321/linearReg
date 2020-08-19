import numpy as np
import matplotlib.pyplot as plt
from GenerateFile import GenerateFile
from Regression import Regression

dataSize = 100
#generates a random data file
g = GenerateFile(numVar=5,minVar=1,maxVar=5,minX=1,maxX=5,noise=2,m=dataSize)
g.makeVariables()
g.makeData()
g.printVariables()
g.printData()

#divide data into train validation and test
train = g.data[0:dataSize * 6/10]
validation = g.data[dataSize * 6/10 : dataSize * 8/10]
test = g.data[dataSize * 8/10: dataSize]

#perform linear regression
r = Regression(0.03,train,validation,test,200)
r.learn()
g.printVariables()
r.printTheta()
print("Test cost: "+str(r.findTestCost()))

#graph the training and validation costs
plt.plot(r.train_history,label="train")
plt.plot(r.validation_history,label="validation")
plt.legend()
plt.plot()
plt.show()
