conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-10
conf['num points'] = 19*3
conf['burn size']  = 100
conf['sample size']= 10000

############################################################################
# resouce allocation
conf['ncpus']=1


############################################################################
# paths to external

conf['path2CJ'] ='../external/CJLIB'
conf['path2LSS']='../external/LSSLIB'
conf['path2DSS']='../external/DSSLIB'

############################################################################
# params
conf['shape']=0

conf['params']={}

conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.89294556274006398056e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    6.33443286558464269120e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15920500644793311729e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.39782079427820671302e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.31266159597196507836e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.85599049505402902138e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['transversity']={}
conf['params']['transversity']['widths0 valence'] = {'value':<<    5.79933092781598658050e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['widths0 sea']     = {'value':<<    4.24126169244575135231e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['u N']             = {'value':<<    1.99312989247765282030e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a']             = {'value':<<    5.15723972394816154718e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b']             = {'value':<<    2.74984123441947003741e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N']             = {'value':<<   -4.12286456902200626473e+00>> ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a']             = {'value':<<    3.05154721871732537153e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b']             = {'value':<<    1.25983194925367563144e+01>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s a']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['transversity']['s b']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

conf['params']['transversity']['u c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']['u d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']             = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    1.46070386805655483276e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    8.89742902394791146392e-02>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    1.38743078543209961140e+01>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<    7.44472833562947355901e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    3.70487086271029619766e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -8.85685932947838949758e+00>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<    1.88762945763237599550e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    4.17285148948135020674e+00>> ,'fixed':False,'min':1e-5,'max':10}

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



conf['params']['boermulders']={}
conf['params']['boermulders']['widths0 valence'] = {'value':<<    3.83985023250973556141e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['boermulders']['widths0 sea']     = {'value':<<    9.32794366294785182170e-02>>,'fixed':False,'min':1e-5,'max':1}

#----------------------------------------------------------------------------------------
conf['params']['boermulders']['u N']  = {'value':<<   -1.32827241573557897070e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['u a']  = {'value':<<    6.84100823141465141930e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['u b']  = {'value':<<    2.64089956004017123448e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['d N']  = {'value':<<   -1.81742082215075084761e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['boermulders']['d a']  = {'value':<<    1.02532853901458675949e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['boermulders']['d b']  = {'value':<<    1.43227516744971117291e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['boermulders']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['boermulders']['s a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':5}
conf['params']['boermulders']['s b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':10}

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




############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['filters']={}

# HERMES MULT

#conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx' # proton   | pi+ | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx' # proton   | pi- | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx' # deuteron | pi+ | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx' # deuteron | pi- | M_Hermes   | hermes 
#
#conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx' # proton   | k+  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx' # proton   | k-  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx' # deuteron | k+  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx' # deuteron | k-  | M_Hermes   | hermes 

# Collins Asy

conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[4001,4000,4002,4004,4003,4005,3027,3025,3010,3012,3005,3013,3026,3000,3003,3016,3004,3018]
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

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

# BoerMulders

conf['datasets']['sidis']['filters'][1]={}
conf['datasets']['sidis']['filters'][1]['idx']=[5019, 5020, 5023, 5024]
conf['datasets']['sidis']['filters'][1]['filter']='z > 0.2 and x > 0.023 and x < 0.6 and y > 0.2 and y < 0.85 and Q2 > 1.0'

# integrated datasets 

conf['datasets']['sidis']['xlsx'][5019]='../database/sidis/expdata/5019.xlsx' # | proton   | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5020]='../database/sidis/expdata/5020.xlsx' # | proton   | pi+ | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5023]='../database/sidis/expdata/5023.xlsx' # | deuteron | pi- | AUUcos2 | hermes 
conf['datasets']['sidis']['xlsx'][5024]='../database/sidis/expdata/5024.xlsx' # | deuteron | pi+ | AUUcos2 | hermes 

#conf['datasets']['sidis']['xlsx'][5017]='../database/sidis/expdata/5017.xlsx' # | proton   | k- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5018]='../database/sidis/expdata/5018.xlsx' # | proton   | k+ | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5021]='../database/sidis/expdata/5021.xlsx' # | deuteron | k- | AUUcos2 | hermes 
#conf['datasets']['sidis']['xlsx'][5022]='../database/sidis/expdata/5022.xlsx' # | deuteron | k+ | AUUcos2 | hermes 

#conf['datasets']['sidis']['xlsx'][5025]='../database/sidis/expdata/5025.xlsx' # | proton   | k- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5026]='../database/sidis/expdata/5026.xlsx' # | proton   | k+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5027]='../database/sidis/expdata/5027.xlsx' # | deuteron | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5028]='../database/sidis/expdata/5028.xlsx' # | deuteron | pi+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5029]='../database/sidis/expdata/5029.xlsx' # | proton   | k- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5030]='../database/sidis/expdata/5030.xlsx' # | proton   | k+ | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5031]='../database/sidis/expdata/5031.xlsx' # | deuteron | pi- | AUUcos  | hermes 
#conf['datasets']['sidis']['xlsx'][5032]='../database/sidis/expdata/5032.xlsx' # | deuteron | pi+ | AUUcos  | hermes 




# add normalization pars

for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 









