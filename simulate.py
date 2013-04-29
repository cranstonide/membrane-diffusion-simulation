# Mark Ide <mide@umassd.edu>
# Rebecca Gaddis <rlgaddis@wpi.edu>
# April 29, 2013

# This is Licensed under the MIT Licence.
# A copy can be found in LICENSE.txt

# Simulation of Diffusion Across a Semi-Permiable Membrane

import numpy
import math

# Constants
A = 6.022 * math.pow(10, 23)
N = 1 * math.pow(10, 5)
k = 1.38 * math.pow(10, -23)
T = 293
kbt = k * T
W = 1 * math.pow(10, -7)
n_a = 2 * N / A

K = {}
K[1] = 3.18 * math.pow(10, -2)
K[2] = 1
K[3] = 0.1

D1 = {}
D1[1] = 3240 * math.pow(10, -12)
D1[2] = 1880 * math.pow(10, -12)

m = {} 
m[1] = 5.36 * math.pow(10, -23)
m[2] = 7.31 * math.pow(10, -23)

C_0 = 0.6

eta = {}
eta[1] = 0.6 * math.pow(10, -6)
eta[2] = 9 * math.pow(10, -6)
eta[3] = 1.92 * math.pow(10, -6)

R_0 = D1[1]/(6 * math.pi * eta[1])

try:
    cvd = open('concentration_vs_distance.dat', 'w')
    dvd = open('diffusion_vs_distance.dat', 'w')
    pvd = open('permeability_vs_distance.dat', 'w')
    fvd = open('flux_vs_distance.dat', 'w')

    # For distance in range
    for r in numpy.arange(1 * math.pow(10, -9), 200 * math.pow(10, -9), 1 * math.pow(10, -9)):

        # Equations
        C_1 = (2 * C_0 - 1) / r

        if r <= 50 * math.pow(10, -9):
            i = 1
        elif r > 50 * math.pow(10, -9) and r <= 150 * math.pow(10, -9):
            i = 2    
        else:
            i = 3

        D = 1 / (6 * math.pi * eta[i] * R_0)
        P = K[i] * D / 50 * math.pow(10, -9)
        J = (-1) * P * C_1

        # Export points
        cvd.write(str(r) + "\t" + str(C_1) + "\n")
        dvd.write(str(r) + "\t" + str(D) + "\n")
        pvd.write(str(r) + "\t" + str(P) + "\n")
        fvd.write(str(r) + "\t" + str(J) + "\n")


finally:
    cvd.close()
    dvd.close()
    pvd.close()
    fvd.close()
