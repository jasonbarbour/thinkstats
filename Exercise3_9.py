'''
Created on Mar 23, 2013

@author: jason
'''
import random
import descriptive
import Cdf
import myplot

def Sample(cdf, n):
    sample = []
    for _ in range(0, n):
        sample.append(cdf.Value(random.random()))
    return sample

if __name__ == '__main__':
    pool, firsts, others = descriptive.MakeTables('.')
    pool.weights = [p.birthwgt_lb for p in pool.records if p.birthwgt_lb in range(0,50)]
    print len(pool.weights)
    
    cdf = Cdf.MakeCdfFromList(pool.weights, "pool")
    sample_cdf = Cdf.MakeCdfFromList(Sample(cdf, 1000), "sample")
    small_cdf = Cdf.MakeCdfFromList(Sample(cdf, 100), "small")
    
    myplot.Cdf(cdf)
    myplot.Cdf(sample_cdf)
    myplot.Cdf(small_cdf)
    myplot.Show()