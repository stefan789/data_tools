set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'magni.ps'
set logscale xy 10
set xrange [0.9:20000]
set xlabel "Time [s]"
set ylabel "AllanDev [pT]"
plot "al.txt" title "Magnicon X9F" with linespoints
