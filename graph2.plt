set terminal png size 1024,768
set output "rate_vs_distance_zoomed.png"
set xlabel "Distance (nm)"
set ylabel "Rate (s^-2)"
set xrange [94:110]
set yrange [0:400000]
unset key
set title "Rate of Diffusion Across Membrane"
plot "rate_vs_distance.dat"
