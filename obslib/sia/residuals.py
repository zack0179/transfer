#!/usr/bin/env python
import sys,os
import numpy as np
from scipy.integrate import quad
from external.DSSLIB.DSS import DSS
from qcdlib.tmdlib import FF
from qcdlib.tmdlib import COLLINS
from qcdlib.aux import AUX
from tools.residuals import _RESIDUALS
from reader import READER
from stfuncs import STFUNCS

class RESIDUALS(_RESIDUALS):

  def __init__(self,conf):
    self.conf=conf
    self.reaction='sia'
    self.tabs=conf['sia tabs']
    self.stfuncs=conf['sia stfuncs']
    self.setup()

  def _get_theory(self,entry):
    k,i=entry
    obs=self.tabs[k]['obs'][i].strip()
    z1 =self.tabs[k]['z1'][i]
    z2 =self.tabs[k]['z2'][i]
    Q2 =self.tabs[k]['Q2'][i]
    factor=self.tabs[k]['S2/1+C2'][i]

    if obs=='AUL-0-PT':
      pT =self.tabs[k]['pT'][i]
      ZUuu =self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi+','pi-') + self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi-','pi+')
      ZLuu =self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi+','pi+') + self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi-','pi-')
      ZUcol=self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi+','pi-') + self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi-','pi+')
      ZLcol=self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi+','pi+') + self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi-','pi-')
      thy=factor*(ZUcol/ZUuu - ZLcol/ZLuu)
    elif obs=='AUC-0-PT':
      pT =self.tabs[k]['pT'][i]
      ZUuu =self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi+','pi-') + self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi-','pi+')
      ZLuu =self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi+','pi+') + self.stfuncs.ZX(1,z1,z2,Q2,pT,'pi-','pi-')
      ZUcol=self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi+','pi-') + self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi-','pi+')
      ZLcol=self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi+','pi+') + self.stfuncs.ZX(2,z1,z2,Q2,pT,'pi-','pi-')
      ZCuu=ZUuu+ZLuu
      ZCcol=ZUcol+ZLcol
      thy=factor*(ZUcol/ZUuu - ZCcol/ZCuu)
    elif obs=='AUL-0-PT-INT':
      ZUuu =self.stfuncs.ZX(1,z1,z2,Q2,None,'pi+','pi-') + self.stfuncs.ZX(1,z1,z2,Q2,None,'pi-','pi+')
      ZLuu =self.stfuncs.ZX(1,z1,z2,Q2,None,'pi+','pi+') + self.stfuncs.ZX(1,z1,z2,Q2,None,'pi-','pi-')
      ZUcol=self.stfuncs.ZX(2,z1,z2,Q2,None,'pi+','pi-') + self.stfuncs.ZX(2,z1,z2,Q2,None,'pi-','pi+')
      ZLcol=self.stfuncs.ZX(2,z1,z2,Q2,None,'pi+','pi+') + self.stfuncs.ZX(2,z1,z2,Q2,None,'pi-','pi-')
      thy=factor*(ZUcol/ZUuu - ZLcol/ZLuu)
    elif obs=='AUC-0-PT-INT':
      ZUuu =self.stfuncs.ZX(1,z1,z2,Q2,None,'pi+','pi-') + self.stfuncs.ZX(1,z1,z2,Q2,None,'pi-','pi+')
      ZLuu =self.stfuncs.ZX(1,z1,z2,Q2,None,'pi+','pi+') + self.stfuncs.ZX(1,z1,z2,Q2,None,'pi-','pi-')
      ZUcol=self.stfuncs.ZX(2,z1,z2,Q2,None,'pi+','pi-') + self.stfuncs.ZX(2,z1,z2,Q2,None,'pi-','pi+')
      ZLcol=self.stfuncs.ZX(2,z1,z2,Q2,None,'pi+','pi+') + self.stfuncs.ZX(2,z1,z2,Q2,None,'pi-','pi-')
      ZCuu=ZUuu+ZLuu
      ZCcol=ZUcol+ZLcol
      thy=factor*(ZUcol/ZUuu - ZCcol/ZCuu)
    else:
      print 'ERR: obs=%s  not implemented'%obs
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
      if len(self.tabs[k]['value'])==0: continue
      res =self._get_residuals(k)
      rres=self._get_rres(k)
      nres=self._get_nres(k)
      
      chi2=np.sum(res**2)
      rchi2=np.sum(rres**2)
      nchi2=nres**2
      col=self.tabs[k]['col'][0].split()[0]
      npts=res.size
      L.append('%7d %10s %5d %10.2f %10.2f %10.2f'%(k,col,npts,chi2,rchi2,nchi2))

    if level==1:
      L.append('-'*100)  

      msg ='col=%7s  '
      msg+='obs=%7s  '
      msg+='z1=%10.3e  '
      msg+='z2=%10.3e  '
      msg+='Q2=%10.3e  '
      msg+='exp=%10.3e  ' 
      msg+='alpha=%10.3e  ' 
      msg+='thy=%10.3e  ' 
      msg+='shift=%10.3e  ' 
      msg+='chi2=%10.3f  '

      for k in self.tabs:
        if len(self.tabs[k]['value'])==0: continue 
        for i in range(len(self.tabs[k]['value'])):
          z1=self.tabs[k]['z1'][i]
          z2=self.tabs[k]['z2'][i]
          Q2=self.tabs[k]['Q2'][i]
          res=self.tabs[k]['residuals'][i]
          thy=self.tabs[k]['thy'][i]
          exp=self.tabs[k]['value'][i]
          alpha=self.tabs[k]['alpha'][i]
          rres=self.tabs[k]['r-residuals'][i]
          col=self.tabs[k]['col'][i]
          obs=self.tabs[k]['obs'][i]
          shift=self.tabs[k]['shift'][i]
          if res<0: chi2=-res**2
          else: chi2=res**2
          L.append(msg%(col,obs,z1,z2,Q2,exp,alpha,thy,shift,chi2))

    if verb==0:
      return L
    elif verb==1:
      for l in L: print l

