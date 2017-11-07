#!/usr/bin/env python
import sys,os
import numpy as np
from tools.bar import BAR
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.tools import load_config
import pylab as py
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
from fitlab.parman import PARMAN


class MCEG:

  def __init__(self,conf):
    self.conf=conf
    conf['aux']=qcdlib.aux.AUX()
    self.setup_tmds()
    conf['parman']=PARMAN(conf)
    self.setup_dis()
    self.setup_sidis()
  
  def dot4(self,A,B):
    return np.einsum('i,i,i',A,B,[1,-1,-1,-1])

  def get_rotation_params(self,k,A):
    '''
    k is a vector along which vector A will be rotated

    '''
    uk=k/np.linalg.norm(k)
    uA=A/np.linalg.norm(A)
    theta = np.arccos(np.dot(uk,uA))
    w=np.cross(uA,uk)
    u=w/np.linalg.norm(w)
    return u,theta

  def rotate(self,u,theta,A):
    '''
    euler-rodriguez rotation formula

    It rotates A around unit vector u by an angle theta

    '''
    sin=np.sin(theta/2)
    cos=np.cos(theta/2)
    a=cos
    b=u[0]*sin
    c=u[1]*sin
    d=u[2]*sin
    w=[b,c,d]
    return A+2*a*np.cross(w,A)+2*np.cross(w,np.cross(w,A))

  def boost(self,B,A):
    C=np.copy(A)
    C[0]=B[0,0]*A[0] + B[0,1]*A[3]
    C[3]=B[1,0]*A[0] + B[1,1]*A[3]
    return C

  def _gen_event2(self):

    E=self.conf['Ebeam']
    M=self.conf['aux'].M
    Mh=self.conf['aux'].Mpi
    S=self.conf['S']

    lini=np.array([E,0,0,E])
    P=np.array([M,0,0,0])

    # step 1
    Efin=np.random.uniform(0,E)
    cos_theta=np.random.uniform(-1,1)
    phi=np.random.uniform(0,2*np.pi)

    sin_theta=np.sqrt(1-cos_theta**2)
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)

    lfin=np.zeros(4)
    lfin[0]=Efin
    lfin[1]=Efin*sin_theta*cos_phi
    lfin[2]=Efin*sin_theta*sin_phi
    lfin[3]=Efin*cos_theta

    q=lini-lfin

    # step 2
    z=np.random.uniform(Mh/q[0],1)
    Eh=z*q[0]
    ph_mom3=np.sqrt(Eh**2-Mh**2)

    # step 3
    ph_perp=np.random.uniform(0,ph_mom3)
    sign=np.random.choice([-1,1])
    phi=np.random.uniform(0,2*np.pi)

    ph_z=np.sqrt(ph_mom3**2-ph_perp**2)*sign

    ph=np.zeros(4)
    ph[0]=Eh
    ph[1]=ph_perp*np.cos(phi)
    ph[2]=ph_perp*np.sin(phi)
    ph[3]=ph_z 

    # step 4

    # make a copy of the 4 vectors in the lab frame
    P_breit=np.copy(P)    
    q_breit=np.copy(q)    
    ph_breit=np.copy(ph)    
    lini_breit=np.copy(lini)    
    lfin_breit=np.copy(lfin)    
    S_breit=np.copy(S)    

    # make the rotation 
    direction=np.array([0,0,-1])
    u,theta=self.get_rotation_params(direction,q[1:])

    P_breit[1:]=self.rotate(u,theta,P_breit[1:])
    q_breit[1:]=self.rotate(u,theta,q_breit[1:])
    ph_breit[1:]=self.rotate(u,theta,ph_breit[1:])
    lini_breit[1:]=self.rotate(u,theta,lini_breit[1:])
    lfin_breit[1:]=self.rotate(u,theta,lfin_breit[1:])
    S_breit[1:]=self.rotate(u,theta,S_breit[1:])

    # make the boost
    Q2=-self.dot4(q,q)
    B=1/Q2**0.5*np.array([[-q_breit[3],q_breit[0]],[q_breit[0],-q_breit[3]]])
    
    P_breit=self.boost(B,P_breit)
    q_breit=self.boost(B,q_breit)
    ph_breit=self.boost(B,ph_breit)
    lini_breit=self.boost(B,lini_breit)
    lfin_breit=self.boost(B,lfin_breit)
    S_breit=self.boost(B,S_breit)

    #print self.dot4(P,P)
    #print self.dot4(P_breit,P_breit)
    #print self.dot4(q,q)
    #print self.dot4(q_breit,q_breit)
    #print q_breit

    x=Q2/self.dot4(P,q)
    y=self.dot4(P,q)/self.dot4(P,lini)
    z=self.dot4(P,ph)/self.dot4(P,q)

    # compute phi_h, phi_S
    lini_cross_lfin=np.cross(lini_breit[1:],lfin_breit[1:])
    lini_cross_lfin/=np.linalg.norm(lini_cross_lfin)
    ph_cross_q = np.cross(ph_breit[1:],q_breit[1:]) 
    ph_cross_q/=np.linalg.norm(ph_cross_q)
    phi_h=np.pi-np.arccos(np.dot(lini_cross_lfin,ph_cross_q))
    phi_S=np.pi/2-np.arccos(np.dot(lini_cross_lfin,ph_cross_q))

    # compute phT
    phT=np.linalg.norm(ph_breit[1:3])

    return x,y,z,Q2,phi_h,phi_S,phT,lini,lfin,P,ph

  def _gen_event(self):

    E=self.conf['Ebeam']
    M=self.conf['aux'].M
    Mh=self.conf['aux'].Mpi
    S=self.conf['S']

    lini=np.array([E,0,0,E])
    P=np.array([M,0,0,0])

    # step 1
  
    x=np.random.uniform(1/(2*M*E),1)
    Q2=np.random.uniform(1,2*M*x*E)

    Efin=E-Q2/(2*M*x)
    cos_theta=1-Q2/(2*E*Efin)
    phi=np.random.uniform(0,2*np.pi)

    sin_theta=np.sqrt(1-cos_theta**2)
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)

    lfin=np.zeros(4)
    lfin[0]=Efin
    lfin[1]=Efin*sin_theta*cos_phi
    lfin[2]=Efin*sin_theta*sin_phi
    lfin[3]=Efin*cos_theta

    q=lini-lfin

    # step 2
    z=np.random.uniform(Mh/q[0],1)
    Eh=z*q[0]
    ph_mom3=np.sqrt(Eh**2-Mh**2)

    # step 3
    ph_perp=np.random.uniform(0,ph_mom3)
    sign=np.random.choice([-1,1])
    phi=np.random.uniform(0,2*np.pi)

    ph_z=np.sqrt(ph_mom3**2-ph_perp**2)*sign

    ph=np.zeros(4)
    ph[0]=Eh
    ph[1]=ph_perp*np.cos(phi)
    ph[2]=ph_perp*np.sin(phi)
    ph[3]=ph_z 

    # step 4

    # make a copy of the 4 vectors in the lab frame
    P_breit=np.copy(P)    
    q_breit=np.copy(q)    
    ph_breit=np.copy(ph)    
    lini_breit=np.copy(lini)    
    lfin_breit=np.copy(lfin)    
    S_breit=np.copy(S)    

    # make the rotation 
    direction=np.array([0,0,-1])
    u,theta=self.get_rotation_params(direction,q[1:])

    P_breit[1:]=self.rotate(u,theta,P_breit[1:])
    q_breit[1:]=self.rotate(u,theta,q_breit[1:])
    ph_breit[1:]=self.rotate(u,theta,ph_breit[1:])
    lini_breit[1:]=self.rotate(u,theta,lini_breit[1:])
    lfin_breit[1:]=self.rotate(u,theta,lfin_breit[1:])
    S_breit[1:]=self.rotate(u,theta,S_breit[1:])

    # make the boost
    Q2=-self.dot4(q,q)
    B=1/Q2**0.5*np.array([[-q_breit[3],q_breit[0]],[q_breit[0],-q_breit[3]]])
    
    P_breit=self.boost(B,P_breit)
    q_breit=self.boost(B,q_breit)
    ph_breit=self.boost(B,ph_breit)
    lini_breit=self.boost(B,lini_breit)
    lfin_breit=self.boost(B,lfin_breit)
    S_breit=self.boost(B,S_breit)

    #print self.dot4(P,P)
    #print self.dot4(P_breit,P_breit)
    #print self.dot4(q,q)
    #print self.dot4(q_breit,q_breit)
    #print q_breit

    y=self.dot4(P,q)/self.dot4(P,lini)

    # compute phi_h, phi_S
    lini_cross_lfin=np.cross(lini_breit[1:],lfin_breit[1:])
    lini_cross_lfin/=np.linalg.norm(lini_cross_lfin)
    ph_cross_q = np.cross(ph_breit[1:],q_breit[1:]) 
    ph_cross_q/=np.linalg.norm(ph_cross_q)
    phi_h=np.pi-np.arccos(np.dot(lini_cross_lfin,ph_cross_q))
    phi_S=np.pi/2-np.arccos(np.dot(lini_cross_lfin,ph_cross_q))

    # compute phT
    phT=np.linalg.norm(ph_breit[1:3])

    # compute spin projections
    gamma=2*M*x/np.sqrt(Q2)
    Sperp=np.linalg.norm(S_breit[1:3])
    Spar=self.dot4(S_breit,q_breit)/self.dot4(P_breit,q_breit)*M/np.sqrt(1+gamma**2) 

    return x,y,z,Q2,phi_h,phi_S,phT,Sperp,Spar,lini,lfin,P,ph

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
    self.sidis =obslib.sidis.stfuncs.STFUNCS(self.conf)

  def test(self):
    data={}
    data['x']=[]
    data['y']=[]
    data['z']=[]
    data['Q2']=[]
    data['phi_h']=[]
    data['phi_S']=[]
    data['phT']=[]
    for i in range(1000):
      try:
        x,y,z,Q2,phi_h,phi_S,phT,Sperp,Spar,lini,lfin,P,ph = self._gen_event()
      except:
        continue
      #if x>1: continue 
      #if Q2>1: continue

      data['x'].append(x)
      data['Q2'].append(Q2)
      data['z'].append(z)
      data['phi_h'].append(phi_h)
      data['phi_S'].append(phi_S)
      data['phT'].append(phT)

    nrows,ncols=2,3
    cnt=0
    for k in ['x','Q2','z','phi_h','phi_S','phT']:
      cnt+=1
      ax=py.subplot(nrows,ncols,cnt)
      ax.hist(data[k],label=k)
      ax.legend()
    py.tight_layout()
    py.savefig('plot.pdf')

  def test2(self):

    for i in range(100):
      try:
        x,y,z,Q2,phi_h,phi_S,pT,Sperp,Spar,lini,lfin,P,ph = self._gen_event()
      except:
        continue

      F=self.sidis.get_FX(1,x,z,Q2,pT,'p','pi+')
      print x,y,z,Q2,phi_h,phi_S,pT,F
      

if __name__=='__main__':

  conf=load_config('input.py')
  conf['aux']=AUX()
  mceg=MCEG(conf)
  mceg.test2()






