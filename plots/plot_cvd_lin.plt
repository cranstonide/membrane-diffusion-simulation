set terminal png size 1024,768
set output "cvd_lin.png"
set xlabel "Distance (m)"
set ylabel "Concentration"
unset key
set title "Linear Concentration"
plot "concentration_vs_distance.dat"
