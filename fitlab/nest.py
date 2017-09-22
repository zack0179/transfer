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
from numpy import linalg as la

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


def _getAplus(A):
  eigval, eigvec = np.linalg.eig(A)
  Q = np.matrix(eigvec)
  xdiag = np.matrix(np.diag(np.maximum(eigval, 0)))
  return Q*xdiag*Q.T

def _getPs(A, W=None):
  W05 = np.matrix(W**.5)
  return  W05.I * _getAplus(W05 * A * W05) * W05.I

def _getPu(A, W=None):
  Aret = np.array(A.copy())
  Aret[W > 0] = np.array(W)[W > 0]
  return np.matrix(Aret)

def nearPD(A, nit=10):
  n = A.shape[0]
  W = np.identity(n) 
  # W is the matrix used for the norm (assumed to be Identity matrix here)
  # the algorithm should work for any diagonal W
  deltaS = 0
  Yk = A.copy()
  for k in range(nit):
      Rk = Yk - deltaS
      Xk = _getPs(Rk, W=W)
      deltaS = Xk - Rk
      Yk = _getPu(Xk, W=W)
  return Yk

def nearPSD(A,epsilon=0):
   n = A.shape[0]
   eigval, eigvec = np.linalg.eig(A)
   val = np.matrix(np.maximum(eigval,epsilon))
   vec = np.matrix(eigvec)
   T = 1/(np.multiply(vec,vec) * val.T)
   T = np.matrix(np.sqrt(np.diag(np.array(T).reshape((n)) )))
   B = T * vec * np.diag(np.array(np.sqrt(val)).reshape((n)))
   out = B*B.T
   return(out)

## need to fix this!!!!


def nearestPD(A):
    """Find the nearest positive-definite matrix to input

    A Python/Numpy port of John D'Errico's `nearestSPD` MATLAB code [1], which
    credits [2].

    [1] https://www.mathworks.com/matlabcentral/fileexchange/42885-nearestspd

    [2] N.J. Higham, "Computing a nearest symmetric positive semidefinite
    matrix" (1988): https://doi.org/10.1016/0024-3795(88)90223-6
    """

    B = (A + A.T) / 2
    _, s, V = la.svd(B)

    H = np.dot(V.T, np.dot(np.diag(s), V))

    A2 = (B + H) / 2

    A3 = (A2 + A2.T) / 2

    if isPD(A3):
        return A3

    spacing = np.spacing(la.norm(A))
    # The above is different from [1]. It appears that MATLAB's `chol` Cholesky
    # decomposition will accept matrixes with exactly 0-eigenvalue, whereas
    # Numpy's will not. So where [1] uses `eps(mineig)` (where `eps` is Matlab
    # for `np.spacing`), we use the above definition. CAVEAT: our `spacing`
    # will be much larger than [1]'s `eps(mineig)`, since `mineig` is usually on
    # the order of 1e-16, and `eps(1e-16)` is on the order of 1e-34, whereas
    # `spacing` will, for Gaussian random matrixes of small dimension, be on
    # othe order of 1e-16. In practice, both ways converge, as the unit test
    # below suggests.
    I = np.eye(A.shape[0])
    k = 1
    while not isPD(A3):
        mineig = np.min(np.real(la.eigvals(A3)))
        A3 += I * (-mineig * k**2 + spacing)
        k += 1

    return A3

def isPD(B):
    """Returns true when input is positive-definite, via Cholesky"""
    try:
        _ = la.cholesky(B)
        return True
    except la.LinAlgError:
        return False

if __name__ == '__main__':
    import numpy as np
    for i in xrange(10):
        for j in xrange(2, 100):
            A = np.random.randn(j, j)
            B = nearestPD(A)
            assert(isPD(B))
    print('unit test passed!')


