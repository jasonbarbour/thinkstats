'''
Created on Mar 10, 2013

@author: jason
'''

import Pmf

def PmfMean(pmf):
    return sum(value * prob for value, prob in pmf.Items())

def PmfVar(pmf):
    mean = PmfMean(pmf)
    return sum(prob * (value - mean)**2 for value, prob in pmf.Items())

if __name__ == '__main__':
    pmf = Pmf.MakePmfFromList([1,2,3,4,5,7,8,9,9,9,9])
    print pmf.Items()
    print "Pmf.Mean():", pmf.Mean()
    print "Pmf.var():", pmf.Var()
    print "PmfMean():", PmfMean(pmf)
    print "PmfVar():", PmfVar(pmf)