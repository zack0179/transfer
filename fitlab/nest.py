#!/usr/bin/env python
import sys,os
import numpy as np
from numpy.random import rand,randn,uniform
from scipy.integrate import quad,simps
from numpy import linalg as LA
from scipy.stats import gaussian_kde
import time
import cPickle 
import pickle 
import zlib
import warnings
warnings.filterwarnings('ignore')
from timeit import default_timer as timer

# aux funcs

def lprint(msg):
  sys.stdout.write('\r')
  sys.stdout.write(msg)
  sys.stdout.flush()

def checkdir(path):
  if not os.path.exists(path): 
    os.makedirs(path)

def save(data,name):  
  compressed=zlib.compress(cPickle.dumps(data))
  f=open(name,"wb")
  f.writelines(compressed)
  f.close()

def load(name): 
  compressed=open(name,"rb").read()
  data=cPickle.loads(zlib.decompress(compressed))
  return data

def load_snapshot(name): 
  data=pickle.loads(open(name,"rb").read())
  self.__dict__.update(data.__dict__)

class ELLIPSE:

  def __init__(self,samples,kappa=1.1,N=None):

    self.N=N    
    self.dim=len(samples[0])
    # generate transformation matrix
    self.y0=np.mean(samples,axis=0)
    cov=np.cov(np.transpose(samples))
    icov=np.linalg.inv(cov)
    w,v=np.linalg.eig(icov)
    v=np.transpose(v)
    for i in range(w.size): v[i]/=w[i]**0.5
    self.T=np.transpose(v)
    
    # get enlargement factor
    self.F=kappa*np.amax([np.einsum('i,ij,j',y-self.y0,icov,y-self.y0) for y in samples])**0.5

    self.gen_new_samples()

  def gen_new_samples(self):
    # generate the unit sphere
    z=np.random.randn(self.N,self.dim)
    r=np.array([np.dot(z[i],z[i])**0.5 for i in range(self.N)])
    X=np.array([z[i]/r[i]*np.random.rand()**(1.0/self.dim) for i in range(self.N)])

    # generate sphere samples
    Y=np.einsum('ij,nj->ni',self.F*self.T,X) + self.y0
    self.Y=[y for y in Y]

  def status(self):
    if len(self.Y)>0: return True
    else: return False

  def get_sample(self):
    return self.Y.pop()

