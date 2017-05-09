#http://www.fraktalwelt.de/myhome/simpiter.htm
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.style as style
style.use('dark_background')

npoints = 10000

ylst = []
xlst = []
color=[]
x=3.001
y=3.04
for i in range(npoints):
    xx = 1-y+ abs(x)
    yy = x
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
