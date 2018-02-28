#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
AN_theory.py - program to calculate A_N in pp -> hX
"""

import sys,os
import numpy as np
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

class ANTHEORY: #This only includes the fragmentation term (see 1701.09170)
    
    def __init__(self):
        self.aux=conf['aux']  
        
        self.Mh={}
        self.Mh['pi+']=self.aux.Mpi
        self.Mh['pi-']=self.aux.Mpi
        self.Mh['k+']=self.aux.Mk
        self.Mh['k-']=self.aux.Mk
        
        self.D={}
        self.D[1] ={'k1':'pdf','k2':'ff'}
        self.D[2] ={'k1':'transversity','k2':'collins'}
    
    def get_pdf(flav,x,Q2): #Collinear unpolarized PDF
        return x*(1.-x) #We will modify this output later
    
    def get_ff(flav,z,Q2): #Collinear unpolarized FF
        return z*(1.-z) #We will modify this output later
    
    def get_trans(flav,x,Q2): #Collinear transversity
        return x*(1.-x) #We will modify this output later
    
    def get_collins(flav,z,Q2): #First moment of Collins
        return z*(1.-z) #We will modify this output later
    
    def get_Dcollins(flav,z,Q2): #Derivative of first moment of Collins
        return z*(1.-z) #We will modify this output later
    
    def get_dsigST(self,i,x,z,xF,pT,rs,k1,k2,target,hadron): #Numerator of the asymmetry, Eq. (24) of 1701.09170
        
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
        
        #Lower limits of the z and x integrations
        zmin = np.sqrt(xF2+xT2)
        xmin = -uu / (z*ss+tt)
        
        oz = 1./z
        ozz = 1./z**2.
        
        xp = -x*tt/(z*x*ss+uu)

        ox  = 1./x
        oxp = 1./xp
        
        #Mandelstam variables at the parton level
        s = x  * xp * ss
        t = x  * tt * oz
        u = xp * uu * oz   
        
        #Convenient combinations of the partonic Mandelstam variables
        M = {'s2':s*s}
        
        print(M[s2])
        
      
    
