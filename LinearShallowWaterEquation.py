

import numpy as np
import matplotlib.pyplot as plt



def initialSine(x, ncycles=1.0):

    return np.sin(2.*np.pi*x*ncycles)    



# Function defining the initial analytic solution
def initialBell(x):

    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)



def update_line(num, x, data, line):
    line.set_data(x, data[:, num])
    return line,


def main(nt):

    # Setup constants:
    #   g: gravity
    g = 1
    #   H: height around which wave oscillates?
    H = 1.0
    #  nx: number of spatial points
    nx = 100
    #  dt: timestep
    dt = 0.001
    # Number of time steps
    #nt = 10

    # Setup spatial, u and h arrays
    x = np.linspace(0., 1.0, nx+1)
    dx = 1.0 / nx

    h = initialBell(x-0.1)
    u = np.zeros_like(h)


    
    # Define New and Old versions of u and h
    uOld, uNew = u.copy(), u.copy()
    hOld, hNew = h.copy(), h.copy()

    #plt.figure(figsize=(12,12))
    # Loop over time...
    for n in range(1,nt):
        
        # Loop over space
        for j in range(1,nx):
            # Calculate the new value for u
            uNew[j] = u[j] - (dt*g/(dx*2.0))*(h[j+1]-h[j-1])
            # Calculate the new value for h, using uNew
            hNew[j] = h[j] - (H*dt/(2.0*dx))*(uNew[j+1]-uNew[j-1])

        # Apply periodic boundary conditions
        uNew[0] = u[0] - (dt*g/(dx*2.0))*(h[1]-h[nx-1])
        uNew[nx] = uNew[0]
        hNew[0] = h[0] - (H*dt/(2.0*dx))*(uNew[1]-uNew[nx-1])
        hNew[nx] = hNew[0]

        # Update 
        u = uNew.copy()
        h = hNew.copy()

    

    #data = np.random.rand(4, 25)

    # Initialise line
    #fig1 = plt.figure()
    #l, = plt.plot([], [], 'r-')
    #plt.xlim(0, 1)
    #plt.ylim(0, 1)
    #plt.xlabel('x')
    #plt.title('test')
    #line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(x,data, l),
    #                               interval=50, blit=True)  

    # Derived quantities
    t = dt * nt


    return x, u, h
 


# Execute the code
nt0 = 0
nt1, nt2, nt3 = nt0, nt0+5, nt0+100
x1, u1, h1 = main(nt=nt1)
x2, u2, h2 = main(nt=nt2)
x3, u3, h3 = main(nt=nt3)


# Plot the solution... Is there an analytic equation?
plt.figure(figsize=(12,12))

plt.subplot(*(2,1,1))
plt.plot(x1, u1, 'k', label="u; nt={0:d}".format(nt1), color='r', lw=2)
plt.plot(x2, u2, 'k', label="u; nt={0:d}".format(nt2), color='0.75')
plt.plot(x3, u3, 'k', label="u; nt={0:d}".format(nt3), color='0.25')
plt.legend(loc="best")
plt.ylabel("u [m/s?]")
plt.axhline(0, linestyle=':', color='k', zorder=-1)


plt.subplot(*(2,1,2))
plt.plot(x1, h1, 'k', label="h; nt={0:d}".format(nt1), color='r', lw=2)
plt.plot(x2, h2, 'k', label="h; nt={0:d}".format(nt2), color='0.75')
plt.plot(x3, h3, 'k', label="h; nt={0:d}".format(nt3), color='0.25')
plt.legend(loc="best")
plt.ylabel("h [m?]")
plt.axhline(0, linestyle=':', color='k', zorder=-1)

plt.show()















