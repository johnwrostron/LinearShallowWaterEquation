

import numpy as np
import matplotlib.pyplot as plt


def analytical_u(x,t):


    a = initialBell(x + t)
    b = initialBell(x - t)
    
    return -0.5*(a - b)



def analytical_h(x,t):

    a = initialBell(x + t)
    b = initialBell(x - t)

    return 0.5*(a + b)



# Function defining the initial analytic solution
def initialBell(x):

    return np.where(x%1. < 0.5, 0.01*np.power(np.sin(2*x*np.pi), 2), 0)



def plot_uandh(x, u, h, u_ana, h_ana, n, dt, dx):

    plt.figure(figsize=(12,8))

    plt.subplot(*(2,1,1))

    plt.plot(x, u, label="u", color="k")
    plt.plot(x, u_ana, label="u [analytical]", color="r")

    plt.legend(loc="upper right")
    plt.ylabel("u [m/s]")
    plt.axhline(0, color='b', zorder=-1, lw=0.5)
    plt.ylim(-0.01, 0.01)


    plt.subplot(*(2,1,2))

    plt.plot(x, h, label="u", color="k")
    plt.plot(x, h_ana, label="u [analytical]", color="r")

    plt.legend(loc="upper right")
    plt.ylabel("h [m]")
    plt.axhline(0, color='b', zorder=-1, lw=0.5)
    plt.ylim(-0.01, 0.01)

    plt.suptitle("time = {0:.3f}".format(n*dt), size=20)
    plt.subplots_adjust(top=0.92)

    plt.savefig("plots/uh_c{0:.2f}_dx{1:.3f}_dt{2:.3f}_t{3:.3f}.png".format(dt/dx, dx,dt,n*dt), dpi=300, bbox_inches="tight")
    plt.close()




def main(nt, plot_t=[1,10,100], dx=0.025, dt=0.001):

    # Setup constants:
    #   g: gravity
    g = 1
    #   H: height around which wave oscillates?
    H = 1.0
    #  nx: number of spatial points
    #nx = 40
    nx = int(1 / dx)
    #  dt: timestep
    dt = 0.001
    # Number of time steps
    #nt = 10

    # Setup spatial, u and h arrays
    x = np.linspace(0., 1.0, nx+1)
    #dx = 1.0 / nx

    h0 = initialBell(x)
    h = h0.copy()

    u0 = np.zeros_like(h)
    u = u0.copy()

    
    # Define New and Old versions of u and h
    uOld, uNew = u.copy(), u.copy()
    hOld, hNew = h.copy(), h.copy()

    #plt.figure(figsize=(12,12))
    # Loop over time...
    u_rmse_arr, h_rmse_arr, t_arr = [], [], []
    for n in range(1,nt):
        
        t_arr.append(n*dt)

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

        # Solve analytic solution for this time
        u_ana = analytical_u(x, dt*n)
        h_ana = analytical_h(x, dt*n)

        # Find mean squared error...
        u_rmse_arr.append(np.sqrt(np.mean((u - u_ana)**2.0)))
        h_rmse_arr.append(np.sqrt(np.mean((h - h_ana)**2.0)))

        if n in plot_t+[nt-1]:
            plot_uandh(x, u, h, u_ana, h_ana, n, dt, dx)


    # Derived quantities
    t = dt * nt

    u_rmse_arr = np.array(u_rmse_arr)
    h_rmse_arr = np.array(h_rmse_arr)
    t_arr = np.array(t_arr)


    return u_rmse_arr, h_rmse_arr, t_arr
 





dx = 0.025
dt = 0.001


plot_t = list(range(0,200,10)) + list(range(0,2000,100))
u_rmse, h_rmse, t_arr = main(nt=2000, plot_t=plot_t, dx=dx, dt=dt)

plt.figure(figsize=(12,8))

plt.subplot(*(2,1,1))

plt.plot(t_arr, u_rmse, label="u RMSE", color="k")

plt.legend(loc="upper right")
plt.ylabel("RMSE")


plt.subplot(*(2,1,2))

plt.plot(t_arr, h_rmse, label="h RMSE", color="k")

plt.legend(loc="upper right")
plt.ylabel("RMSE")

plt.savefig("plots/RMSE_dx{0:.3f}_dt{1:.3f}.png".format(dx,dt), dpi=300, bbox_inches="tight")
plt.close()















