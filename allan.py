import numpy as np

def allanVar(data, sf=1):
    leng = len(data)
    trange = np.unique(np.around(np.array([10**((i-1)*np.log10(leng/(sf*2))/20) for i
        in range(1,21)]),0))
    print trange
    trangesf = trange*sf

    av = []

    for t in trangesf:
        a = []
        for i in range(0,int(np.round(len(data)/t,0))):
            a.append(data[(i*t):(i*t + t)])
        av.append(a)
    
    avn = [e for e in av if e]
    
    av = []
    for tq in range(len(avn)):
        h = []
        k = 0
        for tqq in range(len(avn[tq])):
            h.append(np.mean(avn[tq][tqq]))
        for qq in range(0,len(h)-1):
            k += ((h[qq+1]-h[qq])**2)
        av.append(k/(2*len(h)-2 ))
            
    avar = np.array(av)
    return np.vstack((trange, avar)).T

def allanDev(data, sf=1):
    alv = allanVar(data, sf)
    return np.vstack([alv[:,0].T, np.sqrt(alv[:,1]).T]).T