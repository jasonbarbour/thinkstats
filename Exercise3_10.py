'''
Created on Mar 23, 2013

@author: jason
'''
import random
import Cdf
import Pmf
import myplot

if __name__ == '__main__':
    random = [random.random() for _ in range(0,1000)]
    
    cdf = Cdf.MakeCdfFromList(random, "cdf")
    pmf = Pmf.MakePmfFromList(random, "pmf")
    
    print pmf.Values()
    
    myplot.Pmf(pmf)
    myplot.Show()
    
    myplot.Cdf(cdf)
    myplot.Show()
    