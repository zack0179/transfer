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

conf['basis'] = 'valence'


conf['params'] = {}

conf['params']['pdf'] = {}
conf['params']['pdf']['widths0 uv']  = {'value': <<    3.34505080233146512292e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['pdf']['widths0 dv']  = {'value': <<    2.99513300773295298995e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['pdf']['widths0 sea']      = {'value': <<    5.04162404339218328531e-01 >> , 'fixed': False, 'min': 0, 'max': 1}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.90400601369301369914e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.82711215654428660304e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    2.22986039557757642626e-01 >> , 'fixed': False, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    1.21274633282052901606e-01 >> , 'fixed': False, 'min': 0, 'max': 1}


############################################################################
# set data sets

conf['datasets'] = {}

# SIDIS

conf['datasets']['sidis'] = {}


conf['datasets']['sidis']['filters'] = {}
conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [
    1000, 1001, 1004, 1005, 1002, 1003, 1006, 1007]
# conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9" # npts    = 978 chi2    = 1078.146278
# conf['datasets']['sidis']['filters'][0]['filter']="z>0.2 and z<0.6 and Q2>1.69 and (pT/z)**2<0.25*Q2" # rapidity Gunar wrote z< 0.2 and z>0.8 are padding bins
#conf['datasets']['sidis']['filters'][0]['filter']="Q2>1.69 and z>0.2 and z<0.6 and pT>0.2 and pT<0.9"
conf['datasets']['sidis']['filters'][0][
    'filter'] = "z>0.2 and z<0.6 and Q2>1.69 and (pT/z)**2<0.25*Q2 and dy>2."


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
