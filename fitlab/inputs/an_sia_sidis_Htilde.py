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

############################################################################
# params

conf['shape'] = 1

conf['params']={}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.24049999999999993605e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.43729999999999996652e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']   = {'value':<<    1.33839999999999986757e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav'] = {'value':<<    2.02660000000000006803e-01>>,'fixed':True,'min':0,'max':1}


conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    7.24450909911687479514e-02>>,'fixed':False,'min':0.05,'max':1.24049999999999993605e-01}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    1.05884303339609020522e-01>>,'fixed':False,'min':1e-5,'max':1.43729999999999996652e-01}
conf['params']['collins']['pi+ u N 1']  = {'value':<<    7.28400207006167477175e-01>>,'fixed':False,'min':0,'max':4}
conf['params']['collins']['pi+ u a 1']  = {'value':<<   -1.79142949835204157161e+00>>,'fixed':False,'min':-2.5,'max':0}
conf['params']['collins']['pi+ u b 1']  = {'value':<<    5.08790815654434602777e+00>>,'fixed':False,'min':3.,'max':7.}

conf['params']['collins']['pi+ d N 1']  = {'value':<<   -3.10359994308474052005e+00>>,'fixed':False,'min':-15,'max':2}
conf['params']['collins']['pi+ d a 1']  = {'value':<<    9.60788654921703066947e-01>>,'fixed':False,'min': 0.,'max':4.5}
conf['params']['collins']['pi+ d b 1']  = {'value':<<    3.31065068586379274151e+00>>,'fixed':False,'min':2.5,'max':3.8}

conf['params']['collins']['pi+ u c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['pi+ u N 2']  = {'value':<<    1.17849344283819288393e+01>>,'fixed':False,'min':1,'max':52}
conf['params']['collins']['pi+ u a 2']  = {'value':<<    6.36039197880496054438e+00>>,'fixed':False,'min':1,'max':20}
conf['params']['collins']['pi+ u b 2']  = {'value':<<    3.12694645447335695110e+00>>,'fixed':False,'min':3,'max':25}

conf['params']['collins']['pi+ d N 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-20,'max':0}
conf['params']['collins']['pi+ d a 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-1,'max':5}
conf['params']['collins']['pi+ d b 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':10}
conf['params']['collins']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}


conf['params']['transversity']={}
conf['params']['transversity']['widths0 valence'] = {'value':<<    5.24140000000000050306e-01>>,'fixed':False,'min':1e-5,'max':0.52414}
conf['params']['transversity']['widths0 sea']     = {'value':<<    5.84650000000000003020e-01>>,'fixed':False,'min':1e-5,'max':0.58465}
conf['params']['transversity']['u N']             = {'value':<<    9.21278751476002177867e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a']             = {'value':<<    9.93866000780363911815e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b']             = {'value':<<    1.86179614855960462450e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N']             = {'value':<<   -9.58630107574165357676e+00>> ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a']             = {'value':<<    3.58592212719485825545e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b']             = {'value':<<    5.39590259638613289894e+00>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']             = {'value':<<   -6.76637850851272426578e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['s a']             = {'value':<<    4.61274764325941166732e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['s b']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':0.,'max':10}

conf['params']['transversity']['u c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']['u d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['Htilde']={}
conf['params']['Htilde']['widths0 pi+ fav']     = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0.05,'max':1.24049999999999993605e-01}
conf['params']['Htilde']['widths0 pi+ unfav']   = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':1.43729999999999996652e-01}
conf['params']['Htilde']['pi+ u N 1']  = {'value':<<   -3.19840378373156886127e+00>>,'fixed':False,'min':-15,'max':15}
conf['params']['Htilde']['pi+ u a 1']  = {'value':<<    4.19416388582135368779e-01>>,'fixed':False,'min':-1,'max':5}
conf['params']['Htilde']['pi+ u b 1']  = {'value':<<    2.80608752015905471566e+00>>,'fixed':False,'min':0,'max':10}

conf['params']['Htilde']['pi+ d N 1']  = {'value':<<    3.27519715636052843877e+00>>,'fixed':False,'min':-15,'max':15}
conf['params']['Htilde']['pi+ d a 1']  = {'value':<<    1.89864150021610966768e+00>>,'fixed':False,'min': -1,'max':5}
conf['params']['Htilde']['pi+ d b 1']  = {'value':<<    3.57694274284563462629e-02>>,'fixed':False,'min':0,'max':10}

conf['params']['Htilde']['pi+ u c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['Htilde']['pi+ d c 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['Htilde']['pi+ u d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
conf['params']['Htilde']['pi+ d d 1']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}


#conf['params']['Htilde']['pi+ u N 2']  = {'value':<<    1.03213181263992765935e+01>>,'fixed':False,'min':1,'max':52}
#conf['params']['Htilde']['pi+ u a 2']  = {'value':<<    5.96651357076961019743e+00>>,'fixed':False,'min':1,'max':20}
#conf['params']['Htilde']['pi+ u b 2']  = {'value':<<    4.15454650307243866791e+00>>,'fixed':False,'min':3,'max':25}
#
#conf['params']['Htilde']['pi+ d N 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-20,'max':0}
#conf['params']['Htilde']['pi+ d a 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-1,'max':5}
#conf['params']['Htilde']['pi+ d b 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':10}
#conf['params']['Htilde']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
#conf['params']['Htilde']['pi+ d c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
#conf['params']['Htilde']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
#conf['params']['Htilde']['pi+ d d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}


############################################################################
# set data sets

conf['datasets']={}

# SIA

conf['datasets']['sia']={}


conf['datasets']['sia']['norm']={}

conf['datasets']['sia']['filters']=[] # npts    = 122 chi2    = 69.799935
#conf['datasets']['sia']['filters'].append("z<0.6")
#conf['datasets']['sia']['filters'].append("Q2>1.69")
#conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.9")


conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='../database/sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='../database/sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='../database/sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='../database/sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='../database/sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='../database/sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][2008]='../database/sia/expdata/2008.xlsx' # | babar      | pi,pi | AUL-0            | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009]='../database/sia/expdata/2009.xlsx' # | babar      | pi,pi | AUC-0            | 16     | z1,z2      |

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

for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}

# AN

conf['datasets']['AN']={}


conf['datasets']['AN']['norm']={}

conf['datasets']['AN']['filters']=[]


conf['datasets']['AN']['xlsx']={}

conf['datasets']['AN']['xlsx'][1000]='../database/AN_pp/expdata/1000.xlsx' # BRAHMS pim 2.3
conf['datasets']['AN']['xlsx'][1001]='../database/AN_pp/expdata/1001.xlsx' # BRAHMS pim 4
conf['datasets']['AN']['xlsx'][1002]='../database/AN_pp/expdata/1002.xlsx' # BRAHMS pip 2.3
conf['datasets']['AN']['xlsx'][1003]='../database/AN_pp/expdata/1003.xlsx' # BRAHMS pip 4
conf['datasets']['AN']['xlsx'][2000]='../database/AN_pp/expdata/2000.xlsx' # STAR piz 04
conf['datasets']['AN']['xlsx'][2001]='../database/AN_pp/expdata/2001.xlsx' # STAR piz 3.3
conf['datasets']['AN']['xlsx'][2002]='../database/AN_pp/expdata/2002.xlsx' # STAR piz 3.68
conf['datasets']['AN']['xlsx'][2003]='../database/AN_pp/expdata/2003.xlsx' # STAR piz 3.7

for k in conf['datasets']['AN']['xlsx']: conf['datasets']['AN']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
