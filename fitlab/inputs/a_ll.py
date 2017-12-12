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


conf['params']['ppdf']={}
conf['params']['ppdf']['widths0 valence']  = {'value':<<    5.90288671102841333571e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['ppdf']['widths0 sea']      = {'value':<<    6.27510853614136498990e-01>>,'fixed':False,'min':1e-5,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    3.64815774542540882663e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    2.81490539708169840161e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['ff']['widths0 k+ fav']   = {'value':<<    1.32408177485670908169e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['ff']['widths0 k+ unfav'] = {'value':<<    1.85494582991636902669e-01>>,'fixed':False,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------

############################################################################
# SIDIS

conf['datasets']['sidis']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[9000, 9001]
conf['datasets']['sidis']['filters'][0]['filter']='z > 0.2 and x > 0.15 and x < 0.86 and y > 0.2 and y < 0.85 and Q2 > 1.00'

# integrated datasets 
conf['datasets']['sidis']['xlsx'][9000]='../database/sidis/expdata/9000.xlsx' # | neutron | pi+ | ALL | clas
conf['datasets']['sidis']['xlsx'][9001]='../database/sidis/expdata/9001.xlsx' # | neutron | pi- | ALL | clas


# integrated datasets normalization 
conf['datasets']['sidis']['norm'][9000]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
conf['datasets']['sidis']['norm'][9001]={'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':-2,'max':2}
