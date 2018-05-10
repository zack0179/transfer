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
conf['ncpus']=4

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
conf['shape']=1
conf['basis']='default'


conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.24140000000000050306e-01>>,'fixed':True,'min':0.3,'max':0.7}
conf['params']['pdf']['widths0 sea']      = {'value':<<    5.84650000000000003020e-01>>,'fixed':True,'min':0.2,'max':1.}
conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.24049999999999993605e-01>>,'fixed':True,'min':0.1,'max':0.2}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.43729999999999996652e-01>>,'fixed':True,'min':0.1,'max':0.2}



conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    1.24049999999999993605e-01>>,'fixed':False,'min':1e-5,'max':0.12405}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    9.22073510991547606874e-02>>,'fixed':False,'min':1e-5,'max':0.14373}
#conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<0.07649>>,'fixed':False,'min':1e-5,'max':0.2}
conf['params']['collins']['pi+ u N 1']  = {'value':<<    1.52948533965102861920e+00>>,'fixed':False,'min':0,'max':5}
conf['params']['collins']['pi+ u a 1']  = {'value':<<   -1.26297747035769281077e+00>>,'fixed':False,'min':-2.59,'max':0}
conf['params']['collins']['pi+ u b 1']  = {'value':<<    3.03348994081082601326e+00>>,'fixed':False,'min':0.5,'max':4.5}

conf['params']['collins']['pi+ d N 1']  = {'value':<<   -6.70019661848445480246e+00>>,'fixed':False,'min':-12,'max':0}
conf['params']['collins']['pi+ d a 1']  = {'value':<<    7.90788237407234806398e-01>>,'fixed':False,'min': -2.,'max':3.}
conf['params']['collins']['pi+ d b 1']  = {'value':<<    3.02696426160740239553e+00>>,'fixed':False,'min':0.0,'max':6.8}

conf['params']['collins']['pi+ u c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':15}
conf['params']['collins']['pi+ u a 2']  = {'value':<<    5.23874999999999957367e+00>>,'fixed':True,'min':0,'max':10}
conf['params']['collins']['pi+ u b 2']  = {'value':<<    3.41155000000000008242e+00>>,'fixed':True,'min':0,'max':10}

conf['params']['collins']['pi+ d N 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-20,'max':0}
conf['params']['collins']['pi+ d a 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['pi+ d b 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']={}
conf['params']['transversity']['widths0 valence'] = {'value':<<    5.24140000000000050306e-01>>,'fixed':False,'min':1e-5,'max':0.52414}
conf['params']['transversity']['widths0 sea']     = {'value':<<    4.04126169244575006445e-01>>,'fixed':True,'min':1e-5,'max':0.58465}
conf['params']['transversity']['u N']             = {'value':<<    3.90228525039118956386e+00>>,'fixed':False,'min':-1,'max':15}
conf['params']['transversity']['u a']             = {'value':<<    7.98756933748900554981e-01>>,'fixed':False,'min':-2,'max':3}
conf['params']['transversity']['u b']             = {'value':<<    5.18083901578981009806e+00>>,'fixed':False,'min':1e-5,'max':12}
conf['params']['transversity']['d N']             = {'value':<<   -1.18206784271460918490e+01>>,'fixed':False,'min':-30,'max':3}
conf['params']['transversity']['d a']             = {'value':<<    7.11562722927955970675e-01>>,'fixed':False,'min':-1,'max':3}
conf['params']['transversity']['d b']             = {'value':<<    6.09620096668816557894e+00>>,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s a']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s b']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':10}

conf['params']['transversity']['u c']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']['u d']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']             = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}

############################################################################
# set data sets
conf['datasets']={}
# Collins Asy

conf['datasets']['sidis']={}
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['filters']={}

conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[4001,4000,4002,4004,4003,4005,3027,3025,3010,3012,3005,3013,3026,3000,3003,3016,3004,3018]
conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

#conf["datasets"]["sidis"]["xlsx"][4007]="../database/sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
#conf["datasets"]["sidis"]["xlsx"][4006]="../database/sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
#conf["datasets"]["sidis"]["xlsx"][4008]="../database/sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
#conf["datasets"]["sidis"]["xlsx"][4010]="../database/sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
#conf["datasets"]["sidis"]["xlsx"][4009]="../database/sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
#conf["datasets"]["sidis"]["xlsx"][4011]="../database/sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
conf["datasets"]["sidis"]["xlsx"][4001]="../database/sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+   pT
conf["datasets"]["sidis"]["xlsx"][4000]="../database/sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+    x
conf["datasets"]["sidis"]["xlsx"][4002]="../database/sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+    z
conf["datasets"]["sidis"]["xlsx"][4004]="../database/sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="../database/sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="../database/sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
#conf["datasets"]["sidis"]["xlsx"][6003]="../database/sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][6004]="../database/sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][6005]="../database/sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][6000]="../database/sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][6001]="../database/sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][6002]="../database/sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3027]="../database/sidis/expdata/3027.xlsx"  #  compass    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3025]="../database/sidis/expdata/3025.xlsx"  #  compass    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3010]="../database/sidis/expdata/3010.xlsx"  #  compass    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3012]="../database/sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="../database/sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="../database/sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
#conf["datasets"]["sidis"]["xlsx"][3024]="../database/sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][3007]="../database/sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][3008]="../database/sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][3021]="../database/sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][3017]="../database/sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][3023]="../database/sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3026]="../database/sidis/expdata/3026.xlsx"  #   HERMES    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="../database/sidis/expdata/3000.xlsx"  #   HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="../database/sidis/expdata/3003.xlsx"  #   HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="../database/sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="../database/sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="../database/sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z

for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}


    
