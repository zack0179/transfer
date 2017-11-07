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
import matplotlib.pyplot as plt

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
    self.D[1] ={'k1':'pdf','k2':'ff'}
    self.D[2] ={'k1':None,'k2':None}
    self.D[3] ={'k1':'ppdf','k2':'ff'}
    self.D[4] ={'k1':'transversity','k2':'collins'}
    self.D[5] ={'k1':'sivers','k2':'ff'}
    self.D[6] ={'k1':None,'k2':None}
    self.D[7] ={'k1':'boermulders','k2':'collins'}
    self.D[8] ={'k1':'pretzelosity','k2':'collins'}
    self.D[9] ={'k1':'wormgearg','k2':'ff'}
    self.D[10]={'k1':'wormgearh','k2':'collins'}
    self.D[11]={'k1':'wormgearg','k2':'ff'}
    self.D[12]={'k1':'ppdf','k2':'ff'}
    self.D[13]={'k1':'wormgearg','k2':'ff'}
    self.D[14]={'k1':'wormgearh','k2':'collins'}
    self.D[15]={'k1':None,'k2':None}
    self.D[16]={'k1':'boermulders','k2':'collins'}
    self.D[17]={'k1':'pdf','k2':'ff'}
    self.D[18]={'k1':'sivers','k2':'ff'}
    self.D[19]={'k1':'transversity','k2':'collins'}
    self.D[20]={'k1':'sivers','k2':'ff'}
    self.D[21]={'k1':'pretzelosity','k2':'collins'}
    self.D[22] ={'k1':'pdf','k2':'ff'}

  def get_K(self,i,x,Q2,z,pT,wq,k1,k2,target,hadron):
    if   i==1: return x
    elif i==2: return 0
    elif i==3: return x
    elif i==4: return 2*x*z*pT*self.Mh[hadron]/wq
    elif i==5: return -2*x*z*pT*self.aux.M/wq
    elif i==6: return 0
    elif i==7: return 4*x*z**2*self.aux.M*pT**2*self.Mh[hadron]/wq**2
    elif i==8: return 2*x*z**3*pT**3*self.Mh[hadron]*self.conf[k1].widths[target]/wq**3
    elif i==9: return 2*x*z*self.aux.M*pT/wq
    elif i==10:return 4*x*z**2*self.aux.M*pT**2*self.Mh[hadron]/wq**2
    elif i==11: return -2*self.aux.M/math.sqrt(Q2)*x*(z**2*self.conf[k1].widths[target]*(pT**2+self.conf[k2].widths[hadron])+self.conf[k2].widths[hadron]**2)/wq**2
    elif i==12: return -2*x*z*pT*self.conf[k1].widths[target]/(math.sqrt(Q2)*wq)
    elif i==13: return -2*x*z**2*pT**2*self.aux.M*self.conf[k1].widths[target]/(math.sqrt(Q2)*wq**2)
    elif i==14: return -8*self.aux.M**3/math.sqrt(Q2)*x*(z**2*self.conf[k1].widths[target]*(pT**2-z**2*self.conf[k1].widths[target])+self.conf[k2].widths[hadron]**2)/wq**3
    elif i==15: return 0
    elif i==16: return -8*self.aux.M*z*pT*self.Mh[hadron]/math.sqrt(Q2)*x*(self.conf[k2].widths[hadron]**2+z**2*self.conf[k1].widths[target]*(pT**2-z**2*self.conf[k1].widths[target]))/wq**3
    elif i==17: return -2*self.aux.M/math.sqrt(Q2)*x*(z*pT/self.aux.M)*self.conf[k1].widths[target]/wq
    elif i==18: return -2*self.aux.M/math.sqrt(Q2)*x*(z**2*self.conf[k1].widths[target]*(pT**2+self.conf[k2].widths[hadron])+self.conf[k2].widths[hadron]**2)/wq**2
    elif i==19: return 4*x*z**2*self.Mh[hadron]/math.sqrt(Q2)*self.conf[k1].widths[target]*(-pT**2+wq)/wq**2
    elif i==20: return -2*self.aux.M**3/math.sqrt(Q2)*x*self.conf[k1].widths[target]/wq**2
    elif i==21: return -8*self.aux.M**2*self.Mh[hadron]/math.sqrt(Q2)*x*z**2*pT**2/wq**2
    elif i==22: return 2*x*z**2*pT**2/Q2*self.conf[k1].widths[target]**2/wq**2

  def get_wq(self,z,k1,k2,target,hadron):
    return z**2*np.abs(self.conf[k1].widths[target]) + np.abs(self.conf[k2].widths[hadron])

  def get_gauss(self,z,pT,wq):
    return np.exp(-pT**2/wq)/(np.pi*wq)

  def get_FX(self,i,x,z,Q2,pT,target,hadron):
    k1=self.D[i]['k1']
    k2=self.D[i]['k2']
    if k1==None or k2==None: return 0
    mu2=Q2
    F=self.conf[k1].get_C(x,mu2,target)
    D=self.conf[k2].get_C(z,mu2,hadron)
    wq=self.get_wq(z,k1,k2,target,hadron)
    gauss=self.get_gauss(z,pT,wq) 
    K=self.get_K(i,x,Q2,z,pT,wq,k1,k2,target,hadron)
    return np.sum(self.e2*K*F*D*gauss)

  def dcs(self,x,Q2,y,z,pT,sangle,hangle,target,hadron):
    coupling=1.0/137
    p1=(1.0-y)/(1.0-y+y**2/2)
    p2=y*(1.0-y/2)/(1.0-y+y**2/2)
    p3=(2.0-y)*(math.sqrt(1.0-y))/(1.0-y+y**2/2)
    p4=y*math.sqrt(1.0-y)/(1.0-y+y**2/2)
    SL=math.cos(sangle)
    ST=math.sin(sangle)
    helicity=1.0
    factor=coupling**2/(x*y*Q2)*(1-y+y**2)
    csleading=factor*(self.get_FX(1,x,z,Q2,pT,target,hadron)+math.cos(2*hangle)*p1*self.get_FX(7,x,z,Q2,pT,target,hadron)+SL*math.sin(2*hangle)*p1*self.get_FX(10,x,z,Q2,pT,target,hadron)+helicity*SL*p2*self.get_FX(3,x,z,Q2,pT,target,hadron)+helicity*ST*math.cos(hangle-sangle)*p2*self.get_FX(9,x,z,Q2,pT,target,hadron)+ST*math.sin(hangle-sangle)*self.get_FX(5,x,z,Q2,pT,target,hadron)+ST*math.sin(hangle+sangle)*p1*self.get_FX(4,x,z,Q2,pT,target,hadron)+ST*math.sin(3*hangle-sangle)*p1*self.get_FX(8,x,z,Q2,pT,target,hadron))

    cssubleading=factor*(math.cos(hangle)*p3*(self.get_FX(16,x,z,Q2,pT,target,hadron)+self.get_FX(17,x,z,Q2,pT,target,hadron))+helicity*math.sin(hangle)*p4*self.get_FX(15,x,z,Q2,pT,target,hadron)+SL*math.sin(hangle)*p3*self.get_FX(14,x,z,Q2,pT,target,hadron)+ST*math.sin(sangle)*p3*(self.get_FX(18,x,z,Q2,pT,target,hadron)+self.get_FX(19,x,z,Q2,pT,target,hadron))+ST*math.sin(2*hangle-sangle)*p3*(self.get_FX(20,x,z,Q2,pT,target,hadron)+self.get_FX(21,x,z,Q2,pT,target,hadron))+helicity*SL*math.cos(hangle)*p4*self.get_FX(12,x,z,Q2,pT,target,hadron)+helicity*ST*math.cos(sangle)*p4*self.get_FX(11,x,z,Q2,pT,target,hadron)+helicity*ST*math.cos(2*hangle-sangle)*p4*self.get_FX(13,x,z,Q2,pT,target,hadron))

    cstotal=csleading+cssubleading
    return cstotal/(2*0.938*11.0*x)

  def unpolarizedCS(self,x,Q2,y,z,pT,sangle,hangle,target,hadron):
    coupling=1.0/137
    p1=(1.0-y)/(1.0-y+y**2/2)
    p2=y*(1.0-y/2)/(1.0-y+y**2/2)
    p3=(2.0-y)*(math.sqrt(1.0-y))/(1.0-y+y**2/2)
    p4=y*math.sqrt(1.0-y)/(1.0-y+y**2/2)
    SL=math.cos(sangle)
    ST=math.sin(sangle)
    helicity=1.0
    factor=coupling**2/(x*y*Q2)*(1-y+y**2)
    cs = factor*(self.get_FX(1,x,z,Q2,pT,target,hadron)+math.cos(2*hangle)*p1*self.get_FX(7,x,z,Q2,pT,target,hadron)+math.cos(hangle)*p3*(self.get_FX(16,x,z,Q2,pT,target,hadron)+self.get_FX(17,x,z,Q2,pT,target,hadron)))
    
    return cs/(2*0.938*11.0*x)

  def get_xsec(self,x,z,y,Q2,pT,phi_h,phi_S,Sperp,Spar,le,target,hadron):
    alfa2=self.aux.alfa**2
    gamma=2*self.aux.M*x/np.sqrt(Q2)
    eps=(1-y-0.25*gamma**2*y**2)/(1-y+0.5*y**2+0.25*gamma**2*y**2)

    beta=np.zeros(19)
    beta[1] =1
    beta[2] =eps
    beta[3] =np.sqrt(2*eps*(1+eps))*np.cos(phi_h)
    beta[4] =eps*np.cos(2*phi_h)
    beta[5] =le    * np.sqrt(2*eps*(1-eps))*np.sin(phi_h)
    beta[6] =Spar  * np.sqrt(2*eps*(1+eps))*np.sin(phi_h)
    beta[7] =Spar  * eps * np.sin(2*phi_h)
    beta[8] =Spar  * le * np.sqrt(1-eps**2)
    beta[9] =Spar  * le * np.sqrt(2*eps*(1-eps))*np.cos(phi_h)
    beta[10]=Sperp * np.sin(phi_h-phi_S)
    beta[11]=Sperp * eps * np.sin(phi_h-phi_S)
    beta[12]=Sperp * eps * np.sin(phi_h+phi_S)
    beta[13]=Sperp * eps * np.sin(3*phi_h-phi_S)
    beta[14]=Sperp * np.sqrt(2*eps*(1+eps))*np.sin(phi_S)
    beta[15]=Sperp * np.sqrt(2*eps*(1+eps))*np.sin(2*phi_h-phi_S)
    beta[16]=Sperp * le * np.sqrt(1-eps**2) * np.cos(phi_h-phi_S)
    beta[17]=Sperp * le * np.sqrt(2*eps*(1-eps)) * np.cos(phi_S)
    beta[18]=Sperp * le * np.sqrt(2*eps*(1-eps)) * np.cos(2*phi_h-phi_S)

    F=np.zeros(19)
    for i in range(1,16): F[i]=self.get_FX(i,x,z,Q2,pT,target,hadron)
    F[16]=self.get_FX(16,x,z,Q2,pT,target,hadron)+self.get_FX(17,x,z,Q2,pT,target,hadron)
    F[17]=self.get_FX(18,x,z,Q2,pT,target,hadron)+self.get_FX(19,x,z,Q2,pT,target,hadron)
    F[18]=self.get_FX(20,x,z,Q2,pT,target,hadron)+self.get_FX(21,x,z,Q2,pT,target,hadron)

    return (alfa**2/x/y/Q2) * (y*2/2/(1-eps)) * np.sum(beta*F)


