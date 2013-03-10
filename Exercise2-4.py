'''
Created on Mar 7, 2013

@author: jason
'''
import Pmf

def RemainingLifetime(pmf, age):
    """Takes a Pmf of lifetimes and an age, and returns a new Pmf 
    that represents the distribution of remaining lifetimes.
    """
    rem = Pmf.Pmf()
    for val, prob in pmf.Items():
        if (val > age):
            rem.Incr(val-age, prob)
    rem.Normalize()
    return rem

if __name__ == '__main__':
        pmf = Pmf.MakePmfFromList([1,2,3,4,5,7,8,9,9,9,9])
        rem = RemainingLifetime(pmf, 5)
        
        for val, prob in sorted(rem.Items()):
            print val, prob