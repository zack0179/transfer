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

############################################################################
# params
conf['basis'] = 'default'

conf['params'] = {}

conf['params']['pdf'] = {}
conf['params']['pdf']['widths0 valence']  = {'value': <<    5.75418353668222470887e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['pdf']['widths0 sea']      = {'value': <<    6.30535705061553208850e-01 >> , 'fixed': False, 'min': 0, 'max': 1}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.16464049998688312648e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.37029914868965041475e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    1.32408445477161240689e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    1.85490773695613619942e-01 >> , 'fixed': False, 'min': 0, 'max': 1}

############################################################################
# set data sets

conf['datasets'] = {}

# SIDIS

conf['datasets']['sidis'] = {}


conf['datasets']['sidis']['filters'] = {}
conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [
    1000, 1001, 1004, 1005, 1002, 1003, 1006, 1007]
# npts    = 978 chi2    = 1206.873681
conf['datasets']['sidis']['filters'][0]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

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

conf['datasets']['sidis']['norm'] = {}
for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
