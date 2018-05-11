#!/usr/bin/env python
import sys,os
import numpy as np
import time
from scipy.integrate import quad,fixed_quad
from external.CJLIB.CJ import CJ
from external.PDF.CT10 import CT10 # Alexei 4/20/2018
from external.LSSLIB.LSS import LSS
from external.DSSLIB.DSS import DSS
from aux import AUX
from scipy.special import gamma, psi
from tools.config import conf

class CORE:

  def p2n(self,p):
    n=np.copy(p)
    u  =n[1]
    ub =n[2]
    d  =n[3]
    db =n[4]
    n[1] = d
    n[2] = db
    n[3] = u
    n[4] = ub
    return n

  def pip2pim(self,pip):
    pim=np.copy(pip)
    u  =pip[1]
    ub =pip[2]
    d  =pip[3]
    db =pip[4]
    pim[1] = ub
    pim[2] = u
    pim[3] = db
    pim[4] = d
    return pim

  def kp2km(self,kp):
    km=np.copy(kp)
    u  =kp[1]
    ub =kp[2]
    s  =kp[5]
    sb =kp[6]
    km[1] = ub
    km[2] = u
    km[5] = sb
    km[6] = s
    return km

  def beta(self,a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

  def get_shape(self,x,p):

    if conf['shape']==0:

        return  p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*x**2)

    elif conf['shape']==1:

       norm=self.beta(1+p[1],p[2]+1)+p[3]*self.beta(1+p[1]+1,p[2]+1)+p[4]*self.beta(1+p[1]+2,p[2]+1)
       return  p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*x**2)/norm

    elif conf['shape']==2:
        
       norm=self.beta(1+p[1],1+p[2])+p[3]*self.beta(1+p[1]+1,1+p[2])+p[4]*self.beta(1+p[1],1+p[2])*(psi(p[1]+p[2]+2)-psi(p[1]+1))
       return  p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*np.log(1/x))/norm

    elif conf['shape'] == 3:
      norm = np.pow((p[1]+p[2]),p[1]+p[2])/(np.pow(p[1],p[1])*np.pow(p[2],p[2]))
      return  norm*p[0]*x**p[1]*(1-x)**p[2]

    elif conf['shape']==4:

       norm=self.beta(2+p[1],p[2]+1)+p[3]*self.beta(2+p[1]+1,p[2]+1)+p[4]*self.beta(2+p[1]+2,p[2]+1)
       return  p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*x**2)/norm

  def get_collinear(self,x,hadron):
    N=np.zeros(11)
    for i in range(11): 
      if 'shape' in self.__dict__:
        N[i]=self.get_shape(x,self.shape[hadron][i])
      if 'shape1' in self.__dict__:
        N[i]=self.get_shape(x,self.shape1[hadron][i])
      if 'shape2' in self.__dict__:
        N[i]+=self.get_shape(x,self.shape2[hadron][i])

    return N

  def get_gauss(self,kT2,hadron):
    return np.exp(-kT2/self.widths[hadron])/np.pi/self.widths[hadron] 

  def get_tmd(self,x,Q2,kT2,hadron):
    C=self.get_C(x,Q2,hadron)
    gauss=self.get_gauss(kT2,hadron)
    return self.K[hadron]*C*gauss

class PDF(CORE):

  def __init__(self):
    if 'basis' not in conf: conf['basis']='default'
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.widths0={}
    if conf['basis'] == 'default':
      self.widths0['valence']=0.3
      self.widths0['sea']=0.3
    if conf['basis'] == 'valence':
      self.widths0['uv']=0.3
      self.widths0['dv']=0.3
      self.widths0['sea']=0.3

    self.widths={}
    self.widths['p']=np.ones(11)

    self.K={}
    self.K['p']=np.ones(11)
    self.K['n']=np.ones(11)

  def setup(self):
    if conf['basis'] == 'default':
      for i in range(11):
        if i==1 or i==3:
          self.widths['p'][i]=self.widths0['valence']
        else:
          self.widths['p'][i]=self.widths0['sea']
      self.widths['n']=self.p2n(self.widths['p'])
    elif conf['basis'] == 'valence':
      for i in range(11):
        if i==1:
          self.widths['p'][i]=self.widths0['uv']
        elif i==3:
          self.widths['p'][i]=self.widths0['dv']
        else:
          self.widths['p'][i]=self.widths0['sea']
      self.widths['n']=self.p2n(self.widths['p'])

  def get_C(self,x,Q2,target='p'):
    C=conf['_pdf'].get_f(x,Q2)
    C[0]=0 # glue is not supported
    if target=='n': C=self.p2n(C)
    return C

