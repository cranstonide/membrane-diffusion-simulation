set terminal png size 1024,768
set output "fvd_lin.png"
set xlabel "Distance (m)"
set ylabel "Flux (m/s)"
unset key
set title "Flux"
plot [:][-4000:1] "datasets/flux_vs_distance.dat"
