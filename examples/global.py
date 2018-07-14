conf = {}

############################################################################
# resouce allocation

conf['ncpus'] = 1

############################################################################
# maxlike setup

conf['screen mode'] = 'plain'
#conf['screen mode']='curses'

############################################################################
# mcsetup

conf['method'] = 'kde'
conf['itmax'] = None
conf['tol'] = 1e-6
conf['kde bw'] = None
conf['num points factor'] = 10


############################################################################
# paths to external

conf['path2CJ'] = '../external/CJLIB'
conf['path2LSS'] = '../external/LSSLIB'
conf['path2DSS'] = '../external/DSSLIB'

############################################################################
# params
conf['shape'] = 0

conf['params'] = {}

conf['params']['pdf'] = {}
conf['params']['pdf']['widths0 valence']  = {'value': <<    5.76958369982397800690e-01 >>, 'fixed': False, 'min': 0, 'max': 1}
conf['params']['pdf']['widths0 sea']      = {'value': <<    6.31374523193443559776e-01 >>, 'fixed': False, 'min': 0, 'max': 1}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.16158979479843646465e-01 >>, 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.37324054423742403230e-01 >>, 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    1.32305559831921548675e-01 >>, 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    1.85464770006172063876e-01 >>, 'fixed': False, 'min': 0, 'max': 1}


