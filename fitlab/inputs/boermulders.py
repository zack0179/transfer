conf={}
conf['screen mode']='plain'
#conf['screen mode']='curses'

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
#conf['params']['pdf']={}
#conf['params']['pdf']['widths0 valence']  = {'value':<<    5.90288671102841333571e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['pdf']['widths0 sea']      = {'value':<<    6.27510853614136498990e-01>>,'fixed':True,'min':1e-5,'max':1}

#conf['params']['ff']={}
#conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15122136046579115476e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36806885749796047769e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 k+ fav']   = {'value':<<    1.32408177485670908169e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 k+ unfav'] = {'value':<<    1.85494582991636902669e-01>>,'fixed':True,'min':1e-5,'max':1}

conf['params']['boermulders']={}
conf['params']['boermulders']['widths0 valence'] = {'value':<<   -2.68055533992934752127e-03>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['boermulders']['widths0 sea']     = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u N']  = {'value':<<   -1.02139902607581590371e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['u a']  = {'value':<<   -9.15238622614731989202e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['u b']  = {'value':<<   -3.91726324806395798106e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['d N']  = {'value':<<    1.15403964552695609269e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['d a']  = {'value':<<   -4.39675637396374829891e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['d b']  = {'value':<<   -1.20730290611103692477e-02>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['boermulders']['s b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

# anti-quark parameters 
conf['params']['boermulders']['ub N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['ub a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['boermulders']['ub b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['db N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['db a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['boermulders']['db b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['boermulders']['sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['sb a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['boermulders']['sb b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}


conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    1.56256385714737100479e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    3.54574638617556159130e-04>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['collins']['pi+ u N']  = {'value':<<    1.34110617818414379343e+00>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<   -4.53955393954721120320e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    2.83625677762590422404e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<    5.33297926321954322837e-03>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<   -5.07374710795743766312e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    8.92442226254274495467e-01>> ,'fixed':False,'min':1e-5,'max':10}

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
conf['datasets']['sidis']['filters']=[]

#conf['datasets']['sidis']['filters'].append("z<0.6")
#conf['datasets']['sidis']['filters'].append("Q2>1.69")
#conf['datasets']['sidis']['filters'].append("pT>0.2 and pT<0.9")

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
