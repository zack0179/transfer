#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys,os
import numpy as np
import pandas as pd
import math
from tools.tools import load_config
from external.CJLIB.CJ import CJ
from external.LSSLIB.LSS import LSS
from external.DSSLIB.DSS import DSS
from qcdlib.tmdlib import PDF,PPDF,FF
from qcdlib.tmdlib import TRANSVERSITY
from qcdlib.tmdlib import COLLINS
from qcdlib.aux import AUX
from tools.config import conf
from scipy.integrate import quad,dblquad,fixed_quad

class ANTHEORY: 
    """
    AN_theory.py - program to calculate A_N in pp -> hX
    This only includes the fragmentation term (see 1701.09170)
    """
    def  __init__(self):
        #self.aux=conf['aux']  
        
        self.Mh={}
        self.Mh['pi+']=0.13957018 #self.aux.Mpi
        self.Mh['pi-']=0.13957018 #self.aux.Mpi
        self.Mh['pi0']=0.1349766 #self.aux.Mpi
        self.Mh['k+']=0.13957018 #self.aux.Mk
        self.Mh['k-']=0.13957018 #self.aux.Mk
        
        self.flavor = ['u','d','s','ub','db','sb','g']
        self.target = ['p']
        self.hadron = ['pi+','pi-','pi0']

        #Common color factors and fractions
        self.c = {'r3':1./3.,'r4':0.25,'r6':1./6.,'r8':0.125,'r9':1./9.,'r18':1./18.,'r24':1./24.,'r27':1./27.}

        self.m={}
        self.Hupol={}
        self.f={}
        self.ft={}
        self.d={}

        self.B1=np.zeros(7*7).reshape((7,7))
        self.B1[1:4,1:4]=np.ones(3*3).reshape((3,3))

    def get_f(self,x,Q2): #Collinear unpolarized PDF
        if (x,Q2) not in self.f:
          self.f[(x,Q2)]=x*(1.-x)*np.ones(7)
        return self.f[(x,Q2)]

    def get_ft(self,x,Q2): #Collinear unpolarized PDF
        if (x,Q2) not in self.ft:
          self.ft[(x,Q2)]=x*(1.-x)*np.ones(7)
        return self.ft[(x,Q2)]
    
    def get_d(self,z,Q2): #Collinear unpolarized FF
        if (z,Q2) not in self.d:
          self.d[(z,Q2)]=z*(1.-z)*np.ones(7)
        return self.d[(z,Q2)]
    
    def get_h1(self,flav,tar,x,Q2): #Collinear transversity
        return x*(1.-x) #We will modify this output later
    
    def get_H1p(self,flav,had,z,Q2): #(H_1^{\perp(1)}(z) - z*dH_1^{\perp(1)}(z)/dz)
        return z*(1.-z) #We will modify this output later
    
    def get_H(self,flav,had,z,Q2): #-2*z*H_1^{\perp(1)}(z)+\tilde{H}(z) 
        return z*(1.-z) #We will modify this output later

    def get_mandelstam(self,s,t,u):
        #Convenient combinations of the partonic Mandelstam variables
        self.m['s2']=s*s
        self.m['s3']=s**3.
        self.m['t2']=t*t
        self.m['t3']=t**3.
        self.m['u2']=u*u
        self.m['u3']=u**3.
        self.m['ostu']=1./(s*t*u)
        self.m['os']=1./s
        self.m['ot']=1./t
        self.m['ou']=1./u
        self.m['st']=s/t
        self.m['su']=s/u
        self.m['ts']=t/s
        self.m['tu']=t/u
        self.m['us']=u/s
        self.m['ut']=u/t
        self.m['st2']=s**2./t**2.
        self.m['su2']=s**2./u**2.
        self.m['ts2']=t**2./s**2.
        self.m['tu2']=t**2./u**2.
        self.m['us2']=u**2./s**2.
        self.m['ut2']=u**2./t**2.
        self.m['os2']=1./s**2.
        self.m['ot2']=1./t**2.
        self.m['ou2']=1./u**2.
        self.m['os3']=1./s**3.
        self.m['ot3']=1./t**3.
        self.m['ou3']=1./u**3.

    def get_Hupol(self):
        #Hard parts for the unpolarized cross section
        self.Hupol['av1']=4.*(self.m['st2']+self.m['ut2'])*self.c['r9']
        self.Hupol['av2']=4.*(self.m['su2']+self.m['tu2'])*self.c['r9']
        self.Hupol['av3']=-8.*self.m['st']*self.m['su']*self.c['r27']
        self.Hupol['av4']=4.*(self.m['ts2']+self.m['us2'])*self.c['r9']
        self.Hupol['av5']=4.*(self.m['st2']+self.m['ut2'])*self.c['r9']
        self.Hupol['av6']=-8.*self.m['ut']*self.m['us']*self.c['r27']
        self.Hupol['av7']=4.*(self.m['ts2']+self.m['us2'])*self.c['r9']
        self.Hupol['av8']=4.*(self.m['su2']+self.m['tu2'])*self.c['r9']
        self.Hupol['av9']=-8.*self.m['tu']*self.m['ts']*self.c['r27']
        self.Hupol['av10']=32.*self.c['r27']*(self.m['tu']+self.m['ut'])*(1. - 9.*self.m['ts']*self.m['us']*self.c['r4'] )
        self.Hupol['av11']=4.*self.c['r9']*(-self.m['su']-self.m['us'])* (1. - 9.*self.m['st']*self.m['ut']*self.c['r4'] )
        self.Hupol['av12']=4.*self.c['r9']*(-self.m['st']-self.m['ts'])*(1. - 9.*self.m['su']*self.m['tu']*self.c['r4'] )
        self.Hupol['av13']=(self.m['tu']+self.m['ut'])*self.c['r6'] - 3.*(self.m['ts2']+self.m['us2'])*self.c['r8']
        self.Hupol['av14']=4.5*(3. - self.m['ts']*self.m['us'] - self.m['st']*self.m['ut'] - self.m['su']*self.m['tu'] )

    #@profile    
    def get_dsig(self,x,z,xF,pT,rs,tar,had): #Calculation of the unpolarized cross section
        
        if pT < 1.: 
            Q = pT
        else: 
            Q = 1.
        
        Q2 = Q*Q
        
        xT  = 2.*pT/rs
        xT2 = xT*xT
        xF2 = xF*xF
        
        #Mandelstam variables at the hadron level
        ss = rs*rs
        tt = -0.5 * ss * ( np.sqrt(xF2+xT2) - xF )
        uu = -0.5 * ss * ( np.sqrt(xF2+xT2) + xF )
        
        oz = 1./z
        ozz = 1./z**2.
        
        xp = -x*tt/(z*x*ss+uu)

        ox  = 1./x
        oxp = 1./xp
        
        #Mandelstam variables at the parton level
        s = x  * xp * ss
        t = x  * tt * oz
        u = xp * uu * oz  
        
        #Prefactor
        denfac = 1. / ( ( z*z*x*ss + uu*z ) * x * xp )
        
        self.get_mandelstam(s,t,u)
        self.get_Hupol()
        
        #Create dictionaries of the nonperturbative functions
        f1x = {}
        f1xp = {}
        D1z = {}
        
        #for flav in self.flavor:
        #    f1x[(flav,tar)] = self.get_pdf(flav,tar,x,Q2)
        #    f1xp[(flav,tar)] = self.get_pdf(flav,tar,xp,Q2)
        #    D1z[(flav,had)] = self.get_ff(flav,had,z,Q2)


        f=self.get_f(x,Q2)
        ft=self.get_ft(x,Q2)
        d=self.get_d(x,Q2)

        upol = 0
        upol+=np.einsum('i,j,i,ij',f,ft,d,self.B1)*self.Hupol['av1']

        return upol
            
        upol = 0
            
        upol+=   ( f1x[('u',tar)]*D1z[('u',had)] + f1x[('d',tar)]*D1z[('d',had)] + f1x[('s',tar)]*D1z[('s',had)] ) \
              * ( f1xp[('u',tar)] + f1xp[('d',tar)] + f1xp[('s',tar)] ) \
              * Hupol['av1'] \
              + ( f1x[('u',tar)] + f1x[('d',tar)] + f1x[('s',tar)] ) \
              * ( f1xp[('u',tar)]*D1z[('u',had)] + f1xp[('d',tar)]*D1z[('d',had)] + f1xp[('s',tar)]*D1z[('s',had)] ) \
              * Hupol['av2'] \
              + ( f1x[('u',tar)]*f1xp[('u',tar)]*D1z[('u',had)] + f1x[('d',tar)]*f1xp[('d',tar)]*D1z[('d',had)] + f1x[('s',tar)]*f1xp[('s',tar)]*D1z[('s',had)] ) \
              * Hupol['av3']
        
        upol+=   ( f1x[('ub',tar)]*D1z[('ub',had)] + f1x[('db',tar)]*D1z[('db',had)] + f1x[('sb',tar)]*D1z[('sb',had)] ) \
              * ( f1xp[('ub',tar)] + f1xp[('db',tar)] + f1xp[('sb',tar)] ) \
              * Hupol['av1'] \
              + ( f1x[('ub',tar)] + f1x[('db',tar)] + f1x[('sb',tar)] ) \
              * ( f1xp[('ub',tar)]*D1z[('ub',had)] + f1xp[('db',tar)]*D1z[('db',had)] + f1xp[('sb',tar)]*D1z[('sb',had)] ) \
              * Hupol['av2'] \
              + ( f1x[('ub',tar)]*f1xp[('ub',tar)]*D1z[('ub',had)] + f1x[('db',tar)]*f1xp[('db',tar)]*D1z[('db',had)] + f1x[('sb',tar)]*f1xp[('sb',tar)]*D1z[('sb',had)] ) \
              * Hupol['av3']

        upol+=   ( f1x[('u',tar)]*D1z[('u',had)] + f1x[('d',tar)]*D1z[('d',had)] + f1x[('s',tar)]*D1z[('s',had)] ) \
              * ( f1xp[('ub',tar)] + f1xp[('db',tar)] + f1xp[('sb',tar)] ) \
              * Hupol['av5'] \
              + ( f1x[('u',tar)]*f1xp[('ub',tar)] + f1x[('d',tar)]*f1xp[('db',tar)] + f1x[('s',tar)]*f1xp[('sb',tar)] ) \
              * ( D1z[('u',had)] + D1z[('d',had)] + D1z[('s',had)] ) \
              * Hupol['av4'] \
              + ( f1x[('u',tar)]*f1xp[('ub',tar)]*D1z[('u',had)] + f1x[('d',tar)]*f1xp[('db',tar)]*D1z[('d',had)] + f1x[('s',tar)]*f1xp[('sb',tar)]*D1z[('s',had)] ) \
              * Hupol['av6']
        
        upol+=   ( f1x[('ub',tar)]*D1z[('ub',had)] + f1x[('db',tar)]*D1z[('db',had)] + f1x[('sb',tar)]*D1z[('sb',had)] ) \
              * ( f1xp[('u',tar)] + f1xp[('d',tar)] + f1xp[('s',tar)] ) \
              * Hupol['av5'] \
              + ( f1x[('ub',tar)]*f1xp[('u',tar)] + f1x[('db',tar)]*f1xp[('d',tar)] + f1x[('sb',tar)]*f1xp[('s',tar)] ) \
              * ( D1z[('ub',had)] + D1z[('db',had)] + D1z[('sb',had)] ) \
              * Hupol['av4'] \
              + ( f1x[('ub',tar)]*f1xp[('u',tar)]*D1z[('ub',had)] + f1x[('db',tar)]*f1xp[('d',tar)]*D1z[('db',had)] + f1x[('sb',tar)]*f1xp[('s',tar)]*D1z[('sb',had)] ) \
              * Hupol['av6']
      
        upol+=   ( f1x[('u',tar)] + f1x[('d',tar)] + f1x[('s',tar)] ) \
              * ( f1xp[('ub',tar)]*D1z[('ub',had)] + f1xp[('db',tar)]*D1z[('db',had)] + f1xp[('sb',tar)]*D1z[('sb',had)] ) \
              * Hupol['av8'] \
              + ( f1x[('u',tar)]*f1xp[('ub',tar)] + f1x[('d',tar)]*f1xp[('db',tar)] + f1x[('s',tar)]*f1xp[('sb',tar)] ) \
              * ( D1z[('ub',had)] + D1z[('db',had)] + D1z[('sb',had)] ) \
              * Hupol['av7'] \
              + (f1x[('u',tar)]*f1xp[('ub',tar)]*D1z[('ub',had)]+f1x[('d',tar)]*f1xp[('db',tar)]*D1z[('db',had)]+f1x[('s',tar)]*f1xp[('sb',tar)]*D1z[('sb',had)]) \
              * Hupol['av9']
          
        upol+=   ( f1x[('ub',tar)] + f1x[('db',tar)] + f1x[('sb',tar)] ) \
              * ( f1xp[('u',tar)]*D1z[('u',had)] + f1xp[('d',tar)]*D1z[('d',had)] + f1xp[('s',tar)]*D1z[('s',had)] ) \
              * Hupol['av8']\
              + ( f1x[('ub',tar)]*f1xp[('u',tar)] + f1x[('db',tar)]*f1xp[('d',tar)] + f1x[('sb',tar)]*f1xp[('s',tar)] ) * ( D1z[('u',had)] + D1z[('d',had)] + D1z[('s',had)] ) \
              * Hupol['av7']\
              + ( f1x[('ub',tar)]*f1xp[('u',tar)]*D1z[('u',had)] + f1x[('db',tar)]*f1xp[('d',tar)]*D1z[('d',had)] + f1x[('sb',tar)]*f1xp[('s',tar)]*D1z[('s',had)] ) \
              * Hupol['av9']
        
        upol+= ( f1x[('u',tar)]*f1xp[('ub',tar)] + f1x[('d',tar)]*f1xp[('db',tar)] + f1x[('s',tar)]*f1xp[('sb',tar)] ) * D1z[('g',had)] * Hupol['av10']
        
        upol+= ( f1x[('ub',tar)]*f1xp[('u',tar)] + f1x[('db',tar)]*f1xp[('d',tar)] + f1x[('sb',tar)]*f1xp[('s',tar)] ) * D1z[('g',had)] * Hupol['av10']
        
        upol+= ( f1x[('u',tar)]*D1z[('u',had)]  + f1x[('d',tar)]*D1z[('d',had)]  + f1x[('s',tar)]*D1z[('s',had)]  ) * f1xp[('g',tar)] * Hupol['av11']
        
        upol+= ( f1x[('ub',tar)]*D1z[('ub',had)] + f1x[('db',tar)]*D1z[('db',had)] + f1x[('sb',tar)]*D1z[('sb',had)] ) * f1xp[('g',tar)] * Hupol['av11']
        
        upol+= ( f1x[('u',tar)]  + f1x[('d',tar)]  + f1x[('s',tar)]  ) * f1xp[('g',tar)] * D1z[('g',had)] * Hupol['av12']
        
        upol+= ( f1x[('ub',tar)] + f1x[('db',tar)] + f1x[('sb',tar)] ) * f1xp[('g',tar)] * D1z[('g',had)] * Hupol['av12']
        
        upol+= f1x[('g',tar)] * f1xp[('g',tar)] * ( D1z[('u',had)] + D1z[('d',had)] + D1z[('s',had)] ) * Hupol['av13']
        
        upol+= f1x[('g',tar)] * f1xp[('g',tar)] * ( D1z[('ub',had)] + D1z[('db',had)] + D1z[('sb',had)] ) * Hupol['av13']
        
        upol+= f1x[('g',tar)] * f1xp[('g',tar)] * D1z[('g',had)] * Hupol['av14']
        
        upol+= f1x[('g',tar)] * ( f1xp[('u',tar)]*D1z[('u',had)] + f1xp[('d',tar)]*D1z[('d',had)] + f1xp[('s',tar)]*D1z[('s',had)]) * Hupol['av12']
        
        upol+= f1x[('g',tar)] * ( f1xp[('ub',tar)]*D1z[('ub',had)] + f1xp[('db',tar)]*D1z[('db',had)] + f1xp[('sb',tar)]*D1z[('sb',had)]) * Hupol['av12']
        
        upol+= f1x[('g',tar)] * ( f1xp[('u',tar)]  + f1xp[('d',tar)]  + f1xp[('s',tar)]  ) * D1z[('g',had)] * Hupol['av11']
        
        upol+= f1x[('g',tar)] * ( f1xp[('ub',tar)] + f1xp[('db',tar)] + f1xp[('sb',tar)] ) * D1z[('g',had)] * Hupol['av11']
        
        return denfac * upol 
        
        
    def get_dsigST(self,x,z,xF,pT,rs,tar,had): #Calculation of the fragmentation term in the transversely polarized cross section
        
        Mh = self.Mh[had]
        
        if pT < 1.: 
            Q = pT
        else: 
            Q = 1.
        
        Q2 = Q*Q
        
        xT  = 2.*pT/rs
        xT2 = xT*xT
        xF2 = xF*xF
        
        #Mandelstam variables at the hadron level
        ss = rs*rs
        tt = -0.5 * ss * ( np.sqrt(xF2+xT2) - xF )
        uu = -0.5 * ss * ( np.sqrt(xF2+xT2) + xF )
        
        oz = 1./z
        ozz = 1./z**2.
        
        xp = -x*tt/(z*x*ss+uu)

        ox  = 1./x
        oxp = 1./xp
        
        #Mandelstam variables at the parton level
        s = x  * xp * ss
        t = x  * tt * oz
        u = xp * uu * oz  
        
        #Prefactor
        numfac = oz * 1. / ( ( z*z*x*ss + uu*z ) * x * xp )
        
        #Common color factors and fractions
        c = {'r3':1./3.,'r4':0.25,'r6':1./6.,'r8':0.125,'r9':1./9.,'r18':1./18.,'r24':1./24.,'r27':1./27.}
        
        #Convenient combinations of the partonic Mandelstam variables
        m = {'s2':s*s,'s3':s**3.,'t2':t*t,'t3':t**3.,'u2':u*u,'u3':u**3.,
             'ostu':1./(s*t*u),'os':1./s,'ot':1./t,'ou':1./u,
             'st':s/t,'su':s/u,'ts':t/s,'tu':t/u,'us':u/s,'ut':u/t,
             'st2':s**2./t**2.,'su2':s**2./u**2.,'ts2':t**2./s**2.,
             'tu2':t**2./u**2.,'us2':u**2./s**2.,'ut2':u**2./t**2.,
             'os2':1./s**2.,'ot2':1./t**2.,'ou2':1./u**2.,
             'os3':1./s**3.,'ot3':1./t**3.,'ou3':1./u**3.}
        
        #Hard parts for the transversely polarized fragmentation term
        HTff = {'ff1a':-c['r9']*m['ot'] + c['r8']*s*(u-s)*m['ot3'] - m['st2']*m['ou'],
                'ff1b':c['r8']*s*(u-s)*m['ot3'] + 0.5*c['r9']*(s-u)*m['ot']*m['ou'] + 0.5*(s-u)*(m['t2']-2.*t*u-2.*m['u2'])*m['ot3']*m['ou'],
                'ff2a':c['r27']*s*(t-u)*m['ot2']*m['ou'] + c['r9']*s*(u-2.*t)*m['ot3'] + s*m['ot2'],
                'ff2b':c['r27']*0.5*s*(t-3.*u)*m['ot2']*m['ou'] - s*u*m['ot3'] + c['r9']*s*(2.*u-t)*m['ot3'] - c['r3']*0.5*m['s2']*m['ot2']*m['ou'],
                'ff3a':c['r27']*s*m['ot2'] + c['r9']*s*(t-s)*m['ot3'] - c['r3']*m['ot'],
                'ff3b':c['r27']*0.5*(3.*s-t)*m['ot2'] + m['s2']*m['ot3'] + c['r9']*s*(t-2.*s)*m['ot3'] + c['r3']*0.5*u*m['ot2'],
                'ff4a':c['r27']*s*m['ot']*m['ou'] - c['r3']*m['ot'],'ff4b':10.*c['r27']*0.5*(s-u)*m['ot']*m['ou'],
                'ff5a':c['r9']*s*(u-2.*t)*m['ot3'] + s*m['ot2'],'ff5b':c['r9']*s*(2.*u-t)*m['ot3'] - s*u*m['ot3'],
                'ff6a':c['r9']*s*(t-s)*m['ot3'],'ff6b':c['r9']*s*(t-2.*s)*m['ot3'] + m['s2']*m['ot3']}
                  
                  
        HTffb = {'ff7a':HTff['ff1a'],'ff7b':HTff['ff1b'],'ff8a':HTff['ff2a'],'ff8b':HTff['ff2b'],
                 'ff9a':HTff['ff3a'],'ff9b':HTff['ff3b'],'ff10a':HTff['ff4a'],'ff10b':HTff['ff4b'],
                 'ff11a':HTff['ff5a'],'ff11b':HTff['ff5b'],'ff12a':HTff['ff6a'],'ff12b':HTff['ff6b']}
        
        #Create dictionaries of the nonperturbative functions
        f1xp = {}
        h1x = {}
        H1pz = {}
        Hz = {}
        Hxxpz = {}
        
        for flav in self.flavor:
            f1xp[(flav,tar)] = self.get_pdf(flav,tar,xp,Q2)
            h1x[(flav,tar)] = self.get_h1(flav,tar,x,Q2)
            H1pz[(flav,had)] = self.get_H1p(flav,had,z,Q2) #Note again H1p(z) = (H_1^{\perp(1)}(z) - z*dH_1^{\perp(1)}(z)/dz)
            Hz[(flav,had)] = self.get_H(flav,had,z,Q2) #Note again H(z) = -2*z*H_1^{\perp(1)}(z)+\tilde{H}(z) 
            
        for i in range(1,7):
            for flav in ['u','d','s']:
                Hxxpz[(i,flav,had)] = H1pz[(flav,had)] * HTff['ff'+str(i)+'a'] + oz * Hz[(flav,had)] * HTff['ff'+str(i)+'b']
        
        for i in range(7,13):
            for flav in ['ub','db','sb']:
                Hxxpz[(i,flav,had)] = H1pz[(flav,had)] * HTffb['ff'+str(i)+'a'] + oz * Hz[(flav,had)] * HTffb['ff'+str(i)+'b']
        
        ffcs = {}
                
        ffcs[1] = f1xp[('g',tar)] * (h1x[('u',tar)]*Hxxpz[(1,'u',had)] + h1x[('d',tar)]*Hxxpz[(1,'d',had)] + h1x[('s',tar)]*Hxxpz[(1,'s',had)])

        ffcs[2] = (h1x[('u',tar)]*f1xp[('u',tar)]*Hxxpz[(2,'u',had)]) + (h1x[('d',tar)]*f1xp[('d',tar)]*Hxxpz[(2,'d',had)]) + (h1x[('s',tar)]*f1xp[('s',tar)]*Hxxpz[(2,'s',had)])

        ffcs[3] = (h1x[('u',tar)]*f1xp[('ub',tar)]*Hxxpz[(3,'u',had)]) + (h1x[('d',tar)]*f1xp[('db',tar)]*Hxxpz[(3,'d',had)]) + (h1x[('s',tar)]*f1xp[('sb',tar)]*Hxxpz[(3,'s',had)])

        ffcs[4] = (h1x[('ub',tar)]*f1xp[('u',tar)]*Hxxpz[(4,'u',had)]) + (h1x[('db',tar)]*f1xp[('d',tar)]*Hxxpz[(4,'d',had)]) + (h1x[('sb',tar)]*f1xp[('s',tar)]*Hxxpz[(4,'s',had)])

        ffcs[5] = f1xp[('u',tar)] * (h1x[('d',tar)]*Hxxpz[(5,'d',had)] + h1x[('s',tar)]*Hxxpz[(5,'s',had)]) + f1xp[('d',tar)] * (h1x[('u',tar)]*Hxxpz[(5,'u',had)] + h1x[('s',tar)]*Hxxpz[(5,'s',had)]) + f1xp[('s',tar)] * (h1x[('u',tar)] * Hxxpz[(5,'u',had)] + h1x[('d',tar)]*Hxxpz[(5,'d',had)])

        ffcs[6] = f1xp[('ub',tar)] * (h1x[('d',tar)]*Hxxpz[(6,'d',had)] + h1x[('s',tar)]*Hxxpz[(6,'s',had)]) + f1xp[('db',tar)] * (h1x[('u',tar)]*Hxxpz[(6,'u',had)] + h1x[('s',tar)]*Hxxpz[(6,'s',had)]) + f1xp[('sb',tar)] * (h1x[('u',tar)]*Hxxpz[(6,'u',had)] + h1x[('d',tar)]*Hxxpz[(6,'d',had)])

        ffcs[7] = f1xp[('g',tar)] * (h1x[('ub',tar)]*Hxxpz[(7,'ub',had)] + h1x[('db',tar)]*Hxxpz[(7,'db',had)] + h1x[('sb',tar)]*Hxxpz[(7,'sb',had)])

        ffcs[8] = (h1x[('ub',tar)]*f1xp[('ub',tar)]*Hxxpz[(8,'ub',had)]) + (h1x[('db',tar)]*f1xp[('db',tar)]*Hxxpz[(8,'db',had)]) + (h1x[('sb',tar)]*f1xp[('sb',tar)]*Hxxpz[(8,'sb',had)])

        ffcs[9] = (h1x[('ub',tar)]*f1xp[('u',tar)]*Hxxpz[(9,'ub',had)]) + (h1x[('db',tar)]*f1xp[('d',tar)]*Hxxpz[(9,'db',had)]) + (h1x[('sb',tar)]*f1xp[('s',tar)]*Hxxpz[(9,'sb',had)])

        ffcs[10] = (h1x[('u',tar)]*f1xp[('ub',tar)]*Hxxpz[(10,'ub',had)]) + (h1x[('d',tar)]*f1xp[('db',tar)]*Hxxpz[(10,'db',had)]) + (h1x[('s',tar)]*f1xp[('sb',tar)]*Hxxpz[(10,'sb',had)])

        ffcs[11] = f1xp[('ub',tar)] * (h1x[('db',tar)]*Hxxpz[(11,'db',had)] + h1x[('sb',tar)]*Hxxpz[(11,'sb',had)]) + f1xp[('db',tar)] * (h1x[('ub',tar)]*Hxxpz[(11,'ub',had)] + h1x[('sb',tar)]*Hxxpz[(11,'sb',had)]) + f1xp[('sb',tar)] * (h1x[('ub',tar)]*Hxxpz[(11,'ub',had)] + h1x[('db',tar)]*Hxxpz[(11,'db',had)])

        ffcs[12] = f1xp[('u',tar)] * (h1x[('db',tar)]*Hxxpz[(12,'db',had)] + h1x[('sb',tar)]*Hxxpz[(12,'sb',had)]) + f1xp[('d',tar)] * (h1x[('ub',tar)]*Hxxpz[(12,'ub',had)] + h1x[('sb',tar)]*Hxxpz[(12,'sb',had)]) + f1xp[('s',tar)] * (h1x[('ub',tar)]*Hxxpz[(12,'ub',had)] + h1x[('db',tar)]*Hxxpz[(12,'db',had)])
        

        ffcs = 2. * Mh * pT * numfac * np.sum(np.array([ffcs[i] for i in range(1,13)])) 
        
        return ffcs

    def get_sig(self,xF,pT,rs,tar,had,mode='gauss',nx=100,nz=100):
        if mode=='gauss':
            dsigdzdx = np.vectorize(lambda x,z: self.get_dsig(x,z,xF,pT,rs,tar,had))
            dsigdz   = np.vectorize(lambda z: fixed_quad(lambda x:dsigdzdx(x,z),xmin(z),1,n=nx)[0])
            sig      = fixed_quad(dsigdz,zmin,1,n=nz)[0]
        elif mode=='quad':
          sig = dblquad(lambda x,z: self.get_dsig(x,z,xF,pT,rs,tar,had),zmin,1.,xmin,lambda x: 1.)[0]
        return sig

    def get_sigST(self,xF,pT,rs,tar,had,mode='gauss',nx=100,nz=100):
        if mode=='gauss':
            dsigdzdx = np.vectorize(lambda x,z: self.get_dsigST(x,z,xF,pT,rs,tar,had))
            dsigdz   = np.vectorize(lambda z: fixed_quad(lambda x:dsigdzdx(x,z),xmin(z),1,n=nx)[0])
            sig      = fixed_quad(dsigdz,zmin,1,n=nz)[0]
        elif mode=='quad':
          sig = dblquad(lambda x,z: self.get_dsigST(x,z,xF,pT,rs,tar,had),zmin,1.,xmin,lambda x: 1.)[0]
        return sig


