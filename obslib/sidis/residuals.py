#!/usr/bin/env python
import sys,os
import numpy as np
from mpmath import fp,mp
from scipy.integrate import quad
import pandas as pd
import time
from tools.residuals import _RESIDUALS
from external.CJLIB.CJ import CJ
from external.DSSLIB.DSS import DSS
from external.LSSLIB.LSS import LSS
from reader import READER
from stfuncs import STFUNCS
from qcdlib.tmdlib import PDF,PPDF,FF
from qcdlib.tmdlib import TRANSVERSITY
from qcdlib.tmdlib import BOERMULDERS
from qcdlib.tmdlib import SIVERS
from qcdlib.tmdlib import PRETZELOSITY
from qcdlib.tmdlib import COLLINS
from qcdlib.tmdlib import WORMGEARG
from qcdlib.tmdlib import WORMGEARH
from qcdlib.aux import AUX
from qcdlib.alphaS import ALPHAS
from obslib.dis.stfuncs import STFUNCS as DIS_STFUNCS

class RESIDUALS(_RESIDUALS):

  def __init__(self,conf):
    self.conf=conf
    self.reaction='sidis'
    self.tabs=conf['sidis tabs']
    self.stfuncs=conf['sidis stfuncs']
    self.dis_stfuncs=conf['dis stfuncs']
    self.setup()

  def get_IFUU(self,FUU,x,zh,Q2,pT,hadron):
    Q=np.sqrt(Q2)
    M=self.conf['aux'].M
    M2=self.conf['aux'].M**2
    if 'pi' in hadron: Mh=self.conf['aux'].Mpi
    if 'k' in hadron:  Mh=self.conf['aux'].Mk
    MhT=np.sqrt(Mh**2+pT**2)
    xn=2*x/(1+np.sqrt(1+4*x**2*M2/Q2))
    yp=0.5*np.log(Q2/xn**2/M2)
    yh=np.log( Q*zh*(Q2-xn**2*M2)/(2*xn**2*M2*MhT) - Q/(xn*M)*np.sqrt(zh**2*(Q2-xn**2*M2)**2/(4*xn**2*M2*MhT**2)-1) )
    dy=yp-yh
    #R=1-np.exp(-self.conf['aux'].alpha*dy)
    #S=self.conf['aux'].N*np.exp(-dy**2/self.conf['aux'].beta/x)
    #S=np.exp(-dy**2/self.conf['aux'].beta/x)
    #print '1 ',R*FUU,'  2:',(1-R)*S
    #print FUU ,self.conf['aux'].N*np.exp(-self.conf['aux'].alpha*x*dy**2)

    #soft=(1+self.conf['aux'].N*np.exp(-self.conf['aux'].alpha*x*dy**2) )
    #print soft
    #823.03  torino
    #764
    #691

  
    if len(self.conf['aux'].soft.keys())==0:
      return FUU 
    else:
      p=[]
      p.append(self.conf['aux'].soft['p0'])
      p.append(self.conf['aux'].soft['p1'])
      p.append(self.conf['aux'].soft['p2'])
      p.append(self.conf['aux'].soft['p3'])
      p.append(self.conf['aux'].soft['p4'])
      p.append(self.conf['aux'].soft['p5'])
      p.append(self.conf['aux'].soft['p6'])
      p.append(self.conf['aux'].soft['p7'])
      p.append(self.conf['aux'].soft['p8'])
      p.append(self.conf['aux'].soft['p9'])
      p.append(self.conf['aux'].soft['p10'])
      p.append(self.conf['aux'].soft['p11'])
      p.append(self.conf['aux'].soft['p12'])
      dy=yh+2
      return FUU*(1+np.sum([p[i]*dy**(i+1) for i in range(len(p))])) #( p[0]*dy + p[1]*(dy/(1-yh))#**p[1]#

  def _get_theory(self,entry):
    k,i=entry
    x =self.tabs[k]['x'][i]
    y =self.tabs[k]['y'][i]
    z =self.tabs[k]['z'][i]
    Q2=self.tabs[k]['Q2'][i]
    pT=self.tabs[k]['pT'][i]
    target=self.tabs[k]['target'][i]
    hadron=self.tabs[k]['hadron'][i]
    obs=self.tabs[k]['obs'][i].strip()
    col=self.tabs[k]['col'][i].strip().upper()

    if obs=='M_Hermes' and target=='proton': 

      FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)
      FUU=self.get_IFUU(FUU,x,z,Q2,pT,hadron)
      F2 =self.dis_stfuncs.get_F2(x,Q2,'p')
      thy = 2*np.pi*pT*FUU/F2

    elif obs=='M_Hermes' and target=='deuteron': 

      FUU = self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)\
           +self.stfuncs.get_FX(1,x,z,Q2,pT,'n',hadron)
      FUU=self.get_IFUU(FUU,x,z,Q2,pT,hadron)
      F2  = self.dis_stfuncs.get_F2(x,Q2,'p')\
           +self.dis_stfuncs.get_F2(x,Q2,'n')

      thy = 2*np.pi*pT*FUU/F2

    elif obs=='AUTcollins':

      if col=='HERMES':  factor= 1   # hermes is sin(phi_s+phi_h)
      if col=='COMPASS': factor=-1   # compass is sin(phi_s+phi_h+pi)
      if col=='HERMES':  factor*= 2*(1-y)/(1+(1-y)**2) # add depolarization factor only for HERMES

      Q2=2.0

      if target=='proton': 

        FUT=self.stfuncs.get_FX(4,x,z,Q2,pT,'p',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)
        thy = factor*FUT/FUU

      elif target=='neutron': 

        FUT=self.stfuncs.get_FX(4,x,z,Q2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'n',hadron)
        thy = factor*FUT/FUU

      elif target=='deuteron': 

        FUT=self.stfuncs.get_FX(4,x,z,Q2,pT,'p',hadron)\
           +self.stfuncs.get_FX(4,x,z,Q2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)\
           +self.stfuncs.get_FX(1,x,z,Q2,pT,'n',hadron)

        thy = factor*FUT/FUU

    elif obs=='AUTsivers':

      Q2=2.0

      if target=='proton': 

        FUT=self.stfuncs.get_FX(5,x,z,Q2,pT,'p',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)
        thy = FUT/FUU

      elif target=='neutron': 

        FUT=self.stfuncs.get_FX(5,x,z,Q2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'n',hadron)
        thy = FUT/FUU

      elif target=='deuteron': 

        FUT=self.stfuncs.get_FX(5,x,z,Q2,pT,'p',hadron)\
           +self.stfuncs.get_FX(5,x,z,Q2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,pT,'p',hadron)\
           +self.stfuncs.get_FX(1,x,z,Q2,pT,'n',hadron)

        thy = FUT/FUU

    elif obs == 'AUUcos':      

      Q2=2.0

      if target == 'proton':

        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'p', hadron) \
               + self.stfuncs.get_FX(17, x, z, Q2, pT, 'p', hadron)
        FUU    = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)
      
      elif target == 'neutron':

        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'n', hadron) \
               + self.stfuncs.get_FX(17, x, z, Q2, pT, 'n', hadron)
        FUU    = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron)
      
      elif target == 'deuteron':

        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, pT, 'p', hadron) \
               + self.stfuncs.get_FX(17, x, z, Q2, pT, 'p', hadron) \
               + self.stfuncs.get_FX(16, x, z, Q2, pT, 'n', hadron) \
               + self.stfuncs.get_FX(17, x, z, Q2, pT, 'n', hadron)

        FUU    = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)\
               + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron)

      epsilon = (1-y)/(1-y+0.5*y**2)
      thy = np.sqrt(2*epsilon*(1+epsilon))*FUUcos/FUU

    elif obs == 'AUUcos2':      

      if target == 'proton':
        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, pT, 'p', hadron)
        FUU     = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)
      
      elif target == 'neutron':

        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, pT, 'n', hadron)
        FUU     = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron)
      
      elif target == 'deuteron':

        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, pT, 'p', hadron)\
                + self.stfuncs.get_FX(7, x, z, Q2, pT, 'n', hadron)

        FUU     = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)\
                + self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron)

      epsilon = (1-y)/(1-y+0.5*y**2)
      thy = (epsilon)*FUUcos2/FUU

    elif obs == 'A_pretzelosity':

      #      if col=='compass':  coeff= 1.00
      #      if col=='hermes':  coeff= 2*(1-y)/(1+(1-y)**2)
      #      if col=='jlab':  coeff= 2*(1-y)/(1+(1-y)**2)

      if target == 'proton':
        FUTsin3 = self.stfuncs.get_FX(8, x, z, Q2, pT, 'p', hadron)
        FUU     = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)

      elif target == 'neutron':

        FUTsin3 = self.stfuncs.get_FX(8, x, z, Q2, pT, 'n', hadron)
        FUU     = self.stfuncs.get_FX(1, x, z, Q2, pT, 'n', hadron)

      elif target == 'deuteron':

        FUTsin3 = self.stfuncs.get_FX(8, x, z, Q2, pT, 'p', hadron)\
                + self.stfuncs.get_FX(8, x, z, Q2, pT, 'n', hadron)

        FUU     = self.stfuncs.get_FX(8, x, z, Q2, pT, 'p', hadron)\
                + self.stfuncs.get_FX(8, x, z, Q2, pT, 'n', hadron)

      coeff= 2*(1-y)/(1+(1-y)**2)
      thy = coeff*FUTsin3/FUU

    elif obs == 'ALL':

      if target == 'proton':
        FLL = self.stfuncs.get_FX(3, x, z, Q2, pT, 'p', hadron)
        FUU = self.stfuncs.get_FX(1, x, z, Q2, pT, 'p', hadron)

      coeff= 2*(1-y)/(1+(1-y)**2)
      thy = coeff*FLL/FUU

    else:
      print 'ERR: exp=%d obs=%s and target=%s not implemented'%(k,obs,target)
      sys.exit()
  
    return k,i,thy

  def gen_report(self,verb=1,level=1):
    """
    verb = 0: Do not print on screen. Only return list of strings
    verv = 1: print on screen the report
    level= 0: only the total chi2s
    level= 1: include point by point 
    """

    L=[]

    L.append(self.reaction)

    for k in self.tabs:
      #print k,len(self.tabs[k]['value'])
      if self.tabs[k]['value'].size==0: continue
      res =self._get_residuals(k)
      rres=self._get_rres(k)
      nres=self._get_nres(k)
      
      chi2=np.sum(res**2)
      rchi2=np.sum(rres**2)
      nchi2=nres**2
      tar=self.tabs[k]['target'][0]
      col=self.tabs[k]['col'][0].split()[0]
      obs=self.tabs[k]['obs'][0].split()[0]
      had=self.tabs[k]['hadron'][0].split()[0]
      npts=res.size
      L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f'%(k,tar,had,col,obs,npts,chi2,rchi2,nchi2))

    if level==1:
      L.append('-'*100)  

      msg ='col=%7s  '
      msg+='obs=%7s  '
      msg+='x=%10.3e  '
      msg+='z=%10.3e  '
      msg+='pT=%10.3e  '
      msg+='Q2=%10.3e  '
      msg+='yh=%10.3e  '
      msg+='yp=%10.3e  '
      msg+='dy=%10.3e  '
      msg+='exp=%10.3e  ' 
      msg+='alpha=%10.3e  ' 
      msg+='thy=%10.3e  ' 
      msg+='shift=%10.3e  ' 
      msg+='chi2=%10.3f  '

      for k in self.tabs:
        if len(self.tabs[k]['value'])==0: continue 
        for i in range(len(self.tabs[k]['value'])):
          x=self.tabs[k]['x'][i]
          z=self.tabs[k]['z'][i]
          pT=self.tabs[k]['pT'][i]
          obs=self.tabs[k]['obs'][i]
          Q2=self.tabs[k]['Q2'][i]
          res=self.tabs[k]['residuals'][i]
          thy=self.tabs[k]['thy'][i]
          exp=self.tabs[k]['value'][i]
          alpha=self.tabs[k]['alpha'][i]
          rres=self.tabs[k]['r-residuals'][i]
          col=self.tabs[k]['col'][i]
          shift=self.tabs[k]['shift'][i]
          yh=self.tabs[k]['yh'][i]
          yp=self.tabs[k]['yp'][i]
          dy=self.tabs[k]['dy'][i]
          if res<0: chi2=-res**2
          else: chi2=res**2
          L.append(msg%(col,obs,x,z,pT,Q2,yh,yp,dy,exp,alpha,thy,shift,chi2))

    if verb==0:
      return L
    elif verb==1:
      for l in L: print l
      return L

