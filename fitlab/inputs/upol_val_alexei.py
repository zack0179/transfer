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
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[1000,1001,1004,1005,1002,1003,1006,1007]
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9" # npts    = 978 chi2    = 1206.873681

conf['datasets']['sidis']['xlsx']={}

conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 

conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 

############################################################################
# params

conf['basis']='valence'


conf['params']={}

conf['params']['pdf']={}
conf['params']['pdf']['widths0 uv']  = {'value':<<    5.88303157642477980716e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['pdf']['widths0 dv']  = {'value':<<    5.88303157642477980716e-01>>,'fixed':'widths0 uv','min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    5.80325048555884071000e-01>>,'fixed':False,'min':0,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.13662953933807320261e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.39856407077580291443e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.29361456236124383601e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.90938600936138125341e-01>>,'fixed':False,'min':0,'max':1}





