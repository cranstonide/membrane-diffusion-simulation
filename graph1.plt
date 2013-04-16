set terminal png size 1024,768
set output "rate_vs_distance.png"
set xlabel "Distance (nm)"
set ylabel "Rate (s^-2)"
unset key
set title "Rate of Diffusion Across Membrane"
plot "rate_vs_distance.dat"
