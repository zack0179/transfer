#!/usr/bin/env python
import sys,os
import numpy as np
from tools.tools import load_config
from external.DSSLIB.DSS import DSS
from qcdlib.tmdlib import FF
from qcdlib.tmdlib import COLLINS
from qcdlib.aux import AUX

class STFUNCS:

  def __init__(self,conf):
    self.aux=conf['aux']  
    self.conf=conf
    eu2,ed2=4/9.,1/9. 
    self.e2=[]
    self.e2.append(0)   # g
    self.e2.append(eu2) # u
    self.e2.append(eu2) # ub
    self.e2.append(ed2) # d
    self.e2.append(ed2) # db
    self.e2.append(ed2) # s
    self.e2.append(ed2) # sb
    self.e2.append(0)   # c
    self.e2.append(0)   # cb
    self.e2.append(0)   # b
    self.e2.append(0)   # bb
    self.e2=np.array(self.e2)

    self.Mh={}
    self.Mh['pi+']=self.aux.Mpi
    self.Mh['pi-']=self.aux.Mpi
    self.Mh['k+']=self.aux.Mk
    self.Mh['k-']=self.aux.Mk

    self.D={}
    self.D[1] ={'k1':'ff','k2':'ff'}
    self.D[2] ={'k1':'collins','k2':'collins'}

  def get_K(self,i,z1,z2,pT,wq,k1,k2,hadron1,hadron2):
    if   i==1:
      if pT != None: return 1
      else : return 1./(2.*np.pi)  
    elif i==2:
      if pT != None: return 4*self.Mh[hadron1]**2*z1**2*pT**2/wq**2
      else: return 2.*self.Mh[hadron1]**2*z1**2/(np.pi*wq)  

  def get_Wq(self,z1,z2,k1,k2,hadron1,hadron2):
    return ( z1**2*self.conf[k1].widths[hadron2]\
            +z2**2*self.conf[k2].widths[hadron1]\
           )/z2**2

  def get_gauss(self,z1,z2,pT,k1,k2,wq):
    if pT != None: return np.exp(-pT**2/wq)/(np.pi*wq)
    else: return 1  

  def ZX(self,i,z1,z2,Q2,pT,hadron1,hadron2):
    k1=self.D[i]['k1']
    k2=self.D[i]['k2']
    if k1==None or k2==None: return 0
    D1=self.conf[k1].get_C(z1,Q2,hadron1)
    D2=self.conf[k2].get_C(z2,Q2,hadron2)
    Wq=self.get_Wq(z1,z2,k1,k2,hadron1,hadron2)
    gauss=self.get_gauss(z1,z2,pT,k1,k2,Wq)
    K=self.get_K(i,z1,z2,pT,Wq,k1,k2,hadron1,hadron2)
    return np.sum(self.e2*K*D1*D2*gauss)


if __name__=='__main__':

  conf={}
  conf['aux']=AUX()

  conf['path2DSS']='../../external/DSSLIB'
  conf['_ff']=DSS(conf)
  conf['ff']=FF(conf)
  conf['collins']=COLLINS(conf)

  stfuncs=STFUNCS(conf)
  z1=0.5
  z2=0.3
  Q2=2.5
  pT=1.0
  hadron1='pi+'
  hadron2='pi-'
  for i in range(1,3): print i,stfuncs.ZX(i,z1,z2,Q2,pT,hadron1,hadron2)








