'''
Created on Mar 26, 2013

@author: jason
'''
import random
import Cdf
import myplot

def paretovariate(alpha, m):
    return m * random.paretovariate(alpha)

def paretosample(count, alpha, m):
    return [paretovariate(alpha, m) for _ in range(0,count)]

if __name__ == '__main__':
    cdf = Cdf.MakeCdfFromList(paretosample(1000, 1, 0.5))
    # myplot.Cdf(cdf, complement=True)
    # myplot.Show(xscale='log', yscale='log')
    myplot.Cdf(cdf)
    myplot.Show()
    