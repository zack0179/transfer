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


conf['params']['collins'] = {}
conf['params']['collins']['widths0 pi+ fav']     = {'value': <<    7.85816134291348195040e-02 >>, 'fixed': False, 'min': 0.05, 'max': 1.24049999999999993605e-01}
conf['params']['collins']['widths0 pi+ unfav']   = {'value': <<    8.11847362254432686202e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1.43729999999999996652e-01}
conf['params']['collins']['pi+ u N 1']  = {'value': <<    3.45757730552646469491e-01 >>, 'fixed': False, 'min': 0, 'max': 4}
conf['params']['collins']['pi+ u a 1']  = {'value': <<   -1.77131071075123491809e+00 >>, 'fixed': False, 'min': -2.5, 'max': 0}
conf['params']['collins']['pi+ u b 1']  = {'value': <<    6.03511109763524267180e+00 >>, 'fixed': False, 'min': 3., 'max': 7.}

conf['params']['collins']['pi+ d N 1']  = {'value': <<   -7.43430153092576251339e+00 >>, 'fixed': False, 'min': -15, 'max': 2}
conf['params']['collins']['pi+ d a 1']  = {'value': <<    5.62381198220940348165e-03 >> , 'fixed': False, 'min': 0., 'max': 4.5}
conf['params']['collins']['pi+ d b 1']  = {'value': <<    3.08347097829055138973e+00 >>, 'fixed': False, 'min': 2.5, 'max': 3.8}

conf['params']['collins']['pi+ u c 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d 1']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}

conf['params']['collins']['pi+ u N 2']  = {'value': <<    9.48477971314817835946e+00 >>, 'fixed': False, 'min': 1, 'max': 52}
conf['params']['collins']['pi+ u a 2']  = {'value': <<    4.36818742227184486637e+00 >>, 'fixed': False, 'min': 1, 'max': 20}
conf['params']['collins']['pi+ u b 2']  = {'value': <<    4.73041840634133237131e+00 >>, 'fixed': False, 'min': 3, 'max': 25}

conf['params']['collins']['pi+ d N 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -20, 'max': 0}
conf['params']['collins']['pi+ d a 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -1, 'max': 5}
conf['params']['collins']['pi+ d b 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['collins']['pi+ u c 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d c 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ u d 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}
conf['params']['collins']['pi+ d d 2']  = {'value': <<    0.00000000000000000000e+00 >>, 'fixed': True, 'min': -10, 'max': 10}


conf['params']['transversity'] = {}
conf['params']['transversity']['widths0 valence'] = {'value': <<    5.24140000000000050306e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 0.52414}
conf['params']['transversity']['widths0 sea']     = {'value': <<    5.84650000000000003020e-01 >>, 'fixed': False, 'min': 1e-5, 'max': 0.58465}
conf['params']['transversity']['u N']             = {'value': <<    9.23667578841576819570e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['u a']             = {'value': <<    4.79318781071835786634e-02 >> , 'fixed': False, 'min': -1, 'max': 10}
conf['params']['transversity']['u b']             = {'value': <<    1.00744182508636148654e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['transversity']['d N']             = {'value': <<   -1.07799848371160944538e+01 >> , 'fixed': False, 'min': -20, 'max': 20}
conf['params']['transversity']['d a']             = {'value': <<    5.42444551003368857778e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
conf['params']['transversity']['d b']             = {'value': <<    4.37270006601641991750e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 20}
conf['params']['transversity']['s N']             = {'value': <<   -2.62214084077536990769e-01 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['transversity']['s a']             = {'value': <<    1.19744146249760596845e-01 >> , 'fixed': False, 'min': -1, 'max': 5}
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
conf['params']['Htilde']['pi+ u N 1']  = {'value': <<   -2.71534798241250063811e+00 >>, 'fixed': False, 'min': -4, 'max': 4}
conf['params']['Htilde']['pi+ u a 1']  = {'value': <<   -8.75877562727971348266e-02 >>, 'fixed': False, 'min': -2.5, 'max': 0}
conf['params']['Htilde']['pi+ u b 1']  = {'value': <<    5.88084592567702379995e+00 >>, 'fixed': False, 'min': 3., 'max': 7.}

conf['params']['Htilde']['pi+ d N 1']  = {'value': <<   -3.13888549967996288714e+00 >>, 'fixed': False, 'min': -15, 'max': 15}
conf['params']['Htilde']['pi+ d a 1']  = {'value': <<    4.37161613192937004158e+00 >> , 'fixed': False, 'min': -2.5, 'max': 4.5}
conf['params']['Htilde']['pi+ d b 1']  = {'value': <<    3.36392276152253222321e+00 >>, 'fixed': False, 'min': 2.5, 'max': 3.8}

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

# AN

conf['datasets']['AN'] = {}


conf['datasets']['AN']['norm'] = {}

conf['datasets']['AN']['filters'] = []


conf['datasets']['AN']['xlsx'] = {}

# conf['datasets']['AN']['xlsx'][1000]='../database/AN_pp/expdata/1000.xlsx' # BRAHMS pim 2.3
# conf['datasets']['AN']['xlsx'][1001]='../database/AN_pp/expdata/1001.xlsx' # BRAHMS pim 4
# conf['datasets']['AN']['xlsx'][1002]='../database/AN_pp/expdata/1002.xlsx' # BRAHMS pip 2.3
# conf['datasets']['AN']['xlsx'][1003]='../database/AN_pp/expdata/1003.xlsx' # BRAHMS pip 4
# STAR piz 04
conf['datasets']['AN']['xlsx'][2000] = '../database/AN_pp/expdata/2000.xlsx'
# STAR piz 3.3
conf['datasets']['AN']['xlsx'][2001] = '../database/AN_pp/expdata/2001.xlsx'
# STAR piz 3.68
conf['datasets']['AN']['xlsx'][2002] = '../database/AN_pp/expdata/2002.xlsx'
# STAR piz 3.7
conf['datasets']['AN']['xlsx'][2003] = '../database/AN_pp/expdata/2003.xlsx'

for k in conf['datasets']['AN']['xlsx']:
    conf['datasets']['AN']['norm'][k] = {
        'value': 1, 'fixed': True, 'min': 0, 'max': 1}
