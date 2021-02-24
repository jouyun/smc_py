import pandas as pd
import sys
import os
import numpy as np
import glob

from multiprocessing import  Pool
import Levenshtein as lv

#Old way, hamming only

def mjollnirv2(lef, rig):
    rtn=0
    if (len(lef)!=len(rig)):
        return 32
    error=False
    for x in range(0,len(rig)):
        if lef[x]!=rig[x]:
            rtn=rtn+1
            if (error):
                return 32
            else:
                error=True
    return rtn   

def hammerv1(left, right):
    rtn = [mjollnirv2(left, r) for r in right]
    return rtn 

class My1stClass:
    data=[]
    def set_data(self, inp):
        self.data=inp
    def myfu(self, inp):
        hamms=hammerv1(inp, self.data)
        mn = np.argmin(hamms)
        return [hamms[mn], mn]

#Good way, levenstein
    
def hammerv2(left, right):
    rtn=[lv.distance(left, r) for r in right]
    return rtn
        
class My3rdClass:
    data=[]
    def set_data(self, inp):
        self.data=inp
    def myfu(self, inp):
        hamms=hammerv2(inp, self.data)
        mn = np.argmin(hamms)
        return [hamms[mn], mn]
