import thinkstats
from math import sqrt

pumpkins = [1, 1, 1, 3, 3, 591]

if __name__ == '__main__':
    mean, var = thinkstats.MeanVar(pumpkins)
    print mean
    print var
    print sqrt(var)
    
