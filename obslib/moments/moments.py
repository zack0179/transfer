#!/usr/bin/env python
import sys,os
import numpy as np
import math
from tools.tools import load_config
from external.CJLIB.CJ import CJ
from external.LSSLIB.LSS import LSS
from external.DSSLIB.DSS import DSS
from qcdlib.tmdlib import PDF,PPDF,FF
from qcdlib.tmdlib import TRANSVERSITY
from qcdlib.tmdlib import BOERMULDERS
from qcdlib.tmdlib import SIVERS
from qcdlib.tmdlib import PRETZELOSITY
from qcdlib.tmdlib import COLLINS
from qcdlib.tmdlib import WORMGEARG
from qcdlib.tmdlib import WORMGEARH
from qcdlib.aux import AUX
from scipy.special import gamma

class MOMENTS:

  def __init__(self,conf):
    self.aux=conf['aux']  
    self.conf=conf

  def beta(self,a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

  def get_moment(self,params):
    N,a,b,c,d=params
    return N*(self.beta(1+a,b+1)+c*self.beta(1+0.5+a,b+1)+d*self.beta(1+1+a,b+1))

  def get_flav(self,flav):
    shape=self.conf['transversity'].shape['p']
    if flav=='u': return self.get_moment(shape[1])
    if flav=='d': return self.get_moment(shape[3])
    if flav=='uv': return self.get_moment(shape[1])-self.get_moment(shape[2])
    if flav=='dv': return self.get_moment(shape[3])-self.get_moment(shape[4])

  def get_gT(self):
    shape=self.conf['transversity'].shape['p']
    mom_u=self.get_moment(shape[1])
    mom_d=self.get_moment(shape[3])
    return mom_u - mom_d

if __name__=='__main__':

  conf={}
  conf['path2CJ'] ='../../external/CJLIB'
  conf['path2LSS']='../../external/LSSLIB'
  conf['path2DSS']='../../external/DSSLIB'

  conf['order']='LO'
  conf['aux']=AUX()
  conf['_pdf']=CJ(conf)
  conf['_ppdf']=LSS(conf)
  conf['_ff']=DSS(conf)

  conf['pdf']=PDF(conf)
  conf['ppdf']=PPDF(conf)
  conf['ff']=FF(conf)
  conf['transversity']=TRANSVERSITY(conf)
  conf['sivers']=SIVERS(conf)
  conf['boermulders']=BOERMULDERS(conf)
  conf['pretzelosity']=PRETZELOSITY(conf)
  conf['wormgearg']=WORMGEARG(conf)
  conf['wormgearh']=WORMGEARH(conf)
  conf['collins']=COLLINS(conf)

  mom=MOMENTS(conf)
  print mom.get_gT()



