#!/usr/bin/env python
import sys,os
import numpy as np 
from numpy.random import choice,randn,uniform
from tools.config import conf,load_config
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

  def __init__(self):
    self.get_ordered_free_params()
    self.set_new_params(self.par,initial=True)

  def get_ordered_free_params(self):
    self.par=[]
    self.order=[]

    for k in conf['params']:
      for kk in conf['params'][k]:
        if conf['params'][k][kk]['fixed']==False:
          #p=uniform(conf['params'][k][kk]['min'],conf['params'][k][kk]['max'],1)[0]
          self.par.append(conf['params'][k][kk]['value'])
          self.order.append([1,k,kk])

    if 'datasets' in conf:
      for k in conf['datasets']:
        for kk in conf['datasets'][k]['norm']:
          if conf['datasets'][k]['norm'][kk]['fixed']==False:
            self.par.append(conf['datasets'][k]['norm'][kk]['value'])
            self.order.append([2,k,kk])

  def set_new_params(self,parnew,initial=False):
    self.shifts=0
    semaphore={}

    for i in range(len(self.order)):
      ii,k,kk=self.order[i]  
      if ii==1:
        if k not in semaphore: semaphore[k]=0
        if conf['params'][k][kk]['value']!=parnew[i]:
          conf['params'][k][kk]['value']=parnew[i]
          semaphore[k]=1
          self.shifts+=1
      elif ii==2:
        if conf['datasets'][k]['norm'][kk]['value']!=parnew[i]:
          conf['datasets'][k]['norm'][kk]['value']=parnew[i]
          self.shifts+=1

    if initial:
      for k in conf['params']: semaphore[k]=1

    self.propagate_params(semaphore)

  def gen_report(self):
    L=[]

    for k in conf['params']:
      for kk in sorted(conf['params'][k]):
        if conf['params'][k][kk]['fixed']==False: 
          if conf['params'][k][kk]['value']<0:
            L.append('%-10s  %-20s  %10.5e'%(k,kk,conf['params'][k][kk]['value']))
          else:
            L.append('%-10s  %-20s   %10.5e'%(k,kk,conf['params'][k][kk]['value']))

    for k in conf['datasets']:
      for kk in conf['datasets'][k]['norm']:
        if conf['datasets'][k]['norm'][kk]['fixed']==False: 
          L.append('%10s %10s %10d  %10.5e'%('norm',k,kk,conf['datasets'][k]['norm'][kk]['value']))
    return L

  def propagate_params(self,semaphore):
    #print 'semaphore:',semaphore
    if 'pdf' in semaphore and semaphore['pdf']==1: self.set_pdf_params()
    if 'ppdf' in semaphore and semaphore['ppdf']==1: self.set_ppdf_params()
    if 'ff'  in semaphore and semaphore['ff']==1:  self.set_ff_params()
    if 'sivers' in semaphore and semaphore['sivers']==1:  self.set_sivers_params()
    if 'transversity' in semaphore and semaphore['transversity']==1:  self.set_transversity_params()
    if 'collins' in semaphore and semaphore['collins']==1:  self.set_collins_params()
    if 'boermulders' in semaphore and semaphore['boermulders']==1:  self.set_boermulders_params()
    if 'pretzelosity' in semaphore and semaphore['pretzelosity']==1:  self.set_pretzelosity_params()
    if 'soft' in semaphore and semaphore['soft']==1: self.set_soft_params()

  def set_pdf_params(self):
    conf['pdf'].widths0['valence']=conf['params']['pdf']['widths0 valence']['value']
    conf['pdf'].widths0['sea']=conf['params']['pdf']['widths0 sea']['value']
    conf['pdf'].setup() 

  def set_ppdf_params(self):
    conf['ppdf'].widths0['valence']=conf['params']['ppdf']['widths0 valence']['value']
    conf['ppdf'].widths0['sea']=conf['params']['ppdf']['widths0 sea']['value']
    conf['ppdf'].setup() 
  
  def set_ff_params(self):
    if 'pi+' in conf['params']['ff']:
      conf['ff'].widths0['pi+ fav']=conf['params']['ff']['widths0 pi+ fav']['value']
      conf['ff'].widths0['pi+ unfav']=conf['params']['ff']['widths0 pi+ unfav']['value']
    if 'k+' in conf['params']['ff']:
      conf['ff'].widths0['k+ fav']=conf['params']['ff']['widths0 k+ fav']['value']
      conf['ff'].widths0['k+ unfav']=conf['params']['ff']['widths0 k+ unfav']['value']
    conf['ff'].setup() 

  def set_sivers_params(self):

    conf['sivers'].widths0['valence']=conf['params']['sivers']['widths0 valence']['value']
    conf['sivers'].widths0['sea']=conf['params']['sivers']['widths0 sea']['value']

    conf['sivers'].shape['p'][1][0]=conf['params']['sivers']['u N']['value']
    conf['sivers'].shape['p'][1][1]=conf['params']['sivers']['u a']['value']
    conf['sivers'].shape['p'][1][2]=conf['params']['sivers']['u b']['value']
    conf['sivers'].shape['p'][1][3]=conf['params']['sivers']['u c']['value']
    conf['sivers'].shape['p'][1][4]=conf['params']['sivers']['u d']['value']

    conf['sivers'].shape['p'][3][0]=conf['params']['sivers']['d N']['value']
    conf['sivers'].shape['p'][3][1]=conf['params']['sivers']['d a']['value']
    conf['sivers'].shape['p'][3][2]=conf['params']['sivers']['d b']['value']
    conf['sivers'].shape['p'][3][3]=conf['params']['sivers']['d c']['value']
    conf['sivers'].shape['p'][3][4]=conf['params']['sivers']['d d']['value']

    conf['sivers'].shape['p'][5][0]=conf['params']['sivers']['s N']['value']
    conf['sivers'].shape['p'][5][1]=conf['params']['sivers']['s a']['value']
    conf['sivers'].shape['p'][5][2]=conf['params']['sivers']['s b']['value']
    conf['sivers'].shape['p'][5][3]=conf['params']['sivers']['s c']['value']
    conf['sivers'].shape['p'][5][4]=conf['params']['sivers']['s d']['value']

    conf['sivers'].shape['p'][2][0]=conf['params']['sivers']['ub N']['value']
    conf['sivers'].shape['p'][2][1]=conf['params']['sivers']['ub a']['value']
    conf['sivers'].shape['p'][2][2]=conf['params']['sivers']['ub b']['value']
    conf['sivers'].shape['p'][2][3]=conf['params']['sivers']['ub c']['value']
    conf['sivers'].shape['p'][2][4]=conf['params']['sivers']['ub d']['value']

    conf['sivers'].shape['p'][4][0]=conf['params']['sivers']['db N']['value']
    conf['sivers'].shape['p'][4][1]=conf['params']['sivers']['db a']['value']
    conf['sivers'].shape['p'][4][2]=conf['params']['sivers']['db b']['value']
    conf['sivers'].shape['p'][4][3]=conf['params']['sivers']['db c']['value']
    conf['sivers'].shape['p'][4][4]=conf['params']['sivers']['db d']['value']

    conf['sivers'].shape['p'][6][0]=conf['params']['sivers']['sb N']['value']
    conf['sivers'].shape['p'][6][1]=conf['params']['sivers']['sb a']['value']
    conf['sivers'].shape['p'][6][2]=conf['params']['sivers']['sb b']['value']
    conf['sivers'].shape['p'][6][3]=conf['params']['sivers']['sb c']['value']
    conf['sivers'].shape['p'][6][4]=conf['params']['sivers']['sb d']['value']

    conf['sivers'].setup() 

  def set_transversity_params(self):
    conf['transversity'].widths0['valence']=conf['params']['transversity']['widths0 valence']['value']
    conf['transversity'].widths0['sea']=conf['params']['transversity']['widths0 sea']['value']

    conf['transversity'].shape['p'][1][0]=conf['params']['transversity']['u N']['value']
    conf['transversity'].shape['p'][1][1]=conf['params']['transversity']['u a']['value']
    conf['transversity'].shape['p'][1][2]=conf['params']['transversity']['u b']['value']
    conf['transversity'].shape['p'][1][3]=conf['params']['transversity']['u c']['value']
    conf['transversity'].shape['p'][1][4]=conf['params']['transversity']['u d']['value']

    conf['transversity'].shape['p'][3][0]=conf['params']['transversity']['d N']['value']
    conf['transversity'].shape['p'][3][1]=conf['params']['transversity']['d a']['value']
    conf['transversity'].shape['p'][3][2]=conf['params']['transversity']['d b']['value']
    conf['transversity'].shape['p'][3][3]=conf['params']['transversity']['d c']['value']
    conf['transversity'].shape['p'][3][4]=conf['params']['transversity']['d d']['value']

    conf['transversity'].shape['p'][5][0]=conf['params']['transversity']['s N']['value']
    conf['transversity'].shape['p'][5][1]=conf['params']['transversity']['s a']['value']
    conf['transversity'].shape['p'][5][2]=conf['params']['transversity']['s b']['value']
    conf['transversity'].shape['p'][5][3]=conf['params']['transversity']['s c']['value']
    conf['transversity'].shape['p'][5][4]=conf['params']['transversity']['s d']['value']

    conf['transversity'].shape['p'][2][0]=conf['params']['transversity']['s N']['value']
    conf['transversity'].shape['p'][2][1]=conf['params']['transversity']['s a']['value']
    conf['transversity'].shape['p'][2][2]=conf['params']['transversity']['s b']['value']
    conf['transversity'].shape['p'][2][3]=conf['params']['transversity']['s c']['value']
    conf['transversity'].shape['p'][2][4]=conf['params']['transversity']['s d']['value']

    conf['transversity'].shape['p'][4][0]=conf['params']['transversity']['s N']['value']
    conf['transversity'].shape['p'][4][1]=conf['params']['transversity']['s a']['value']
    conf['transversity'].shape['p'][4][2]=conf['params']['transversity']['s b']['value']
    conf['transversity'].shape['p'][4][3]=conf['params']['transversity']['s c']['value']
    conf['transversity'].shape['p'][4][4]=conf['params']['transversity']['s d']['value']

    conf['transversity'].shape['p'][6][0]=conf['params']['transversity']['s N']['value']
    conf['transversity'].shape['p'][6][1]=conf['params']['transversity']['s a']['value']
    conf['transversity'].shape['p'][6][2]=conf['params']['transversity']['s b']['value']
    conf['transversity'].shape['p'][6][3]=conf['params']['transversity']['s c']['value']
    conf['transversity'].shape['p'][6][4]=conf['params']['transversity']['s d']['value']

    conf['transversity'].setup() 

  def set_boermulders_params(self):
    ''' Currently we're using the symmetric sea approximation 
    where below, all sea quark parameters are set based on the 
    value of the s quark parameters. 
    '''

    conf['boermulders'].widths0['valence']=conf['params']['boermulders']['widths0 valence']['value']
    conf['boermulders'].widths0['sea']=conf['params']['boermulders']['widths0 sea']['value']
    conf['boermulders'].shape['p'][1][0]=conf['params']['boermulders']['u N']['value']
    conf['boermulders'].shape['p'][1][1]=conf['params']['boermulders']['u a']['value']
    conf['boermulders'].shape['p'][1][2]=conf['params']['boermulders']['u b']['value']
    conf['boermulders'].shape['p'][3][0]=conf['params']['boermulders']['d N']['value']
    conf['boermulders'].shape['p'][3][1]=conf['params']['boermulders']['d a']['value']
    conf['boermulders'].shape['p'][3][2]=conf['params']['boermulders']['d b']['value']
    conf['boermulders'].shape['p'][4][0]=conf['params']['boermulders']['s N']['value']
    conf['boermulders'].shape['p'][4][1]=conf['params']['boermulders']['s a']['value']
    conf['boermulders'].shape['p'][4][2]=conf['params']['boermulders']['s b']['value']
    conf['boermulders'].shape['p'][5][0]=conf['params']['boermulders']['s N']['value']
    conf['boermulders'].shape['p'][5][1]=conf['params']['boermulders']['s a']['value']
    conf['boermulders'].shape['p'][5][2]=conf['params']['boermulders']['s b']['value']
    conf['boermulders'].shape['p'][6][0]=conf['params']['boermulders']['s N']['value']
    conf['boermulders'].shape['p'][6][1]=conf['params']['boermulders']['s a']['value']
    conf['boermulders'].shape['p'][6][2]=conf['params']['boermulders']['s b']['value']
    conf['boermulders'].shape['p'][2][0]=conf['params']['boermulders']['s N']['value']
    conf['boermulders'].shape['p'][2][1]=conf['params']['boermulders']['s a']['value']
    conf['boermulders'].shape['p'][2][2]=conf['params']['boermulders']['s b']['value']
    conf['boermulders'].setup() 

  def set_pretzelosity_params(self):
    ''' Currently we're using the symmetric sea approximation 
    where below, all sea quark parameters are set based on the 
    value of the s quark parameters. 
    '''

    conf['pretzelosity'].widths0['valence']=conf['params']['pretzelosity']['widths0 valence']['value']
    conf['pretzelosity'].widths0['sea']=conf['params']['pretzelosity']['widths0 sea']['value']
    conf['pretzelosity'].shape['p'][1][0]=conf['params']['pretzelosity']['u N']['value']
    conf['pretzelosity'].shape['p'][1][1]=conf['params']['pretzelosity']['u a']['value']
    conf['pretzelosity'].shape['p'][1][2]=conf['params']['pretzelosity']['u b']['value']
    conf['pretzelosity'].shape['p'][3][0]=conf['params']['pretzelosity']['d N']['value']
    conf['pretzelosity'].shape['p'][3][1]=conf['params']['pretzelosity']['d a']['value']
    conf['pretzelosity'].shape['p'][3][2]=conf['params']['pretzelosity']['d b']['value']
    conf['pretzelosity'].shape['p'][4][0]=conf['params']['pretzelosity']['s N']['value']
    conf['pretzelosity'].shape['p'][4][1]=conf['params']['pretzelosity']['s a']['value']
    conf['pretzelosity'].shape['p'][4][2]=conf['params']['pretzelosity']['s b']['value']
    conf['pretzelosity'].shape['p'][5][0]=conf['params']['pretzelosity']['s N']['value']
    conf['pretzelosity'].shape['p'][5][1]=conf['params']['pretzelosity']['s a']['value']
    conf['pretzelosity'].shape['p'][5][2]=conf['params']['pretzelosity']['s b']['value']
    conf['pretzelosity'].shape['p'][6][0]=conf['params']['pretzelosity']['s N']['value']
    conf['pretzelosity'].shape['p'][6][1]=conf['params']['pretzelosity']['s a']['value']
    conf['pretzelosity'].shape['p'][6][2]=conf['params']['pretzelosity']['s b']['value']
    conf['pretzelosity'].shape['p'][2][0]=conf['params']['pretzelosity']['s N']['value']
    conf['pretzelosity'].shape['p'][2][1]=conf['params']['pretzelosity']['s a']['value']
    conf['pretzelosity'].shape['p'][2][2]=conf['params']['pretzelosity']['s b']['value']
    conf['pretzelosity'].setup() 

  def set_collins_params(self):

    if 'pi+ u N 1' in conf['params']['collins']: 

      conf['collins'].widths0['pi+ fav']     = conf['params']['collins']['widths0 pi+ fav']['value']
      conf['collins'].widths0['pi+ unfav']   = conf['params']['collins']['widths0 pi+ unfav']['value']

      conf['collins'].shape1['pi+'][1][0]=conf['params']['collins']['pi+ u N 1']['value']
      conf['collins'].shape1['pi+'][1][1]=conf['params']['collins']['pi+ u a 1']['value']
      conf['collins'].shape1['pi+'][1][2]=conf['params']['collins']['pi+ u b 1']['value']
      conf['collins'].shape1['pi+'][1][3]=conf['params']['collins']['pi+ u c 1']['value']
      conf['collins'].shape1['pi+'][1][4]=conf['params']['collins']['pi+ u d 1']['value']

      conf['collins'].shape1['pi+'][2][0]=conf['params']['collins']['pi+ d N 1']['value']
      conf['collins'].shape1['pi+'][2][1]=conf['params']['collins']['pi+ d a 1']['value']
      conf['collins'].shape1['pi+'][2][2]=conf['params']['collins']['pi+ d b 1']['value']
      conf['collins'].shape1['pi+'][2][3]=conf['params']['collins']['pi+ d c 1']['value']
      conf['collins'].shape1['pi+'][2][4]=conf['params']['collins']['pi+ d d 1']['value']

      conf['collins'].shape1['pi+'][3][0]=conf['params']['collins']['pi+ d N 1']['value']
      conf['collins'].shape1['pi+'][3][1]=conf['params']['collins']['pi+ d a 1']['value']
      conf['collins'].shape1['pi+'][3][2]=conf['params']['collins']['pi+ d b 1']['value']
      conf['collins'].shape1['pi+'][3][3]=conf['params']['collins']['pi+ d c 1']['value']
      conf['collins'].shape1['pi+'][3][4]=conf['params']['collins']['pi+ d d 1']['value']

      conf['collins'].shape1['pi+'][4][0]=conf['params']['collins']['pi+ u N 1']['value']
      conf['collins'].shape1['pi+'][4][1]=conf['params']['collins']['pi+ u a 1']['value']
      conf['collins'].shape1['pi+'][4][2]=conf['params']['collins']['pi+ u b 1']['value']
      conf['collins'].shape1['pi+'][4][3]=conf['params']['collins']['pi+ u c 1']['value']
      conf['collins'].shape1['pi+'][4][4]=conf['params']['collins']['pi+ u d 1']['value']

      conf['collins'].shape1['pi+'][5][0]=conf['params']['collins']['pi+ d N 1']['value']
      conf['collins'].shape1['pi+'][5][1]=conf['params']['collins']['pi+ d a 1']['value']
      conf['collins'].shape1['pi+'][5][2]=conf['params']['collins']['pi+ d b 1']['value']
      conf['collins'].shape1['pi+'][5][3]=conf['params']['collins']['pi+ d c 1']['value']
      conf['collins'].shape1['pi+'][5][4]=conf['params']['collins']['pi+ d d 1']['value']

      conf['collins'].shape1['pi+'][6][0]=conf['params']['collins']['pi+ d N 1']['value']
      conf['collins'].shape1['pi+'][6][1]=conf['params']['collins']['pi+ d a 1']['value']
      conf['collins'].shape1['pi+'][6][2]=conf['params']['collins']['pi+ d b 1']['value']
      conf['collins'].shape1['pi+'][6][3]=conf['params']['collins']['pi+ d c 1']['value']
      conf['collins'].shape1['pi+'][6][4]=conf['params']['collins']['pi+ d d 1']['value']

      #------------------

      conf['collins'].shape2['pi+'][1][0]=conf['params']['collins']['pi+ u N 2']['value']
      conf['collins'].shape2['pi+'][1][1]=conf['params']['collins']['pi+ u a 2']['value']
      conf['collins'].shape2['pi+'][1][2]=conf['params']['collins']['pi+ u b 2']['value']
      conf['collins'].shape2['pi+'][1][3]=conf['params']['collins']['pi+ u c 2']['value']
      conf['collins'].shape2['pi+'][1][4]=conf['params']['collins']['pi+ u d 2']['value']

      conf['collins'].shape2['pi+'][4][0]=conf['params']['collins']['pi+ u N 2']['value']
      conf['collins'].shape2['pi+'][4][1]=conf['params']['collins']['pi+ u a 2']['value']
      conf['collins'].shape2['pi+'][4][2]=conf['params']['collins']['pi+ u b 2']['value']
      conf['collins'].shape2['pi+'][4][3]=conf['params']['collins']['pi+ u c 2']['value']
      conf['collins'].shape2['pi+'][4][4]=conf['params']['collins']['pi+ u d 2']['value']


    if 'k+ u N 1' in conf['params']['collins']: 
      conf['collins'].widths0['k+ fav']     = conf['params']['collins']['widths0 k+ fav']['value']
      conf['collins'].widths0['k+ unfav']   = conf['params']['collins']['widths0 k+ unfav']['value']

      conf['collins'].shape1['k+'][1][0]=conf['params']['collins']['k+ u N 1']['value']
      conf['collins'].shape1['k+'][1][1]=conf['params']['collins']['k+ u a 1']['value']
      conf['collins'].shape1['k+'][1][2]=conf['params']['collins']['k+ u b 1']['value']
      conf['collins'].shape1['k+'][1][3]=conf['params']['collins']['k+ u c 1']['value']
      conf['collins'].shape1['k+'][1][4]=conf['params']['collins']['k+ u d 1']['value']

      conf['collins'].shape1['k+'][2][0]=conf['params']['collins']['k+ d N 1']['value']
      conf['collins'].shape1['k+'][2][1]=conf['params']['collins']['k+ d a 1']['value']
      conf['collins'].shape1['k+'][2][2]=conf['params']['collins']['k+ d b 1']['value']
      conf['collins'].shape1['k+'][2][3]=conf['params']['collins']['k+ d c 1']['value']
      conf['collins'].shape1['k+'][2][4]=conf['params']['collins']['k+ d d 1']['value']

      conf['collins'].shape1['k+'][3][0]=conf['params']['collins']['k+ d N 1']['value']
      conf['collins'].shape1['k+'][3][1]=conf['params']['collins']['k+ d a 1']['value']
      conf['collins'].shape1['k+'][3][2]=conf['params']['collins']['k+ d b 1']['value']
      conf['collins'].shape1['k+'][3][3]=conf['params']['collins']['k+ d c 1']['value']
      conf['collins'].shape1['k+'][3][4]=conf['params']['collins']['k+ d d 1']['value']

      conf['collins'].shape1['k+'][4][0]=conf['params']['collins']['k+ d N 1']['value']
      conf['collins'].shape1['k+'][4][1]=conf['params']['collins']['k+ d a 1']['value']
      conf['collins'].shape1['k+'][4][2]=conf['params']['collins']['k+ d b 1']['value']
      conf['collins'].shape1['k+'][4][3]=conf['params']['collins']['k+ d c 1']['value']
      conf['collins'].shape1['k+'][4][4]=conf['params']['collins']['k+ d d 1']['value']

      conf['collins'].shape1['k+'][5][0]=conf['params']['collins']['k+ d N 1']['value']
      conf['collins'].shape1['k+'][5][1]=conf['params']['collins']['k+ d a 1']['value']
      conf['collins'].shape1['k+'][5][2]=conf['params']['collins']['k+ d b 1']['value']
      conf['collins'].shape1['k+'][5][3]=conf['params']['collins']['k+ d c 1']['value']
      conf['collins'].shape1['k+'][5][4]=conf['params']['collins']['k+ d d 1']['value']

      conf['collins'].shape1['k+'][6][0]=conf['params']['collins']['k+ sb N 1']['value']
      conf['collins'].shape1['k+'][6][1]=conf['params']['collins']['k+ sb a 1']['value']
      conf['collins'].shape1['k+'][6][2]=conf['params']['collins']['k+ sb b 1']['value']
      conf['collins'].shape1['k+'][6][3]=conf['params']['collins']['k+ sb c 1']['value']
      conf['collins'].shape1['k+'][6][4]=conf['params']['collins']['k+ sb d 1']['value']

    conf['collins'].setup() 

  def set_soft_params(self):
    for k in conf['params']['soft']:
      conf['aux'].soft[k]=conf['params']['soft'][k]['value']

if __name__=='__main__':

  load_config('input.py')

  # setup for inclusive dis
  conf['alphaSmode']='backward'
  conf['Q20']=1
  conf['order']='NLO'
  conf['aux']=AUX()
  conf['alphaS']=ALPHAS()
  conf['pdf-NLO']=CJ()
  conf['dis stfuncs']=DIS_STFUNCS()

  # setup tmds
  conf['order']='LO'
  conf['_pdf']=CJ()
  conf['_ppdf']=LSS()
  conf['_ff']=DSS()
  conf['pdf']=PDF()
  conf['ppdf']=PPDF()
  conf['ff']=FF()
  conf['transversity']=TRANSVERSITY()
  conf['sivers']=SIVERS()
  conf['boermulders']=BOERMULDERS()
  conf['pretzelosity']=PRETZELOSITY()
  conf['wormgearg']=WORMGEARG()
  conf['wormgearh']=WORMGEARH()
  conf['collins']=COLLINS()

  # setup sidis
  conf['sidis tabs']=SIDIS_READER().load_data_sets('sidis')
  conf['sidis stfuncs']=SIDIS_STFUNCS()
  conf['sidis residuals']=SIDIS_RESIDUALS()

  parman=PARMAN()




