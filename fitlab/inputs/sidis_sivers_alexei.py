conf={}

############################################################################
conf['method']='cov'
conf['kappa']=1.4
conf['tol']=0.8e-4
conf['num points'] = 100
conf['burn size']  = 500
conf['sample size']= 10000

############################################################################
# resouce allocation

conf['ncpus']=16

############################################################################
# paths to external

#conf['path2CJ'] ='../external/CJLIB'
#conf['path2LSS']='../external/LSSLIB'
#conf['path2DSS']='../external/DSSLIB'

############################################################################
# params
conf['shape']=1

conf['params']={}

conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.70529084906132410993e-01>>,'fixed':False,'min':0,'max':10}
conf['params']['pdf']['widths0 sea']      = {'value':<<    9.05881359564491006608e-01>>,'fixed':False,'min':0,'max':10}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    2.09495986820052271238e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.93430515700360017295e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    2.95033410728077538643e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.60639839770686576603e-01>>,'fixed':False,'min':0,'max':1}

conf['params']['sivers']={}
conf['params']['sivers']['widths0 valence'] = {'value':<<    3.73339140231546018356e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['sivers']['widths0 sea']     = {'value':<<    8.61391945667360658945e-01>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['sivers']['u N']  = {'value':<<   -1.99015570269111707891e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['u a']  = {'value':<<   -2.45405229714120598494e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['u b']  = {'value':<<    1.88354870449787270559e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['u c']  = {'value':<<   -1.82323560585785626742e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['d N']  = {'value':<<    2.21605720535108935421e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['d a']  = {'value':<<   -2.03177313183136920571e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['d b']  = {'value':<<    4.02014558006558075931e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['d c']  = {'value':<<   -1.68752277201169476051e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':1}
conf['params']['sivers']['s a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':2}
conf['params']['sivers']['s b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':0,'max':25}
conf['params']['sivers']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-5,'max':5}
conf['params']['sivers']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['ub N']  = {'value':<<    3.25235044514182100595e-02>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['ub a']  = {'value':<<    2.15267325241758455956e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['ub b']  = {'value':<<    1.55044008589557869016e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['ub c']  = {'value':<<    1.66695193506958405649e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['ub d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['db N']  = {'value':<<    9.60167985928469039369e-03>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['db a']  = {'value':<<   -1.30786537372008737634e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['db b']  = {'value':<<    5.19595560596371797146e-01>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['db c']  = {'value':<<    9.80028458941023417061e-01>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['db d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-30,'max':30}
conf['params']['sivers']['sb a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-1,'max':15}
conf['params']['sivers']['sb b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':1e-5,'max':30}
conf['params']['sivers']['sb c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-5,'max':5}
conf['params']['sivers']['sb d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}


############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=range(1000,2000) 
#conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and (pT/z)**2<0.25*Q2" # rapidity Gunar wrote z< 0.2 and z>0.8 are padding bins
conf['datasets']['sidis']['filters'][0]['filter']="Q2>1.69 and z>0.2 and z<0.6 and pT>0.2 and pT<0.9" 


conf['datasets']['sidis']['filters'][1]={}
conf['datasets']['sidis']['filters'][1]['idx']=range(2000,2500)
conf['datasets']['sidis']['filters'][1]['filter']="Q2>1.0 and z<0.7 and pT<0.9"

conf['datasets']['sidis']['xlsx']={}

conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 

conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 


conf['datasets']['sidis']['xlsx'][2000]='../database/sidis/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2001]='../database/sidis/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x  
conf['datasets']['sidis']['xlsx'][2002]='../database/sidis/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z  
conf['datasets']['sidis']['xlsx'][2003]='../database/sidis/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2004]='../database/sidis/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x  
conf['datasets']['sidis']['xlsx'][2005]='../database/sidis/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z  
#conf['datasets']['sidis']['xlsx'][2006]='../database/sidis/expdata/2006.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | PT 
#conf['datasets']['sidis']['xlsx'][2007]='../database/sidis/expdata/2007.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | x 
#conf['datasets']['sidis']['xlsx'][2008]='../database/sidis/expdata/2008.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2009]='../database/sidis/expdata/2009.xlsx'  # proton   | k+     | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2010]='../database/sidis/expdata/2010.xlsx'  # proton   | k+     | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2011]='../database/sidis/expdata/2011.xlsx'  # proton   | k+     | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2012]='../database/sidis/expdata/2012.xlsx'  # proton   | k-     | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2013]='../database/sidis/expdata/2013.xlsx'  # proton   | k-     | AUTsivers  | hermes     | x 
conf['datasets']['sidis']['xlsx'][2014]='../database/sidis/expdata/2014.xlsx'  # proton   | k-     | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2015]='../database/sidis/expdata/2015.xlsx'  # neutron  | pi+    | AUTsivers  | jlab       | x 
conf['datasets']['sidis']['xlsx'][2016]='../database/sidis/expdata/2016.xlsx'  # neutron  | pi-    | AUTsivers  | jlab       | x
#conf['datasets']['sidis']['xlsx'][2017]='../database/sidis/expdata/2017.xlsx'  # proton   | k0     | AUTsivers  | compass    | PT 
#conf['datasets']['sidis']['xlsx'][2018]='../database/sidis/expdata/2018.xlsx'  # proton   | k0     | AUTsivers  | compass    | x
#conf['datasets']['sidis']['xlsx'][2019]='../database/sidis/expdata/2019.xlsx'  # proton   | k0     | AUTsivers  | compass    | z
#conf['datasets']['sidis']['xlsx'][2020]='../database/sidis/expdata/2020.xlsx'  # proton   | h+     | AUTsivers  | compass    | PT
#conf['datasets']['sidis']['xlsx'][2021]='../database/sidis/expdata/2021.xlsx'  # proton   | h+     | AUTsivers  | compass    | x #
#conf['datasets']['sidis']['xlsx'][2022]='../database/sidis/expdata/2022.xlsx'  # proton   | h+     | AUTsivers  | compass    | z 
#conf['datasets']['sidis']['xlsx'][2023]='../database/sidis/expdata/2023.xlsx'  # proton   | h-     | AUTsivers  | compass    | PT 
#conf['datasets']['sidis']['xlsx'][2024]='../database/sidis/expdata/2024.xlsx'  # proton   | h-     | AUTsivers  | compass    | x
#conf['datasets']['sidis']['xlsx'][2025]='../database/sidis/expdata/2025.xlsx'  # proton   | h-     | AUTsivers  | compass    | z 
conf['datasets']['sidis']['xlsx'][2026]='../database/sidis/expdata/2026.xlsx'  # deuteron | pi+    | AUTsivers  | compass    | PT 
conf['datasets']['sidis']['xlsx'][2027]='../database/sidis/expdata/2027.xlsx'  # deuteron | pi+    | AUTsivers  | compass    | x 
conf['datasets']['sidis']['xlsx'][2028]='../database/sidis/expdata/2028.xlsx'  # deuteron | pi+    | AUTsivers  | compass    | z 
conf['datasets']['sidis']['xlsx'][2029]='../database/sidis/expdata/2029.xlsx'  # deuteron | pi-    | AUTsivers  | compass    | PT 
conf['datasets']['sidis']['xlsx'][2030]='../database/sidis/expdata/2030.xlsx'  # deuteron | pi-    | AUTsivers  | compass    | x 
conf['datasets']['sidis']['xlsx'][2031]='../database/sidis/expdata/2031.xlsx'  # deuteron | pi-    | AUTsivers  | compass    | z 
conf['datasets']['sidis']['xlsx'][2032]='../database/sidis/expdata/2032.xlsx'  # deuteron | k+     | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2033]='../database/sidis/expdata/2033.xlsx'  # deuteron | k+     | AUTsivers  | compass    | x 
conf['datasets']['sidis']['xlsx'][2034]='../database/sidis/expdata/2034.xlsx'  # deuteron | k+     | AUTsivers  | compass    | z 
conf['datasets']['sidis']['xlsx'][2035]='../database/sidis/expdata/2035.xlsx'  # deuteron | k-     | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2036]='../database/sidis/expdata/2036.xlsx'  # deuteron | k-     | AUTsivers  | compass    | x 
conf['datasets']['sidis']['xlsx'][2037]='../database/sidis/expdata/2037.xlsx'  # deuteron | k-     | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2038]='../database/sidis/expdata/2038.xlsx'  # neutron  | k+     | AUTsivers  | jlab    | x 
conf['datasets']['sidis']['xlsx'][2039]='../database/sidis/expdata/2039.xlsx'  # neutron  | k-     | AUTsivers  | jlab    | z 


for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 




