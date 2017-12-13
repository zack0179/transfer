#!/usr/bin/env python
import sys,os
import numpy as np 
from numpy.random import choice,randn,uniform
from tools.tools import load_config
import pandas as pd
from external.CJLIB.CJ import CJ
from external.DSSLIB.DSS import DSS
from external.LSSLIB.LSS import LSS
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
from obslib.sidis.reader import READER as SIDIS_READER
from obslib.sidis.stfuncs import STFUNCS as SIDIS_STFUNCS
from obslib.sidis.residuals import RESIDUALS as SIDIS_RESIDUALS

class PARMAN:

  def __init__(self,conf):
    self.conf=conf
    self.get_ordered_free_params()
    self.set_new_params(self.par,initial=True)

  def get_ordered_free_params(self):
    self.par=[]
    self.order=[]

    for k in self.conf['params']:
      for kk in self.conf['params'][k]:
        if self.conf['params'][k][kk]['fixed']==False:
          #p=uniform(self.conf['params'][k][kk]['min'],self.conf['params'][k][kk]['max'],1)[0]
          self.par.append(self.conf['params'][k][kk]['value'])
          self.order.append([1,k,kk])

    if 'datasets' in self.conf:
      for k in self.conf['datasets']:
        for kk in self.conf['datasets'][k]['norm']:
          if self.conf['datasets'][k]['norm'][kk]['fixed']==False:
            self.par.append(self.conf['datasets'][k]['norm'][kk]['value'])
            self.order.append([2,k,kk])
        
  def set_new_params(self,parnew,initial=False):
    self.shifts=0
    semaphore={}

    for i in range(len(self.order)):
      ii,k,kk=self.order[i]  
      if ii==1:
        if k not in semaphore: semaphore[k]=0
        if self.conf['params'][k][kk]['value']!=parnew[i]:
          self.conf['params'][k][kk]['value']=parnew[i]
          semaphore[k]=1
          self.shifts+=1
      elif ii==2:
        if self.conf['datasets'][k]['norm'][kk]['value']!=parnew[i]:
          self.conf['datasets'][k]['norm'][kk]['value']=parnew[i]
          self.shifts+=1

    if initial:
      for k in self.conf['params']: semaphore[k]=1

    self.propagate_params(semaphore)

  def gen_report(self):
    L=[]

    for k in self.conf['params']:
      for kk in sorted(self.conf['params'][k]):
        if self.conf['params'][k][kk]['fixed']==False: 
          if self.conf['params'][k][kk]['value']<0:
            L.append('%-10s  %-20s  %10.5e'%(k,kk,self.conf['params'][k][kk]['value']))
          else:
            L.append('%-10s  %-20s   %10.5e'%(k,kk,self.conf['params'][k][kk]['value']))

    for k in self.conf['datasets']:
      for kk in self.conf['datasets'][k]['norm']:
        if self.conf['datasets'][k]['norm'][kk]['fixed']==False: 
          L.append('%10s %10s %10d  %10.5e'%('norm',k,kk,self.conf['datasets'][k]['norm'][kk]['value']))
    return L

  def propagate_params(self,semaphore):
    #print 'semaphore:',semaphore
    if 'pdf' in semaphore and semaphore['pdf']==1: self.set_pdf_params()
    if 'ff'  in semaphore and semaphore['ff']==1:  self.set_ff_params()
    if 'sivers' in semaphore and semaphore['sivers']==1:  self.set_sivers_params()
    if 'transversity' in semaphore and semaphore['transversity']==1:  self.set_transversity_params()
    if 'collins' in semaphore and semaphore['collins']==1:  self.set_collins_params()
    if 'boermulders' in semaphore and semaphore['boermulders']==1:  self.set_boermulders_params()
    if 'pretzelosity' in semaphore and semaphore['pretzelosity']==1:  self.set_pretzelosity_params()
    if 'soft' in semaphore and semaphore['soft']==1: self.set_soft_params()

  def set_pdf_params(self):
    self.conf['pdf'].widths0['valence']=self.conf['params']['pdf']['widths0 valence']['value']
    self.conf['pdf'].widths0['sea']=self.conf['params']['pdf']['widths0 sea']['value']
    self.conf['pdf'].setup() 
  
  def set_ff_params(self):
    self.conf['ff'].widths0['pi+ fav']=self.conf['params']['ff']['widths0 pi+ fav']['value']
    self.conf['ff'].widths0['pi+ unfav']=self.conf['params']['ff']['widths0 pi+ unfav']['value']
    self.conf['ff'].widths0['k+ fav']=self.conf['params']['ff']['widths0 k+ fav']['value']
    self.conf['ff'].widths0['k+ unfav']=self.conf['params']['ff']['widths0 k+ unfav']['value']
    self.conf['ff'].setup() 

  def set_sivers_params(self):

    self.conf['sivers'].widths0['valence']=self.conf['params']['sivers']['widths0 valence']['value']
    self.conf['sivers'].widths0['sea']=self.conf['params']['sivers']['widths0 sea']['value']

    self.conf['sivers'].shape['p'][1][0]=self.conf['params']['sivers']['u N']['value']
    self.conf['sivers'].shape['p'][1][1]=self.conf['params']['sivers']['u a']['value']
    self.conf['sivers'].shape['p'][1][2]=self.conf['params']['sivers']['u b']['value']
    self.conf['sivers'].shape['p'][1][3]=self.conf['params']['sivers']['u c']['value']
    self.conf['sivers'].shape['p'][1][4]=self.conf['params']['sivers']['u d']['value']

    self.conf['sivers'].shape['p'][3][0]=self.conf['params']['sivers']['d N']['value']
    self.conf['sivers'].shape['p'][3][1]=self.conf['params']['sivers']['d a']['value']
    self.conf['sivers'].shape['p'][3][2]=self.conf['params']['sivers']['d b']['value']
    self.conf['sivers'].shape['p'][3][3]=self.conf['params']['sivers']['d c']['value']
    self.conf['sivers'].shape['p'][3][4]=self.conf['params']['sivers']['d d']['value']

    self.conf['sivers'].shape['p'][5][0]=self.conf['params']['sivers']['s N']['value']
    self.conf['sivers'].shape['p'][5][1]=self.conf['params']['sivers']['s a']['value']
    self.conf['sivers'].shape['p'][5][2]=self.conf['params']['sivers']['s b']['value']
    self.conf['sivers'].shape['p'][5][3]=self.conf['params']['sivers']['s c']['value']
    self.conf['sivers'].shape['p'][5][4]=self.conf['params']['sivers']['s d']['value']

    self.conf['sivers'].shape['p'][2][0]=self.conf['params']['sivers']['ub N']['value']
    self.conf['sivers'].shape['p'][2][1]=self.conf['params']['sivers']['ub a']['value']
    self.conf['sivers'].shape['p'][2][2]=self.conf['params']['sivers']['ub b']['value']
    self.conf['sivers'].shape['p'][2][3]=self.conf['params']['sivers']['ub c']['value']
    self.conf['sivers'].shape['p'][2][4]=self.conf['params']['sivers']['ub d']['value']

    self.conf['sivers'].shape['p'][4][0]=self.conf['params']['sivers']['db N']['value']
    self.conf['sivers'].shape['p'][4][1]=self.conf['params']['sivers']['db a']['value']
    self.conf['sivers'].shape['p'][4][2]=self.conf['params']['sivers']['db b']['value']
    self.conf['sivers'].shape['p'][4][3]=self.conf['params']['sivers']['db c']['value']
    self.conf['sivers'].shape['p'][4][4]=self.conf['params']['sivers']['db d']['value']

    self.conf['sivers'].shape['p'][6][0]=self.conf['params']['sivers']['sb N']['value']
    self.conf['sivers'].shape['p'][6][1]=self.conf['params']['sivers']['sb a']['value']
    self.conf['sivers'].shape['p'][6][2]=self.conf['params']['sivers']['sb b']['value']
    self.conf['sivers'].shape['p'][6][3]=self.conf['params']['sivers']['sb c']['value']
    self.conf['sivers'].shape['p'][6][4]=self.conf['params']['sivers']['sb d']['value']

    self.conf['sivers'].setup() 

  def set_transversity_params(self):

    self.conf['transversity'].widths0['valence']=self.conf['params']['transversity']['widths0 valence']['value']
    self.conf['transversity'].widths0['sea']=self.conf['params']['transversity']['widths0 sea']['value']

    self.conf['transversity'].shape['p'][1][0]=self.conf['params']['transversity']['u N']['value']
    self.conf['transversity'].shape['p'][1][1]=self.conf['params']['transversity']['u a']['value']
    self.conf['transversity'].shape['p'][1][2]=self.conf['params']['transversity']['u b']['value']
    self.conf['transversity'].shape['p'][1][3]=self.conf['params']['transversity']['u c']['value']
    self.conf['transversity'].shape['p'][1][4]=self.conf['params']['transversity']['u d']['value']

    self.conf['transversity'].shape['p'][3][0]=self.conf['params']['transversity']['d N']['value']
    self.conf['transversity'].shape['p'][3][1]=self.conf['params']['transversity']['d a']['value']
    self.conf['transversity'].shape['p'][3][2]=self.conf['params']['transversity']['d b']['value']
    self.conf['transversity'].shape['p'][3][3]=self.conf['params']['transversity']['d c']['value']
    self.conf['transversity'].shape['p'][3][4]=self.conf['params']['transversity']['d d']['value']

    self.conf['transversity'].shape['p'][5][0]=self.conf['params']['transversity']['s N']['value']
    self.conf['transversity'].shape['p'][5][1]=self.conf['params']['transversity']['s a']['value']
    self.conf['transversity'].shape['p'][5][2]=self.conf['params']['transversity']['s b']['value']
    self.conf['transversity'].shape['p'][5][3]=self.conf['params']['transversity']['s c']['value']
    self.conf['transversity'].shape['p'][5][4]=self.conf['params']['transversity']['s d']['value']

    self.conf['transversity'].shape['p'][2][0]=self.conf['params']['transversity']['s N']['value']
    self.conf['transversity'].shape['p'][2][1]=self.conf['params']['transversity']['s a']['value']
    self.conf['transversity'].shape['p'][2][2]=self.conf['params']['transversity']['s b']['value']
    self.conf['transversity'].shape['p'][2][3]=self.conf['params']['transversity']['s c']['value']
    self.conf['transversity'].shape['p'][2][4]=self.conf['params']['transversity']['s d']['value']

    self.conf['transversity'].shape['p'][4][0]=self.conf['params']['transversity']['s N']['value']
    self.conf['transversity'].shape['p'][4][1]=self.conf['params']['transversity']['s a']['value']
    self.conf['transversity'].shape['p'][4][2]=self.conf['params']['transversity']['s b']['value']
    self.conf['transversity'].shape['p'][4][3]=self.conf['params']['transversity']['s c']['value']
    self.conf['transversity'].shape['p'][4][4]=self.conf['params']['transversity']['s d']['value']

    self.conf['transversity'].shape['p'][6][0]=self.conf['params']['transversity']['s N']['value']
    self.conf['transversity'].shape['p'][6][1]=self.conf['params']['transversity']['s a']['value']
    self.conf['transversity'].shape['p'][6][2]=self.conf['params']['transversity']['s b']['value']
    self.conf['transversity'].shape['p'][6][3]=self.conf['params']['transversity']['s c']['value']
    self.conf['transversity'].shape['p'][6][4]=self.conf['params']['transversity']['s d']['value']

    self.conf['transversity'].setup() 

  def set_boermulders_params(self):
    ''' Currently we're using the symmetric sea approximation 
    where below, all sea quark parameters are set based on the 
    value of the s quark parameters. 
    '''

    self.conf['boermulders'].widths0['valence']=self.conf['params']['boermulders']['widths0 valence']['value']
    self.conf['boermulders'].widths0['sea']=self.conf['params']['boermulders']['widths0 sea']['value']
    self.conf['boermulders'].shape['p'][1][0]=self.conf['params']['boermulders']['u N']['value']
    self.conf['boermulders'].shape['p'][1][1]=self.conf['params']['boermulders']['u a']['value']
    self.conf['boermulders'].shape['p'][1][2]=self.conf['params']['boermulders']['u b']['value']
    self.conf['boermulders'].shape['p'][3][0]=self.conf['params']['boermulders']['d N']['value']
    self.conf['boermulders'].shape['p'][3][1]=self.conf['params']['boermulders']['d a']['value']
    self.conf['boermulders'].shape['p'][3][2]=self.conf['params']['boermulders']['d b']['value']
    self.conf['boermulders'].shape['p'][4][0]=self.conf['params']['boermulders']['s N']['value']
    self.conf['boermulders'].shape['p'][4][1]=self.conf['params']['boermulders']['s a']['value']
    self.conf['boermulders'].shape['p'][4][2]=self.conf['params']['boermulders']['s b']['value']
    self.conf['boermulders'].shape['p'][5][0]=self.conf['params']['boermulders']['s N']['value']
    self.conf['boermulders'].shape['p'][5][1]=self.conf['params']['boermulders']['s a']['value']
    self.conf['boermulders'].shape['p'][5][2]=self.conf['params']['boermulders']['s b']['value']
    self.conf['boermulders'].shape['p'][6][0]=self.conf['params']['boermulders']['s N']['value']
    self.conf['boermulders'].shape['p'][6][1]=self.conf['params']['boermulders']['s a']['value']
    self.conf['boermulders'].shape['p'][6][2]=self.conf['params']['boermulders']['s b']['value']
    self.conf['boermulders'].shape['p'][2][0]=self.conf['params']['boermulders']['s N']['value']
    self.conf['boermulders'].shape['p'][2][1]=self.conf['params']['boermulders']['s a']['value']
    self.conf['boermulders'].shape['p'][2][2]=self.conf['params']['boermulders']['s b']['value']
    self.conf['boermulders'].setup() 

  def set_pretzelosity_params(self):
    ''' Currently we're using the symmetric sea approximation 
    where below, all sea quark parameters are set based on the 
    value of the s quark parameters. 
    '''

    self.conf['pretzelosity'].widths0['valence']=self.conf['params']['pretzelosity']['widths0 valence']['value']
    self.conf['pretzelosity'].widths0['sea']=self.conf['params']['pretzelosity']['widths0 sea']['value']
    self.conf['pretzelosity'].shape['p'][1][0]=self.conf['params']['pretzelosity']['u N']['value']
    self.conf['pretzelosity'].shape['p'][1][1]=self.conf['params']['pretzelosity']['u a']['value']
    self.conf['pretzelosity'].shape['p'][1][2]=self.conf['params']['pretzelosity']['u b']['value']
    self.conf['pretzelosity'].shape['p'][3][0]=self.conf['params']['pretzelosity']['d N']['value']
    self.conf['pretzelosity'].shape['p'][3][1]=self.conf['params']['pretzelosity']['d a']['value']
    self.conf['pretzelosity'].shape['p'][3][2]=self.conf['params']['pretzelosity']['d b']['value']
    self.conf['pretzelosity'].shape['p'][4][0]=self.conf['params']['pretzelosity']['s N']['value']
    self.conf['pretzelosity'].shape['p'][4][1]=self.conf['params']['pretzelosity']['s a']['value']
    self.conf['pretzelosity'].shape['p'][4][2]=self.conf['params']['pretzelosity']['s b']['value']
    self.conf['pretzelosity'].shape['p'][5][0]=self.conf['params']['pretzelosity']['s N']['value']
    self.conf['pretzelosity'].shape['p'][5][1]=self.conf['params']['pretzelosity']['s a']['value']
    self.conf['pretzelosity'].shape['p'][5][2]=self.conf['params']['pretzelosity']['s b']['value']
    self.conf['pretzelosity'].shape['p'][6][0]=self.conf['params']['pretzelosity']['s N']['value']
    self.conf['pretzelosity'].shape['p'][6][1]=self.conf['params']['pretzelosity']['s a']['value']
    self.conf['pretzelosity'].shape['p'][6][2]=self.conf['params']['pretzelosity']['s b']['value']
    self.conf['pretzelosity'].shape['p'][2][0]=self.conf['params']['pretzelosity']['s N']['value']
    self.conf['pretzelosity'].shape['p'][2][1]=self.conf['params']['pretzelosity']['s a']['value']
    self.conf['pretzelosity'].shape['p'][2][2]=self.conf['params']['pretzelosity']['s b']['value']
    self.conf['pretzelosity'].setup() 

  def set_collins_params(self):

    self.conf['collins'].widths0['pi+ fav']     = self.conf['params']['collins']['widths0 pi+ fav']['value']
    self.conf['collins'].widths0['pi+ unfav']   = self.conf['params']['collins']['widths0 pi+ unfav']['value']

    self.conf['collins'].shape['pi+'][1][0]=self.conf['params']['collins']['pi+ u N']['value']
    self.conf['collins'].shape['pi+'][1][1]=self.conf['params']['collins']['pi+ u a']['value']
    self.conf['collins'].shape['pi+'][1][2]=self.conf['params']['collins']['pi+ u b']['value']
    self.conf['collins'].shape['pi+'][1][3]=self.conf['params']['collins']['pi+ u c']['value']
    self.conf['collins'].shape['pi+'][1][4]=self.conf['params']['collins']['pi+ u d']['value']

    self.conf['collins'].shape['pi+'][2][0]=self.conf['params']['collins']['pi+ d N']['value']
    self.conf['collins'].shape['pi+'][2][1]=self.conf['params']['collins']['pi+ d a']['value']
    self.conf['collins'].shape['pi+'][2][2]=self.conf['params']['collins']['pi+ d b']['value']
    self.conf['collins'].shape['pi+'][2][3]=self.conf['params']['collins']['pi+ d c']['value']
    self.conf['collins'].shape['pi+'][2][4]=self.conf['params']['collins']['pi+ d d']['value']

    self.conf['collins'].shape['pi+'][3][0]=self.conf['params']['collins']['pi+ d N']['value']
    self.conf['collins'].shape['pi+'][3][1]=self.conf['params']['collins']['pi+ d a']['value']
    self.conf['collins'].shape['pi+'][3][2]=self.conf['params']['collins']['pi+ d b']['value']
    self.conf['collins'].shape['pi+'][3][3]=self.conf['params']['collins']['pi+ d c']['value']
    self.conf['collins'].shape['pi+'][3][4]=self.conf['params']['collins']['pi+ d d']['value']

    self.conf['collins'].shape['pi+'][4][0]=self.conf['params']['collins']['pi+ u N']['value']
    self.conf['collins'].shape['pi+'][4][1]=self.conf['params']['collins']['pi+ u a']['value']
    self.conf['collins'].shape['pi+'][4][2]=self.conf['params']['collins']['pi+ u b']['value']
    self.conf['collins'].shape['pi+'][4][3]=self.conf['params']['collins']['pi+ u c']['value']
    self.conf['collins'].shape['pi+'][4][4]=self.conf['params']['collins']['pi+ u d']['value']

    self.conf['collins'].shape['pi+'][5][0]=self.conf['params']['collins']['pi+ d N']['value']
    self.conf['collins'].shape['pi+'][5][1]=self.conf['params']['collins']['pi+ d a']['value']
    self.conf['collins'].shape['pi+'][5][2]=self.conf['params']['collins']['pi+ d b']['value']
    self.conf['collins'].shape['pi+'][5][3]=self.conf['params']['collins']['pi+ d c']['value']
    self.conf['collins'].shape['pi+'][5][4]=self.conf['params']['collins']['pi+ d d']['value']

    self.conf['collins'].shape['pi+'][6][0]=self.conf['params']['collins']['pi+ d N']['value']
    self.conf['collins'].shape['pi+'][6][1]=self.conf['params']['collins']['pi+ d a']['value']
    self.conf['collins'].shape['pi+'][6][2]=self.conf['params']['collins']['pi+ d b']['value']
    self.conf['collins'].shape['pi+'][6][3]=self.conf['params']['collins']['pi+ d c']['value']
    self.conf['collins'].shape['pi+'][6][4]=self.conf['params']['collins']['pi+ d d']['value']

    self.conf['collins'].widths0['k+ fav']     = self.conf['params']['collins']['widths0 k+ fav']['value']
    self.conf['collins'].widths0['k+ unfav']   = self.conf['params']['collins']['widths0 k+ unfav']['value']

    self.conf['collins'].shape['k+'][1][0]=self.conf['params']['collins']['k+ u N']['value']
    self.conf['collins'].shape['k+'][1][1]=self.conf['params']['collins']['k+ u a']['value']
    self.conf['collins'].shape['k+'][1][2]=self.conf['params']['collins']['k+ u b']['value']
    self.conf['collins'].shape['k+'][1][3]=self.conf['params']['collins']['k+ u c']['value']
    self.conf['collins'].shape['k+'][1][4]=self.conf['params']['collins']['k+ u d']['value']

    self.conf['collins'].shape['k+'][2][0]=self.conf['params']['collins']['k+ d N']['value']
    self.conf['collins'].shape['k+'][2][1]=self.conf['params']['collins']['k+ d a']['value']
    self.conf['collins'].shape['k+'][2][2]=self.conf['params']['collins']['k+ d b']['value']
    self.conf['collins'].shape['k+'][2][3]=self.conf['params']['collins']['k+ d c']['value']
    self.conf['collins'].shape['k+'][2][4]=self.conf['params']['collins']['k+ d d']['value']

    self.conf['collins'].shape['k+'][3][0]=self.conf['params']['collins']['k+ d N']['value']
    self.conf['collins'].shape['k+'][3][1]=self.conf['params']['collins']['k+ d a']['value']
    self.conf['collins'].shape['k+'][3][2]=self.conf['params']['collins']['k+ d b']['value']
    self.conf['collins'].shape['k+'][3][3]=self.conf['params']['collins']['k+ d c']['value']
    self.conf['collins'].shape['k+'][3][4]=self.conf['params']['collins']['k+ d d']['value']

    self.conf['collins'].shape['k+'][4][0]=self.conf['params']['collins']['k+ d N']['value']
    self.conf['collins'].shape['k+'][4][1]=self.conf['params']['collins']['k+ d a']['value']
    self.conf['collins'].shape['k+'][4][2]=self.conf['params']['collins']['k+ d b']['value']
    self.conf['collins'].shape['k+'][4][3]=self.conf['params']['collins']['k+ d c']['value']
    self.conf['collins'].shape['k+'][4][4]=self.conf['params']['collins']['k+ d d']['value']

    self.conf['collins'].shape['k+'][5][0]=self.conf['params']['collins']['k+ d N']['value']
    self.conf['collins'].shape['k+'][5][1]=self.conf['params']['collins']['k+ d a']['value']
    self.conf['collins'].shape['k+'][5][2]=self.conf['params']['collins']['k+ d b']['value']
    self.conf['collins'].shape['k+'][5][3]=self.conf['params']['collins']['k+ d c']['value']
    self.conf['collins'].shape['k+'][5][4]=self.conf['params']['collins']['k+ d d']['value']

    self.conf['collins'].shape['k+'][6][0]=self.conf['params']['collins']['k+ sb N']['value']
    self.conf['collins'].shape['k+'][6][1]=self.conf['params']['collins']['k+ sb a']['value']
    self.conf['collins'].shape['k+'][6][2]=self.conf['params']['collins']['k+ sb b']['value']
    self.conf['collins'].shape['k+'][6][3]=self.conf['params']['collins']['k+ sb c']['value']
    self.conf['collins'].shape['k+'][6][4]=self.conf['params']['collins']['k+ sb d']['value']

    self.conf['collins'].setup() 

  def set_soft_params(self):
    self.conf['aux'].alpha=self.conf['params']['soft']['alpha']['value']
    self.conf['aux'].beta=self.conf['params']['soft']['beta']['value']
    self.conf['aux'].N=self.conf['params']['soft']['N']['value']

if __name__=='__main__':

  conf=load_config('input.py')

  # setup for inclusive dis
  conf['alphaSmode']='backward'
  conf['Q20']=1
  conf['order']='NLO'
  conf['aux']=AUX()
  conf['alphaS']=ALPHAS(conf)
  conf['pdf-NLO']=CJ(conf)
  conf['dis stfuncs']=DIS_STFUNCS(conf)

  # setup tmds
  conf['order']='LO'
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

  # setup sidis
  conf['sidis tabs']=SIDIS_READER(conf).load_data_sets('sidis')
  conf['sidis stfuncs']=SIDIS_STFUNCS(conf)
  conf['sidis residuals']=SIDIS_RESIDUALS(conf)

  parman=PARMAN(conf)