class ELLIPSE:

  def __init__(self,samples,kappa=1.0,N=None):

    self.N=N    
    self.dim=len(samples[0])
    # generate transformation matrix
    self.y0=np.mean(samples,axis=0)

    cov=np.cov(np.transpose(samples))
    if isPD(cov)==False:
      cov=nearestPD(cov)

    w,v=np.linalg.eig(cov)
    if np.any(np.isnan(v)): raise ValueError('nan eigenvectors')
    #if np.any(w<0): raise ValueError('negative eigenvalues')
    w=np.abs(w)

    #flag=False
    ###if det<0: flag=True
    #for i in range(len(w)):
    #  if any(np.isnan(v[i])): flag=True
    #if flag==True:
    #  cov=nearPSD(cov)

    #mask = w < 1.e-10
    #if np.any(mask):
    #  nzprod = np.product(w[~mask])  # product of nonzero eigenvalues
    #  nzeros = mask.sum()  # number of zero eigenvalues
    #  w[mask] = (V / nzprod) ** (1./nzeros)  # adjust zero eigvals
    #  cov = np.dot(np.dot(v, np.diag(w)), np.linalg.inv(v))  # re-form cov


    icov=np.linalg.inv(cov)
    if np.any(np.isnan(icov)): raise ValueError('icov is nan')
    self.det=np.linalg.det(cov)


    v=np.transpose(v)
    for i in range(w.size): v[i]*=w[i]**0.5
    self.T=np.transpose(v)
    if np.any(np.isnan(self.T)): raise ValueError('T is nan')
    self.w=w
    self.v=v
    
    # get enlargement factor
    self.F=kappa*np.amax([np.einsum('i,ij,j',y-self.y0,icov,y-self.y0) for y in samples])**0.5
    if np.isnan(self.F): raise ValueError('F is nan')
    self.V=(self.F*self.det)**0.5
    self.gen_new_samples()

  def gen_new_samples(self):

    # generate the unit sphere
    z=np.random.randn(self.N,self.dim)
    r=np.array([np.dot(z[i],z[i])**0.5 for i in range(self.N)])
    X=np.array([z[i]/r[i]*np.random.rand()**(1.0/self.dim) for i in range(self.N)])
    #print '='*100
    #print 'det='
    #print self.det
    #print 'w='
    #print self.w
    #print 'X='
    #print X[0]


    # generate sphere samples
    Y=np.einsum('ij,nj->ni',self.F*self.T,X) + self.y0
    #print Y[-10:]
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
    self.V0=np.prod(self.dp)
    self.Vk=self.V0
    self.msg=''

    if 'nestout' not in conf:
      self.samples_p=[]
      self.samples_x=[1]
      self.samples_l=[0]
      self.samples_nll=[]
      self.logz=[]
      self.cnt=0 # counter
      self.attempts=None
      self.set_active_sets(self.N)
    else:
      self.active_p=conf['nestout']['active p']
      self.active_nll=conf['nestout']['active nll']
      self.samples_p=conf['nestout']['samples'][::-1]
      self.samples_x=conf['nestout']['x'][::-1]
      self.samples_l=conf['nestout']['l'][::-1]
      self.samples_nll=[-np.log(l) for l in self.samples_l]
      self.logz=conf['nestout']['logz']
      self.cnt=len(self.samples_l) # counter
      self.attempts=None

    self.status='ready'

  # param generators
  
  def gen_par(self):
    u=uniform(0,1,self.dim)
    return self.pmin + u*self.dp    
  
  def gen_par_flat(self,nll,verb=False):
    self.attempts=0
    pmin=np.amin(self.active_p,axis=0)
    pmax=np.amax(self.active_p,axis=0)
    dp=pmax-pmin
    self.Vk=np.prod(dp)
    while 1:
      self.attempts+=1
      u=uniform(0,1,self.dim)
      p=pmin + u*dp
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
    dim=len(par)  
    delta=0.1#self.conf['hmc delta']
    steps=30#self.conf['hmc steps']
  
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
      print 'hmc attempt',self.attempts
      p0=randn(dim)
      p=np.copy(p0)
      q=np.copy(q0)
      p=p0-delta/2*get_dU(q0)
      q=q0+delta*p
      for i in range(steps):
        print 'walking',i
        p=p-delta*get_dU(q)
        q=q+delta*get_dK(p)
      p=p-delta/2*get_dU(q)
      _nll = self.get_nll(q)
      if _nll<nll: break
    return q,_nll

  #@profile
  def gen_par_cov(self,nll,p0=None,verb=False):
    self.attempts=0
    #print 'building ellipse'
    ellipse=ELLIPSE(self.active_p,self.conf['kappa'],self.conf['sample size'])
    #print 'got ellips'
    self.Vk=ellipse.V
    #pmin=np.amin(self.active_p,axis=0)
    #pmax=np.amax(self.active_p,axis=0)
    #dp=pmax-pmin
    #out=0
    #failed=False
    #if ellipse.det<=0: failed=False
    cnt=0
    #print 'start loop'
    while 1:
      self.attempts+=1
      if verb: print 'cov attempt',self.attempts
      if ellipse.status()==False: ellipse.gen_new_samples()
      p=ellipse.get_sample().real
      if np.any(np.isnan(p)):
        raise ValueError('parameters are nan')
      
      #if self.attempts<1000:
      #  p=ellipse.get_sample().real
      #  self.msg='normal'
      #elif len(self.samples_p)>cnt:
      #  print 
      #  print '-----------'
      #  cnt+=1
      #  q=[p_ for p_ in self.active_p]
      #  for i in range(cnt): q.append(self.samples_p[-i])
      #  ellipse=ELLIPSE(q,self.conf['kappa'],self.conf['sample size'])
      #  self.attemps=0
      #  self.msg='increasing active p',cnt
      #  continue
      #if out<1000 and failed==False:
      #  p=ellipse.get_sample().real
      #else:
      #  u=uniform(0,1,self.dim)
      #  p=pmin + u*dp

      #print self.attempts
      # check limits
      if any([x<0 for x in p-self.pmin]) or any([x<0 for x in self.pmax-p]): continue
      #print 'get nll'
      _nll = self.get_nll(p)
      if _nll<nll: break
    #print 'out>>>'
    return p,_nll

  # nested sampling routines
  
  #@profile
  def gen_sample(self):
  
    # remove entry from active arrays
    imax=np.argmax(self.active_nll)
    nll=self.active_nll.pop(imax)
    p=self.active_p.pop(imax)

    # update samples 
    self.samples_nll.append(nll)
    self.samples_l.append(np.exp(-nll))
    self.samples_p.append(p)
    self.samples_x.append(self.samples_x[-1]*self.factor)  
    self.cnt+=1
  
    # sample new parms
    #print 
    #print 'request'
    if self.conf['method']=='flat': _p,_nll=self.gen_par_flat(nll)
    if self.conf['method']=='cov':  _p,_nll=self.gen_par_cov(nll,p)
    if self.conf['method']=='kde':  _p,_nll=self.gen_par_kde(nll)
    if self.conf['method']=='hmc':  _p,_nll=self.gen_par_hmc(p,nll)
    #print 'got it'
  
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
      cnt_active+=1
      self.active_p.append(p)
      self.active_nll.append(nll)
      if cnt_active==N: break

  def next(self,t_elapsed):
    self.gen_sample()
    self.logz.append(self.get_logz())
    if self.cnt>2: 
      z_past=np.exp(self.logz[-2])
      z_current=np.exp(self.logz[-1])
      rel = np.abs(1-z_past/z_current)
      nllmax=np.amax(self.active_nll)
      nllmin=np.amin(self.active_nll)
      msg='iter=%d  logz=%.3f rel-err=%.3e  t-elapsed=%.3e  nll_min=%.3e nll_max=%0.3e  attemps=%10d  Vk/V0=%0.3e  %s  '
      msg=msg%(self.cnt,self.logz[-1],rel,t_elapsed,nllmin,nllmax,self.attempts,self.Vk/self.V0,self.msg)
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
    data['active p']=self.active_p
    data['active nll']=self.active_nll
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

