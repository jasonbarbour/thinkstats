'''
Created on Mar 31, 2013

@author: jason
'''
import erf

if __name__ == '__main__':
    print erf.NormalCdf(115, 100, 15)
    print erf.NormalCdf(130, 100, 15)
    print erf.NormalCdf(145, 100, 15)
    print erf.NormalCdf(190, 100, 15)
    print (1 - erf.NormalCdf(190, 100, 15)) * 6000000000