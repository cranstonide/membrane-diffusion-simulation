set terminal png size 1024,768
set output "rate_vs_concenration.png"
set xlabel "Concentration (mol/m^3)"
set ylabel "Rate (s^-2)"
unset key
set title "Rate vs. Concentration"
plot "rate_vs_concentration.dat"
