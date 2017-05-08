import numpy as np
import random
import matplotlib.pyplot as plt
npoints = 10000
a= random.uniform(-50, 50)
b= random.uniform(-50, 50)
c= random.uniform(-50, 50)

ylst = []
xlst = []
color=[]
x=1
y=1

for i in range(npoints):
    xx = y - (x)/abs(x) * (abs(b*x - c))**0.5
    yy = a - x
    x = xx
    y = yy
    xlst.append(x)
    ylst.append(y)
    color.append(i)
plt.scatter(xlst, ylst, c=color, s=1)
plt.show()