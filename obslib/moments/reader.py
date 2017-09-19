#!/usr/bin/env python
import sys,os
import numpy as np
import pandas as pd
from tools.reader import _READER

class READER(_READER):

  def __init__(self,conf):
    self.conf=conf

  def modify_table(self,tab,k):
    pass
    #tab=self.apply_cuts(tab,k)
    return tab

if __name__ == "__main__":

  conf={}
  conf['datasets']={}
  conf['datasets']['lattice']={}
  conf['datasets']['lattice']['xlsx']={}
  conf['datasets']['lattice']['xlsx'][1000]='../../database/lattice/1000.xlsx'  # lattice gT(u-d)
  TAB=READER(conf).load_data_sets('lattice')
  print TAB





