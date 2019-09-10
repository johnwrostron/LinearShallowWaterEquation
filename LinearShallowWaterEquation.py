

import numpy as np
import matplotlib.pyplot as plt



def initialSine(x, ncycles=1.0):

    return np.sin(2.*np.pi*x*ncycles)    



# Function defining the initial analytic solution
def initialBell(x):

    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)


def main(nt):

    # Setup constants:
    #   g: gravity
    g = 9.81
    #   H: height around which wave oscillates?
    H = 1.0
    #  nx: number of spatial points
    nx = 200
    #  dt: timestep
    dt = 0.01
    # Number of time steps
    #nt = 10

    # Setup spatial, u and h arrays
    x = np.linspace(0., 1.0, nx+1)
    dx = 1.0 / nx

    h = initialBell(x)
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
            # Calculate the new value for h...
            #    - do I use uNew or u? I'll go with u now
            hNew[j] = h[j] - (H*dt/(2.0*dx))*(u[j+1]-u[j-1])
        # Apply periodic boundary conditions
        uNew[0] = u[0] - (dt*g/(dx*2.0))*(h[1]-h[nx-1])
        uNew[nx] = uNew[0]
        hNew[0] = h[0] - (H*dt/(2.0*dx))*(u[1]-u[nx-1])
        hNew[nx] = hNew[0]        

        # Update 
        u = uNew.copy()
        h = hNew.copy()

    # Derived quantities
    t = dt * nt


    # Plot the solution... Is there an analytic equation?
    #plt.figure(figsize=(12,12))

    #plt.subplot(*(2,1,1))
    #plt.plot(x, u, 'k', label="u")
    #plt.legend(loc="best")
    #plt.ylabel("u [m/s?]")
    #plt.axhline(0, linestyle=':', color='k')

    #plt.subplot(*(2,1,2))
    #plt.plot(x, h, 'k', label="u")
    #plt.legend(loc="best")
    #plt.ylabel("h [m?]")
    #plt.axhline(0, linestyle=':', color='k')

    return x, u, h
 


# Execute the code
nt0 = 0
nt1, nt2, nt3 = nt0, nt0+3, nt0+6
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















