set terminal png size 1024,768
set output "plots/images/cvd_log.png"
set xlabel "Distance (m)"
set ylabel "Concentration"
set logscale xy
unset key
set title "Logarithmic Concentration"
plot "datasets/concentration_vs_distance.dat"
