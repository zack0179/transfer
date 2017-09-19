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

  def _get_theory(self,entry):
    k,i=entry
    x =self.tabs[k]['x'][i]
    y =self.tabs[k]['y'][i]
    z =self.tabs[k]['z'][i]
    Q2=self.tabs[k]['Q2'][i]
    mu2=2.0
    pT=self.tabs[k]['pT'][i]
    target=self.tabs[k]['target'][i]
    hadron=self.tabs[k]['hadron'][i]
    obs=self.tabs[k]['obs'][i].strip()
    col=self.tabs[k]['col'][i].strip().upper()

    if obs=='M_Hermes' and target=='proton': 

      FUU=self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'p',hadron)
      F2 =self.dis_stfuncs.get_F2(x,Q2,'p')
      thy = 2*np.pi*pT*FUU/F2

    elif obs=='M_Hermes' and target=='deuteron': 

      FUU = self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'p',hadron)\
           +self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'n',hadron)
      F2  = self.dis_stfuncs.get_F2(x,Q2,'p')\
           +self.dis_stfuncs.get_F2(x,Q2,'n')
      thy = 2*np.pi*pT*FUU/F2

    elif obs.startswith('AUT'):

      if   'collins' in obs: 

        ii=4
        if col=='HERMES':  phase=1    # hermes is sin(phi_s+phi_h)
        if col=='COMPASS': phase=-1  # compass is sin(phi_s+phi_h+pi)

      elif 'sivers' in obs : 
        ii=5
        phase=1

      Q2=2.0


      if target=='proton': 

        FUT=self.stfuncs.get_FX(ii,x,z,Q2,mu2,pT,'p',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'p',hadron)
        thy = phase*FUT/FUU

      elif target=='neutron': 

        FUT=self.stfuncs.get_FX(ii,x,z,Q2,mu2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'n',hadron)
        thy = phase*FUT/FUU

      elif target=='deuteron': 

        FUT=self.stfuncs.get_FX(ii,x,z,Q2,mu2,pT,'p',hadron)\
           +self.stfuncs.get_FX(ii,x,z,Q2,mu2,pT,'n',hadron)
        FUU=self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'p',hadron)\
           +self.stfuncs.get_FX(1,x,z,Q2,mu2,pT,'n',hadron)

        thy = phase*FUT/FUU

    elif obs == 'AUUcos':      
      if target == 'proton':
        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, mu2, pT, 'p', hadron) \
            + self.stfuncs.get_FX(17, x, z, Q2, mu2, pT, 'p', hadron)
        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'p', hadron)
      
      elif target == 'neutron':
        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, mu2, pT, 'n', hadron) \
            + self.stfuncs.get_FX(17, x, z, Q2, mu2, pT, 'n', hadron)
        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'n', hadron)
      
      elif target == 'deuteron':
        FUUcos = self.stfuncs.get_FX(16, x, z, Q2, mu2, pT, 'p', hadron) \
            + self.stfuncs.get_FX(17, x, z, Q2, mu2, pT, 'p', hadron) \
            + self.stfuncs.get_FX(16, x, z, Q2, mu2, pT, 'n', hadron) \
            + self.stfuncs.get_FX(17, x, z, Q2, mu2, pT, 'n', hadron)

        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'p', hadron)\
            + self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'n', hadron)

      epsilon = (1-y)/(1-y+0.5*y**2)
      thy = np.sqrt(2*epsilon*(1+epsilon))*FUUcos/FUU

    elif obs == 'AUUcos2':      
      if target == 'proton':
        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, mu2, pT, 'p', hadron)
        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'p', hadron)
      
      elif target == 'neutron':
        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, mu2, pT, 'n', hadron)
        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'n', hadron)
      
      elif target == 'deuteron':
        FUUcos2 = self.stfuncs.get_FX(7, x, z, Q2, mu2, pT, 'p', hadron)\
            + self.stfuncs.get_FX(7, x, z, Q2, mu2, pT, 'n', hadron)

        FUU = self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'p', hadron)\
            + self.stfuncs.get_FX(1, x, z, Q2, mu2, pT, 'n', hadron)

      epsilon = (1-y)/(1-y+0.5*y**2)
      thy = (epsilon)*FUUcos2/FUU

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
      print k,len(self.tabs[k]['value'])
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
          if res<0: chi2=-res**2
          else: chi2=res**2
          L.append(msg%(col,obs,x,z,pT,Q2,exp,alpha,thy,shift,chi2))

    if verb==0:
      return L
    elif verb==1:
      for l in L: print l

