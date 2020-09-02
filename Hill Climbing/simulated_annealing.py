import math
import matplotlib.pylab as plt
import random
import numpy as np

class SA:
    def __init__(self,alpha,minT,maxIterations,function):
        self.function = function
        self.min_temp = minT
        self.max_iterations = maxIterations
        self.alpha = alpha

    def runSA(self):
        
        f = self.function
        T = 1
        x = random.randint(5000,25000)/10000
        y = self.function(x)
        current_solution = x
        max_val = x
        ys = []
        xs = []
        xs.append(x)
        while T > self.min_temp:
            i = 0
            while i < self.max_iterations:
                if(f(current_solution)  > f(max_val)):
                    max_val = current_solution

                # Neighbor/Successor Selection:
                r_direction = random.choice(['Left','Right'])
                x = current_solution
                dydx = (f(x+0.01) - f(x))/0.01
                if dydx > 2:
                    r_direction = 'Right'
                r_steps = 0
                if abs(dydx) < 1:
                    r_steps = 0.5
                elif abs(dydx) < 3:
                    r_steps = 0.3
                else :
                    r_steps = 0.1
                
                # random direction move 
                # and movement is considered to be from a range and not a single point
                # to avoid searching a area more than once
                new_solution = 0
                if r_direction == 'Left':
                    new_solution = min(xs) - r_steps
                    if new_solution < 0.5:
                        new_solution = 0.5
                else:
                    new_solution = max(xs) + r_steps
                    if new_solution > 2.5:
                        new_solution = 2.5


                # probablity
                p = math.exp((f(current_solution) - f(new_solution))/T)
                
                
                if random.random() < p:
                    current_solution = new_solution
                    # print(f(current_solution))
                    ys.append(f(current_solution))
                    xs.append(current_solution)
                
                i+=1

            T = T * self.alpha
            #print(f(current_solution))
        print(max(ys))
        print(min(xs) ,max(xs))
        return max_val

def f(x):
    return np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4


sa = SA(0.95 , 0.0001 , 100 , f)
x_ = sa.runSA()
print(f(x_))
y_ = f(x_)



x = np.linspace(0.48,2.52,2000)
y = np.sin(x*10*np.pi % (2*np.pi)) / (2*x) + (x-1)**4


plt.plot(x,y)
plt.scatter(x_,y_, color="green",s=60)
plt.show()