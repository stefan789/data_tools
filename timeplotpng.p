set terminal pngcairo size 700,524  enhanced font 'Helvetica,10'
set output 'timeplots2.png'
set xlabel "Time [s]"
set ylabel "B [pT]"
plot "data/time_S22_CH014.txt" title "Magnicon" with linespoints pi 10000, \
     "data/time_S28_CH014.txt" title "Bilt I" with linespoints pi 10000
