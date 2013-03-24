'''
Created on Mar 18, 2013

@author: jason
'''
import relay
import Cdf
import myplot

if __name__ == '__main__':
    cdf = Cdf.MakeCdfFromList(relay.GetSpeeds(relay.ReadResults()))
    print cdf.Items()
    
    myplot.Cdf(cdf)
    myplot.Show()