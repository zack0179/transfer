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
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15151579728561548333e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36784756168045196212e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.34062655687440246410e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.87915286213150012351e-01>>,'fixed':True,'min':0,'max':1} 

conf['params']['collins']={}
conf['params']['collins']['widths0 k+ fav']     = {'value':<<    7.40824956410565064330e-03>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 k+ unfav']   = {'value':<<    5.18174564231686611560e-03>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['collins']['k+ u N 1']  = {'value':<<    1.05308965881160077060e+01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ u a 1']  = {'value':<<    2.75791171110632493679e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ u b 1']  = {'value':<<    5.28397623443379149677e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ u c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ d N 1']  = {'value':<<    2.25691387358529144125e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ d a 1']  = {'value':<<   -1.84124803090292665786e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ d b 1']  = {'value':<<    2.89617796112264169750e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ d c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

#conf['params']['collins']['k+ u N 2']  = {'value':<<    2.11150078306284516572e+00>> ,'fixed':False,'min':-10,'max':10}
#conf['params']['collins']['k+ u a 2']  = {'value':<<    2.71508421683099232524e+00>> ,'fixed':False,'min':-1,'max':5}
#conf['params']['collins']['k+ u b 2']  = {'value':<<    2.75387728005980081392e+00>> ,'fixed':False,'min':1e-5,'max':10}
#conf['params']['collins']['k+ u c 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
#conf['params']['collins']['k+ u d 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ sb N 1']  = {'value':<<   -1.22702012387014183781e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ sb a 1']  = {'value':<<   -3.74873700401006870742e-01>> ,'fixed':False,'min':-3,'max':5}
conf['params']['collins']['k+ sb b 1']  = {'value':<<    9.42469260617111448397e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ sb c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}


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

conf['datasets']['sia']['xlsx'][2000]='../database/sia/expdata/2000.xlsx' # babar | k,k | AUL-0     | 16      | z1,z2  |    
conf['datasets']['sia']['xlsx'][2002]='../database/sia/expdata/2002.xlsx' # babar | k,k | AUC-0     | 16      | z1,z2  |    

for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 


