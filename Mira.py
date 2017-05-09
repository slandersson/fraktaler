#http://www.fraktalwelt.de/myhome/simpiter.htm
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.style as style
style.use('dark_background')

npoints = 100000
a=0.4
b = 1.0

ylst = []
xlst = []
color=[]
x=4
y=0
for i in range(npoints):
    xx = b*y + a*x-(1-a) * (2*x**2)/ (1+x**2)
    yy = -x + a*xx - (1-a) * (2*xx**2)/(1+xx**2)
    x = xx
    y = yy
    xlst.append(x)
    ylst.append(y)
    color.append(i)

print "Output Created"
fig = plt.gcf()
fig.canvas.set_window_title('Mira Attractor Machine')
plt.scatter(xlst, ylst, c=color, s=1, cmap=cm.jet)
plt.axis('off')
plt.show()
