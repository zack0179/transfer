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
#conf['params']['pdf']={}
#conf['params']['pdf']['widths0 valence']  = {'value':<<    5.90288671102841333571e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['pdf']['widths0 sea']      = {'value':<<    6.27510853614136498990e-01>>,'fixed':True,'min':1e-5,'max':1}

#conf['params']['ff']={}
#conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15122136046579115476e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36806885749796047769e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 k+ fav']   = {'value':<<    1.32408177485670908169e-01>>,'fixed':True,'min':1e-5,'max':1}
#conf['params']['ff']['widths0 k+ unfav'] = {'value':<<    1.85494582991636902669e-01>>,'fixed':True,'min':1e-5,'max':1}

conf['params']['pretzelosity']={}
conf['params']['pretzelosity']['widths0 valence'] = {'value':<<    6.62401853528338246946e-04>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['pretzelosity']['widths0 sea']     = {'value':<<    9.86199935641373093276e-02>>,'fixed':False,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------
conf['params']['pretzelosity']['u N']  = {'value':<<   -7.89516312009176512987e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['pretzelosity']['u a']  = {'value':<<    1.00000000000655120402e-05>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['pretzelosity']['u b']  = {'value':<<    8.27556924946045135982e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['pretzelosity']['d N']  = {'value':<<    1.22233637848631082612e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['pretzelosity']['d a']  = {'value':<<    6.25072397407901325650e-01>> ,'fixed':False,'min':1e-5,'max':5}
conf['params']['pretzelosity']['d b']  = {'value':<<    7.84363081824918584317e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['pretzelosity']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s a']  = {'value':<<    5.53070929403782773903e-01>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['s b']  = {'value':<<    2.39050712257790154425e+00>> ,'fixed':True,'min':1e-5,'max':10}

# anti-quark parameters 
conf['params']['pretzelosity']['ub N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['ub a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['ub b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['db N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['db a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['db b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}
conf['params']['pretzelosity']['sb a']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':5}
conf['params']['pretzelosity']['sb b']  = {'value':<<    1.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

#----------------------------------------------------------------------------------------
conf['params']['pretzelosity']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['pretzelosity']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    6.45892468420083964986e-02>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    2.76949627510227891491e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    1.03513362588519619578e+01>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<   -1.00000000000000000000e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    6.34082800762176290732e+00>> ,'fixed':False,'min':-1,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -3.00532308880009058072e+00>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<    7.84653168853393534476e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    2.16067172676201169068e+00>> ,'fixed':False,'min':-1,'max':10}
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
conf['datasets']['sidis']['filters'][0]['idx']=[8001]
conf['datasets']['sidis']['filters'][0]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.00'
conf['datasets']['sidis']['filters'][1]={}
conf['datasets']['sidis']['filters'][1]['idx']=[8005, 8006, 8007]
conf['datasets']['sidis']['filters'][1]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.00'

# integrated datasets 
#conf['datasets']['sidis']['xlsx'][8000]='../database/sidis/expdata/8000.xlsx' # | neutron | pi- | A_pretzelosity | jlab
conf['datasets']['sidis']['xlsx'][8001]='../database/sidis/expdata/8001.xlsx' # | neutron | pi+ | A_pretzelosity | jlab
#conf['datasets']['sidis']['xlsx'][8002]='../database/sidis/expdata/8002.xlsx' # | proton | pi- | A_pretzelosity | hermes
#conf['datasets']['sidis']['xlsx'][8003]='../database/sidis/expdata/8003.xlsx' # | proton | pi- | A_pretzelosity | hermes
#conf['datasets']['sidis']['xlsx'][8004]='../database/sidis/expdata/8004.xlsx' # | proton | pi- | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8005]='../database/sidis/expdata/8005.xlsx' # | proton | pi+ | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8006]='../database/sidis/expdata/8006.xlsx' # | proton | pi+ | A_pretzelosity | hermes
conf['datasets']['sidis']['xlsx'][8007]='../database/sidis/expdata/8007.xlsx' # | proton | pi+ | A_pretzelosity | hermes


# integrated datasets normalization 
#conf['datasets']['sidis']['norm'][8000]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][8001]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][8002]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][8003]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
#conf['datasets']['sidis']['norm'][8004]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][8005]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][8006]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][8007]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
