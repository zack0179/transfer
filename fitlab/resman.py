#!/usr/bin/env python
import sys,os
import argparse
import numpy as np
from numpy.random import choice,randn,uniform
from tools.tools import load_config
import pandas as pd
import external.CJLIB.CJ
import external.DSSLIB.DSS
import external.LSSLIB.LSS
import qcdlib.tmdlib
import qcdlib.aux
import qcdlib.alphaS
import obslib.dis.stfuncs
import obslib.sidis.stfuncs
import obslib.sidis.residuals
import obslib.sidis.reader
import obslib.sia.stfuncs
import obslib.sia.residuals
import obslib.sia.reader
import obslib.moments.reader 
import obslib.moments.moments
import obslib.moments.residuals
from parman import PARMAN
from speedtest import SPEEDTEST
from mcsamp import MCSAMP
from maxlike import ML

class RESMAN:

  def __init__(self,conf):
    self.conf=conf
    self.npts=0
    conf['aux']=qcdlib.aux.AUX()
    self.setup_tmds()
    conf['parman']=PARMAN(conf)
    conf['moments']=obslib.moments.moments.MOMENTS(conf)
    if 'sidis' in conf['datasets']:
      self.setup_dis()
      self.setup_sidis()
    if 'sia' in conf['datasets']:
      self.setup_sia()
    if 'moments' in conf['datasets']:
      self.setup_moments()

  def setup_dis(self):
    conf=self.conf
    conf['alphaSmode']='backward'
    conf['Q20']=1
    #conf['order']='NLO'
    conf['order']='LO'
    conf['alphaS']=qcdlib.alphaS.ALPHAS(conf)
    conf['pdf-NLO']=external.CJLIB.CJ.CJ(conf)
    conf['dis stfuncs']=obslib.dis.stfuncs.STFUNCS(conf)

  def setup_tmds(self):
    conf=self.conf
    conf['order']='LO'
    conf['_pdf'] =external.CJLIB.CJ.CJ(conf)
    conf['_ppdf']=external.LSSLIB.LSS.LSS(conf)
    conf['_ff']  =external.DSSLIB.DSS.DSS(conf)
    conf['pdf']  =qcdlib.tmdlib.PDF(conf)
    conf['ppdf'] =qcdlib.tmdlib.PPDF(conf)
    conf['ff']   =qcdlib.tmdlib.FF(conf)
    conf['transversity']=qcdlib.tmdlib.TRANSVERSITY(conf)
    conf['sivers']      =qcdlib.tmdlib.SIVERS(conf)
    conf['boermulders'] =qcdlib.tmdlib.BOERMULDERS(conf)
    conf['pretzelosity']=qcdlib.tmdlib.PRETZELOSITY(conf)
    conf['wormgearg']   =qcdlib.tmdlib.WORMGEARG(conf)
    conf['wormgearh']   =qcdlib.tmdlib.WORMGEARH(conf)
    conf['collins']     =qcdlib.tmdlib.COLLINS(conf)
    
  def setup_sidis(self):
    conf=self.conf
    conf['sidis tabs']      =obslib.sidis.reader.READER(conf).load_data_sets('sidis')
    conf['sidis stfuncs']   =obslib.sidis.stfuncs.STFUNCS(conf)
    self.sidisres=obslib.sidis.residuals.RESIDUALS(conf)
    res,rres,nres=self.sidisres.get_residuals()
    self.npts+=res.size

  def setup_sia(self):
    conf=self.conf
    conf['sia tabs']      =obslib.sia.reader.READER(conf).load_data_sets('sia')
    conf['sia stfuncs']   =obslib.sia.stfuncs.STFUNCS(conf)
    self.siares=obslib.sia.residuals.RESIDUALS(conf)
    res,rres,nres=self.siares.get_residuals()
    self.npts+=res.size

  def setup_moments(self):
    conf=self.conf
    conf['moments tabs']=obslib.moments.reader.READER(conf).load_data_sets('moments')
    conf['moments']=obslib.moments.moments.MOMENTS(conf)
    self.momres=obslib.moments.residuals.RESIDUALS(conf)
    res,rres,nres=self.momres.get_residuals()
    self.npts+=res.size

  def _get_residuals(self,func,res,rres,nres):
    _res,_rres,_nres=func()
    res=np.append(res,_res)
    rres=np.append(rres,_rres)
    nres=np.append(nres,_nres)
    return res,rres,nres
    
  def get_residuals(self,par):
    self.conf['parman'].set_new_params(par)
    res,rres,nres=[],[],[]
    if 'sidis'   in self.conf['datasets']: res,rres,nres=self._get_residuals(self.sidisres.get_residuals,res,rres,nres)
    if 'sia'     in self.conf['datasets']: res,rres,nres=self._get_residuals(self.siares.get_residuals,res,rres,nres)
    if 'moments' in self.conf['datasets']: res,rres,nres=self._get_residuals(self.momres.get_residuals,res,rres,nres)
    return res,rres,nres

  def gen_report(self,verb=0,level=0):
    L=[]
    if 'sidis'   in self.conf['datasets']: L.extend(self.sidisres.gen_report(verb,level))
    if 'sia'     in self.conf['datasets']: L.extend(self.siares.gen_report(verb,level))
    if 'moments' in self.conf['datasets']: L.extend(self.momres.gen_report(verb,level))
    return L

if __name__=='__main__':

  ap = argparse.ArgumentParser()
  ap.add_argument('config', help='config file (e.g. input.py)')
  msg =" 0: speedtest"
  msg+=" 1: maxlike-minimize"
  msg+=" 2: maxlike-leastsq"
  msg+=" 3: mcsamp-nest"
  msg+=" 4: mcsamp-imc"
  msg+=" 5: mcsamp-analysis"
  ap.add_argument('-t','--task',type=int,default=0,help=msg)
  ap.add_argument('-i','--runid',type=int,default=0,help=msg)
  #ap.add_argument('-o','--outdir',type=str,default='.',help="output directory (default: %(default)s)")
  #ap.add_argument('-x','--ignoresnap',action='store_true',help='do not load snapshot file')
  ap.add_argument('-f','--file',type=str,default='',help=" path to nest file")
  #ap.add_argument('-q','--snapshot',type=str,default='.',help=" path to snapshot file")
  args = ap.parse_args()
  
  conf=load_config(args.config)
  conf['args']=args
  conf['resman']=RESMAN(conf)

  if   args.task==0: SPEEDTEST(conf).run()
  elif args.task==1: ML(conf).run_minimize()
  elif args.task==2: ML(conf).run_leastsq()
  elif args.task==3: MCSAMP(conf).run_nest()
  elif args.task==4: MCSAMP(conf).run_imc()
  elif args.task==5: MCSAMP(conf).analysis()


