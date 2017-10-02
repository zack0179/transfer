conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.1
conf['tol']=10e-4
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
conf['shape']=1

conf['params']={}

conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.89294556274006398056e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    6.33443286558464269120e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.15920500644793311729e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.39782079427820671302e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.31266159597196507836e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.85599049505402902138e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['sivers']={}
conf['params']['sivers']['widths0 valence'] = {'value':<<    1.00000000000000008180e-05>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['sivers']['widths0 sea']     = {'value':<<    1.00000000000000008180e-05>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['sivers']['u N']  = {'value':<<   -4.08504700699463596525e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['sivers']['u a']  = {'value':<<   -1.46378744077062528106e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['sivers']['u b']  = {'value':<<    2.65710282183419943536e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['sivers']['d N']  = {'value':<<    5.95938731516630015861e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['sivers']['d a']  = {'value':<<    1.99159193816886848083e-02>> ,'fixed':False,'min':-1,'max':5}
conf['params']['sivers']['d b']  = {'value':<<    4.44849390113346299103e+00>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['sivers']['s N']  = {'value':<<    3.60560145990245148329e-02>> ,'fixed':False,'min':-10,'max':10}
conf['params']['sivers']['s a']  = {'value':<<    2.78658701417087151242e-02>> ,'fixed':False,'min':-1,'max':5}
conf['params']['sivers']['s b']  = {'value':<<    1.00000000000000008180e-05>> ,'fixed':False,'min':1e-5,'max':10}

conf['params']['sivers']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['sivers']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['sivers']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['sivers']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['sivers']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['sivers']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}

conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['xlsx']={}

conf["datasets"]["sidis"]["xlsx"][2000]="../database/sidis/expdata/2000.xlsx" # proton   | pi+    | AUTsivers  | hermes     | PT  
conf["datasets"]["sidis"]["xlsx"][2001]="../database/sidis/expdata/2001.xlsx" # proton   | pi+    | AUTsivers  | hermes     | x   
conf["datasets"]["sidis"]["xlsx"][2002]="../database/sidis/expdata/2002.xlsx" # proton   | pi+    | AUTsivers  | hermes     | z   
conf["datasets"]["sidis"]["xlsx"][2003]="../database/sidis/expdata/2003.xlsx" # proton   | pi-    | AUTsivers  | hermes     | PT  
conf["datasets"]["sidis"]["xlsx"][2004]="../database/sidis/expdata/2004.xlsx" # proton   | pi-    | AUTsivers  | hermes     | x   
conf["datasets"]["sidis"]["xlsx"][2005]="../database/sidis/expdata/2005.xlsx" # proton   | pi-    | AUTsivers  | hermes     | z   

conf["datasets"]["sidis"]["xlsx"][2026]="../database/sidis/expdata/2026.xlsx" # deuteron | pi+    | AUTsivers  | compass    | PT  
conf["datasets"]["sidis"]["xlsx"][2027]="../database/sidis/expdata/2027.xlsx" # deuteron | pi+    | AUTsivers  | compass    | x   
conf["datasets"]["sidis"]["xlsx"][2028]="../database/sidis/expdata/2028.xlsx" # deuteron | pi+    | AUTsivers  | compass    | z   
conf["datasets"]["sidis"]["xlsx"][2029]="../database/sidis/expdata/2029.xlsx" # deuteron | pi-    | AUTsivers  | compass    | PT  
conf["datasets"]["sidis"]["xlsx"][2030]="../database/sidis/expdata/2030.xlsx" # deuteron | pi-    | AUTsivers  | compass    | x   
conf["datasets"]["sidis"]["xlsx"][2031]="../database/sidis/expdata/2031.xlsx" # deuteron | pi-    | AUTsivers  | compass    | z   

for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[2000,2001,2002,2003,2004,2005,2026,2027,2028,2029,2030,2031]
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"



#conf["datasets"]["sidis"]["xlsx"][2015]="../database/sidis/expdata/2015.xlsx" # neutron  | pi+    | AUTsivers  | jlab       | x   
#conf["datasets"]["sidis"]["xlsx"][2016]="../database/sidis/expdata/2016.xlsx" # neutron  | pi-    | AUTsivers  | jlab       | x   

#conf["datasets"]["sidis"]["xlsx"][2006]="../database/sidis/expdata/2006.xlsx" # proton   | pi0    | AUTsivers  | hermes     | PT  
#conf["datasets"]["sidis"]["xlsx"][2007]="../database/sidis/expdata/2007.xlsx" # proton   | pi0    | AUTsivers  | hermes     | x   
#conf["datasets"]["sidis"]["xlsx"][2008]="../database/sidis/expdata/2008.xlsx" # proton   | pi0    | AUTsivers  | hermes     | z   

#conf["datasets"]["sidis"]["xlsx"][2009]="../database/sidis/expdata/2009.xlsx" # proton   | k+     | AUTsivers  | hermes     | PT  
#conf["datasets"]["sidis"]["xlsx"][2010]="../database/sidis/expdata/2010.xlsx" # proton   | k+     | AUTsivers  | hermes     | x   
#conf["datasets"]["sidis"]["xlsx"][2011]="../database/sidis/expdata/2011.xlsx" # proton   | k+     | AUTsivers  | hermes     | z   
#conf["datasets"]["sidis"]["xlsx"][2012]="../database/sidis/expdata/2012.xlsx" # proton   | k-     | AUTsivers  | hermes     | PT  
#conf["datasets"]["sidis"]["xlsx"][2013]="../database/sidis/expdata/2013.xlsx" # proton   | k-     | AUTsivers  | hermes     | x   
#conf["datasets"]["sidis"]["xlsx"][2014]="../database/sidis/expdata/2014.xlsx" # proton   | k-     | AUTsivers  | hermes     | z   
#conf["datasets"]["sidis"]["xlsx"][2017]="../database/sidis/expdata/2017.xlsx" # proton   | k0     | AUTsivers  | compass    | PT  
#conf["datasets"]["sidis"]["xlsx"][2018]="../database/sidis/expdata/2018.xlsx" # proton   | k0     | AUTsivers  | compass    | x   
#conf["datasets"]["sidis"]["xlsx"][2019]="../database/sidis/expdata/2019.xlsx" # proton   | k0     | AUTsivers  | compass    | z   
#conf["datasets"]["sidis"]["xlsx"][2032]="../database/sidis/expdata/2032.xlsx" # deuteron | k+     | AUTsivers  | compass    | PT  
#conf["datasets"]["sidis"]["xlsx"][2033]="../database/sidis/expdata/2033.xlsx" # deuteron | k+     | AUTsivers  | compass    | x   
#conf["datasets"]["sidis"]["xlsx"][2034]="../database/sidis/expdata/2034.xlsx" # deuteron | k+     | AUTsivers  | compass    | z   
#conf["datasets"]["sidis"]["xlsx"][2035]="../database/sidis/expdata/2035.xlsx" # deuteron | k-     | AUTsivers  | compass    | PT  
#conf["datasets"]["sidis"]["xlsx"][2036]="../database/sidis/expdata/2036.xlsx" # deuteron | k-     | AUTsivers  | compass    | x   
#conf["datasets"]["sidis"]["xlsx"][2037]="../database/sidis/expdata/2037.xlsx" # deuteron | k-     | AUTsivers  | compass    | z   
#conf["datasets"]["sidis"]["xlsx"][2038]="../database/sidis/expdata/2038.xlsx" # neutron  | k+     | AUTsivers  | jlab       | x   
#conf["datasets"]["sidis"]["xlsx"][2039]="../database/sidis/expdata/2039.xlsx" # neutron  | k-     | AUTsivers  | jlab       | x   

#conf["datasets"]["sidis"]["xlsx"][2500]="../database/sidis/expdata/2500.xlsx" # neutron  | pi+    | AUTsivers  | solid      | x 
#conf["datasets"]["sidis"]["xlsx"][2501]="../database/sidis/expdata/2501.xlsx" # neutron  | pi-    | AUTsivers  | solid      | x 
#conf["datasets"]["sidis"]["xlsx"][2502]="../database/sidis/expdata/2502.xlsx" # proton   | pi+    | AUTsivers  | solid      | x 
#conf["datasets"]["sidis"]["xlsx"][2503]="../database/sidis/expdata/2503.xlsx" # proton   | pi-    | AUTsivers  | solid      | x 
#conf["datasets"]["sidis"]["xlsx"][2504]="../database/sidis/expdata/2504.xlsx" # proton   | pi+    | AUTsivers  | clas12     | x 
#conf["datasets"]["sidis"]["xlsx"][2505]="../database/sidis/expdata/2505.xlsx" # proton   | pi-    | AUTsivers  | clas12     | x 
#conf["datasets"]["sidis"]["xlsx"][2506]="../database/sidis/expdata/2506.xlsx" # neutron  | pi+    | AUTsivers  | sbs        | x 
#conf["datasets"]["sidis"]["xlsx"][2507]="../database/sidis/expdata/2507.xlsx" # neutron  | pi-    | AUTsivers  | sbs        | x 
#conf["datasets"]["sidis"]["xlsx"][2508]="../database/sidis/expdata/2508.xlsx" # neutron  | pi+    | AUTsivers  | solid stat | x 
#conf["datasets"]["sidis"]["xlsx"][2509]="../database/sidis/expdata/2509.xlsx" # neutron  | pi-    | AUTsivers  | solid stat | x 
#conf["datasets"]["sidis"]["xlsx"][2510]="../database/sidis/expdata/2510.xlsx" # proton   | pi+    | AUTsivers  | solid stat | x 
#conf["datasets"]["sidis"]["xlsx"][2511]="../database/sidis/expdata/2511.xlsx" # proton   | pi-    | AUTsivers  | solid stat | x 
