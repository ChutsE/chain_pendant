
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
def chain(Xs = [3, 5], Ys = [0, 2], steps = 20):
    fig = plt.figure()
    ax = fig.gca()
    xs = np.arange(Xs[0], Xs[1], (Xs[1]-Xs[0])/steps)
    ys = np.arange(Ys[0], Ys[1], (Ys[1]-Ys[0])/steps)
    len_chain = 6 # > sqrt(Xsmax^2+Ysmax^2)


    def frame(t):
        ax.clear()
        plt.xlim(-1, 5)
        plt.ylim(-3, 2)

        alpha = math.sqrt( ((len_chain**2)/((ys[t]**2)+(xs[t]**2))) - 1 )
        x = (xs[t] + ys[t]*alpha) / 2
        y = -math.sqrt(((len_chain/2)**2) - (x**2))

        plt.plot([0,x,xs[t]],[0,y,ys[t]])
        print(x**2 + y**2, (x-xs[t])**2+(y-ys[t])**2)
        
    T = np.arange(steps)
    anim = animation.FuncAnimation(fig, frame, T)
    plt.show()
    #anim.save("animation.mp4", writer= 'ffmpeg')
chain()
