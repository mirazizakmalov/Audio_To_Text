import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Our function
def f(x,a):
    return (x**2 /3) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a* np.pi * x)

#Setting up the axis
fig, ax = plt.subplots()
x = np.linspace(-2.5, 2.5, 400)
line, = ax.plot([], [], 'r-', lw = 2)

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_xlabel('x')
ax.set_ylabel("f(x)")

def update(frame):
    a = -2.5 + frame * 0.05 
    y = f(x,a)
    line.set_data(x,y)
    return line,

ani = animation.FuncAnimation(fig, update, frames = 300, interval = 50, blit = True)

plt.show()