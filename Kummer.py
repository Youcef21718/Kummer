import time
import numpy as np
import matplotlib.pyplot as plt

def mul(a,b):
    c = np.zeros(2)
    c[0] = a[0]*b[0] - a[1]*b[1]
    c[1] = a[0]*b[1] + a[1]*b[0]
    return c

def pow(a,n):
    if(n==0):
        return np.asarray([1,0])
    else:
        return mul(a,pow(a,n-1))

def root(n):
    return np.asarray([np.cos(2*np.pi/n), np.sin(2*np.pi/n)])

def plot(a):
    plt.plot(a[0], a[1], 'k.', markersize=3, markeredgewidth=0)

def plot_circle(center, radius):
    
    x = np.linspace(-radius+center[0], radius+center[0], num=100)
    y = np.linspace(-radius+center[1], radius+center[1], num=100)[:, None]
    plt.contour(x, y.ravel(), (x-center[0])**2 + (y-center[1])**2, [radius**2], linewidths=1, colors='k')

def finish_plot():
    plt.axis('equal')
    plot_margin = 2

    x0, x1, y0, y1 = plt.axis()
    plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
    
    plt.savefig(str(int(time.time()))+'.jpg', format='jpg', dpi=600)

    # Get current size
    fig_size = plt.rcParams["figure.figsize"]
    #print("Current size:", fig_size)
   
    # Set figure width to 12 and height to 9
    fig_size[0] = 12
    fig_size[1] = 9
    plt.rcParams["figure.figsize"] = fig_size
    
    plt.show()

def recurs(x,a,r,level):
    if(level==r):
        plot(a)
    else:
        for i in range(x):
            recurs(x,a+i*pow(root(r),level),r,level+1)

def kummer(x,r):
    plot_circle(np.zeros(2),1)
    recurs(x,np.zeros(2),r,0)
    finish_plot()

kummer(5,5)