conf={}
conf['screen mode']='plain'
#conf['screen mode']='curses'

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-4
conf['num points'] = 19*100
conf['burn size']  = 100
conf['sample size']= 10000

############################################################################
# path to output 
conf['output dir']='runs/boermulders'

############################################################################
# paths to external

conf['path2CJ'] ='../external/CJLIB'
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# set data sets

conf['bootstrap']=False
conf['training frac']=1.0
conf['ncpus']=1
conf['datasets']={}


# unnormalized 
conf['shape'] = 0

############################################################################
# params

conf['params']={}


# these are included when using the observable AUUcos for it has two terms 
# the second of which depends on f1 * D1
conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.90288671102841333571e-01>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    6.27510853614136498990e-01>>,'fixed':True,'min':1e-5,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15122136046579115476e-01>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36806885749796047769e-01>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['ff']['widths0 k+ fav']   = {'value':<<    1.32408177485670908169e-01>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['ff']['widths0 k+ unfav'] = {'value':<<    1.85494582991636902669e-01>>,'fixed':True,'min':1e-5,'max':1}

conf['params']['boermulders']={}
conf['params']['boermulders']['widths0 valence'] = {'value':<<   -1.22577139544071178948e-05>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['boermulders']['widths0 sea']     = {'value':<<    3.86199935641373115480e-02>>,'fixed':False,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u N']  = {'value':<<   -3.30312733608226505311e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['u a']  = {'value':<<   -4.00404083500269292184e-01>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['boermulders']['u b']  = {'value':<<    9.64463840138559191928e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['d N']  = {'value':<<   -6.56613566583236618612e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['d a']  = {'value':<<    7.18116697586528018871e-03>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['boermulders']['d b']  = {'value':<<    1.09893946694127802033e+01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s a']  = {'value':<<    5.53070929403782773903e-01>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['boermulders']['s b']  = {'value':<<    2.39050712257790154425e+00>> ,'fixed':True,'min':1e-5,'max':10}

# anti-quark parameters 
conf['params']['boermulders']['ub N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['ub a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['boermulders']['ub b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['db N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['db a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['boermulders']['db b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['sb a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['boermulders']['sb b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    4.48787237198106592206e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    1.28992783556386519939e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    5.07064105791088692854e+00>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<    6.30425323192389797100e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    1.79233758632234962960e+00>> ,'fixed':False,'min':-1,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -1.80127977516045323370e+00>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<    8.54798514625790151200e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    4.01942175354687947220e+00>> ,'fixed':False,'min':-1,'max':10}
conf['params']['collins']['pi+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['widths0 k+ fav']     = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':1}
conf['params']['collins']['widths0 k+ unfav']   = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':2}
conf['params']['collins']['k+ u N']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-5,'max':20}
conf['params']['collins']['k+ u a']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ u b']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ d N']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':20}
conf['params']['collins']['k+ d a']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':10}
conf['params']['collins']['k+ d b']   = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':20}
conf['params']['collins']['k+ sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-20,'max':20}
conf['params']['collins']['k+ sb a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['k+ sb b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['k+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['k+ sb d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

############################################################################
# SIDIS

conf['datasets']['sidis']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[5002, 5003, 5006, 5007]
#conf['datasets']['sidis']['filters'][0]['filter']='z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9'
conf['datasets']['sidis']['filters'][0]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.0'


# new stuff 
#conf['datasets']['sidis']['xlsx'][5000]='../database/sidis/expdata/5000.xlsx' # | proton   | k-  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5001]='../database/sidis/expdata/5001.xlsx' # | proton   | k+  | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5002]='../database/sidis/expdata/5002.xlsx' # | proton   | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5003]='../database/sidis/expdata/5003.xlsx' # | proton   | pi+ | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5004]='../database/sidis/expdata/5004.xlsx' # | deuteron | k-  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5005]='../database/sidis/expdata/5005.xlsx' # | deuteron | k+  | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5006]='../database/sidis/expdata/5006.xlsx' # | deuteron | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5007]='../database/sidis/expdata/5007.xlsx' # | deuteron | pi+ | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5008]='../database/sidis/expdata/5008.xlsx' # | proton   | k-  | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5009]='../database/sidis/expdata/5009.xlsx' # | proton   | k+  | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5010]='../database/sidis/expdata/5010.xlsx' # | proton   | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5011]='../database/sidis/expdata/5011.xlsx' # | proton   | pi+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5012]='../database/sidis/expdata/5012.xlsx' # | deuteron | k-  | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5013]='../database/sidis/expdata/5013.xlsx' # | deuteron | k+  | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5014]='../database/sidis/expdata/5014.xlsx' # | deuteron | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5015]='../database/sidis/expdata/5015.xlsx' # | deuteron | pi+ | AUUcos  | hermes 

#conf['datasets']['sidis']['norm'][5000]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5001]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5002]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5003]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5004]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5005]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5006]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5007]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5008]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5009]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5010]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5011]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5012]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5013]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5014]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5015]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
