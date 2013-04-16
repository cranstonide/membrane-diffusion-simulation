# Mark Ide <mide@umassd.edu>
# Rebecca Gaddis <rlgaddis@wpi.edu>
# April 14, 2013

# Simulation of Diffusion Across a Semi-Permiable Membrane

import numpy
import math

# Open one file per dataset
try:
    rvd = open('rate_vs_distance.dat', 'w')
    cvt = open('concentration_vs_time.dat', 'w')
    rvc = open('rate_vs_concentration.dat', 'w')
    cvt2 = open('concentration_vs_time_2.dat', 'w')
    rvc2 = open('rate_vs_concentration_2.dat', 'w')
    
    # Area is currently a constant (1) but that may change
    for area in numpy.arange(1, 2, 1):
        # Simulate across time (start, end, step)
        # Start must be greater that 0, otherwise division by zero will occur
        for time in numpy.arange(0.001, .5, 0.001):

            # We'll simulate across a bunch of distances. (start, end, step)
            for distance in numpy.arange(50, 150, .1):

                # Begin Calculations -------------------------------------------

                # Define constants
                number_particles = 10000
                diffusion_constant = 0.00002

                permeability = 0
                if distance < 100:
                    permeability = 1
                elif distance >= 100 and distance < 104:
                    permeability = 0.1
                elif distance >= 104:
                    permeability = 1
    
                # Concentration gradients
                concentration = (number_particles / (math.sqrt(4 * math.pi * diffusion_constant * time)) * math.exp((-1) * (math.pow(distance * math.pow(10, -9), 2))/(4 * diffusion_constant * time)))
                concentration2 = (-1) * (number_particles / (math.sqrt(4 * math.pi * diffusion_constant * time)) * math.exp((math.pow(distance * math.pow(10, -9), 2))/(4 * diffusion_constant * time)))
                
                # Rate of particles inside changing
                rate = area * permeability * (concentration / distance)
                rate2 = area * permeability * (concentration2 / distance)
           
                # Write outputs to file ----------------------------------------
                cvt.write(str(time) + ", " + str(concentration) + "\n")
                cvt2.write(str(time) + ", " + str(concentration2) + "\n")

                # We only need rate/distance for one time (Just pick one valid time)
                if time == 0.001:
                    rvd.write(str(distance) + ", " + str(rate) + "\n")
                    rvc.write(str(concentration) + ", " + str(rate) + "\n")
                    rvc2.write(str(concentration2) + ", " + str(rate2) + "\n")
    
finally:
    # Close all the file handles
    rvd.close()
    cvt.close()
    rvc.close()
    cvt2.close()
    rvc2.close()
