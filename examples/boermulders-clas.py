############################################################################
conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-10
conf['num points'] = 30 #self.npar*3
conf['burn size']  = 10
conf['sample size']= 10000

############################################################################
# path to output
conf['output dir']='runs/boermulders'

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
############################################################################
# params

conf['params']={}


# these are included when using the observable AUUcos for it has two terms 
# the second of which depends on f1 * D1
#conf['params']['pdf']={}
#conf['params']['pdf']['widths0 valence']  = {'value':5.90288671102841333571e-01,'fixed':True,'min':1e-5,'max':1}
#conf['params']['pdf']['widths0 sea']      = {'value':6.27510853614136498990e-01,'fixed':True,'min':1e-5,'max':1}

#conf['params']['ff']={}
#conf['params']['ff']['widths0 pi+ fav']   = {'value':1.15151579728561548333e-01,'fixed':True,'min':0,'max':1}
#conf['params']['ff']['widths0 pi+ unfav'] = {'value':1.36784756168045196212e-01,'fixed':True,'min':0,'max':1}
#conf['params']['ff']['widths0 k+ fav']    = {'value':1.34062655687440246410e-01,'fixed':True,'min':0,'max':1}
#conf['params']['ff']['widths0 k+ unfav'] = {'value':1.85494582991636902669e-01,'fixed':True,'min':1e-5,'max':1}

conf['params']['boermulders']={}
conf['params']['boermulders']['widths0 valence'] = {'value':2.99994257869736280497e-01,'fixed':False,'min':1e-5,'max':1}
conf['params']['boermulders']['widths0 sea']     = {'value':2.32794366294785171068e-01,'fixed':False,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u N']  = {'value':5.42650693708019993267e+00,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['u a']  = {'value':1.61391852452949091656e+00,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['u b']  = {'value':1.13975971617359173038e+00,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['d N']  = {'value':7.33483204762133667032e+00,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['d a']  = {'value':1.96985180239880541819e-01,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['d b']  = {'value':1.00000000000000008180e-01,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['s N']  = {'value':1.00000000000000000000e+00,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['s a']  = {'value':1.00000000000000008180e+00,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['s b']  = {'value':1.00000000000000008180e+00,'fixed':False,'min':1e-5,'max':10}


#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u c']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['u d']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d c']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d d']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s c']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s d']  = {'value':0.00000000000000000000e+00,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':0.07502,'fixed':False,'min':0.05,'max':0.5}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':0.07649,'fixed':False,'min':1e-5,'max':0.5}
conf['params']['collins']['pi+ u N 1']  = {'value': 1.01381,'fixed':False,'min':0,'max':10}
conf['params']['collins']['pi+ u a 1']  = {'value': 1.58758,'fixed':False,'min':-0.9,'max':5}
conf['params']['collins']['pi+ u b 1']  = {'value': 2.77410,'fixed':False,'min':-0.9,'max':5}

conf['params']['collins']['pi+ d N 1']  = {'value':-7.94373,'fixed':False,'min':-15,'max':0}
conf['params']['collins']['pi+ d a 1']  = {'value': 3.14003,'fixed':False,'min':-0.9,'max':5}
conf['params']['collins']['pi+ d b 1']  = {'value': 3.27627,'fixed':False,'min':-0.9,'max':5}

conf['params']['collins']['pi+ u c 1']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 1']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 1']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 1']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N 2']  = {'value': 6.31940,'fixed':False,'min':0,'max':10}
conf['params']['collins']['pi+ u a 2']  = {'value': 2.53240,'fixed':False,'min':-0.9,'max':5}
conf['params']['collins']['pi+ u b 2']  = {'value': 2.32471,'fixed':False,'min':-0.9,'max':5}

conf['params']['collins']['pi+ d N 2']  = {'value': 0.0,'fixed':True,'min':-20,'max':0}
conf['params']['collins']['pi+ d a 2']  = {'value': 0.0,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['pi+ d b 2']  = {'value': 0.0,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 2']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 2']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 2']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 2']  = {'value': 0.0,'fixed':True,'min':-10,'max':10}


############################################################################
# SIDIS

conf['datasets']={}
conf['datasets']['sidis']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[7002, 7003]

# does nothing 
conf['datasets']['sidis']['filters'][0]['filter']='z < 1.0 and Q2>1.69'

# clas measurement 
conf['datasets']['sidis']['xlsx'][7002]='../database/sidis/expdata/7002.xlsx' # | proton   | pi- | AUUcos2 | clas 
conf['datasets']['sidis']['xlsx'][7003]='../database/sidis/expdata/7003.xlsx' # | proton   | pi+ | AUUcos2 | clas

conf['datasets']['sidis']['norm'][7002]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][7003]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