if __name__=='__main__':

  conf={}
  conf['datasets']={}
  conf['datasets']['sidis']={}
  conf['datasets']['sidis']['xlsx']={}
  conf['datasets']['sidis']['norm']={}

  '''
  conf['datasets']['sidis']['xlsx'][1000]='../database/SIDIS/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
  conf['datasets']['sidis']['xlsx'][1001]='../database/SIDIS/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
  conf['datasets']['sidis']['xlsx'][1004]='../database/SIDIS/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
  conf['datasets']['sidis']['xlsx'][1005]='../database/SIDIS/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 
  conf['datasets']['sidis']['norm'][1000]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2} 
  conf['datasets']['sidis']['norm'][1001]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][1004]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][1005]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}

  conf['datasets']['sidis']['xlsx'][2000]='../database/SIDIS/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT 
  conf['datasets']['sidis']['xlsx'][2001]='../database/SIDIS/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x  
  conf['datasets']['sidis']['xlsx'][2002]='../database/SIDIS/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z  
  conf['datasets']['sidis']['xlsx'][2003]='../database/SIDIS/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT 
  conf['datasets']['sidis']['xlsx'][2004]='../database/SIDIS/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x  
  conf['datasets']['sidis']['xlsx'][2005]='../database/SIDIS/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z  
  conf['datasets']['sidis']['norm'][2000]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2} 
  conf['datasets']['sidis']['norm'][2001]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][2002]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][2003]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][2004]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  conf['datasets']['sidis']['norm'][2005]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
  '''
   
  # testing 
  conf['datasets']['sidis']['xlsx'][5000]='../../database/SIDIS/expdata/5000.xlsx' # | proton | k- | AUUcos2 | hermes 
  conf['datasets']['sidis']['norm'][5000]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}

  conf['datasets']['sidis']['xlsx'][5008]='../../database/SIDIS/expdata/5008.xlsx' # | proton | k- | AUUcos | hermes 
  conf['datasets']['sidis']['norm'][5008]={'value':    1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}

  conf['datasets']['sidis']['filters']={}
  conf['datasets']['sidis']['filters'][1]={}
  conf['datasets']['sidis']['filters'][1]['list']=range(1000,6000)
  conf['datasets']['sidis']['filters'][1]['cond']=[]
  conf['datasets']['sidis']['filters'][1]['cond'].append("z<0.6")
  conf['datasets']['sidis']['filters'][1]['cond'].append("Q2>1.69")
  conf['datasets']['sidis']['filters'][1]['cond'].append("pT>0.2 and pT<0.9")

  conf['sidis tabs']=READER(conf).load_data_sets('sidis')
  #####################################################
  conf['path2CJ'] ='../../external/CJLIB'
  conf['path2LSS']='../../external/LSSLIB'
  conf['path2DSS']='../../external/DSSLIB'

  # setup for inclusive dis
  conf['alphaSmode']='backward'
  conf['Q20']=1
  conf['order']='LO'
  conf['aux']=AUX()
  conf['alphaS']=ALPHAS(conf)
  conf['pdf-NLO']=CJ(conf)
  conf['dis stfuncs']=DIS_STFUNCS(conf)

  # setup tmd sidis
  conf['order']='LO'
  conf['mu2'] = 2.0
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
  conf['sidis stfuncs']=STFUNCS(conf)

  #####################################################
  conf['residuals']=RESIDUALS(conf)
  conf['residuals'].get_residuals()
  conf['residuals'].gen_report(verb=1,level=1)

  



