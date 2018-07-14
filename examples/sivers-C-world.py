conf = {}

############################################################################
conf['method'] = 'cov'
conf['kappa'] = 1.4
conf['tol'] = 0.8e-4
conf['num points'] = 100
conf['burn size'] = 500
conf['sample size'] = 10000

############################################################################
# resouce allocation

conf['ncpus'] = 4

############################################################################
# paths to external

conf['path2CJ'] = '../external/CJLIB'
conf['path2LSS'] = '../external/LSSLIB'
conf['path2DSS'] = '../external/DSSLIB'

############################################################################
# params
conf['shape'] = 1

conf['params'] = {}

conf['params']['pdf'] = {}
conf['params']['pdf']['widths0 valence']  = {'value': <<    6.03670446947477734589e-01 >> , 'fixed': False, 'min': 0.45, 'max': 0.75}
conf['params']['pdf']['widths0 sea']      = {'value': <<    6.38997454166326361857e-01 >> , 'fixed': False, 'min': 0.3, 'max': 1}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.14520495314371806295e-01 >> , 'fixed': False, 'min': 0.07, 'max': 0.17}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.39465134298549620073e-01 >> , 'fixed': False, 'min': 0.1, 'max': 0.2}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    1.31266159597196507836e-01 >> , 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    1.85599049505402902138e-01 >> , 'fixed': True, 'min': 0, 'max': 1}

conf['params']['sivers'] = {}
conf['params']['sivers']['widths0 valence'] = {'value': << 0.5 >> , 'fixed': False, 'min': 1e-5, 'max': 1}
conf['params']['sivers']['widths0 sea']     = {'value': << 0.5 >> , 'fixed': False, 'min': 1e-5, 'max': 2}

