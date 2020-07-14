class Regression:
    theta = []
    data = None
    a = 1 #learning rate
    epochs = None

    def __init__(self,a,data, epochs):
        self.a=a
        self.data = data
        self.epochs = epochs
        for i in range(len(data[0])):
            self.theta.append(0)

    def learn(self):
        for i in range(self.epochs):
           self.update()
           print(str(self.cost()))

    def update(self):
        temp = []
        for i in range(len(self.theta)-1):
            sum=0
            for j in self.data:
                p = self.predict(j)
                sum+=(p-j[len(j)-1])*j[i]

            nTheta = self.theta[i]-sum/len(self.data)*self.a
            temp.append(nTheta)

        #update constant
        sum = 0
        for j in self.data:
            p = self.predict(j)
            sum += (p - j[len(j) - 1])
        nTheta = self.theta[len(self.theta)-1] - sum / len(self.data) * self.a
        temp.append(nTheta)

        self.theta = temp


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

    def cost(self):
        sum = 0
        for i in self.data:
            temp = self.predict(i)-i[len(i)-1]
            sum+=temp*temp
        return sum