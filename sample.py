
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
def chain(Xs = [0.5, 9.5], Ys = [0, 0.01], steps = 150):
    fig = plt.figure()
    ax = fig.gca()
    xs = np.arange(Xs[0], Xs[1], (Xs[1]-Xs[0])/steps)
    ys = np.arange(Ys[0], Ys[1], (Ys[1]-Ys[0])/steps)
    len_chain = 10 # > sqrt(Xsmax^2+Ysmax^2)


    def frame(t):
        ax.clear()
        plt.xlim(-.5, 10)
        plt.ylim(-5, 1)

        alpha = math.sqrt( ((len_chain**2)/((ys[t]**2)+(xs[t]**2))) - 1 )
        x = (xs[t] + ys[t]*alpha) / 2
        y = -math.sqrt(((len_chain/2)**2) - (x**2))

        plt.plot([0,x,xs[t]],[0,y,ys[t]])
        
    T = np.arange(steps)
    anim = animation.FuncAnimation(fig, frame, T)
    writergif = animation.PillowWriter(fps=30)
    anim.save('animation_point.gif',writer=writergif)
    plt.show()
chain()
