conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-10
conf['num points'] = 30 #self.npar*3
conf['burn size']  = 10
conf['sample size']= 10000


############################################################################
# resouce allocation

conf['ncpus']=1

############################################################################
# maxlike setup

conf['screen mode']='plain'
#conf['screen mode']='curses'

############################################################################
# mcsetup

conf['method']='kde'
conf['itmax']=None
conf['tol']=1e-6
conf['kde bw']=None
conf['num points factor']=10

############################################################################
# paths to external

conf['path2CJ'] ='../external/CJLIB'
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# params

conf['shape'] = 1

conf['params']={}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15920500644793311729e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.39782079427820671302e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':1}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    2.15700971883240444349e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    7.11533776040739057711e-02>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['collins']['pi+ u N 1']  = {'value':<<    6.09357995206367530211e-03>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ u a 1']  = {'value':<<   -4.03320731623216044426e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b 1']  = {'value':<<   -1.43508775990798920219e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N 2']  = {'value':<<   -5.61391239456793414320e+02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ u a 2']  = {'value':<<    3.12057960499049968917e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b 2']  = {'value':<<    8.17410784870165230132e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ d N 1']  = {'value':<<   -1.46716426270008515331e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ d a 1']  = {'value':<<   -7.09202263727072956812e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b 1']  = {'value':<<    2.71620521770619260948e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}


############################################################################
# set data sets

conf['datasets']={}

# SIA

conf['datasets']['sia']={}


conf['datasets']['sia']['norm']={}

conf['datasets']['sia']['filters']=[]
#conf['datasets']['sia']['filters'].append("z<0.6") 
#conf['datasets']['sia']['filters'].append("Q2>1.69") 
#conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.9") 


conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='../database/sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |    
conf['datasets']['sia']['xlsx'][1001]='../database/sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |    
conf['datasets']['sia']['xlsx'][1002]='../database/sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |    
conf['datasets']['sia']['xlsx'][1003]='../database/sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |    
conf['datasets']['sia']['xlsx'][1004]='../database/sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |    
conf['datasets']['sia']['xlsx'][1005]='../database/sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |   
conf['datasets']['sia']['xlsx'][3000]='../database/sia/expdata/3000.xlsx' # bes3  | pi,pi | AUL-0     | 6      | z1,z2      |    
conf['datasets']['sia']['xlsx'][3001]='../database/sia/expdata/3001.xlsx' # bes3  | pi,pi | AUC-0     | 6      | z1,z2      |    
conf['datasets']['sia']['xlsx'][3002]='../database/sia/expdata/3002.xlsx' # bes3  | pi,pi | AUL-0     | 6      | z1,z2,pt   |    
conf['datasets']['sia']['xlsx'][3003]='../database/sia/expdata/3003.xlsx' # bes3  | pi,pi | AUC-0     | 6      | z1,z2,pt   |    


for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 


