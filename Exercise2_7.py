'''
Created on Mar 12, 2013

@author: jason
'''

import descriptive
import Pmf
from matplotlib import pyplot
from collections import namedtuple
import myplot

def ConditionalProbOne(pmf, x):
    copy = pmf.Copy(pmf)
    cohort = {val:1000*prob for val, prob in copy.Items() if val >= x }
    return Pmf.MakePmfFromDict(cohort).Prob(x)
    
def ConditionalProbTwo(pmf, x):
    copy = pmf.Copy(pmf)
    [copy.Remove(val) for val in copy.Values() if val < x]
    copy.Normalize()
    return copy.Prob(x)

def plot(pool, firsts, others):
    # values = range(min(pool.pmf.Values()), max(pool.pmf.Values())-1)
    values = range(35, 46)
    print values
    
    probs = {}
    probs[firsts.pmf.name] = []
    probs[others.pmf.name] = []
    for val in values:
        probs[firsts.pmf.name].append(ConditionalProbTwo(firsts.pmf, val))
        probs[others.pmf.name].append(ConditionalProbTwo(others.pmf, val))
        
    pyplot.clf()        
    for name, ps in probs.iteritems():
        pyplot.plot(values, ps, label=name)
        print name, ps
    pyplot.show()
        

def main(name, data_dir=''):
    pool, firsts, others = descriptive.MakeTables(data_dir)

    plot(pool, firsts, others)

    print "1 Pool", ConditionalProbOne(pool.pmf, 39)
    print "1 First", ConditionalProbOne(firsts.pmf, 39)
    print "1 Others", ConditionalProbOne(others.pmf, 39)
    
    print "2 Pool", ConditionalProbTwo(pool.pmf, 39)
    print "2 First", ConditionalProbTwo(firsts.pmf, 39)
    print "2 Others", ConditionalProbTwo(others.pmf, 39)
    
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)