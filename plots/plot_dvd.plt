set terminal png size 1024,768
set output "dvd_lin.png"
set xlabel "Distance (m)"
set ylabel "Diffusion (m^2 / sec)"
unset key
set title "Diffusion"
plot "diffusion_vs_distance.dat"
