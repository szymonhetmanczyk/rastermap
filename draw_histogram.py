import numpy as np
import matplotlib.pyplot as plt

def histogram(band,comp):
    '''funkcja wyswietlajaca histogram z rastra,
    jako argumenty należy podać band = kanal oraz comp = ilosc przedzialow'''
    min,max,mean,sd = band.GetStatistics(1,0)
    minx=int(min - (10 + min) % 10)
    maxx=int(max - (10 + max) % 10)
    hist = band.GetHistogram(minx,maxx,int((maxx-minx)/comp))
    x = np.arange((maxx-minx)/comp)
    xt = np.linspace(minx,maxx,int((maxx-minx)/comp))
    xat = np.linspace(0,(maxx-minx)/comp,int((maxx-minx)/comp))
    plt.bar(x, np.asarray(hist),linewidth=1,width=1,color='red')
    plt.xticks(xat,xt.astype(int))
    plt.show()