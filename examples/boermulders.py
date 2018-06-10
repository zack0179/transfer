conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-10
conf['num points'] = 30 #self.npar*3
conf['burn size']  = 10
conf['sample size']= 10000

conf['screen mode']='plain'
#conf['screen mode']='curses'

conf['ncpus']=1
############################################################################
# path to output 
conf['output dir']='runs/boermulders'

############################################################################
# paths to external

conf['path2CJ'] ='../external/CJLIB'
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# mcsetup

conf['method']='kde'
conf['itmax']=None
conf['tol']=1e-6
conf['kde bw']=None
conf['num points factor']=10


# unnormalized 
conf['shape'] = 1

############################################################################
# params

conf['params']={}


# these are included when using the observable AUUcos for it has two terms 
# the second of which depends on f1 * D1
conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':5.90288671102841333571e-01,'fixed':True,'min':1e-5,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':6.27510853614136498990e-01,'fixed':True,'min':1e-5,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':1.15151579728561548333e-01,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':1.36784756168045196212e-01,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':1.34062655687440246410e-01,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav'] = {'value':1.85494582991636902669e-01,'fixed':True,'min':1e-5,'max':1}

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
conf['datasets']['sidis']['filters'][0]['idx']=[5019, 5020, 5023, 5024]
#conf['datasets']['sidis']['filters'][0]['filter']='z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9'
conf['datasets']['sidis']['filters'][0]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.0'


# integrated datasets 
#conf['datasets']['sidis']['xlsx'][5017]='../database/sidis/expdata/5017.xlsx' # | proton   | k- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5018]='../database/sidis/expdata/5018.xlsx' # | proton   | k+ | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5019]='../database/sidis/expdata/5019.xlsx' # | proton   | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5020]='../database/sidis/expdata/5020.xlsx' # | proton   | pi+ | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5021]='../database/sidis/expdata/5021.xlsx' # | deuteron | k- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5022]='../database/sidis/expdata/5022.xlsx' # | deuteron | k+ | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5023]='../database/sidis/expdata/5023.xlsx' # | deuteron | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5024]='../database/sidis/expdata/5024.xlsx' # | deuteron | pi+ | AUUcos2 | hermes 

#conf['datasets']['sidis']['xlsx'][5025]='../database/sidis/expdata/5025.xlsx' # | proton   | k- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5026]='../database/sidis/expdata/5026.xlsx' # | proton   | k+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5027]='../database/sidis/expdata/5027.xlsx' # | deuteron | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5028]='../database/sidis/expdata/5028.xlsx' # | deuteron | pi+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5029]='../database/sidis/expdata/5029.xlsx' # | proton   | k- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5030]='../database/sidis/expdata/5030.xlsx' # | proton   | k+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5031]='../database/sidis/expdata/5031.xlsx' # | deuteron | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5032]='../database/sidis/expdata/5032.xlsx' # | deuteron | pi+ | AUUcos  | hermes 

# integrated datasets normalization 
#conf['datasets']['sidis']['norm'][5017]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5018]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5019]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5020]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5021]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5022]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5023]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5024]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}

#conf['datasets']['sidis']['norm'][5025]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5026]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5027]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5028]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5029]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5030]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5031]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5032]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}

# new stuff 
#conf['datasets']['sidis']['xlsx'][5000]='../database/sidis/expdata/5000.xlsx' # | proton   | k-  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5001]='../database/sidis/expdata/5001.xlsx' # | proton   | k+  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5002]='../database/sidis/expdata/5002.xlsx' # | proton   | pi- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5003]='../database/sidis/expdata/5003.xlsx' # | proton   | pi+ | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5004]='../database/sidis/expdata/5004.xlsx' # | deuteron | k-  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5005]='../database/sidis/expdata/5005.xlsx' # | deuteron | k+  | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5006]='../database/sidis/expdata/5006.xlsx' # | deuteron | pi- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5007]='../database/sidis/expdata/5007.xlsx' # | deuteron | pi+ | AUUcos2 | hermes 
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
#conf['datasets']['sidis']['norm'][5002]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5003]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5004]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5005]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5006]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5007]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5008]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5009]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5010]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5011]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5012]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5013]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5014]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][5015]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}

conf['datasets']['sidis']['norm'][5019]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5020]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5023]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][5024]={'value':1.00000000000000000000e+00,'fixed':True,'min':-2,'max':2}
