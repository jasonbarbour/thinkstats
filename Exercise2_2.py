import first_solution
import sys
import thinkstats
from math import sqrt
from first_solution import ProcessTables

def StdDev(t):
    mean, variance = thinkstats.MeanVar(t.lengths)
    return sqrt(variance)

def main(name, data_dir='.'):
    table, firsts, others = first_solution.MakeTables(data_dir)
    first_solution.ProcessTables(firsts, others)
    
    print "Mean difference:", thinkstats.Mean(firsts.lengths) - thinkstats.Mean(others.lengths)
    print "Std. deviation of firsts:", StdDev(firsts)
    print "Std. deviation of others:", StdDev(others)

if __name__ == '__main__':
    main(*sys.argv)