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
conf['params']['collins']['widths0 k+ fav']     = {'value':<<    1.22423257190011208762e-01>>,'fixed':False,'min':1e-5,'max':1.34062655687440246410e-01}
conf['params']['collins']['widths0 k+ unfav']   = {'value':<<    1.67747867678876172448e-01>>,'fixed':False,'min':1e-5,'max':1.87915286213150012351e-01}

conf['params']['collins']['k+ u N 1']  = {'value':<<   -1.14905529351804758242e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ u a 1']  = {'value':<<    6.10439434138660974583e-02>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ u b 1']  = {'value':<<    1.22506161060726537215e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ u c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ u N 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u a 2']  = {'value':<<    1.21696249480095164408e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ u b 2']  = {'value':<<    6.68147670605282328893e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ u c 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u d 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ d N 1']  = {'value':<<   -1.12264949972402972023e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ d a 1']  = {'value':<<    8.73481410387574985776e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ d b 1']  = {'value':<<    2.90513038346563323699e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ d c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ sb N 1']  = {'value':<<    1.31174999492275456969e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ sb a 1']  = {'value':<<   -7.81316449149517477935e-01>> ,'fixed':False,'min':-3,'max':5}
conf['params']['collins']['k+ sb b 1']  = {'value':<<    4.68573122948860998349e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ sb c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['k+ sb N 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb a 2']  = {'value':<<    1.21696249480095164408e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ sb b 2']  = {'value':<<    6.68147670605282328893e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ sb c 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb d 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    5.12667335827526118863e-02>>,'fixed':False,'min':1e-5,'max':1.15151579728561548333e-01}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    6.93975226626413616016e-02>>,'fixed':False,'min':1e-5,'max':1.36784756168045196212e-01}

conf['params']['collins']['pi+ u N 1']  = {'value':<<    6.73788167770143497926e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ u a 1']  = {'value':<<    1.83010052764936759218e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b 1']  = {'value':<<    4.98801808074242281066e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 1']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N 2']  = {'value':<<    3.94885950211991354486e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ u a 2']  = {'value':<<    1.22674156881876461611e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b 2']  = {'value':<<    1.87892936264560406201e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ d N 1']  = {'value':<<   -7.35181769717152683308e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ d a 1']  = {'value':<<   -2.75326692751743884457e+00>> ,'fixed':False,'min':-3,'max':5}
conf['params']['collins']['pi+ d b 1']  = {'value':<<    1.59217227866623955990e+00>> ,'fixed':False,'min':1e-5,'max':10}
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

conf['datasets']['sia']['xlsx'][2000]='../database/sia/expdata/2000.xlsx' # babar | k,k | AUL-0     | 16      | z1,z2  |    
conf['datasets']['sia']['xlsx'][2002]='../database/sia/expdata/2002.xlsx' # babar | k,k | AUC-0     | 16      | z1,z2  |    
conf['datasets']['sia']['xlsx'][2004]='../database/sia/expdata/2004.xlsx' # babar | k,pi | AUL-0     | 16      | z1,z2  |
conf['datasets']['sia']['xlsx'][2005]='../database/sia/expdata/2005.xlsx' # babar | k,pi | AUC-0     | 16      | z1,z2  |
conf['datasets']['sia']['xlsx'][2008]='../database/sia/expdata/2008.xlsx' # babar | pi,pi | AUL-0     | 16      | z1,z2  |
conf['datasets']['sia']['xlsx'][2009]='../database/sia/expdata/2009.xlsx' # babar | pi,pi | AUC-0     | 16      | z1,z2  |
conf['datasets']['sia']['xlsx'][1000]='../database/sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='../database/sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='../database/sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='../database/sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='../database/sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='../database/sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |

for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 


