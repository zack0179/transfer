conf={}

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
conf['path2CT10'] ='../external/PDF'
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# params

conf['params']={}


conf['params']['ppdf']={}
conf['params']['ppdf']['widths0 valence']  = {'value':<<    4.31687891981962168497e-01>>,'fixed':False,'min':0,'max':10}
conf['params']['ppdf']['widths0 sea']      = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':10}


conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.90482207933462066585e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    6.23829823377092362868e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15151579728561534455e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36784756168045168456e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.34062655687440218655e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.87915286213149984595e-01>>,'fixed':True,'min':0,'max':1}



############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[9000,9001]
conf['datasets']['sidis']['filters'][0]['filter']="z>0"
#conf['datasets']['sidis']['filters'][0]['filter']='z > 0.2 and x > 0.15 and x < 0.86 and y > 0.2 and y < 0.85 and Q2 > 1.00'

conf['datasets']['sidis']['xlsx']={}


    
conf['datasets']['sidis']['xlsx'][2000]='../database/sidis/expdata/9000.xlsx'  # |  proton | pi+    | ALL | clas 
conf['datasets']['sidis']['xlsx'][2001]='../database/sidis/expdata/9001.xlsx'  # |  proton | pi-    | ALL | clas 
#conf['datasets']['sidis']['xlsx'][2002]='../database/sidis/expdata/9002.xlsx'  # |  proton | pi0    | ALL | clas 
    
    
conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 






