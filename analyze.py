import numpy as np
import Gnuplot
import allan

def readfile(fil):
    with open(str(fil)) as f:
        tmp = []
        for line in f:
            tmp.append([float(x) for x in line.split()])
        dat = [(tmp[i][0]- tmp[0][0], tmp[i][1], tmp[i][3], tmp[i][2]) for i in
                range(0, len(tmp))]
    return np.asarray(dat)

def readbinfile(fil):
    dat = np.fromfile(fil, dtype ="<f4")
    dat = dat/1000 - np.mean(dat/1000)
    t = np.linspace(0,len(dat)/125,len(dat))
    data = np.vstack([t.T, dat.T]).T
    return data

def saveouttxt(dat, fil):
    np.savetxt(str(fil), np.transpose((dat[:,0], dat[:,1], dat[:,2],
        dat[:,3])), delimiter="\t", newline="\n")

def createTplot(data):
    g = Gnuplot.Gnuplot()
    g.title("Plot Example")
    g("set autoscale")
    g("set style data lines")
    g.xlabel("Time [s]")
    g.ylabel("B [nT]")
    d = Gnuplot.Data(data[:,0], data[:,1], title="Bx")
    dd = Gnuplot.Data(data[:,0], data[:,2], title="By")
    ddd = Gnuplot.Data(data[:,0], data[:,3], title="Bz")
    g.plot(d,dd,ddd)
    g.hardcopy("gp_test.ps", enhanced=1, color=1)
    return g

def plotAllanDev(data, comp, sf):
    B = {1: "Bx", 2: "By", 3: "Bz"}
    g = Gnuplot.Gnuplot()
    g("set logscale xy 10")
    g("set style data linespoints")
#    g("set format y '%.0e'")
    if isinstance(comp, int):
        aldat = data[:,comp]
        aldev = allan.allanDev(aldat, sf)
        d = Gnuplot.Data(aldev[:,0], aldev[:,1], title=str(B[comp]))
        g.plot(d)
        return g
    else:
        for i in comp:
            aldat = data[:,i]
            aldev = allan.allanDev(aldat, sf)
            d = Gnuplot.Data(aldev[:,0], aldev[:,1], title=str(B[i]))
            g.replot(d)
        return g

def getAllanDev(data, comp, sf):
    aldat = data[:,comp]
    aldev = allan.allanDev(aldat, sf)
    np.savetxt("al.txt",aldev)
    return aldev
#    else:
#       aldata = []
#        for i in comp:
#            aldat = data[:,i]
#            aldev = allan.allanDev(aldat, sf)
#            aldata.append(aldat)
#        return np.asarray(aldata)

