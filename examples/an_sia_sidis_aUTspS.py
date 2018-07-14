conf = {}

conf['nprocs'] = 10

# mcsamp
conf['nruns'] = 1
conf['factor'] = 2
conf['tol'] = 1e-10
conf['itmax'] = int(1e7)
conf['block size'] = 100
conf['kappa'] = 1
conf['nll shift'] = 0

############################################################################
# params

conf['shape'] = 1

conf['evo'] = 'no'  # if 'no', set evo parameters to 'fixed':True
conf['Q02evo'] = 4.0
conf['lam2evo'] = 0.04

conf['params'] = {}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.24049999999999993605e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.43729999999999996652e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']   = {'value': <<    1.33839999999999986757e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav'] = {'value': <<    2.02660000000000006803e-01 >>, 'fixed': True, 'min': 0, 'max': 1}


conf['params']['collins'] = {}
conf['params']['collins']['widths0 pi+ fav']     = {'value': <<    7.34198999999999962762e-02 >>, 'fixed': True, 'min': 0.05, 'max': 0.15}
conf['params']['collins']['widths0 pi+ unfav']   = {'value': <<    1.10086000000000003296e-01 >>, 'fixed': True, 'min': 0.01, 'max': 0.15}
conf['params']['collins']['pi+ u N0 1']  = {'value': <<    8.34895000000000053753e-01 >>, 'fixed': True, 'min': 0.5, 'max': 1.2}
conf['params']['collins']['pi+ u a0 1']  = {'value': <<   -1.74327999999999994074e+00 >>, 'fixed': True, 'min': -2.5, 'max': 0}
conf['params']['collins']['pi+ u b0 1']  = {'value': <<    5.27420000000000044338e+00 >>, 'fixed': True, 'min': 3.0, 'max': 8.0}

conf['params']['collins']['pi+ d N0 1']  = {'value': <<   -3.67221000000000019625e+00 >>, 'fixed': True, 'min': -5, 'max': 0.0}
conf['params']['collins']['pi+ d a0 1']  = {'value': <<    1.07126000000000010104e+00 >> , 'fixed': True, 'min': 0.0, 'max': 3.0}
conf['params']['collins']['pi+ d b0 1']  = {'value': <<    3.47646999999999994913e+00 >>, 'fixed': True, 'min': 2.0, 'max': 6.0}

conf['params']['collins']['pi+ u c0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u N0 2']  = {'value': <<    1.30562000000000004718e+01 >>, 'fixed': True, 'min': 5.0, 'max': 20.0}
conf['params']['collins']['pi+ u a0 2']  = {'value': <<    6.15828000000000042036e+00 >>, 'fixed': True, 'min': 3.0, 'max': 10.0}
conf['params']['collins']['pi+ u b0 2']  = {'value': <<    3.15447999999999995069e+00 >>, 'fixed': True, 'min': 2.0, 'max': 5.0}

conf['params']['collins']['pi+ d N0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d a0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d b0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u c0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d0 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u N1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u a1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u b1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ d N1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d a1 1']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d b1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u c1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u N1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u a1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u b1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ d N1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d a1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d b1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u c1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d1 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}


conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {'value': <<    5.50345680361288502880e-01 >>, 'fixed': False, 'min': 0.5, 'max': 0.6}
conf['params']['transversity']['widths0 sea']     = {'value': <<    5.85061843485717658631e-01 >>, 'fixed': False, 'min': 0.5, 'max': 0.6}
conf['params']['transversity']['u N0']             = {'value': <<    1.18666555505933981607e+01 >> , 'fixed': False, 'min': 10.0, 'max': 15.0}
conf['params']['transversity']['u a0']             = {'value': <<    8.73769446704037888729e-01 >> , 'fixed': False, 'min': 0.8, 'max': 1.0}
conf['params']['transversity']['u b0']             = {'value': <<    4.00000000000000000000e+00 >> , 'fixed': False, 'min': 0.0, 'max': 4.0}
conf['params']['transversity']['d N0']             = {'value': <<   -1.26245077631693742859e+01 >> , 'fixed': False, 'min': -15.0, 'max': -10.0}
conf['params']['transversity']['d a0']             = {'value': <<    5.53128257832711023312e-01 >> , 'fixed': False, 'min': 0.4, 'max': 0.6}
conf['params']['transversity']['d b0']             = {'value': <<    4.61794646379189721586e+00 >> , 'fixed': False, 'min': 3.0, 'max': 8.0}
conf['params']['transversity']['s N0']             = {'value': <<   -6.36132605204942636057e-02 >> , 'fixed': False, 'min': -0.2, 'max': 0.2}
conf['params']['transversity']['s a0']             = {'value': <<    2.80348696471695912891e-01 >> , 'fixed': False, 'min': -0.3, 'max': 0.3}
conf['params']['transversity']['s b0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 0., 'max': 10}

conf['params']['transversity']['u c0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d c0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s c0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u d0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d0']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u N1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['u a1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['u b1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d N1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d a1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d b1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s N1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s a1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s b1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u c1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d c1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s c1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u d1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d1']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}


conf['params']['Htilde'] = {}
conf['params']['Htilde']['widths0 pi+ fav']     = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['Htilde']['widths0 pi+ unfav']   = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['Htilde']['pi+ u N0 1']  = {'value': <<   -3.77295018654073732733e+00 >>, 'fixed': False, 'min': -10.0, 'max': 0.0}
conf['params']['Htilde']['pi+ u a0 1']  = {'value': <<    3.88641141918057542171e+00 >>, 'fixed': False, 'min': -1.0, 'max': 5.0}
conf['params']['Htilde']['pi+ u b0 1']  = {'value': <<    3.95758967710698605913e+00 >>, 'fixed': False, 'min': 0.0, 'max': 8.0}

conf['params']['Htilde']['pi+ d N0 1']  = {'value': <<    4.63227549396215909638e+00 >>, 'fixed': False, 'min': 0.0, 'max': 10.0}
conf['params']['Htilde']['pi+ d a0 1']  = {'value': <<    2.70573558704474503855e+00 >> , 'fixed': False, 'min': -1.0, 'max': 8.0}
conf['params']['Htilde']['pi+ d b0 1']  = {'value': <<    2.14130848250342875616e+00 >>, 'fixed': False, 'min': 0.0, 'max': 8.0}

conf['params']['Htilde']['pi+ u c0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d c0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ u d0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d d0 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['Htilde']['pi+ u N1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ u a1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ u b1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['Htilde']['pi+ d N1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d a1 1']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d b1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['Htilde']['pi+ u c1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d c1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ u d1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d d1 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}


# conf['params']['Htilde']['pi+ u N 2']  = {'value':<<    1.03213181263992765935e+01>>,'fixed':False,'min':1,'max':52}
# conf['params']['Htilde']['pi+ u a 2']  = {'value':<<    5.96651357076961019743e+00>>,'fixed':False,'min':1,'max':20}
# conf['params']['Htilde']['pi+ u b 2']  = {'value':<<    4.15454650307243866791e+00>>,'fixed':False,'min':3,'max':25}
#
# conf['params']['Htilde']['pi+ d N 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-20,'max':0}
# conf['params']['Htilde']['pi+ d a 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-1,'max':5}
# conf['params']['Htilde']['pi+ d b 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':1e-5,'max':10}
# conf['params']['Htilde']['pi+ u c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
# conf['params']['Htilde']['pi+ d c 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
# conf['params']['Htilde']['pi+ u d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}
# conf['params']['Htilde']['pi+ d d 2']  = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':-10,'max':10}


############################################################################
# set data sets

conf['datasets'] = {}

# SIA

conf['datasets']['sia'] = {}


conf['datasets']['sia']['norm'] = {}

conf['datasets']['sia']['filters'] = []  # npts    = 122 chi2    = 69.799935
# conf['datasets']['sia']['filters'].append("z<0.6")
# conf['datasets']['sia']['filters'].append("Q2>1.69")
#conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.9")


conf['datasets']['sia']['xlsx'] = {}

# babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1000] = 'sia/expdata/1000.xlsx'
# babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001] = 'sia/expdata/1001.xlsx'
# babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1002] = 'sia/expdata/1002.xlsx'
# babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003] = 'sia/expdata/1003.xlsx'
# belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1004] = 'sia/expdata/1004.xlsx'
# belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005] = 'sia/expdata/1005.xlsx'
# | babar      | pi,pi | AUL-0            | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2008] = 'sia/expdata/2008.xlsx'
# | babar      | pi,pi | AUC-0            | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009] = 'sia/expdata/2009.xlsx'

# Collins and AUTsinphiS SIDIS

conf['datasets']['sidis'] = {}
conf['datasets']['sidis']['norm'] = {}
conf['datasets']['sidis']['xlsx'] = {}
conf['datasets']['sidis']['filters'] = {}

conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [4001, 4000, 4002, 4004, 4003, 4005, 3027,
                                                  3025, 3010, 3012, 3005, 3013, 3026, 3000, 3003, 3016, 3004, 3018, 9011, 9022, 9033, 9044]
conf['datasets']['sidis']['filters'][0]['filter'] = "z>0.2 and z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

# conf["datasets"]["sidis"]["xlsx"][4007]="../database/sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
# conf["datasets"]["sidis"]["xlsx"][4006]="../database/sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
# conf["datasets"]["sidis"]["xlsx"][4008]="../database/sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
# conf["datasets"]["sidis"]["xlsx"][4010]="../database/sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
# conf["datasets"]["sidis"]["xlsx"][4009]="../database/sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
# conf["datasets"]["sidis"]["xlsx"][4011]="../database/sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
# compass  deuteron  pi+   pT
conf["datasets"]["sidis"]["xlsx"][4001] = "sidis/expdata/4001.xlsx"
# compass  deuteron  pi+    x
conf["datasets"]["sidis"]["xlsx"][4000] = "sidis/expdata/4000.xlsx"
# compass  deuteron  pi+    z
conf["datasets"]["sidis"]["xlsx"][4002] = "sidis/expdata/4002.xlsx"
# compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4004] = "sidis/expdata/4004.xlsx"
# compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4003] = "sidis/expdata/4003.xlsx"
# compass  deuteron  pi-    z
conf["datasets"]["sidis"]["xlsx"][4005] = "sidis/expdata/4005.xlsx"
# conf["datasets"]["sidis"]["xlsx"][6003]="../database/sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
# conf["datasets"]["sidis"]["xlsx"][6004]="../database/sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
# conf["datasets"]["sidis"]["xlsx"][6005]="../database/sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
# conf["datasets"]["sidis"]["xlsx"][6000]="../database/sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
# conf["datasets"]["sidis"]["xlsx"][6001]="../database/sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
# conf["datasets"]["sidis"]["xlsx"][6002]="../database/sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
# compass    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3027] = "sidis/expdata/3027.xlsx"
# compass    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3025] = "sidis/expdata/3025.xlsx"
# compass    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3010] = "sidis/expdata/3010.xlsx"
# compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3012] = "sidis/expdata/3012.xlsx"
# compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3005] = "sidis/expdata/3005.xlsx"
# compass    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3013] = "sidis/expdata/3013.xlsx"
# conf["datasets"]["sidis"]["xlsx"][3024]="../database/sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
# conf["datasets"]["sidis"]["xlsx"][3007]="../database/sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
# conf["datasets"]["sidis"]["xlsx"][3008]="../database/sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
# conf["datasets"]["sidis"]["xlsx"][3021]="../database/sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
# conf["datasets"]["sidis"]["xlsx"][3017]="../database/sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
# conf["datasets"]["sidis"]["xlsx"][3023]="../database/sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
# HERMES    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3026] = "sidis/expdata/3026.xlsx"
# HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3000] = "sidis/expdata/3000.xlsx"
# HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3003] = "sidis/expdata/3003.xlsx"
# HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3016] = "sidis/expdata/3016.xlsx"
# HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3004] = "sidis/expdata/3004.xlsx"
# HERMES    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3018] = "sidis/expdata/3018.xlsx"

# COMPASS    proton  h+    z
conf["datasets"]["sidis"]["xlsx"][9011] = "sidis/expdata/9011.xlsx"
# COMPASS    proton  h-    z
conf["datasets"]["sidis"]["xlsx"][9022] = "sidis/expdata/9022.xlsx"
# COMPASS    proton  h+    x
conf["datasets"]["sidis"]["xlsx"][9033] = "sidis/expdata/9033.xlsx"
# COMPASS    proton  h-    x
conf["datasets"]["sidis"]["xlsx"][9044] = "sidis/expdata/9044.xlsx"

# AN

conf['datasets']['AN'] = {}


conf['datasets']['AN']['norm'] = {}

conf['datasets']['AN']['filters'] = []


conf['datasets']['AN']['xlsx'] = {}

conf['datasets']['AN']['xlsx'][1000] = 'AN_pp/expdata/1000.xlsx'  # BRAHMS pim 2.3
conf['datasets']['AN']['xlsx'][1001] = 'AN_pp/expdata/1001.xlsx'  # BRAHMS pim 4
conf['datasets']['AN']['xlsx'][1002] = 'AN_pp/expdata/1002.xlsx'  # BRAHMS pip 2.3
conf['datasets']['AN']['xlsx'][1003] = 'AN_pp/expdata/1003.xlsx'  # BRAHMS pip 4
conf['datasets']['AN']['xlsx'][2000] = 'AN_pp/expdata/2000.xlsx'  # STAR piz 04
conf['datasets']['AN']['xlsx'][2001] = 'AN_pp/expdata/2001.xlsx'  # STAR piz 3.3
conf['datasets']['AN']['xlsx'][2002] = 'AN_pp/expdata/2002.xlsx'  # STAR piz 3.68
conf['datasets']['AN']['xlsx'][2003] = 'AN_pp/expdata/2003.xlsx'  # STAR piz 3.7

for k in conf['datasets']['sia']['xlsx']:
    conf['datasets']['sia']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
for k in conf['datasets']['AN']['xlsx']:
    conf['datasets']['AN']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