if __name__=='__main__':

  conf={}
  conf['path2CJ'] ='../../external/CJLIB'
  conf['path2LSS']='../../external/LSSLIB'
  conf['path2DSS']='../../external/DSSLIB'

  conf['order']='LO'
  conf['shape'] = 0
  conf['aux']  =AUX()
  conf['_pdf'] =CJ(conf)
  conf['_ppdf']=LSS(conf)
  conf['_ff']  =DSS(conf)

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

  stfuncs=STFUNCS(conf)
  x=0.25
  z=0.5
  Q2=2.4
  mu2=2.0
  E=11.0
  m=0.938
  pT=0.3
  y=Q2/(2*m*E*x)
  sangle=math.pi*0.0
  hangle=math.pi/2
  target='p'
  hadron='pi+' 
  for i in range(1,22): print i,stfuncs.get_FX(i,x,z,Q2,pT,target,hadron)
  print stfuncs.dcs(x,Q2,y,z,pT,sangle,hangle,target,hadron)
  print stfuncs.unpolarizedCS(x,Q2,y,z,pT,sangle,hangle,target,hadron)
#  for j in range(1,36): plt.plot([j*math.pi/18] , [stfuncs.unpolarizedCS(x,Q2,mu2,y,z,pT,sangle,j*math.pi/18,target,hadron)], 'ro')
  for j in range(1,36): plt.plot([j*math.pi/18] , [stfuncs.dcs(x,Q2,y,z,pT,sangle,j*math.pi/18,target,hadron)], 'ro')

  plt.xlabel('Hadronic Angle (rad)')
  plt.ylabel('Full Cross Section')
  plt.title('WW-type Approximation for $Q^2=3.6$')

  plt.show()
  
