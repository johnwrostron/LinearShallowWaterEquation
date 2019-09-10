import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, x, data, line):
    line.set_data(x, data[:, num])
    return line,



fig1 = plt.figure()

# Fixing random state for reproducibility
np.random.seed(19680801)

data = np.random.rand(4, 25)
x = np.linspace(0,1,4)
print(data.T)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(x,data, l),
                                   interval=50, blit=True)

plt.show()
# To save the animation, use the command: line_ani.save('lines.mp4')
