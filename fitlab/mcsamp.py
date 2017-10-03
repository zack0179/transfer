#!/usr/bin/env python
import sys,os
import numpy as np
from tools.tools import load,save,checkdir,load_config
from tools.bar import BAR
from nest import NEST
from imc import IMC
import pandas as pd

class MCSAMP:

  def __init__(self,conf):
    self.conf=conf

  def get_residuals(self,par):
    res,rres,nres=self.conf['resman'].get_residuals(par)
    if len(rres)!=0: res=np.append(res,rres)
    if len(nres)!=0: res=np.append(res,nres)
    return res 

  def loglike(self,par):
    return -0.5*np.sum(self.get_residuals(par)**2)

  def nll(self,par):
    res=self.get_residuals(par)
    return 0.5*(np.sum(res**2)-res.size)

  def likelihood(self,par):
    res=self.get_residuals(par)
    return np.exp(-0.5*(np.sum(res**2)-res.size))

  def linmap(self,q,pmin,pmax): 
    return (pmax-pmin)*q+pmin 

  def get_par_lims(self):
    plims=[]
    for i in range(len(self.conf['parman'].order)):
      ii,k,kk=self.conf['parman'].order[i]
      if ii==1:
        pmin=self.conf['params'][k][kk]['min']
        pmax=self.conf['params'][k][kk]['max']
      elif ii==2:
        pmin=self.conf['datasets'][k]['norm'][kk]['min']
        pmax=self.conf['datasets'][k]['norm'][kk]['max']
      plims.append([pmin,pmax])
    return plims

  def run_nest(self):

    inputfile=self.conf['args'].config
    run_id=inputfile.replace('inputs/','')
    outputdir='outputs/%s'%run_id.replace('.py','')
    checkdir(outputdir)
    os.system('cp %s %s/'%(inputfile,outputdir))

    self.npar=len(self.conf['parman'].par)
    par=self.conf['parman'].par
    res=self.get_residuals(par)

    conf={}
    if self.conf['args'].file!='':
      conf['nestout']=load(self.conf['args'].file)

    conf['nll'] = self.nll
    conf['par lims'] = self.get_par_lims()
    conf['method']=self.conf['method']
    conf['kappa']=self.conf['kappa']
    conf['tol']=self.conf['tol']
    conf['num points'] = self.conf['num points']
    conf['sample size']= self.conf['sample size']
    conf['burn size']= self.conf['burn size']
    conf['data size']=len(res)
    nest=NEST(conf).run()
    save(nest,'%s/nest%d'%(outputdir,self.conf['args'].runid))

  def run_imc(self):

    inputfile=self.conf['args'].config
    run_id=inputfile.replace('inputs/','')
    outputdir='outputs/%s'%run_id.replace('.py','')
    checkdir(outputdir)
    os.system('cp %s %s/'%(inputfile,outputdir))

    self.npar=len(self.conf['parman'].par)

    conf={}
    conf['nll'] = self.nll
    conf['par lims'] = self.get_par_lims()
    conf['kappa']=1.1
    conf['tol']=10e-10
    conf['num points'] = 50
    imc=IMC(conf).run()
    save(imc,'%s/nest%d'%(outputdir,self.conf['args'].runid))

  # analysis routines. Use analysis as the gate

  def analysis(self):
    self.get_dvt()

  def get_dvt(self):
    resman=self.conf['resman']
    inputfile=self.conf['args'].config
    run_id=inputfile.replace('inputs/','')
    outputdir='outputs/%s'%run_id.replace('.py','')

    def get_RAW():
      RAW={}
      for k in self.conf['datasets']: 
        RAW[k]={}
        for kk in self.conf['datasets'][k]['xlsx']: 
          RAW[k][kk]=[]
      return RAW

    for i in range(10):
      # load nestfile
      nest=load('%s/nest%d'%(outputdir,i))
      # cut parameters that wont contribute
      wmin_cut=1e-7
      weights=[nest['weights'][j] for j in range(len(nest['weights'])) if nest['weights'][j]>wmin_cut]
      samples=[nest['samples'][j] for j in range(len(nest['weights'])) if nest['weights'][j]>wmin_cut]
      weights/=np.sum(weights)

      THY=get_RAW()
      RES=get_RAW()
      bar=BAR('gen chi2 values for nest%d'%i,len(samples))
      for ii in range(len(samples)):
        par=samples[ii]
        resman.get_residuals(par)
        for k in RES:
          if k=='sidis': 
            for kk in RES[k]: 
              THY[k][kk].append(np.copy(resman.sidisres.tabs[kk]['thy']))
              RES[k][kk].append(np.copy(resman.sidisres.tabs[kk]['residuals']))
          if k=='moments': 
            for kk in RES[k]:
              THY[k][kk].append(np.copy(resman.momres.tabs[kk]['thy']))
              RES[k][kk].append(np.copy(resman.momres.tabs[kk]['residuals']))
        bar.next()
      bar.finish()
      RAW={'THY':THY,'RES':RES}
      save(RAW,'%s/raw%d'%(outputdir,i))

  def simulation(self):
    resman=self.conf['resman']
    inputfile=self.conf['args'].config
    nestfile=self.conf['args'].file
    List=[int(idx) for idx in self.conf['args'].list]
    reaction=self.conf['args'].reaction
    
    nest=load(nestfile)
    par=nest['samples'][0]
    resman.get_residuals(par)

    if reaction=='sidis':
      for k in List:
        npts=resman.sidisres.tabs[k]['value'].size
        resman.sidisres.tabs[k]['value']=resman.sidisres.tabs[k]['thy']+np.random.randn(npts)*resman.sidisres.tabs[k]['alpha']
        tab=pd.DataFrame(resman.sidisres.tabs[k])
        writer = pd.ExcelWriter(self.conf['datasets'][reaction]['xlsx'][k])
        tab.to_excel(writer,'Sheet1')
        writer.save()
    else:
      raise ValueError('reaction not supported for simulation. revise MCSAMP.simulation @ mcsamp.py')


