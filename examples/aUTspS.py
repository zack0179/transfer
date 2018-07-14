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
conf['ncpus'] = 4

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

conf['shape'] = 1

conf['params'] = {}

conf['params']['ff'] = {}
conf['params']['ff']['widths0 pi+ fav']   = {'value': <<    1.24049999999999993605e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value': <<    1.43729999999999996652e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ fav']   = {'value': <<    1.33839999999999986757e-01 >>, 'fixed': True, 'min': 0, 'max': 1}
conf['params']['ff']['widths0 k+ unfav'] = {'value': <<    2.02660000000000006803e-01 >>, 'fixed': True, 'min': 0, 'max': 1}


conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {'value': <<    5.24140000000000050306e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 0.52414}
conf['params']['transversity']['widths0 sea']     = {'value': <<    5.84650000000000003020e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 0.58465}
conf['params']['transversity']['u N']             = {'value': <<    8.94813003799857220599e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['u a']             = {'value': <<    2.67175781432258130366e+00 >> , 'fixed': False, 'min': -1, 'max': 10}
conf['params']['transversity']['u b']             = {'value': <<    2.69329330535173516736e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['d N']             = {'value': <<   -8.13627735800177731562e+00 >> , 'fixed': False, 'min': -20, 'max': 20}
conf['params']['transversity']['d a']             = {'value': <<    3.70376212030867124625e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['d b']             = {'value': <<    2.18142271253462816105e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['transversity']['s N']             = {'value': <<    4.11089042164620110942e-01 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['s a']             = {'value': <<    1.56962539981397419808e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['s b']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 0., 'max': 10}

conf['params']['transversity']['u c']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d c']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s c']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['transversity']['u d']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['d d']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['transversity']['s d']             = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['Htilde'] = {}
conf['params']['Htilde']['widths0 pi+ fav']     = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 0.05, 'max': 1.24049999999999993605e-01}
conf['params']['Htilde']['widths0 pi+ unfav']   = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 1.43729999999999996652e-01}
conf['params']['Htilde']['pi+ u N 1']  = {'value': <<   -2.05760931661718204921e+00 >>, 'fixed': False, 'min': -15, 'max': 15}
conf['params']['Htilde']['pi+ u a 1']  = {'value': <<    7.77516080912076468223e-01 >>, 'fixed': False, 'min': -1, 'max': 5}
conf['params']['Htilde']['pi+ u b 1']  = {'value': <<    2.67197688236972075160e+00 >>, 'fixed': False, 'min': 0, 'max': 10}

conf['params']['Htilde']['pi+ d N 1']  = {'value': <<    1.46772895245558943067e+00 >>, 'fixed': False, 'min': -15, 'max': 15}
conf['params']['Htilde']['pi+ d a 1']  = {'value': <<    2.45363438069647266104e+00 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['Htilde']['pi+ d b 1']  = {'value': <<    1.38055779752141560834e-01 >>, 'fixed': False, 'min': 0, 'max': 10}

conf['params']['Htilde']['pi+ u c 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d c 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ u d 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['Htilde']['pi+ d d 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

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

# AUTsinphiS

conf['datasets']['sidis'] = {}
conf['datasets']['sidis']['norm'] = {}
conf['datasets']['sidis']['xlsx'] = {}
conf['datasets']['sidis']['filters'] = {}

conf['datasets']['sidis']['filters'][0] = {}
conf['datasets']['sidis']['filters'][0]['idx'] = [9011, 9022, 9033, 9044]
conf['datasets']['sidis']['filters'][0]['filter'] = "z>0.2 and z<0.8 and Q2>1.69 and pT>0.2 and pT<0.9"

# COMPASS    proton  h+    z
conf["datasets"]["sidis"]["xlsx"][9011] = "../database/sidis/expdata/9011.xlsx"
# COMPASS    proton  h-    z
conf["datasets"]["sidis"]["xlsx"][9022] = "../database/sidis/expdata/9022.xlsx"
# COMPASS    proton  h+    x
conf["datasets"]["sidis"]["xlsx"][9033] = "../database/sidis/expdata/9033.xlsx"
# COMPASS    proton  h-    x
conf["datasets"]["sidis"]["xlsx"][9044] = "../database/sidis/expdata/9044.xlsx"


#for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
for k in conf['datasets']['sidis']['xlsx']:
    conf['datasets']['sidis']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