conf['params']['sivers']['u N']  = {'value': << 0 >>, 'fixed': False, 'min': -0.5, 'max': 0.5}
conf['params']['sivers']['u a']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 2}
conf['params']['sivers']['u b']  = {'value': << 0 >>, 'fixed': False, 'min': 0, 'max': 25}
conf['params']['sivers']['u c']  = {'value': << 0 >>, 'fixed': False, 'min': -5, 'max': 5}
conf['params']['sivers']['u d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}

conf['params']['sivers']['d N']  = {'value': << 0 >>, 'fixed': False, 'min': -0.5, 'max': 0.5}
conf['params']['sivers']['d a']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 2}
conf['params']['sivers']['d b']  = {'value': << 0 >>, 'fixed': False, 'min': 0, 'max': 25}
conf['params']['sivers']['d c']  = {'value': << 0 >>, 'fixed': False, 'min': -5, 'max': 5}
conf['params']['sivers']['d d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}

conf['params']['sivers']['s N']  = {'value': << 0 >>, 'fixed': True, 'min': -1, 'max': 1}
conf['params']['sivers']['s a']  = {'value': << 0 >>, 'fixed': True, 'min': -1, 'max': 2}
conf['params']['sivers']['s b']  = {'value': << 0 >>, 'fixed': True, 'min': 0, 'max': 25}
conf['params']['sivers']['s c']  = {'value': << 0 >>, 'fixed': True, 'min': -5, 'max': 5}
conf['params']['sivers']['s d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}

conf['params']['sivers']['ub N']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 1}
conf['params']['sivers']['ub a']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 2}
conf['params']['sivers']['ub b']  = {'value': << 0 >>, 'fixed': False, 'min': 0, 'max': 25}
conf['params']['sivers']['ub c']  = {'value': << 0 >>, 'fixed': False, 'min': -5, 'max': 5}
conf['params']['sivers']['ub d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}

conf['params']['sivers']['db N']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 1}
conf['params']['sivers']['db a']  = {'value': << 0 >>, 'fixed': False, 'min': -1, 'max': 2}
conf['params']['sivers']['db b']  = {'value': << 0 >>, 'fixed': False, 'min': 0, 'max': 25}
conf['params']['sivers']['db c']  = {'value': << 0 >>, 'fixed': False, 'min': -5, 'max': 5}
conf['params']['sivers']['db d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}

conf['params']['sivers']['sb N']  = {'value': << 0 >>, 'fixed': True, 'min': -30, 'max': 30}
conf['params']['sivers']['sb a']  = {'value': << 0 >>, 'fixed': True, 'min': -1, 'max': 15}
conf['params']['sivers']['sb b']  = {'value': << 0 >>, 'fixed': True, 'min': 1e-5, 'max': 30}
conf['params']['sivers']['sb c']  = {'value': << 0 >>, 'fixed': True, 'min': -5, 'max': 5}
conf['params']['sivers']['sb d']  = {'value': << 0 >>, 'fixed': True, 'min': -2, 'max': 2}


############################################################################
# set data sets

conf['datasets'] = {}

# SIDIS

conf['datasets']['sidis'] = {}


conf['datasets']['sidis']['norm'] = {}

conf['datasets']['sidis']['filters'] = {}
conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = range(1000, 2000)
conf['datasets']['sidis']['filters'][0]['filter'] = "Q2>1.69 and z<0.6 and pT>0.2 and pT<0.9"

conf['datasets']['sidis']['filters'][1] = {}
conf['datasets']['sidis']['filters'][1]['idx'] = range(2000, 2500)
conf['datasets']['sidis']['filters'][1]['filter'] = "Q2>1.0 and z<0.7 and pT<0.9"

conf['datasets']['sidis']['xlsx'] = {}

# proton   | pi+ | M_Hermes   | hermes
conf['datasets']['sidis']['xlsx'][1000] = '../database/sidis/expdata/1000.xlsx'
# proton   | pi- | M_Hermes   | hermes
conf['datasets']['sidis']['xlsx'][1001] = '../database/sidis/expdata/1001.xlsx'
# deuteron | pi+ | M_Hermes   | hermes
conf['datasets']['sidis']['xlsx'][1004] = '../database/sidis/expdata/1004.xlsx'
# deuteron | pi- | M_Hermes   | hermes
conf['datasets']['sidis']['xlsx'][1005] = '../database/sidis/expdata/1005.xlsx'
#
# conf['datasets']['sidis']['xlsx'][1002]='../database/sidis/expdata/1002.xlsx' # proton   | k+  | M_Hermes   | hermes
# conf['datasets']['sidis']['xlsx'][1003]='../database/sidis/expdata/1003.xlsx' # proton   | k-  | M_Hermes   | hermes
# conf['datasets']['sidis']['xlsx'][1006]='../database/sidis/expdata/1006.xlsx' # deuteron | k+  | M_Hermes   | hermes
# conf['datasets']['sidis']['xlsx'][1007]='../database/sidis/expdata/1007.xlsx' # deuteron | k-  | M_Hermes   | hermes


# proton   | pi+    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2000] = '../database/sidis/expdata/2000.xlsx'
# proton   | pi+    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2001] = '../database/sidis/expdata/2001.xlsx'
# proton   | pi+    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2002] = '../database/sidis/expdata/2002.xlsx'
# proton   | pi-    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2003] = '../database/sidis/expdata/2003.xlsx'
# proton   | pi-    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2004] = '../database/sidis/expdata/2004.xlsx'
# proton   | pi-    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2005] = '../database/sidis/expdata/2005.xlsx'
# conf['datasets']['sidis']['xlsx'][2006]='../database/sidis/expdata/2006.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | PT
# conf['datasets']['sidis']['xlsx'][2007]='../database/sidis/expdata/2007.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | x
# conf['datasets']['sidis']['xlsx'][2008]='../database/sidis/expdata/2008.xlsx'  # proton   | pi0    | AUTsivers  | hermes     | z
# conf['datasets']['sidis']['xlsx'][2009]='../database/sidis/expdata/2009.xlsx'  # proton   | k+     | AUTsivers  | hermes     | PT
# conf['datasets']['sidis']['xlsx'][2010]='../database/sidis/expdata/2010.xlsx'  # proton   | k+     | AUTsivers  | hermes     | x
# conf['datasets']['sidis']['xlsx'][2011]='../database/sidis/expdata/2011.xlsx'  # proton   | k+     | AUTsivers  | hermes     | z
# conf['datasets']['sidis']['xlsx'][2012]='../database/sidis/expdata/2012.xlsx'  # proton   | k-     | AUTsivers  | hermes     | PT
# conf['datasets']['sidis']['xlsx'][2013]='../database/sidis/expdata/2013.xlsx'  # proton   | k-     | AUTsivers  | hermes     | x
# conf['datasets']['sidis']['xlsx'][2014]='../database/sidis/expdata/2014.xlsx'  # proton   | k-     | AUTsivers  | hermes     | z
# neutron  | pi+    | AUTsivers  | jlab       | x
conf['datasets']['sidis']['xlsx'][2015] = '../database/sidis/expdata/2015.xlsx'
# neutron  | pi-    | AUTsivers  | jlab       | x
conf['datasets']['sidis']['xlsx'][2016] = '../database/sidis/expdata/2016.xlsx'
# conf['datasets']['sidis']['xlsx'][2017]='../database/sidis/expdata/2017.xlsx'  # proton   | k0     | AUTsivers  | compass    | PT
# conf['datasets']['sidis']['xlsx'][2018]='../database/sidis/expdata/2018.xlsx'  # proton   | k0     | AUTsivers  | compass    | x
# conf['datasets']['sidis']['xlsx'][2019]='../database/sidis/expdata/2019.xlsx'  # proton   | k0     | AUTsivers  | compass    | z
# conf['datasets']['sidis']['xlsx'][2020]='../database/sidis/expdata/2020.xlsx'  # proton   | h+     | AUTsivers  | compass    | PT
# conf['datasets']['sidis']['xlsx'][2021]='../database/sidis/expdata/2021.xlsx'  # proton   | h+     | AUTsivers  | compass    | x
# conf['datasets']['sidis']['xlsx'][2022]='../database/sidis/expdata/2022.xlsx'  # proton   | h+     | AUTsivers  | compass    | z
# conf['datasets']['sidis']['xlsx'][2023]='../database/sidis/expdata/2023.xlsx'  # proton   | h-     | AUTsivers  | compass    | PT
# conf['datasets']['sidis']['xlsx'][2024]='../database/sidis/expdata/2024.xlsx'  # proton   | h-     | AUTsivers  | compass    | x
# conf['datasets']['sidis']['xlsx'][2025]='../database/sidis/expdata/2025.xlsx'  # proton   | h-     | AUTsivers  | compass    | z
# deuteron | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2026] = '../database/sidis/expdata/2026.xlsx'
# deuteron | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2027] = '../database/sidis/expdata/2027.xlsx'
# deuteron | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2028] = '../database/sidis/expdata/2028.xlsx'
# deuteron | pi-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2029] = '../database/sidis/expdata/2029.xlsx'
# deuteron | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2030] = '../database/sidis/expdata/2030.xlsx'
# deuteron | pi-    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2031] = '../database/sidis/expdata/2031.xlsx'
# conf['datasets']['sidis']['xlsx'][2032]='../database/sidis/expdata/2032.xlsx'  # deuteron | k+     | AUTsivers  | compass    | PT
# conf['datasets']['sidis']['xlsx'][2033]='../database/sidis/expdata/2033.xlsx'  # deuteron | k+     | AUTsivers  | compass    | x
# conf['datasets']['sidis']['xlsx'][2034]='../database/sidis/expdata/2034.xlsx'  # deuteron | k+     | AUTsivers  | compass    | z
# conf['datasets']['sidis']['xlsx'][2035]='../database/sidis/expdata/2035.xlsx'  # deuteron | k-     | AUTsivers  | compass    | PT
# conf['datasets']['sidis']['xlsx'][2036]='../database/sidis/expdata/2036.xlsx'  # deuteron | k-     | AUTsivers  | compass    | x
# conf['datasets']['sidis']['xlsx'][2037]='../database/sidis/expdata/2037.xlsx'  # deuteron | k-     | AUTsivers  | compass    | z
# conf['datasets']['sidis']['xlsx'][2038]='../database/sidis/expdata/2038.xlsx'  # neutron  | k+     | AUTsivers  | jlab    | x
# conf['datasets']['sidis']['xlsx'][2039]='../database/sidis/expdata/2039.xlsx'  # neutron  | k-     | AUTsivers  | jlab    | z


for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
