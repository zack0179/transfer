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
conf['params']['transversity']['widths0 valence'] = {'value':<<    2.55415159149558479434e-02>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['widths0 sea']     = {'value':<<    1.00000000000100008890e-05>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['transversity']['u N']  = {'value':<<    9.91116095642410543931e-01>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['u a']  = {'value':<<    3.04593481957941669691e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['transversity']['u b']  = {'value':<<    9.59479919259112357111e-01>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['transversity']['d N']  = {'value':<<   -1.01683585986255353717e+00>> ,'fixed':False,'min':-20,'max':20}
conf['params']['transversity']['d a']  = {'value':<<   -2.64455778963504695156e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['d b']  = {'value':<<    1.39167175388266173286e-02>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['transversity']['s N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['s a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['transversity']['s b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':1e-5,'max':10}

conf['params']['transversity']['u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['transversity']['s c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}

conf['params']['transversity']['u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['transversity']['s d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']={}
conf['params']['collins']['widths0 pi+ fav']     = {'value':<<    1.65034602577130262713e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value':<<    1.05829785928662545302e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['pi+ u N']  = {'value':<<    9.21904004250079123217e-01>> ,'fixed':False,'min':0,'max':20}
conf['params']['collins']['pi+ u a']  = {'value':<<   -1.00000000000000000000e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ u b']  = {'value':<<    3.04109507336040163494e+00>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['pi+ d N']  = {'value':<<   -2.22324663044086656694e-01>> ,'fixed':False,'min':-20,'max':0}
conf['params']['collins']['pi+ d a']  = {'value':<<   -9.99724621802289270533e-01>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['pi+ d b']  = {'value':<<    1.30102971560926894412e+00>> ,'fixed':False,'min':1e-5,'max':10}

conf['params']['collins']['pi+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['pi+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}

conf['params']['collins']['pi+ u d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}
conf['params']['collins']['pi+ d d']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':True,'min':-10,'max':10}

conf['params']['collins']['widths0 k+ fav']     = {'value':<<    1.79134333518971178290e-01>>,'fixed':False,'min':1e-5,'max':1}
conf['params']['collins']['widths0 k+ unfav']   = {'value':<<    2.51796371609382230172e-01>>,'fixed':False,'min':1e-5,'max':2}
conf['params']['collins']['k+ u N']  = {'value':<<    2.49420253053134821641e+00>> ,'fixed':False,'min':-5,'max':20}
conf['params']['collins']['k+ u a']  = {'value':<<   -9.46328421494753158072e-02>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ u b']  = {'value':<<    1.00000000000000008180e-05>> ,'fixed':False,'min':1e-5,'max':10}
conf['params']['collins']['k+ d N']  = {'value':<<   -4.57665726638100817114e-02>> ,'fixed':False,'min':-10,'max':20}
conf['params']['collins']['k+ d a']  = {'value':<<   -7.96368735991260567886e-01>> ,'fixed':False,'min':-1,'max':10}
conf['params']['collins']['k+ d b']  = {'value':<<    1.68910849832908738222e+00>> ,'fixed':False,'min':1e-5,'max':20}
conf['params']['collins']['k+ sb N']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-20,'max':20}
conf['params']['collins']['k+ sb a']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-1,'max':5}
conf['params']['collins']['k+ sb b']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':1e-5,'max':10}

conf['params']['collins']['k+ u c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ d c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}
conf['params']['collins']['k+ sb c']  = {'value':<<    0.00000000000000000000e+00>> ,'fixed':False,'min':-10,'max':10}

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

conf['datasets']['sidis']['xlsx'][3000]='../database/sidis/expdata/3000.xlsx' # proton   | pi+ | AUTcollins | hermes  | x
conf['datasets']['sidis']['xlsx'][3003]='../database/sidis/expdata/3003.xlsx' # proton   | pi+ | AUTcollins | hermes  | z
conf['datasets']['sidis']['xlsx'][3026]='../database/sidis/expdata/3026.xlsx' # proton   | pi+ | AUTcollins | hermes  | pt
conf['datasets']['sidis']['xlsx'][3004]='../database/sidis/expdata/3004.xlsx' # proton   | pi- | AUTcollins | hermes  | x
conf['datasets']['sidis']['xlsx'][3018]='../database/sidis/expdata/3018.xlsx' # proton   | pi- | AUTcollins | hermes  | z
conf['datasets']['sidis']['xlsx'][3016]='../database/sidis/expdata/3016.xlsx' # proton   | pi- | AUTcollins | hermes  | pt

conf['datasets']['sidis']['xlsx'][3025]='../database/sidis/expdata/3025.xlsx' # proton   | pi+ | AUTcollins | compass | x
conf['datasets']['sidis']['xlsx'][3010]='../database/sidis/expdata/3010.xlsx' # proton   | pi+ | AUTcollins | compass | z
conf['datasets']['sidis']['xlsx'][3027]='../database/sidis/expdata/3027.xlsx' # proton   | pi+ | AUTcollins | compass | pt
conf['datasets']['sidis']['xlsx'][3005]='../database/sidis/expdata/3005.xlsx' # proton   | pi- | AUTcollins | compass | x
conf['datasets']['sidis']['xlsx'][3012]='../database/sidis/expdata/3012.xlsx' # proton   | pi- | AUTcollins | compass | pt
conf['datasets']['sidis']['xlsx'][3013]='../database/sidis/expdata/3013.xlsx' # proton   | pi- | AUTcollins | compass | z

conf['datasets']['sidis']['xlsx'][4000]='../database/sidis/expdata/4000.xlsx' # deuteron | pi+ | AUTcollins | compass | x
conf['datasets']['sidis']['xlsx'][4001]='../database/sidis/expdata/4001.xlsx' # deuteron | pi+ | AUTcollins | compass | pt
conf['datasets']['sidis']['xlsx'][4002]='../database/sidis/expdata/4002.xlsx' # deuteron | pi+ | AUTcollins | compass | z
conf['datasets']['sidis']['xlsx'][4003]='../database/sidis/expdata/4003.xlsx' # deuteron | pi- | AUTcollins | compass | x
conf['datasets']['sidis']['xlsx'][4004]='../database/sidis/expdata/4004.xlsx' # deuteron | pi- | AUTcollins | compass | pt
conf['datasets']['sidis']['xlsx'][4005]='../database/sidis/expdata/4005.xlsx' # deuteron | pi- | AUTcollins | compass | z

conf['datasets']['sidis']['xlsx'][3007]='../database/sidis/expdata/3007.xlsx' # proton   | k+  | AUTcollins | hermes  | x  
conf['datasets']['sidis']['xlsx'][3008]='../database/sidis/expdata/3008.xlsx' # proton   | k+  | AUTcollins | hermes  | z  
conf['datasets']['sidis']['xlsx'][3024]='../database/sidis/expdata/3024.xlsx' # proton   | k+  | AUTcollins | hermes  | pt 
conf['datasets']['sidis']['xlsx'][3017]='../database/sidis/expdata/3017.xlsx' # proton   | k-  | AUTcollins | hermes  | x  
conf['datasets']['sidis']['xlsx'][3021]='../database/sidis/expdata/3021.xlsx' # proton   | k-  | AUTcollins | hermes  | pt 
conf['datasets']['sidis']['xlsx'][3023]='../database/sidis/expdata/3023.xlsx' # proton   | k-  | AUTcollins | hermes  | z  

conf['datasets']['sidis']['xlsx'][4006]='../database/sidis/expdata/4006.xlsx' # proton   | k+  | AUTcollins | hermes  | x  
conf['datasets']['sidis']['xlsx'][4008]='../database/sidis/expdata/4008.xlsx' # proton   | k+  | AUTcollins | hermes  | z  
conf['datasets']['sidis']['xlsx'][4007]='../database/sidis/expdata/4007.xlsx' # proton   | k+  | AUTcollins | hermes  | pt 
conf['datasets']['sidis']['xlsx'][4009]='../database/sidis/expdata/4009.xlsx' # proton   | k-  | AUTcollins | hermes  | x  
conf['datasets']['sidis']['xlsx'][4011]='../database/sidis/expdata/4011.xlsx' # proton   | k-  | AUTcollins | hermes  | z  
conf['datasets']['sidis']['xlsx'][4010]='../database/sidis/expdata/4010.xlsx' # proton   | k-  | AUTcollins | hermes  | pt 

for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 




