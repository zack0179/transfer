conf = {}

############################################################################
conf['method'] = 'cov'
conf['kappa'] = 1.1
conf['tol'] = 10e-4
conf['num points'] = 19 * 100
conf['burn size'] = 100
conf['sample size'] = 10000

############################################################################
# resouce allocation
conf['ncpus'] = 1


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
conf['params']['pdf']['widths0 valence']  = {'value': <<    5.89294556274006398056e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['pdf']['widths0 sea']      = {'value': <<    6.33443286558464269120e-01 >>, 'fixed': True, 'min': 0, 'max': 1}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.15920500644793311729e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.39782079427820671302e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    1.31266159597196507836e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    1.85599049505402902138e-01 >>, 'fixed': True, 'min': 0, 'max': 1}

conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {'value': <<    5.20436295422538663935e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['transversity']['widths0 sea']     = {'value': <<    4.00280935704888873872e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['transversity']['u N']  = {'value': <<    1.77397143330937034911e-01 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['u a']  = {'value': <<   -6.15129904278362005243e-02 >> , 'fixed': False, 'min': -1, 'max': 10}
conf['params']['transversity']['u b']  = {'value': <<    2.34714097335981364267e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['d N']  = {'value': <<   -2.41090368109697084087e-01 >> , 'fixed': False, 'min': -20, 'max': 20}
conf['params']['transversity']['d a']  = {'value': <<    6.69487009385128617467e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['d b']  = {'value': <<    8.15465962574718261635e-01 >> , 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['transversity']['s N']  = {'value': <<    2.24496057063511486596e-02 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['s a']  = {'value': <<   -5.73209824137443479941e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['s b']  = {'value': <<    9.41274131546565584472e-01 >> , 'fixed': False, 'min': 1e-5, 'max': 10}

conf['params']['transversity']['u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins'] = {}
conf['params']['collins']['widths0 pi+ fav']     = {'value': <<    5.74471362831243670399e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1}
conf['params']['collins']['widths0 pi+ unfav']   = {'value': <<    7.09717274473449233341e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['collins']['pi+ u N']  = {'value': <<    3.93873825870092275636e+00 >> , 'fixed': False, 'min': 0, 'max': 20}
conf['params']['collins']['pi+ u a']  = {'value': <<   -9.71154742613683730212e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ u b']  = {'value': <<    1.56892659654149380088e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['collins']['pi+ d N']  = {'value': <<   -3.33492280264958829150e+00 >> , 'fixed': False, 'min': -20, 'max': 0}
conf['params']['collins']['pi+ d a']  = {'value': <<   -9.26698817815867492698e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ d b']  = {'value': <<    1.63282947840754255608e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}

conf['params']['collins']['pi+ u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['widths0 k+ fav']     = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 1}
conf['params']['collins']['widths0 k+ unfav']   = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 2}
conf['params']['collins']['k+ u N']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -5, 'max': 20}
conf['params']['collins']['k+ u a']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['k+ u b']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['collins']['k+ d N']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 20}
conf['params']['collins']['k+ d a']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 10}
conf['params']['collins']['k+ d b']   = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 20}
conf['params']['collins']['k+ sb N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -20, 'max': 20}
conf['params']['collins']['k+ sb a']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['k+ sb b']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}

conf['params']['collins']['k+ u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ sb c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['k+ u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['k+ sb d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}


############################################################################
# set data sets

conf['datasets'] = {}

# SIDIS

conf['datasets']['sidis'] = {}

conf['datasets']['sidis']['filters'] = {}
conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [4001, 4000, 4002, 4004, 4003,
                                                  4005, 3027, 3025, 3010, 3012, 3005, 3013, 3026, 3000, 3003, 3016, 3004, 3018]
conf['datasets']['sidis']['filters'][0]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

conf['datasets']['sidis']['norm'] = {}
conf['datasets']['sidis']['xlsx'] = {}

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


for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
