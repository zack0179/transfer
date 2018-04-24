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
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.69551926301538280484e-01>>,'fixed':True,'min':0,'max':10}
conf['params']['pdf']['widths0 sea']      = {'value':<<    9.35593184368213037772e-01>>,'fixed':True,'min':0,'max':10}

conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    2.09495986820052271238e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.93430515700360017295e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 h+ fav']   = {'value':<<    2.09495986820052271238e-01>>,'fixed':'widths0 pi+ fav','min':0,'max':1}
conf['params']['ff']['widths0 h+ unfav'] = {'value':<<    1.93430515700360017295e-01>>,'fixed':'widths0 pi+ unfav','min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    2.95033410728077538643e-01>>,'fixed':True,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.60639839770686576603e-01>>,'fixed':True,'min':0,'max':1}

conf['params']['sivers']={}
conf['params']['sivers']['widths0 valence'] = {'value':<<    1.34036675438694741214e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['sivers']['widths0 sea']     = {'value':<<    1.00000000000000008180e-05>>,'fixed':False,'min':1e-5,'max':2}

conf['params']['sivers']['u N']  = {'value':<<   -1.69552164792897752665e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['u a']  = {'value':<<   -7.73562379627252827419e-02>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['u b']  = {'value':<<    1.83915696576254994454e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['u c']  = {'value':<<   -1.94773229018291282877e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['d N']  = {'value':<<    1.83711529743710383356e-01>> ,'fixed':False,'min':-0.5,'max':0.5}
conf['params']['sivers']['d a']  = {'value':<<   -1.71895493647501562684e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['d b']  = {'value':<<    3.06964667218077735811e+00>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['d c']  = {'value':<<   -1.29253344082840904150e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['ub N']  = {'value':<<   -1.24992208724338769998e-02>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['ub a']  = {'value':<<    3.18951892632872491262e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['ub b']  = {'value':<<    7.64079970262786289936e-01>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['ub c']  = {'value':<<    1.56488779304495784217e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['ub d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['db N']  = {'value':<<   -8.08459217708248391310e-03>> ,'fixed':False,'min':-1,'max':1}
conf['params']['sivers']['db a']  = {'value':<<   -1.08149326788944066813e-01>> ,'fixed':False,'min':-1,'max':2}
conf['params']['sivers']['db b']  = {'value':<<    5.58163239378362874277e-01>> ,'fixed':False,'min':0,'max':25}
conf['params']['sivers']['db c']  = {'value':<<    9.05509770953299431007e-01>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['db d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['sb N']  = {'value':<<   -2.12255948374549495428e-02>> ,'fixed':False,'min':-30,'max':30}
conf['params']['sivers']['sb a']  = {'value':<<   -3.72562038880691837051e-01>> ,'fixed':False,'min':-1,'max':15}
conf['params']['sivers']['sb b']  = {'value':<<    3.50410383099806210794e-01>> ,'fixed':False,'min':1e-5,'max':30}
conf['params']['sivers']['sb c']  = {'value':<<   -1.32734791839451271578e+00>> ,'fixed':False,'min':-5,'max':5}
conf['params']['sivers']['sb d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-2,'max':2}

conf['params']['sivers']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':'sb N','min':-1,'max':1}
conf['params']['sivers']['s a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':'sb a','min':-1,'max':2}
conf['params']['sivers']['s b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':'sb b','min':0,'max':25}
conf['params']['sivers']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':'sb c','min':-5,'max':5}
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
#conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and (pT/z)**2<0.25*Q2" # rapidity Gunar wrote z< 0.2 and z>0.8 are padding bins
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
conf['datasets']['sidis']['xlsx'][2040]='../database/sidis/expdata/2040.xlsx'  # proton   | h+     | AUTsivers  | compass    | PT (z>0.1 2040-2045) | 2017
conf['datasets']['sidis']['xlsx'][2041]='../database/sidis/expdata/2041.xlsx'  # proton   | h+     | AUTsivers  | compass    | x #
conf['datasets']['sidis']['xlsx'][2042]='../database/sidis/expdata/2042.xlsx'  # proton   | h+     | AUTsivers  | compass    | z 
conf['datasets']['sidis']['xlsx'][2043]='../database/sidis/expdata/2043.xlsx'  # proton   | h-     | AUTsivers  | compass    | PT 
conf['datasets']['sidis']['xlsx'][2044]='../database/sidis/expdata/2044.xlsx'  # proton   | h-     | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2045]='../database/sidis/expdata/2045.xlsx'  # proton   | h-     | AUTsivers  | compass    | z 


for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 




