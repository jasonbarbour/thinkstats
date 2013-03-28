'''
Created on Mar 26, 2013

@author: jason
'''
import random
import Cdf
import myplot

def Expov(mean, count):
    values = []
    for _ in range(0, count):
        values.append(random.expovariate(1/mean))
    return values

if __name__ == '__main__':
    cdf = Cdf.MakeCdfFromList(Expov(32.6, 44))
    scale = myplot.Cdf(cdf, complement=True)
    myplot.Show(xscale='linear', yscale='log')