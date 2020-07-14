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

    def update(self):
        temp = []
        for i in range(len(self.theta)-1):
            sum=0
            for j in self.data:
                p = self.predict(i)
                sum+=(p-j[len(j)-1])*j[i]

            nTheta = self.theta[i]-sum/len(self.data)*self.a
            temp.append(nTheta)

        #update constant
        sum = 0
        for j in self.data:
            p = self.predict(i)
            sum += (p - j[len(j) - 1])
        nTheta = self.theta[i] - sum / len(self.data) * self.a
        temp.append(nTheta)

        theta = temp


    def predict(self,row):
        sum = 0
        for i in range(len(self.theta)-1):#the last one is the constant so it doesn't get multiplied by x
            sum+=self.theta[i]*row[i]
        sum+=self.theta[len(self.theta)-1]
        return sum

