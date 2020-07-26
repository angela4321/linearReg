class Regression:
    theta = []
    data = None
    test = None
    validation = None
    a = 1 #learning rate
    epochs = None

    def __init__(self,a,data, test, validation, epochs):
        self.a=a
        self.data = data
        self.test = test
        self.validation = validation
        self.epochs = epochs
        for i in range(len(data[0])):
            self.theta.append(0)    #set the default theta as 0

    def learn(self):
        for i in range(self.epochs):
           self.update()
           print("Training: "+str(self.cost(self.data)))
           print("Test: " + str(self.cost(self.test))+"\n")

    #performs gradient descent
    def update(self):
        temp = []
        for i in range(len(self.theta)-1):
            sum=0
            for j in self.data:
                p = self.predict(j)
                sum+=(p-j[len(j)-1])*j[i]

            nTheta = self.theta[i]-sum/len(self.data)*self.a    #updates theta values
            temp.append(nTheta)

        #update constant
        sum = 0
        for j in self.data:
            p = self.predict(j)
            sum += (p - j[len(j) - 1])
        nTheta = self.theta[len(self.theta)-1] - sum / len(self.data) * self.a
        temp.append(nTheta)

        self.theta = temp   #set theta to new updated values


    def predict(self,row):
        sum = 0
        for i in range(len(self.theta)-1):#the last one is the constant so it doesn't get multiplied by x
            sum+=self.theta[i]*row[i]
        sum+=self.theta[len(self.theta)-1]
        return sum

    def printTheta(self):
        s = ""
        for i in self.theta:
            s+=str(i)+" "
        print(s)

    def validate(self):
        return self.cost(self.validation)

    #calculates average square difference
    def cost(self, data):
        sum = 0
        for i in data:
            temp = self.predict(i)-i[len(i)-1]
            sum+=temp*temp
        return sum/len(data)