# Will be formulating my own implemination of the basic level set method on a
# sqaure grid with the goal of implimenting a simple 2 phase problem of one
# phase moving bottom to top towards another

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

def two_phase_level_set_evolution(F=1,t_final=1 ):
    # 1. Grid setup
    N = 100
    L = 2.0
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    X, Y = np.meshgrid(x, y)

    dx = x[1] - x[0]

    # Signed Distance Function for this problem is just distance from x-axis
    phi = Y

    # F = 1  by default. Velocity will be constant and in the vertical direction
    t_final = 1 # amount of time to run the sim for
    dt = (0.9*dx/F)  # CLF condition, set alpha = 0.9
    num_steps = int(t_final/dt)

    # Want to make an animation of the level set traveling
    phi_history = [phi.copy()]  # store every step's phi for the animation


    #Start of Numerics
    for step in range(num_steps):
        phi_x_fwd = (np.roll(phi, -1, axis=1) - phi) / dx # not needed in this case since the velocity in
        phi_x_bwd = (phi - np.roll(phi,  1, axis=1)) / dx # horizontal direction is zero.
        phi_y_fwd = (np.roll(phi, -1, axis=0) - phi) / dx
        phi_y_bwd = (phi - np.roll(phi,  1, axis=0)) / dx

        # upwind differencing
        if F == 0:
            break # no movement throughout simulation, phi stays the same
        elif F > 0:
            gradient_phi_magnitude = (phi - phi_y_bwd)/dx
        else: # F < 0
            gradient_phi_magnitude = (phi_y_fwd - phi)/dx


        # Update phi with new values
        phi = phi - dt * F * gradient_phi_magnitude

        phi_history.append(phi.copy()) # save a snapshot after each step

        # --- Now build the animation from the saved snapshots ---
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(X.min(), X.max())
    ax.set_ylim(Y.min(), Y.max())
    ax.set_aspect('equal')

    def update(frame):
        ax.clear()
        ax.set_xlim(X.min(), X.max())
        ax.set_ylim(Y.min(), Y.max())
        ax.set_aspect('equal')
        ax.set_title(f"Step {frame}")
        ax.contour(X, Y, phi_history[frame], levels=[0], colors='red')

    ani = animation.FuncAnimation(fig, update, frames=len(phi_history), interval=50)

    # Save as gif (needs pillow) or mp4 (needs ffmpeg)
    ani.save("level_set_evolution.gif", writer='pillow', fps=20)
    plt.show()
