set terminal png size 1024,768
set output "pvd_lin.png"
set xlabel "Distance (m)"
set ylabel "Permeability (m/s)"
unset key
set title "Permeability"
plot "datasets/permeability_vs_distance.dat"
