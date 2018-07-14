conf = {}

############################################################################
# sidis setup

conf['Ebeam'] = 11.0
conf['S'] = np.array([0, 0, 0, 0])
# conf['S']=np.array([0,0,1,0])
conf['hadron'] = 'pi+'
conf['target'] = 'p'
conf['le'] = 0

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

# from here on nothing is fitted.

conf['params']['boermulders'] = {}
conf['params']['boermulders']['widths0 valence'] = {'value': <<    2.30514134510557133773e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1}
conf['params']['boermulders']['widths0 sea']     = {'value': <<    9.86199935641373093276e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1}

conf['params']['boermulders']['u N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['boermulders']['u a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['u b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['boermulders']['u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['boermulders']['d N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['boermulders']['d a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['d b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['boermulders']['d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['boermulders']['s N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['boermulders']['s a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['s b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['s c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['boermulders']['s d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['boermulders']['ub N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['ub a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['ub b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}

conf['params']['boermulders']['db N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['db a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['db b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}

conf['params']['boermulders']['sb N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['boermulders']['sb a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['boermulders']['sb b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}


conf['params']['pretzelosity'] = {}
conf['params']['pretzelosity']['widths0 valence'] = {'value': <<    2.30514134510557133773e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1}
conf['params']['pretzelosity']['widths0 sea']     = {'value': <<    9.86199935641373093276e-02 >>, 'fixed': False, 'min': 1e-5, 'max': 1}

conf['params']['pretzelosity']['u N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['u a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['u b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['u c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['u d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['pretzelosity']['d N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': False, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['d a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['d b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': False, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['d c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['d d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['pretzelosity']['s N']  = {'value': <<   0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['s a']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['s b']  = {'value': <<   1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['s c']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}
conf['params']['pretzelosity']['s d']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': -10, 'max': 10}

conf['params']['pretzelosity']['ub N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['ub a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['ub b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}

conf['params']['pretzelosity']['db N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['db a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['db b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}

conf['params']['pretzelosity']['sb N']  = {'value': <<    0.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
conf['params']['pretzelosity']['sb a']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 5}
conf['params']['pretzelosity']['sb b']  = {'value': <<    1.00000000000000000000e+00 >> , 'fixed': True, 'min': 1e-5, 'max': 10}
