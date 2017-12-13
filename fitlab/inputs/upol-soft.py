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
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# params

conf['params']={}


conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.90397088634672662089e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    6.24543870091293751301e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15152841891949825337e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.36780456247591997165e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.34062655687440218655e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.87915286213149984595e-01>>,'fixed':True,'min':0,'max':1}


conf['params']['soft']={}
conf['params']['soft']['p0']   = {'value':<<    6.09374499048764484144e+00>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p1']   = {'value':<<   -4.94825406306475059637e+01>>,'fixed':False,'min':0,'max':10}
conf['params']['soft']['p2']   = {'value':<<    1.71773187465265209539e+02>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p3']   = {'value':<<   -3.22637116860113451366e+02>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p4']   = {'value':<<    3.43891943844187210289e+02>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p5']   = {'value':<<   -1.84474970453346884369e+02>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p6']   = {'value':<<   -1.68463802023786457518e+00>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p7']   = {'value':<<    7.42513600278312253522e+01>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p8']   = {'value':<<   -5.41884680157435951742e+01>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p9']   = {'value':<<    2.03825057312113884223e+01>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p10']  = {'value':<<   -4.44730872017878997582e+00>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p11']  = {'value':<<    5.34330348782463548929e-01>>,'fixed':False,'min':0,'max':100}
conf['params']['soft']['p12']  = {'value':<<   -2.74425352801649542756e-02>>,'fixed':False,'min':0,'max':100}

############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[1000,1001,1004,1005,1002,1003,1006,1007]
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

conf['datasets']['sidis']['xlsx']={}

conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 

#conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 






