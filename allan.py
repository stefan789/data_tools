import numpy as np

def allanVar(data, sf=1):
    '''
    calculates allan variance
    according to eq 8.13a in
    David W. Allan, John H. Shoaf and Donald Halford: 
    Statistics of Time and Frequency Data Analysis,
    NBS Monograph 140, pages 151–204, 1974
    '''

    nd = np.array(data)
    
    # list of integration times, without last
    integration_lengths = np.unique(np.floor(sf/np.arange(1, len(data)+1)))[:-1]

    av = []
    
    for anint in integration_lengths:
        # Shorten 
        shorten_by = len(nd) % anint
        thend = nd
        if shorten_by != 0:
            thend = nd[:-shorten_by]

        x = thend.reshape(-1, anint).mean(axis=1)

        av.appen([anint*sf, ((x[1:] - x[:-1])**2).mean()/2])

    # return 2 dim array with allan var vs. integration time
    return np.array(av)

def allanDev(data, sf=1):
    alv = allanVar(data, sf)
    alv[:,1] = np.sqrt(alv[:,1])
    return alv
