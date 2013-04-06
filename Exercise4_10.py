'''
Created on Apr 2, 2013

@author: jason
'''

import random
import matplotlib.pyplot as pyplot
import descriptive
import rankit

def NormalPlot(values):
    xs = [random.normalvariate(0, 1) for _ in range(len(values))]
    xs.sort()
    values.sort()
    print xs
    print values
    
    pyplot.clf()
    pyplot.plot(xs, values, 'b.', markersize=3)
    pyplot.show()
    
    
if __name__ == '__main__':
    pool, firsts, others = descriptive.MakeTables(".")
    values = [1, 2, 3, 5, 2, 3, 4, 1, 7]
    NormalPlot(pool.lengths)
    # rankit.MakeNormalPlot(pool.lengths, root='exercise4_10')
    