if __name__=='__main__':

  conf={}
  conf['aux']=AUX()
  conf['path2DSS']='../../external/DSSLIB'
  conf['_ff']=DSS(conf)
  conf['ff']=FF(conf)
  conf['collins']=COLLINS(conf)
  conf['sia stfuncs']=STFUNCS(conf)


  conf['datasets']={}
  conf['datasets']['sia']={}
  conf['datasets']['sia']['xlsx']={}
  conf['datasets']['sia']['xlsx'][1000]='../../database/sia/expdata/1000.xlsx'  #   babar      | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
  conf['datasets']['sia']['xlsx'][1001]='../../database/sia/expdata/1001.xlsx'  #   babar      | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
  #conf['datasets']['sia']['xlsx'][1002]='../database/sia/expdata/1002.xlsx'  #   babar      | pi,pi | AUC-0     | 36     | z1,z2      |
  #conf['datasets']['sia']['xlsx'][1003]='../database/sia/expdata/1003.xlsx'  #   babar      | pi,pi | AUL-0     | 36     | z1,z2      |
  #conf['datasets']['sia']['xlsx'][1004]='../database/sia/expdata/1004.xlsx'  #   belle      | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
  #conf['datasets']['sia']['xlsx'][1005]='../database/sia/expdata/1005.xlsx'  #   belle      | pi,pi | AUT-0     | 16     | z1,z2,qT   |
  conf['datasets']['sia']['norm']={}
  conf['datasets']['sia']['norm'][1000]={'value':1,'fixed':False} 
  conf['datasets']['sia']['norm'][1001]={'value':1,'fixed':False}
  #conf['datasets']['sia']['norm'][1002]={'value':1,'fixed':False}
  #conf['datasets']['sia']['norm'][1003]={'value':1,'fixed':False}
  #conf['datasets']['sia']['norm'][1004]={'value':1,'fixed':False}
  #conf['datasets']['sia']['norm'][1005]={'value':1,'fixed':False}

  #conf['datasets']['sia']['filters']=[]
  #conf['datasets']['sia']['filters'].append("z<0.6") 
  #conf['datasets']['sia']['filters'].append("Q2>1.69") 
  #conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.8") 
  conf['sia tabs']=READER(conf).load_data_sets('sia')
  conf['residuals']=RESIDUALS(conf)
  conf['residuals'].get_residuals()
  conf['residuals'].gen_report(verb=1,level=1)







