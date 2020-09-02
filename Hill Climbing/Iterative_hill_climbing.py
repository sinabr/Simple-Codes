import math
import matplotlib.pylab as plt
import random
import numpy as np


class hillClimbing:

    def __init__(self,f,x,learning_rate):
        self.function = f
        self.x = x


    def runHC(self):
        initial_x = self.x

        learning_rate = 0.001

        x = self.x
        func = self.function

        def derivative(func , x , h = 0.001):
            return (func(x + h) - func(x - h))/(2*h)

        initial_x = x
        x_ = x
        dydx_ = derivative(self.function,self.x)
        while dydx_ == 0 :
            x_test = x + 0.01
            y_test = func(x_test)
            if(y_test < func(x_)):
                x_ += random.randint(5000,25000) / 10000
                dydx_ = derivative

        dydx = dydx_

        while abs(dydx_) > 0.1 and derivative(func,x_ + 0.01)<derivative(func,x_):
            dydx_ = dydx
            # Gradient Decsent Iterations
            x_ = x_ + learning_rate * dydx_
            dydx = derivative(func,x_)

            if x_ < 0.5 :
                x_ = 0.5
                break

            if x_ > 2.5 :
                x_ = 2.5
                break

        final_y = func(x_)
        return x_ , final_y


def f(x):
    return np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4

xs = []
ys = []

for i  in range(100):
    x_i = random.randint(5000,25000) / 10000

    hc = hillClimbing(f,x_i,0.001)
    x_t , y_t = hc.runHC()

    xs.append(x_t)
    ys.append(y_t)

x = np.linspace(0.5,2.5,2000)
y = np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4

max_y = max(ys)
index = ys.index(max(ys))
max_x = xs[index]


plt.plot(x,y)
plt.scatter(max_x , max_y , color='green' ,s=60)
plt.show()