# Will be formulating my own implemination of the basic level set method on a
# sqaure grid with the goal of implimenting a simple 2 phase problem of one
# phase moving bottom to top towards another

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def two_phase_level_set_evolution():
    # 1. Grid setup
    N = 100
    L = 2.0
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    X, Y = np.meshgrid(x, y)

    dx = x[1] - x[0]

    # Signed Distance Function for this problem is just distance from x-axis
    phi = Y

    F = 1 # Velocity will be constant and upwards
    t_final = 1 # amount of time to run the sim for
    dt = (0.9*dx/F)  # CLF condition, set alpha = 0.9 -->
    num_steps = int(t_final/dt)