class NEST:

  def __init__(self,conf):
    self.conf=conf
    self.get_nll = conf['nll']
    self.pmin=np.array([entry[0] for entry in conf['par lims']])
    self.pmax=np.array([entry[1] for entry in conf['par lims']])
    self.dp=np.array([entry[1]-entry[0] for entry in conf['par lims']])
    self.dim =len(conf['par lims']) 
    self.jac=np.prod(self.dp)
    self.N=conf['num points'] # number of active set
    self.factor=self.N/(self.N+1.) # factor to estimate prior mass

    self.samples_p=[]
    self.samples_x=[1]
    self.samples_l=[0]
    self.samples_nll=[]
    self.logz=[]
    self.cnt=0 # counter
    self.attempts=None
    self.set_active_sets(self.N)
    self.status='warming'
    #if conf['method']=='cov':
    #  self.ellipse=ELLIPSE(self.active_p,conf['kappa'],conf['sample size'])

  # param generators
  
  def gen_par(self):
    u=uniform(0,1,self.dim)
    return self.pmin + u*self.dp    
  
  def gen_par_flat(self,nll):
    self.attempts=0
    while 1:
      self.attempts+=1
      p=self.gen_par()
      _nll = self.get_nll(p)
      if _nll<nll: break
    return p,_nll
  
  def gen_par_kde(self,nll):
    kde=gaussian_kde(np.transpose(self.active_p),self.conf['kde bw'])
    self.attempts=0
    while 1:
      p=np.transpose(kde.resample(1))[0]
      if any([x<0 for x in p-self.pmin]): continue
      if any([x<0 for x in self.pmax-p]): continue    
      self.attempts+=1
      _nll = self.get_nll(p)
      if _nll<nll: break
    return p,_nll
  
  def gen_par_hmc(self,par,nll):
  
    delta=self.conf['hmc delta']
    steps=self.conf['hmc steps']
  
    get_U=lambda q: self.get_nll(q)
    
    def get_dU_i(i,q):
      h=0.01*q
      shift=np.zeros(dim)
      shift[i]=h[i]
      return (get_U(q+shift)-get_U(q-shift))/2/h[i]
    
    get_dU=lambda q: np.array([get_dU_i(i,q) for i in range(dim)])
    get_K=lambda p: np.dot(p,p)/2
    get_dK=lambda p: p
    get_H=lambda q,p: get_U(q) + get_K(p)
  
    q0=np.copy(par)
    H0=get_H(q0,par)
    while 1:
      p0=randn(dim)
      p=np.copy(p0)
      q=np.copy(q0)
      p=p0-delta/2*get_dU(q0)
      q=q0+delta*p
      for i in range(steps):
        p=p-delta*get_dU(q)
        q=q+delta*get_dK(p)
      p=p-delta/2*get_dU(q)
      _nll = get_nll(q)
      if _nll<nll: break
    return q,_nll

  def gen_par_cov(self,nll):
    self.attempts=0
    ellipse=ELLIPSE(self.active_p,self.conf['kappa'],self.conf['sample size'])
    while 1:
      self.attempts+=1
      if ellipse.status()==False:
        #ellipse=ELLIPSE(self.active_p,self.conf['kappa'],self.conf['sample size'])
        #self.ellipse=ELLIPSE(self.active_p,self.conf['kappa'],self.conf['sample size'])
        ellipse.gen_new_samples()
      p=ellipse.get_sample()
      if any([x<0 for x in p-self.pmin]): continue
      if any([x<0 for x in self.pmax-p]): continue    
      _nll = self.get_nll(p)
      if _nll<nll: break
    return p,_nll

  # nested sampling routines
  
  def gen_sample(self):
  
    # remove entry from active arrays
    #imax=np.argmax(self.active_nll)
    nll=self.active_nll.pop()
    p=self.active_p.pop()

    # update samples 
    self.samples_nll.append(nll)
    self.samples_l.append(np.exp(-nll))
    self.samples_p.append(p)
    self.samples_x.append(self.samples_x[-1]*self.factor)  
    self.cnt+=1
  
    # sample new parms
    if self.conf['method']=='flat': _p,_nll=self.gen_par_flat(nll)
    if self.conf['method']=='cov':  _p,_nll=self.gen_par_cov(nll)
    if self.conf['method']=='kde':  _p,_nll=self.gen_par_kde(nll)
    if self.conf['method']=='hmc':  _p,_nll=self.gen_par_hmc(p,nll)
  
    self.active_nll.append(_nll)
    self.active_p.append(_p)
  
  def get_logz(self):
    return np.log(np.trapz(self.samples_l[::-1],self.samples_x[::-1])*self.jac)
  
  def set_active_sets(self,N):
    self.active_p=[]
    self.active_nll=[]
    cnt_active=0
    while 1:
      lprint('getting initial active p: %d/%d'%(cnt_active+1,N))
      p=self.gen_par()
      nll=self.get_nll(p)
      #if np.exp(-nll)>0:
      cnt_active+=1
      self.active_p.append(p)
      self.active_nll.append(nll)
      if cnt_active==N: break
    I=np.argsort(self.active_nll)
    self.active_nll=[self.active_nll[i] for i in I]
    self.active_p=[self.active_p[i] for i in I]

  def next(self,t_elapsed):
    self.gen_sample()
    self.logz.append(self.get_logz())
    if self.cnt>2: 
      z_past=np.exp(self.logz[-2])
      z_current=np.exp(self.logz[-1])
      rel = np.abs(1-z_past/z_current)
      nllmax=self.active_nll[-1]
      nllmin=self.active_nll[0]
      msg='iter=%d  logz=%.3f rel-err=%.3e  t-elapsed=%.3e  nll_min=%.3e nll_max=%0.3e  attemps=%10d'
      msg=msg%(self.cnt,self.logz[-1],rel,t_elapsed,nllmin,nllmax,self.attempts)
      lprint(msg)
      # stopping criterion
      if 'itmax' in self.conf and self.cnt==self.conf['itmax']: 
        self.status='stop'
      if self.logz[-1]>-1e10  and self.conf['tol']!=None:
        if rel<self.conf['tol']: self.status='stop'
        #l=np.exp(-self.active_nll[0])
        #x=self.samples_x[-1]
        #dz=l*x
        #if np.log(dz)<self.logz[-1]+np.log(self.conf['tol']):
        #  self.status='stop'

  def results(self):
    log_x=np.log(self.samples_x)
    log_l=np.log(self.samples_l)
    log_w=log_x+log_l-self.logz[-1]
    weights=np.exp(log_w)
    weights/=np.sum(weights)
  
    data={}
    data['samples']=self.samples_p[::-1]
    data['x']=self.samples_x[1:][::-1]
    data['l']=self.samples_l[1:][::-1]
    data['logz']=self.logz
    data['weights']=weights[1:][::-1]

    return data

  def run(self):
  
    t1=timer()
    print 
    while 1:
      try:
        t2=timer()
        self.next(t2-t1)
        if self.status=='stop': break
      except KeyboardInterrupt:
        break
    print 
    return self.results() 
 
if __name__=='__main__':

  shift1=np.array([1, 1])
  shift2=np.array([1,-1])
  widths=[1,1,1,1]
  def likelihood(a):
    return 1./(2*np.pi*widths[0]**2)* np.exp(-np.sum((a-shift1)**2/2/widths[0]**2))\
         + 1./(2*np.pi*widths[1]**2)* np.exp(-np.sum((a+shift1)**2/2/widths[1]**2))\
         + 1./(2*np.pi*widths[2]**2)* np.exp(-np.sum((a-shift2)**2/2/widths[2]**2))\
         + 1./(2*np.pi*widths[3]**2)* np.exp(-np.sum((a+shift2)**2/2/widths[3]**2))
  nll=lambda p: -np.log(likelihood(p))


  print 'True:'
  print 'logz=',np.log(4)


  print 
  print 'Nested Sampling:'
  conf={}
  conf['method']='cov'
  conf['kappa']=1.1

  #conf['method']='kde'
  #conf['kde bw']=None
  ##conf['itmax']=None

  conf['nll'] = nll
  conf['par lims'] =[[-20,20],[-20,20]]
  conf['tol']=1e-4
  for N in [100,200,300,400,500]:
    conf['num points'] = N
    conf['sample size']= N
    print 'N=',N
    NEST(conf).run()

  print 
  print 'VEGAS:'
  import vegas
  integ = vegas.Integrator([[-20, 20], [-20, 20]])
  result = integ(likelihood, nitn=10, neval=1000)
  print result.summary() 
  print 'logz = %s    Q = %.2f' % (np.log(result), result.Q)
