class FF(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.widths0={}
    self.widths0['pi+ fav']  =0.12
    self.widths0['pi+ unfav']=0.12
    self.widths0['h+ fav']  =0.12
    self.widths0['h+ unfav']=0.12
    self.widths0['k+ fav']   =0.12
    self.widths0['k+ unfav'] =0.12
    
    self.widths={}
    self.widths['pi+']=np.ones(11)
    self.widths['h+']=np.ones(11)
    self.widths['k+'] =np.ones(11)

    self.K={}
    self.K['pi+']=np.ones(11)
    self.K['h+']=np.ones(11)
    self.K['k+'] =np.ones(11)
    self.K['pi-']=np.ones(11)
    self.K['h-']=np.ones(11)
    self.K['k-'] =np.ones(11)

  def get_K(self, z, hadron):
    return 1.0

  def setup(self):
    # u  1
    # ub 2
    # d  3
    # db 4
    # s  5
    # sb 6
    # c  7
    # cb 8
    # b  9
    # bb 10
    for i in range(1,11):
      if i==1 or i==4:
        self.widths['pi+'][i]=np.copy(self.widths0['pi+ fav'])
      else: 
        self.widths['pi+'][i]=np.copy(self.widths0['pi+ unfav'])

    for i in range(1,11):
      if i==1 or i==4:
        self.widths['h+'][i]=np.copy(self.widths0['h+ fav'])
      else: 
        self.widths['h+'][i]=np.copy(self.widths0['h+ unfav'])

    for i in range(1,11):
      if i==1 or i==6:
        self.widths['k+'][i]=np.copy(self.widths0['k+ fav'])
      else: 
        self.widths['k+'][i]=np.copy(self.widths0['k+ unfav'])

    self.widths['pi-']=self.pip2pim(self.widths['pi+'])
    self.widths['h-']=self.pip2pim(self.widths['h+'])
    self.widths['k-'] =self.kp2km(self.widths['k+'])

  def get_C(self,x,Q2,hadron='pi+'):
    C=conf['_ff'].get_f(x,Q2,hadron)
    C[0]=0 # glue is not supported
    return C

class COLLINS(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.Mh={}
    self.Mh['pi+']=self.aux.Mpi
    self.Mh['pi-']=self.aux.Mpi
    self.Mh['h+']=self.aux.Mpi
    self.Mh['h-']=self.aux.Mpi
    self.Mh['k+']=self.aux.Mk
    self.Mh['k-']=self.aux.Mk

    self.widths0={}
    self.widths0['pi+ fav']  =0.11
    self.widths0['pi+ unfav']=0.11
    self.widths0['h+ fav']  =0.11
    self.widths0['h+ unfav']=0.11
    self.widths0['k+ fav']   =0.11
    self.widths0['k+ unfav'] =0.11

    self.shape1={}
    self.shape1['pi+']=np.zeros((11,5))
    self.shape1['h+']=np.zeros((11,5))
    self.shape1['k+']=np.zeros((11,5))

    self.shape2={}
    self.shape2['pi+']=np.zeros((11,5))
    self.shape2['h+']=np.zeros((11,5))
    self.shape2['k+']=np.zeros((11,5))
    
    self.widths={}
    self.widths['pi+']=np.ones(11)
    self.widths['h+']=np.ones(11)
    self.widths['k+'] =np.ones(11)

    self.K={}
    self.K['pi+']=np.ones(11)
    self.K['h+']=np.ones(11)
    self.K['k+'] =np.ones(11)
    self.K['pi-']=np.ones(11)
    self.K['h-']=np.ones(11)
    self.K['k-'] =np.ones(11)

    self.norm={}

  def get_norm(self,hadron):
    return 1#np.sqrt(np.exp(1)/2)*self.widths[hadron]*self.M[hadron]**3/(self.Mh[hadron]*(self.M[hadron]**2+self.widths[hadron])**2)

  def get_K(self,z,hadron):
    return 2*z**2*self.Mh[hadron]**2/self.widths[hadron]

  def setup(self):
    # 1,  2,  3,  4,  5,  6,  7,  8,  9, 10
    # u, ub,  d, db,  s, sb,  c, cb,  b, bb
    for i in range(1,11):
      if i==1 or i==4:
        self.widths['pi+'][i]=np.copy(self.widths0['pi+ fav'])
      else: 
        self.widths['pi+'][i]=np.copy(self.widths0['pi+ unfav'])

    for i in range(1,11):
      if i==1 or i==4:
        self.widths['h+'][i]=np.copy(self.widths0['h+ fav'])
      else: 
        self.widths['h+'][i]=np.copy(self.widths0['h+ unfav'])

        
    for i in range(1,11):
      if i==1 or i==6:
        self.widths['k+'][i]=np.copy(self.widths0['k+ fav'])
      else: 
        self.widths['k+'][i]=np.copy(self.widths0['k+ unfav'])

    self.shape1['pi-']=self.pip2pim(self.shape1['pi+'])
    self.shape2['pi-']=self.pip2pim(self.shape2['pi+'])

    self.shape1['h-']=self.pip2pim(self.shape1['h+'])
    self.shape2['h-']=self.pip2pim(self.shape2['h+'])
    
    self.shape1['k-']=self.kp2km(self.shape1['k+'])
    self.shape2['k-']=self.kp2km(self.shape2['k+'])

    self.widths['pi-']=self.pip2pim(self.widths['pi+'])
    self.widths['h-']=self.pip2pim(self.widths['h+'])
    self.widths['k-']=self.kp2km(self.widths['k+'])

    for hadron in ['pi+','pi-','h+','h-','k+','k-']:
      self.norm[hadron]=self.get_norm(hadron) 
      self.K[hadron]=self.get_K(1.0,hadron) 

  def get_C(self,z,Q2,hadron='pi+'):
    #ff=conf['_ff'].get_f(z,Q2,hadron)
    C=self.get_collinear(z,hadron)#*ff
    C[0]=0 # glue is not supported
    return C

class SIVERS(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.shape={}
    self.shape['p']=np.zeros((11,5))
    self.shape['p'][1]=[0.46,1.11,3.64,0,0]
    self.shape['p'][3]=[-1,1.11,3.64,0,0]

    self.widths0={}
    self.widths0['valence']=0.26
    self.widths0['sea']=0.26

    self.widths={}
    self.widths['p']=np.ones(11)

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']
    self.shape['n']=self.p2n(self.shape['p'])
    self.widths['n']=self.p2n(self.widths['p'])

  def get_C(self,x,Q2,target='p'):
    C=self.get_collinear(x,target)
    if target=='n': C=self.p2n(C)
    return C

class TRANSVERSITY(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    conf['shape']=0
    self.shape={}
    self.shape['p']=np.zeros((11,5))
    self.shape['p'][1]=[0.46,1.11,3.64,0,0] #u
    self.shape['p'][3]=[-1,1.11,3.64,0,0] #d
    self.shape['p'][2]=[0.,1.,1.,0,0] #ub
    self.shape['p'][4]=[0.,1.,1.,0,0] #db
    self.shape['p'][5]=[0.,1.,1.,0,0] #s
    self.shape['p'][6]=[0.,1.,1.,0,0] #sb
    self.shape['p'][7]=[0.,1.,1.,0,0] #c
    self.shape['p'][8]=[0.,1.,1.,0,0] #cb

    self.widths0={}
    self.widths0['valence']=0.26
    self.widths0['sea']=0.26

    self.widths={}
    self.widths['p']=np.ones(11)

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']
    self.shape['n']=self.p2n(self.shape['p'])
    self.widths['n']=self.p2n(self.widths['p'])

  def get_C(self,x,Q2,target='p'):
    C=self.get_collinear(x,target)
    if target=='n': C=self.p2n(C)
    return C

class PPDF(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):
    self.widths0={}
    self.widths0['valence']=0.19
    self.widths0['sea']=0.19

    self.widths={}
    self.widths['p']=np.ones(11)

    self.K={}
    self.K['p']=np.ones(11)
    self.K['n']=np.ones(11)

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']

    self.widths['n']=self.p2n(self.widths['p'])

  def get_C(self,x,Q2,target='p'):
    C=conf['_ppdf'].get_f(x,Q2)
    C[0]=0 # glue is not supported
    if target=='n': C=self.p2n(C)
    return C

class BOERMULDERS(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.shape={}
    self.shape['p']=np.zeros((11,5))
    self.shape['p'][1]=[-0.49,0,0,0,0]
    self.shape['p'][3]=[-1.0,0,0,0,0]

    self.widths0={}
    self.widths0['valence']=0.085
    self.widths0['sea']=0.085

    self.widths={}
    self.widths['p']=np.ones(11)

    #self.M={}
    #self.M['p']=0.1**0.5
    #self.M['n']=0.1**0.5

    self.K={}
    #self.norm={}

  def get_K(self,x,hadron):
    return 2*self.aux.M2/self.widths[hadron]

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']
    self.shape['n']=self.p2n(self.shape['p'])
    self.widths['n']=self.p2n(self.widths['p'])
    for hadron in ['p','n']:
      #self.norm[hadron]=self.get_norm(hadron)
      self.K[hadron]=self.get_K(1.0,hadron)

  def get_C(self,x,Q2,target='p'):
    C=self.get_collinear(x,target)
    if target=='n': C=self.p2n(C)
    return C

class PRETZELOSITY(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):

    self.shape={}
    self.shape['p']=np.zeros((11,5))
    self.shape['p'][1]=[1,2.5,2,0,0]
    self.shape['p'][3]=[-1.0,2.5,2,0,0]

    self.widths0={}
    self.widths0['valence']=0.137
    self.widths0['sea']=0.137

    self.widths={}
    self.widths['p']=np.ones(11)

    #self.M={}
    #self.M['p']=self.aux.M
    #self.M['n']=self.aux.M

    self.K={}
    #self.norm={}

  def get_K(self,x,hadron):
    return 2*self.aux.M2**2/self.widths[hadron]**2

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']
    self.shape['n']=self.p2n(self.shape['p'])
    self.widths['n']=self.p2n(self.widths['p'])
    for hadron in ['p','n']:
      self.K[hadron]=self.get_K(1.0,hadron)

  def get_C(self,x,Q2,target='p'):
    C=self.get_collinear(x,target)
    if target=='n': C=self.p2n(C)
    return C

class WORMGEARG(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):
    self.K={}
    self.K['p']=np.ones(11)
    self.K['n']=np.ones(11)

    self.widths0={}
    self.widths0['valence']=0.19
    self.widths0['sea']=0.19

    self.widths={}
    self.widths['p']=np.ones(11)

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']
    self.widths['n']=self.p2n(self.widths['p'])

  def pol(self,i,x,Q2,target): 
    return conf['_ppdf'].get_f(x,Q2)[i]
 
  def get_C(self,x,Q2,target='p'):
    #C = np.array([x*quad(lambda y: self.pol(i,x,Q2,target)/y,x,1)[0] for i in range(11)])
    #C = np.array([x*fixed_quad(np.vectorize(lambda y: self.pol(i,x,Q2,target)/y),x,1)[0] for i in range(11)])
    C=np.zeros(11)
    C[0]=0 # glue is not supported!!!  
    if target=='n': C=self.p2n(C)
    return C

class WORMGEARH(CORE):

  def __init__(self):
    self.aux=conf['aux']
    self.set_default_params()
    self.setup()

  def set_default_params(self):
    self.K={}
    self.K['p']=np.ones(11)
    self.K['n']=np.ones(11)

    self.widths0={}
    self.widths0['valence']=0.25
    self.widths0['sea']=0.25

    self.widths={}
    self.widths['p']=np.ones(11)

  def setup(self):
    for i in range(11):
      if i==1 or i==3:
        self.widths['p'][i]=self.widths0['valence']
      else:
        self.widths['p'][i]=self.widths0['sea']

    self.widths['n']=self.p2n(self.widths['p'])

  def trans(self,i,x,Q2,target):
    return conf['transversity'].get_C(x,Q2,target)[i]

  def get_C(self,x,Q2,target='p'):
    #C = np.array([x*quad(lambda y: self.trans(i,x,Q2,target)/y,x,1)[0] for i in range(11)])
    #C = np.array([x*fixed_quad(np.vectorize(lambda y: self.trans(i,x,Q2,target)/y),x,1)[0] for i in range(11)])
    C=np.zeros(11)
    C[0]=0 # glue is not supported!!!  
    if target=='n': C=self.p2n(C)
    return C


if __name__=='__main__':

  conf['path2CJ'] ='../external/CJLIB'
  conf['path2LSS']='../external/LSSLIB'
  conf['path2DSS']='../external/DSSLIB'
  conf['path2CT10'] ='../external/PDF'

  conf['order']='LO'
  conf['aux']=AUX()
  #conf['_pdf']=CT10()
  conf['_pdf']=CJ()
  conf['_ppdf']=LSS()
  conf['_ff']=DSS()
  conf['hadron']='pi'

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

  x=0.15
  Q2=2.4
  dist=['pdf','ppdf','ff','transversity','sivers','boermulders']
  dist.extend(['pretzelosity','wormgearg','wormgearh','collins'])
  for k in dist:
    print k
    print conf[k].get_C(x,Q2)





