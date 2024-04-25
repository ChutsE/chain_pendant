import matplotlib.pyplot as plt
import matplotlib.animation as animation
from catenaria import catenaria
import numpy as np

def chain(Xs = [0.5, 9.5], Ys = [0, 0.01], frames = 150, num_linspace = 10000):
    fig = plt.figure()
    ax = fig.gca()
    xs = np.linspace(Xs[0], Xs[1], frames)
    ys = np.linspace(Ys[0], Ys[1], frames)

    def frame(t):
        ax.clear()
        plt.xlim(-.5, 10)
        plt.ylim(-5, 1)

        x = np.linspace(0, xs[t], num_linspace)
        y = catenaria(x, B = [xs[t], ys[t]], L = 10)
        
        plt.plot(x,y)
        
    T = np.arange(frames)
    anim = animation.FuncAnimation(fig, frame, T)
    writergif = animation.PillowWriter(fps=30)
    anim.save('animation.gif',writer=writergif)

    plt.show()
    
chain()
