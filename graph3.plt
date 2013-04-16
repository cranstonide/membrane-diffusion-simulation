set terminal png size 1024,768
set output "concentration_vs_time.png"
set xlabel "Time (s)"
set ylabel "Concentration (mol/m^3)"
unset key
set title "Concentration Gradient"
plot "concentration_vs_time.dat", "concentration_vs_time_2.dat"
