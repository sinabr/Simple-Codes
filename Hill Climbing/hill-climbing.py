import math
import matplotlib.pylab as plt
import random
import numpy as np


def f(x):
    return np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4

# -(sin(10 * pi * x) / (2 * x ** 2)) + ((5 * pi * cos(10 * pi * x)) / x) + 4 * (x - 1) ** 3

def derivative(f , x , h = 0.001):
    return -(np.sin(10 * np.pi * x) / (2 * x ** 2)) + ((5 * np.pi * np.cos(10 * np.pi * x)) / x) + 4 * (x - 1) ** 3



x_ = random.randint(5000,25000) / 10000
x_ = 2.2


initial_x = x_

learning_rate = 0.001

dydx_ = derivative(f,x_)
while dydx_ == 0 :
    x_test = x_ + 0.01
    y_test = f(x_test)
    if(y_test < f(x_)):
        x_ += random.randint(5000,25000) / 10000
        dydx_ = derivative


xs = []
ys = []

dydx = dydx_

while abs(dydx_) > 0.1:
    dydx_ = dydx
    # Gradient Decsent Iterations
    x_ = x_ + learning_rate * dydx_
    dydx = derivative(f,x_)

    if x_ < 0.5 :
        x_ = 0.5
        break

    if x_ > 2.5 :
        x_ = 2.5
        break

    xs.append(x_)
    ys.append(f(x_)) 

initial_y = f(initial_x)
final_y = f(x_)

x = np.linspace(0.5,2.5,2000)
y = np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4

plt.plot(x,y)
plt.plot(initial_x,initial_y,color='r',marker='o')
plt.plot(x_,final_y,color='g',marker='o')
plt.scatter(xs,ys)
plt.text(0.6,5,'red: start\ngreen: end',ha='center', va='center')
plt.show()


