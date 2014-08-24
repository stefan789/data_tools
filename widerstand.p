set terminal pngcairo enhanced color font 'Helvetica, 10'
set output "widerstand.png"
set xrange [0:100]
set yrange [0:6000]
set xlabel "T [°C]"
set ylabel "R [Ohm]"
plot 1058.77*(1 + 3.9e-3 * (x-23)) title "R(T) Al" with lines, \
4200*(1 + 3.8e-3 * (x-23)) title "R(T) Pt" with lines