if __name__=='__main__':

  rs = 200.
  tar = 'p'
  had='pi-'
  pT=1.10
  xF=0.2375
  xT  = 2.*pT/rs
  xF2 = xF*xF
  xT2 = xT*xT
  
  #Mandelstam variables at the hadron level
  ss = rs*rs
  tt = -0.5 * ss * ( np.sqrt(xF2+xT2) - xF )
  uu = -0.5 * ss * ( np.sqrt(xF2+xT2) + xF )
  
  #Lower limits of the z and x integrations
  zmin = np.sqrt(xF2+xT2)
  xmin = lambda z: -uu/(z*ss+tt)

  anthy=ANTHEORY()

  def test():
    print anthy.get_sig(xF,pT,rs,tar,had,mode='gauss',nx=100,nz=100)

  from timeit import Timer
  t = Timer("test()", "from __main__ import test")
  print 't elapsed ',t.timeit(number=1) 




  #print anthy.get_dsig(xmin(zmin),zmin,xF,pT,rs,tar,had)
  #print anthy.get_dsigST(0.3,0.6,xF,pT,rs,tar,had)


  #Integration of the numerator from xmin to 1 and from zmin to 1 (the values for xmin and zmin are above)


  
  #Integration of the denominator from xmin to 1 and from zmin to 1 (the values for xmin and zmin are above)
  #den = dblquad(lambda x,z: ANTHEORY().get_dsig(x,z,xF,pT,rs,tar,had),zmin,1.,xmin,lambda x: 1.)
  
  #AN = num[0]/den[0]
  #print(AN)
      
    
