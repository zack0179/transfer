conf = {}

############################################################################
conf['method'] = 'cov'
conf['kappa'] = 1.1
conf['tol'] = 10e-10
conf['num points'] = 30  # self.npar*3
conf['burn size'] = 10
conf['sample size'] = 10000


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

conf['params'] = {}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.15920500644793311729e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.39782079427820671302e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']    = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 0, 'max': 1}

conf['params']['collins'] = {}
conf['params']['collins']['widths0 pi+ fav'] = {
    'value': 7.47958632885192820083e-02, 'fixed': False, 'min': 0.05, 'max': 0.10}
conf['params']['collins']['widths0 pi+ unfav'] = {
    'value': 0.059763576917398841815e+00, 'fixed': False, 'min': 0.05, 'max': 0.136784756168045196212}
conf['params']['collins']['pi+ u N 1'] = {
    'value': 4.49239476315589936206e+00, 'fixed': False, 'min': 0, 'max': 3}
conf['params']['collins']['pi+ u a 1'] = {
    'value': -8.28098465048009213518e-01, 'fixed': False, 'min': -1.9, 'max': 0}
conf['params']['collins']['pi+ u b 1'] = {
    'value': 6.60780815284983358282e+00, 'fixed': False, 'min': 2, 'max': 6}
conf['params']['collins']['pi+ d N 1'] = {
    'value': -4.14852904854067539020e+00, 'fixed': False, 'min': -12, 'max': 0.0}
conf['params']['collins']['pi+ d a 1'] = {
    'value': 1.00000000000000000000e+00, 'fixed': False, 'min': 0, 'max': 7.0}
conf['params']['collins']['pi+ d b 1'] = {
    'value': 2.37348461151638101541e+00, 'fixed': False, 'min': 2.5, 'max': 4.0}

conf['params']['collins']['pi+ u c 1'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c 1'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d 1'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d 1'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u N 2'] = {
    'value': 6.11150078306284516572e+00, 'fixed': False, 'min': 0, 'max': 15}
conf['params']['collins']['pi+ u a 2'] = {
    'value': 4.71508421683099232524e+00, 'fixed': False, 'min': 1, 'max': 8.0}
conf['params']['collins']['pi+ u b 2'] = {
    'value': 2.75387728005980081392e+00, 'fixed': False, 'min': 0, 'max': 5}

conf['params']['collins']['pi+ d N 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -20, 'max': 0}
conf['params']['collins']['pi+ d a 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ d b 2'] = {'value': 0.0,
                                          'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['collins']['pi+ u c 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d 2'] = {'value': 0.0,
                                          'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {
    'value': 0.5, 'fixed': False, 'min': 1e-5, 'max': 2}
conf['params']['transversity']['widths0 sea'] = {
    'value': 0.0, 'fixed': True, 'min': 1e-5, 'max': 2}
conf['params']['transversity']['u N'] = {
    'value': 1, 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['u a'] = {
    'value': -0.5, 'fixed': False, 'min': -1, 'max': 10}
conf['params']['transversity']['u b'] = {
    'value': 3.0, 'fixed': False, 'min': 1, 'max': 10}
conf['params']['transversity']['d N'] = {
    'value': 1.0, 'fixed': False, 'min': -20, 'max': 20}
conf['params']['transversity']['d a'] = {
    'value': -0.5, 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['d b'] = {
    'value': 3.0, 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['transversity']['s N'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s a'] = {
    'value': -0.5, 'fixed': True, 'min': -1, 'max': 5}
conf['params']['transversity']['s b'] = {
    'value': 3.0, 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['u c'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d c'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s c'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['u d'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d'] = {
    'value': 0.0, 'fixed': True, 'min': -10, 'max': 10}

############################################################################
# set data sets

conf['datasets'] = {}

# SIA

conf['datasets']['sia'] = {}


conf['datasets']['sia']['norm'] = {}

conf['datasets']['sia']['filter'] = 'Q2 > 1.69'


conf['datasets']['sia']['xlsx'] = {}

# babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1000] = '../database/sia/expdata/1000.xlsx'
# babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001] = '../database/sia/expdata/1001.xlsx'
# babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1002] = '../database/sia/expdata/1002.xlsx'
# babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003] = '../database/sia/expdata/1003.xlsx'
# belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1004] = '../database/sia/expdata/1004.xlsx'
# belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005] = '../database/sia/expdata/1005.xlsx'
# conf['datasets']['sia']['xlsx'][3000]='../database/sia/expdata/3000.xlsx' # besIII | pi,pi | AUL-0            | 6      | z1,z2      |
# conf['datasets']['sia']['xlsx'][3001]='../database/sia/expdata/3001.xlsx' # besIII | pi,pi | AUC-0            | 6      | z1,z2      |
# conf['datasets']['sia']['xlsx'][3002]='../database/sia/expdata/3002.xlsx' # besIII | pi,pi | AUL-0            | 6      | z1,z2,pt   |
# conf['datasets']['sia']['xlsx'][3003]='../database/sia/expdata/3003.xlsx' # besIII | pi,pi | AUC-0            | 6      | z1,z2,pt   |

# Collins Asy

conf['datasets']['sidis'] = {}
conf['datasets']['sidis']['norm'] = {}
conf['datasets']['sidis']['xlsx'] = {}
conf['datasets']['sidis']['filters'] = {}

conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [4001, 4000, 4002, 4004, 4003,
                                                  4005, 3027, 3025, 3010, 3012, 3005, 3013, 3026, 3000, 3003, 3016, 3004, 3018]
conf['datasets']['sidis']['filters'][0]['filter'] = "z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"

# conf["datasets"]["sidis"]["xlsx"][4007]="../database/sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
# conf["datasets"]["sidis"]["xlsx"][4006]="../database/sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
# conf["datasets"]["sidis"]["xlsx"][4008]="../database/sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
# conf["datasets"]["sidis"]["xlsx"][4010]="../database/sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
# conf["datasets"]["sidis"]["xlsx"][4009]="../database/sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
# conf["datasets"]["sidis"]["xlsx"][4011]="../database/sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
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
# conf["datasets"]["sidis"]["xlsx"][6003]="../database/sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
# conf["datasets"]["sidis"]["xlsx"][6004]="../database/sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
# conf["datasets"]["sidis"]["xlsx"][6005]="../database/sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
# conf["datasets"]["sidis"]["xlsx"][6000]="../database/sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
# conf["datasets"]["sidis"]["xlsx"][6001]="../database/sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
# conf["datasets"]["sidis"]["xlsx"][6002]="../database/sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
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
# conf["datasets"]["sidis"]["xlsx"][3024]="../database/sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
# conf["datasets"]["sidis"]["xlsx"][3007]="../database/sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
# conf["datasets"]["sidis"]["xlsx"][3008]="../database/sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
# conf["datasets"]["sidis"]["xlsx"][3021]="../database/sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
# conf["datasets"]["sidis"]["xlsx"][3017]="../database/sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
# conf["datasets"]["sidis"]["xlsx"][3023]="../database/sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
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

for k in conf['datasets']['sia']['xlsx']:
    conf['datasets']['sia']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
