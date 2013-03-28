'''
Created on Mar 26, 2013

@author: jason
'''
import Exercise4_3
import Cdf
import ctypes


if __name__ == '__main__':
    sample = Exercise4_3.paretosample(60000000, 1.7, 100)
    cdf = Cdf.MakeCdfFromList(sample)
    print 'Mean', cdf.Mean()
    print 'Max', max(cdf.Values())

