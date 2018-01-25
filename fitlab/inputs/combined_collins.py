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
conf['params']={}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15920500644793311729e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.39782079427820671302e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':1}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    7.72910652513744272918e-02>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    1.14315393134556870791e+01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    4.30496632152482100464e-02>> ,'fixed':False,'min':0,'max':1000}
conf['params']['collins']['pi+ u a']  = {'value':<<   -2.91203792158932550649e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    3.58763164329581385470e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -2.07036285221656093750e+14>> ,'fixed':False,'min':-1000,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<    1.35311766916463120936e+01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    4.12467335487279669337e+01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['widths0 k+ fav']     = {'value':<<    1.79134333518971178290e-01>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['collins']['widths0 k+ unfav']   = {'value':<<    2.51796371609382285683e-01>>,'fixed':True,'min':1e-5,'max':2}
conf['params']['collins']['k+ u N']  = {'value':<<    4.94202530531348216414e-01>> ,'fixed':True,'min':-5,'max':20}
conf['params']['collins']['k+ u a']  = {'value':<<   -9.46328421494753158072e-02>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ u b']  = {'value':<<    1.00000000000000008180e-05>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ d N']  = {'value':<<   -4.57665726638101233448e-02>> ,'fixed':True,'min':-10,'max':20}
conf['params']['collins']['k+ d a']  = {'value':<<   -7.96368735991260123797e-01>> ,'fixed':True,'min':-1,'max':10}
conf['params']['collins']['k+ d b']  = {'value':<<    1.68910849832908738222e+00>> ,'fixed':True,'min':1e-5,'max':20}
conf['params']['collins']['k+ sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-20,'max':20}
conf['params']['collins']['k+ sb a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ sb b']  = {'value':<<    1.00000000000000008180e-05>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']={}
conf['params']['transversity']['widths0 valence'] = {'value':<<    5.02343824054610976759e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['widths0 sea']     = {'value':<<    4.84126169244575077499e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['u N']             = {'value':<<    2.98369646289212875345e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a']             = {'value':<<    4.52997228155483211420e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b']             = {'value':<<    2.99190645442837288570e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N']             = {'value':<<   -5.94859239972188547085e+00>> ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a']             = {'value':<<    3.26452082501464901920e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b']             = {'value':<<    2.15721426584817965733e+00>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s a']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s b']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['transversity']['u c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['u d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['pretzelosity']={}
conf['params']['pretzelosity']['widths0 valence'] = {'value':<<   -1.18255846193868527751e-05>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['pretzelosity']['widths0 sea']     = {'value':<<    1.26199935641373106598e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['pretzelosity']['u N']  = {'value':<<   -1.34432687108274984134e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['pretzelosity']['u a']  = {'value':<<    1.94260732695551796567e+00>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['pretzelosity']['u b']  = {'value':<<    7.33297678746845082998e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['pretzelosity']['d N']  = {'value':<<   -6.58908115208943545582e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['pretzelosity']['d a']  = {'value':<<    1.53391679201503139396e+00>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['pretzelosity']['d b']  = {'value':<<    8.77415980550143004280e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['pretzelosity']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s a']  = {'value':<<    5.53070929403782773903e-01>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['s b']  = {'value':<<    2.39050712257790154425e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['ub N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['ub a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['ub b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['db N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['db a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['db b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['sb a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['sb b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

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

for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 


# SIDIS
conf['datasets']['sidis']={}
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['filters']={}

# Collins Asy
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[4001,4000,4002,4004,4003,4005,3027,3025,3010,3012,3005,3013,3026,3000,3003,3016,3004,3018]
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"
conf["datasets"]["sidis"]["xlsx"][4001]="../database/sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+   pT
conf["datasets"]["sidis"]["xlsx"][4000]="../database/sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+    x
conf["datasets"]["sidis"]["xlsx"][4002]="../database/sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+    z
conf["datasets"]["sidis"]["xlsx"][4004]="../database/sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="../database/sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="../database/sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
conf["datasets"]["sidis"]["xlsx"][3027]="../database/sidis/expdata/3027.xlsx"  #  compass    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3025]="../database/sidis/expdata/3025.xlsx"  #  compass    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3010]="../database/sidis/expdata/3010.xlsx"  #  compass    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3012]="../database/sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="../database/sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="../database/sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3026]="../database/sidis/expdata/3026.xlsx"  #   HERMES    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="../database/sidis/expdata/3000.xlsx"  #   HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="../database/sidis/expdata/3003.xlsx"  #   HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="../database/sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="../database/sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="../database/sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z

# Pretzelosity

conf['datasets']['sidis']['filters'][1]={}
conf['datasets']['sidis']['filters'][1]['idx']=[8000, 8001]
conf['datasets']['sidis']['filters'][1]['filter']='z > 0.2 and x > 0.15 and x < 0.36 and y > 0.2 and y < 0.85 and Q2 > 1.30'
conf['datasets']['sidis']['filters'][2]={}
conf['datasets']['sidis']['filters'][2]['idx']=[8002, 8003, 8004, 8005, 8006, 8007]
conf['datasets']['sidis']['filters'][2]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.00'

conf['datasets']['sidis']['xlsx'][8000]='../database/sidis/expdata/8000.xlsx' # | neutron | pi- | A_pretzelosity | jlab
conf['datasets']['sidis']['xlsx'][8001]='../database/sidis/expdata/8001.xlsx' # | neutron | pi+ | A_pretzelosity | jlab
conf['datasets']['sidis']['xlsx'][8002]='../database/sidis/expdata/8002.xlsx' # | proton | pi- | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8003]='../database/sidis/expdata/8003.xlsx' # | proton | pi- | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8004]='../database/sidis/expdata/8004.xlsx' # | proton | pi- | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8005]='../database/sidis/expdata/8005.xlsx' # | proton | pi+ | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8006]='../database/sidis/expdata/8006.xlsx' # | proton | pi+ | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8007]='../database/sidis/expdata/8007.xlsx' # | proton | pi+ | A_pretzelosity | hermes

# add normalization pars
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 