def example1():

  dim=2
  sigma=np.ones(dim)
  mean=np.zeros(dim)*0.1
  def likelihood(p):
    norm=1/np.prod(np.sqrt(2*np.pi*sigma**2))
    return norm * np.exp(-0.5*np.sum((p-mean)**2/sigma**2))

  nll=lambda p: -np.log(likelihood(p))


  print 'True:'
  print 'logz=',np.log(1)
  print 'min nll=',nll(np.zeros(dim))
  print 
  #print 'VEGAS:'
  #import vegas
  #integ = vegas.Integrator([[-5, 5] for i in range(dim)])
  #result = integ(likelihood, nitn=10, neval=1000)
  #print result.summary() 
  #print 'logz = %s    Q = %.2f' % (np.log(result), result.Q)

  print 
  print 'Nested Sampling:'
  conf={}
  conf['nll'] = nll
  conf['par lims'] =[[-5,5] for i in range(dim)]
  conf['tol']=1e-10
  conf['num points'] = 50

  conf['method']='cov'
  conf['kappa']=1.0
  conf['sample size']= 100

  #conf['method']='kde'
  #conf['kde bw']=None

  NEST(conf).run()

def example2():

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
  conf['nll'] = nll
  conf['par lims'] =[[-20,20],[-20,20]]
  conf['tol']=1e-4
  conf['num points'] = 100


  conf['method']='cov'
  conf['kappa']=1

  #conf['method']='kde'
  #conf['kde bw']=None
  ##conf['itmax']=None

  conf['sample size']= N
  print 'N=',N
  NEST(conf).run()

  #print 
  #print 'VEGAS:'
  #import vegas
  #integ = vegas.Integrator([[-20, 20], [-20, 20]])
  #result = integ(likelihood, nitn=10, neval=1000)
  #print result.summary() 
  #print 'logz = %s    Q = %.2f' % (np.log(result), result.Q)

if __name__=='__main__':

  example1()







