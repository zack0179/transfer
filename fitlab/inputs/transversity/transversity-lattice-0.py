conf={}

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
conf['params']['transversity']['widths0 valence'] = {'value':<<    4.58381547706826486532e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['widths0 sea']     = {'value':<<    2.86187176364728790290e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['u N']  = {'value':<<    9.47962979682381717828e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a']  = {'value':<<   -1.39829529228670423890e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b']  = {'value':<<    9.48389907916761920603e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N']  = {'value':<<   -1.01603769646785080383e-01>> ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a']  = {'value':<<    1.39468988368021129531e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b']  = {'value':<<    3.90127320887096118440e-01>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']  = {'value':<<    1.89982378181352135060e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['s a']  = {'value':<<   -4.77330518076467313904e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['s b']  = {'value':<<    1.18698546242516389526e+00>> ,'fixed':False,'min':1e-5,'max':10}

conf['params']['transversity']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['transversity']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    6.93960471735179940111e-02>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    8.77842686543386374609e-02>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    3.57622311735262421450e+00>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<   -1.00000000000000000000e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    1.44669708642777683494e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -3.49369899506799175271e+00>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<   -9.49336216255647791229e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    1.69101094539472507350e+00>> ,'fixed':False,'min':1e-5,'max':10}

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
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']=[]
conf['datasets']['sidis']['filters'].append("z<0.6") 
conf['datasets']['sidis']['filters'].append("Q2>1.69") 
conf['datasets']['sidis']['filters'].append("pT>0.2 and pT<0.9") 


conf['datasets']['sidis']['xlsx']={}

#conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx' # proton   | pi+ | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx' # proton   | pi- | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx' # deuteron | pi+ | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx' # deuteron | pi- | M_Hermes   | hermes 
#
#conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx' # proton   | k+  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx' # proton   | k-  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx' # deuteron | k+  | M_Hermes   | hermes 
#conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx' # deuteron | k-  | M_Hermes   | hermes 

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


# Lattice

conf['datasets']['moments']={}
conf['datasets']['moments']['filters']=[]

conf['datasets']['moments']['xlsx']={}
conf['datasets']['moments']['xlsx'][1000]='../database/lattice/1000.xlsx' 

conf['datasets']['moments']['norm']={}
for k in conf['datasets']['moments']['xlsx']: conf['datasets']['moments']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 