conf['params']['sivers'] = {}
conf['params']['sivers']['widths0 valence'] = {'value': <<    4.49833744155398729259e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['sivers']['widths0 sea']     = {'value': <<    3.88407094276222220053e-01 >>, 'fixed': True, 'min': 1e-5, 'max': 2}

conf['params']['sivers']['u N']   = {'value': <<   -1.44002327865379059491e-01 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['sivers']['u a']   = {'value': <<   -3.22611717013585042046e-01 >> , 'fixed': False, 'min': -1, 'max': 10}
conf['params']['sivers']['u b']   = {'value': <<    2.50140617485588467872e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['sivers']['u c']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['u d']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['sivers']['d N']   = {'value': <<    3.31954662533302136129e-01 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['sivers']['d a']   = {'value': <<   -4.93669463785545367673e-02 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['sivers']['d b']   = {'value': <<    3.66714686996533245633e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['sivers']['d c']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['d d']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['sivers']['s N']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['s a']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['sivers']['s b']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['sivers']['s c']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['s d']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['sivers']['ub N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['ub a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['sivers']['ub b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['sivers']['ub c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['ub d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['sivers']['db N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['db a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['sivers']['db b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['sivers']['db c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['db d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['sivers']['sb N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['sb a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['sivers']['sb b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['sivers']['sb c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['sivers']['sb d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}


conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {'value': <<    1.14087161821951665885e+00 >>, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['transversity']['widths0 sea']     = {'value': <<    8.08598292899885162655e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 2}

conf['params']['transversity']['u N']  = {'value': <<    8.81656925150748893572e-02 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['u a']  = {'value': <<   -6.65739794911139881606e-02 >> , 'fixed': False, 'min': -1, 'max': 10}
conf['params']['transversity']['u b']  = {'value': <<    3.72981828855215535867e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['d N']  = {'value': <<   -4.71948437062817471865e-01 >> , 'fixed': False, 'min': -20, 'max': 20}
conf['params']['transversity']['d a']  = {'value': <<    8.48639340206871928274e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['d b']  = {'value': <<    1.74425429631759820737e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['transversity']['d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['s N']  = {'value': <<    8.65762657154642810420e-03 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['s a']  = {'value': <<   -6.69439350505441121975e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['s b']  = {'value': <<    7.08478874710872474907e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['s c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins'] = {}
conf['params']['collins']['widths0 pi+ fav']     = {'value': <<    1.64142320809162954825e-05 >>, 'fixed': False, 'min': 1e-5, 'max': 1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value': <<    2.89507283268815099331e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 2}

conf['params']['collins']['pi+ u N']  = {'value': <<    4.77874337230863410753e+00 >> , 'fixed': False, 'min': 0, 'max': 20}
conf['params']['collins']['pi+ u a']  = {'value': <<   -9.92237685314148021298e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ u b']  = {'value': <<    5.36612402107576547117e-01 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['collins']['pi+ u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ d N']  = {'value': <<   -3.44315526665336069101e+00 >> , 'fixed': False, 'min': -20, 'max': 0}
conf['params']['collins']['pi+ d a']  = {'value': <<   -1.00665757191093918621e+00 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ d b']  = {'value': <<    2.54884985297969712814e-01 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['collins']['pi+ d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['widths0 k+ fav']     = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 1}
conf['params']['collins']['widths0 k+ unfav']   = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 2}

conf['params']['collins']['k+ u N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -5, 'max': 20}
conf['params']['collins']['k+ u a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['k+ u b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['collins']['k+ u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['k+ d N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 20}
conf['params']['collins']['k+ d a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 10}
conf['params']['collins']['k+ d b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 20}
conf['params']['collins']['k+ d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['k+ sb N'] = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -20, 'max': 20}
conf['params']['collins']['k+ sb a'] = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['k+ sb b'] = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['collins']['k+ sb c'] = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ sb d'] = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}


############################################################################
# set data sets

conf['datasets'] = {}

# SIDIS

conf['datasets']['sidis'] = {}
conf['datasets']['sidis']['norm'] = {}
conf['datasets']['sidis']['filters'] = {}
conf['datasets']['sidis']['xlsx'] = {}


# |  proton   | pi+    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1000] = '../database/sidis/expdata/1000.xlsx'
# |  proton   | pi-    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1001] = '../database/sidis/expdata/1001.xlsx'
# |  deuteron | pi+    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1004] = '../database/sidis/expdata/1004.xlsx'
# |  deuteron | pi-    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1005] = '../database/sidis/expdata/1005.xlsx'
# |  proton   | k+    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1002] = '../database/sidis/expdata/1002.xlsx'
# |  proton   | k-    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1003] = '../database/sidis/expdata/1003.xlsx'
# |  deuteron | k+    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1006] = '../database/sidis/expdata/1006.xlsx'
# |  deuteron | k-    | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1007] = '../database/sidis/expdata/1007.xlsx'
conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [
    1000, 1001, 1004, 1005, 1002, 1003, 1006, 1007]
conf['datasets']['sidis']['filters'][0]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"


# proton   | pi+    | AUTsivers  | hermes     | PT
conf["datasets"]["sidis"]["xlsx"][2000] = "../database/sidis/expdata/2000.xlsx"
# proton   | pi+    | AUTsivers  | hermes     | x
conf["datasets"]["sidis"]["xlsx"][2001] = "../database/sidis/expdata/2001.xlsx"
# proton   | pi+    | AUTsivers  | hermes     | z
conf["datasets"]["sidis"]["xlsx"][2002] = "../database/sidis/expdata/2002.xlsx"
# proton   | pi-    | AUTsivers  | hermes     | PT
conf["datasets"]["sidis"]["xlsx"][2003] = "../database/sidis/expdata/2003.xlsx"
# proton   | pi-    | AUTsivers  | hermes     | x
conf["datasets"]["sidis"]["xlsx"][2004] = "../database/sidis/expdata/2004.xlsx"
# proton   | pi-    | AUTsivers  | hermes     | z
conf["datasets"]["sidis"]["xlsx"][2005] = "../database/sidis/expdata/2005.xlsx"
# deuteron | pi+    | AUTsivers  | compass    | PT
conf["datasets"]["sidis"]["xlsx"][2026] = "../database/sidis/expdata/2026.xlsx"
# deuteron | pi+    | AUTsivers  | compass    | x
conf["datasets"]["sidis"]["xlsx"][2027] = "../database/sidis/expdata/2027.xlsx"
# deuteron | pi+    | AUTsivers  | compass    | z
conf["datasets"]["sidis"]["xlsx"][2028] = "../database/sidis/expdata/2028.xlsx"
# deuteron | pi-    | AUTsivers  | compass    | PT
conf["datasets"]["sidis"]["xlsx"][2029] = "../database/sidis/expdata/2029.xlsx"
# deuteron | pi-    | AUTsivers  | compass    | x
conf["datasets"]["sidis"]["xlsx"][2030] = "../database/sidis/expdata/2030.xlsx"
# deuteron | pi-    | AUTsivers  | compass    | z
conf["datasets"]["sidis"]["xlsx"][2031] = "../database/sidis/expdata/2031.xlsx"
conf['datasets']['sidis']['filters'][1] = {}
conf['datasets']['sidis']['filters'][1]['idx'] = [2000, 2001,
                                                  2002, 2003, 2004, 2005, 2026, 2027, 2028, 2029, 2030, 2031]
conf['datasets']['sidis']['filters'][1]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"


# compass  deuteron  pi+   pT
conf["datasets"]["sidis"]["xlsx"][4001] = "../database/sidis/expdata/4001.xlsx"
# compass  deuteron  pi+    x
conf["datasets"]["sidis"]["xlsx"][4000] = "../database/sidis/expdata/4000.xlsx"
# compass  deuteron  pi+    z
conf["datasets"]["sidis"]["xlsx"][4002] = "../database/sidis/expdata/4002.xlsx"
# compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4004] = "../database/sidis/expdata/4004.xlsx"
# compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4003] = "../database/sidis/expdata/4003.xlsx"
# compass  deuteron  pi-    z
conf["datasets"]["sidis"]["xlsx"][4005] = "../database/sidis/expdata/4005.xlsx"
# compass    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3027] = "../database/sidis/expdata/3027.xlsx"
# compass    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3025] = "../database/sidis/expdata/3025.xlsx"
# compass    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3010] = "../database/sidis/expdata/3010.xlsx"
# compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3012] = "../database/sidis/expdata/3012.xlsx"
# compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3005] = "../database/sidis/expdata/3005.xlsx"
# compass    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3013] = "../database/sidis/expdata/3013.xlsx"
# HERMES    proton  pi+   pt
conf["datasets"]["sidis"]["xlsx"][3026] = "../database/sidis/expdata/3026.xlsx"
# HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][3000] = "../database/sidis/expdata/3000.xlsx"
# HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][3003] = "../database/sidis/expdata/3003.xlsx"
# HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3016] = "../database/sidis/expdata/3016.xlsx"
# HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3004] = "../database/sidis/expdata/3004.xlsx"
# HERMES    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3018] = "../database/sidis/expdata/3018.xlsx"
conf['datasets']['sidis']['filters'][2] = {}
conf['datasets']['sidis']['filters'][2]['idx'] = [4001, 4000, 4002, 4004, 4003,
                                                  4005, 3027, 3025, 3010, 3012, 3005, 3013, 3026, 3000, 3003, 3016, 3004, 3018]
conf['datasets']['sidis']['filters'][2]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"


for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
