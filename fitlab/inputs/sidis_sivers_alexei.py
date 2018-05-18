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

conf['ncpus']=4

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
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.24140000000000050306e-01>>,'fixed':True,'min':0,'max':10}
conf['params']['pdf']['widths0 sea']      = {'value':<<    5.84650000000000003020e-01>>,'fixed':True,'min':0,'max':10}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.24049999999999993605e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.43729999999999996652e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 h+ fav']   = {'value':<<    1.24049999999999993605e-01>>,'fixed':'widths0 pi+ fav','min':0,'max':1}
conf['params']['ff']['widths0 h+ unfav'] = {'value':<<    1.43729999999999996652e-01>>,'fixed':'widths0 pi+ unfav','min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.33839999999999986757e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    2.02660000000000006803e-01>>,'fixed':True,'min':0,'max':1}


 
conf['params']['sivers']={}
conf['params']['sivers']['widths0 valence'] = {'value':<<    3.74660480608947854542e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['sivers']['widths0 sea']     = {'value':<<    3.60810400551778709399e-02>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['sivers']['u N']  = {'value':<<   -2.03568242514484881722e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['u a']  = {'value':<<   -1.93677199209763450938e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['u b']  = {'value':<<    3.22449270298309009775e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['u c']  = {'value':<<    5.32024251671565528987e-01>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['d N']  = {'value':<<    2.80115870397849853202e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['d a']  = {'value':<<   -4.42038869289290703435e-02>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['d b']  = {'value':<<    6.69239878613034644417e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['d c']  = {'value':<<    1.58357599720565844770e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['ub N']  = {'value':<<    6.45677089211802446300e-02>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['ub a']  = {'value':<<    6.50777429133934881555e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['ub b']  = {'value':<<    2.38944904300343807790e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['ub c']  = {'value':<<    3.29488699262210538166e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['ub d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['db N']  = {'value':<<    1.80465177492385997482e-02>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['db a']  = {'value':<<   -4.51146267326795191721e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['db b']  = {'value':<<    5.09508861339085772357e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['db c']  = {'value':<<    1.43547183356968011125e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['db d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['sb N']  = {'value':<<   -6.74236529965721448354e-02>> ,'fixed':False,'min':-30,'max':30}
conf['params']['sivers']['sb a']  = {'value':<<    3.01768437566481750878e-01>> ,'fixed':False,'min':-1,'max':15}
conf['params']['sivers']['sb b']  = {'value':<<    4.62919137075176756468e+00>> ,'fixed':False,'min':1e-5,'max':30}
conf['params']['sivers']['sb c']  = {'value':<<    3.76446795161979375077e-01>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['sb d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['s N']  = {'value':<<   -6.74236529965721448354e-02>> ,'fixed':'sb N','min':-1,'max':1}
conf['params']['sivers']['s a']  = {'value':<<    3.01768437566481750878e-01>> ,'fixed':'sb a','min':-1,'max':2}
conf['params']['sivers']['s b']  = {'value':<<    4.62919137075176756468e+00>> ,'fixed':'sb b','min':0,'max':25}
conf['params']['sivers']['s c']  = {'value':<<    3.76446795161979375077e-01>> ,'fixed':'sb c','min':-5,'max':5}
conf['params']['sivers']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':'sb d','min':-2,'max':2}


############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['norm']={}

conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=range(1000,2000) 
conf['datasets']['sidis']['filters'][0]['filter']="Q2>1.69 and z>0.2 and z<0.6 and pT>0.2 and pT<0.9" 


conf['datasets']['sidis']['filters'][1]={}
conf['datasets']['sidis']['filters'][1]['idx']=range(2000,2500)
conf['datasets']['sidis']['filters'][1]['filter']="Q2>1.0 and z<0.7 and pT<0.9"

conf['datasets']['sidis']['xlsx']={}

#conf['datasets']['sidis']['xlsx'][1000]='../database/sidis/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1001]='../database/sidis/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1004]='../database/sidis/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1005]='../database/sidis/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 

#conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
#conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 


conf['datasets']['sidis']['xlsx'][2000]='../database/sidis/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2001]='../database/sidis/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x  
conf['datasets']['sidis']['xlsx'][2002]='../database/sidis/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z  
conf['datasets']['sidis']['xlsx'][2003]='../database/sidis/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2004]='../database/sidis/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x  
conf['datasets']['sidis']['xlsx'][2005]='../database/sidis/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z  
##conf['datasets']['sidis']['xlsx'][2006]='../database/sidis/expdata/2006.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | PT 
##conf['datasets']['sidis']['xlsx'][2007]='../database/sidis/expdata/2007.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | x 
##conf['datasets']['sidis']['xlsx'][2008]='../database/sidis/expdata/2008.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2009]='../database/sidis/expdata/2009.xlsx'  # proton   | k+     | AUTsivers  | hermes     | PT 
conf['datasets']['sidis']['xlsx'][2010]='../database/sidis/expdata/2010.xlsx'  # proton   | k+     | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2011]='../database/sidis/expdata/2011.xlsx'  # proton   | k+     | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2012]='../database/sidis/expdata/2012.xlsx'  # proton   | k-     | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2013]='../database/sidis/expdata/2013.xlsx'  # proton   | k-     | AUTsivers  | hermes     | x 
conf['datasets']['sidis']['xlsx'][2014]='../database/sidis/expdata/2014.xlsx'  # proton   | k-     | AUTsivers  | hermes     | z 
conf['datasets']['sidis']['xlsx'][2015]='../database/sidis/expdata/2015.xlsx'  # neutron  | pi+    | AUTsivers  | jlab       | x 
conf['datasets']['sidis']['xlsx'][2016]='../database/sidis/expdata/2016.xlsx'  # neutron  | pi-    | AUTsivers  | jlab       | x
##conf['datasets']['sidis']['xlsx'][2017]='../database/sidis/expdata/2017.xlsx'  # proton   | k0     | AUTsivers  | compass    | PT 
##conf['datasets']['sidis']['xlsx'][2018]='../database/sidis/expdata/2018.xlsx'  # proton   | k0     | AUTsivers  | compass    | x
##conf['datasets']['sidis']['xlsx'][2019]='../database/sidis/expdata/2019.xlsx'  # proton   | k0     | AUTsivers  | compass    | z
##conf['datasets']['sidis']['xlsx'][2020]='../database/sidis/expdata/2020.xlsx'  # proton   | h+     | AUTsivers  | compass    | PT
##conf['datasets']['sidis']['xlsx'][2021]='../database/sidis/expdata/2021.xlsx'  # proton   | h+     | AUTsivers  | compass    | x #
##conf['datasets']['sidis']['xlsx'][2022]='../database/sidis/expdata/2022.xlsx'  # proton   | h+     | AUTsivers  | compass    | z 
##conf['datasets']['sidis']['xlsx'][2023]='../database/sidis/expdata/2023.xlsx'  # proton   | h-     | AUTsivers  | compass    | PT 
##conf['datasets']['sidis']['xlsx'][2024]='../database/sidis/expdata/2024.xlsx'  # proton   | h-     | AUTsivers  | compass    | x
##conf['datasets']['sidis']['xlsx'][2025]='../database/sidis/expdata/2025.xlsx'  # proton   | h-     | AUTsivers  | compass    | z 
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
#conf['datasets']['sidis']['xlsx'][2040]='../database/sidis/expdata/2040.xlsx'  # proton   | h+     | AUTsivers  | compass    | PT (z>0.1 2040-2045) | 2017
#conf['datasets']['sidis']['xlsx'][2041]='../database/sidis/expdata/2041.xlsx'  # proton   | h+     | AUTsivers  | compass    | x #
#conf['datasets']['sidis']['xlsx'][2042]='../database/sidis/expdata/2042.xlsx'  # proton   | h+     | AUTsivers  | compass    | z 
#conf['datasets']['sidis']['xlsx'][2043]='../database/sidis/expdata/2043.xlsx'  # proton   | h-     | AUTsivers  | compass    | PT 
#conf['datasets']['sidis']['xlsx'][2044]='../database/sidis/expdata/2044.xlsx'  # proton   | h-     | AUTsivers  | compass    | x
#conf['datasets']['sidis']['xlsx'][2045]='../database/sidis/expdata/2045.xlsx'  # proton   | h-     | AUTsivers  | compass    | z 


for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 




