import numpy as np
import matplotlib.pyplot as plt
from littletool import dataload, caculate_rtrain, see_dev1predict, see_dev2predict


hp_a_serachlist   = list(enumerate(np.linspace(0,0.0077,100)))
hp_win_serachlist = list(enumerate(np.linspace(0,0.0150,100)))

# betalist = np.array([
# 0,
# 0.00000001,
# 0.00000011,
# 0.00000021,
# 0.00000031,
# 0.00000041,
# 0.00000051
# 0.00000061,
# 0.00000071,
# 0.00000081,
# 0.00000091,
# 0.00000100,
# 0.000005,
# 0.000010,
# 0.000015,
# 0.000020,
# 0.000025,
# 0.000030,
# 0.000035,
# 0.000040,
# 0.000045,
# 0.000055,
# 0.000060,
# 0.000065,
# 0.000070,
# 0.000075,
# 0.000080,
# 0.000085,
# 0.000090,
# 0.000095,
# 0.000100
# ])

# betalist = np.array([0, 1e-8, 10e-8, 30e-8, 50e-8, 70e-8, 90e-8,
# 110e-8, 130e-8, 150e-8, 170e-8, 190e-8, 210e-8, 230e-8, 250e-8, 270e-8,
# 300e-8, 330e-8, 360e-8, 400e-8, 450e-8, 500e-8, 550e-8, 1000e-8, 1750e-8])

betalist = np.array([0, 0.6e-7, 0.8e-7, 0.9e-7, 1.0e-7, 1.5e-7, 2.0e-7, 2.5e-7, 3.0e-7, 3.5e-7,
4.5e-7, 5.0e-7, 5.5e-7, 6.0e-7, 6.5e-7, 7.0e-7, 7.5e-7, 8.0e-7, 8.5e-7, 9.0e-7, 9.5e-7, 10.0e-7,
11e-7, 12e-7, 14e-7])

'''
L = 40, Q = 200
l = 200, Q = 1000
part1Q = part2Q = ... = part10Q = 20
l = 10

只对一个 (win_key, a_key)
只对16种 (hp_a, hp_win)
只对10个beta

10*16*10大约需要5天，可以接受。如果GPU可行的话仅需1天。



用logging捕捉错误，
捕捉程序暂停的种类，
hander模块，



'''

beta_searchlist   = list(enumerate(betalist))

key_list = (('Win1', 'A1'), ('Win2', 'A2'), ('Win3', 'A3'), ('Win4', 'A4'), ('Win0', 'A0'))


# for win_key, a_key in key_list[4:5]:
#     utrain, udev1, udev2, fixedparameter = dataload(win_key, a_key)
#     T1, T2, T3, Din, Dr, hp_width, Win, A, a_key, win_key = fixedparameter
#     for hp_a_index, hp_a in hp_a_serachlist[52:60:2]:
#         for hp_win_index, hp_win in hp_win_serachlist[60:70:2]:
#             findparameter = (hp_a, hp_win, hp_a_index, hp_win_index)
#             xtrain, rtrain_nearfuture = caculate_rtrain(utrain, findparameter, fixedparameter)
#             for beta_index, beta in beta_searchlist[0:5]:
#                 P = np.linalg.inv( xtrain.T.dot(xtrain) + beta*np.eye(2*Dr) ).dot(xtrain.T).dot(utrain)
#                 see_dev1predict(udev1, P, beta_index, beta, rtrain_nearfuture, findparameter, fixedparameter)
#                 # see_dev2predict(udev1, udev2, P, beta_index, beta, findparameter, fixedparameter)


for win_key, a_key in key_list[0:1]:
    utrain, udev1, udev2, fixedparameter = dataload(win_key, a_key)
    T1, T2, T3, Din, Dr, hp_width, Win, A, a_key, win_key = fixedparameter
    for hp_a_index, hp_a in hp_a_serachlist[52:60:2]:
        for hp_win_index, hp_win in hp_win_serachlist[60:70:2]:
            findparameter = (hp_a, hp_win, hp_a_index, hp_win_index)
            xtrain, rtrain_nearfuture = caculate_rtrain(utrain, findparameter, fixedparameter)
            for beta_index, beta in beta_searchlist[0:5]:
                P = np.linalg.inv( xtrain.T.dot(xtrain) + beta*np.eye(2*Dr) ).dot(xtrain.T).dot(utrain)
                see_dev1predict(udev1, P, beta_index, beta, rtrain_nearfuture, findparameter, fixedparameter)
                # see_dev2predict(udev1, udev2, P, beta_index, beta, findparameter, fixedparameter)



'''
1,3,5,7,9,11,13,15,17,19,21,23,25
40,45,50,55,60,65,70,75,80,85,90
13*11*6min=


# old meshgrid:
hp_a_serachlist
array([0.     , 0.00015, 0.0003 , 0.00045, 0.0006 , 0.00075, 0.0009 ,
       0.00105, 0.0012 , 0.00135, 0.0015 , 0.00165, 0.0018 , 0.00195,
       0.0021 , 0.00225, 0.0024 , 0.00255, 0.0027 , 0.00285, 0.003  ,
       0.00315, 0.0033 , 0.00345, 0.0036 , 0.00375, 0.0039 , 0.00405,
       0.0042 , 0.00435, 0.0045 , 0.00465, 0.0048 , 0.00495, 0.0051 ,
       0.00525, 0.0054 , 0.00555, 0.0057 , 0.00585, 0.006  , 0.00615,
       0.0063 , 0.00645, 0.0066 , 0.00675, 0.0069 , 0.00705, 0.0072 ,
       0.00735, 0.0075 , 0.00765, 0.0078 , 0.00795, 0.0081 , 0.00825,
       0.0084 , 0.00855, 0.0087 , 0.00885, 0.009  , 0.00915, 0.0093 ,
       0.00945, 0.0096 , 0.00975, 0.0099 , 0.01005, 0.0102 , 0.01035,
       0.0105 , 0.01065, 0.0108 , 0.01095, 0.0111 , 0.01125, 0.0114 ,
       0.01155, 0.0117 , 0.01185, 0.012  , 0.01215, 0.0123 , 0.01245,
       0.0126 , 0.01275, 0.0129 , 0.01305, 0.0132 , 0.01335, 0.0135 ,
       0.01365, 0.0138 , 0.01395, 0.0141 , 0.01425, 0.0144 , 0.01455,
       0.0147 , 0.01485, 0.015  ])
hp_win_serachlist
array([0.    , 0.0005, 0.001 , 0.0015, 0.002 , 0.0025, 0.003 , 0.0035,
       0.004 , 0.0045, 0.005 , 0.0055, 0.006 , 0.0065, 0.007 , 0.0075,
       0.008 , 0.0085, 0.009 , 0.0095, 0.01  , 0.0105, 0.011 , 0.0115,
       0.012 , 0.0125, 0.013 , 0.0135, 0.014 , 0.0145, 0.015 , 0.0155,
       0.016 , 0.0165, 0.017 , 0.0175, 0.018 , 0.0185, 0.019 , 0.0195,
       0.02  , 0.0205, 0.021 , 0.0215, 0.022 , 0.0225, 0.023 , 0.0235,
       0.024 , 0.0245, 0.025 , 0.0255, 0.026 , 0.0265, 0.027 , 0.0275,
       0.028 , 0.0285, 0.029 , 0.0295, 0.03  , 0.0305, 0.031 , 0.0315,
       0.032 , 0.0325, 0.033 , 0.0335, 0.034 , 0.0345, 0.035 , 0.0355,
       0.036 , 0.0365, 0.037 , 0.0375, 0.038 , 0.0385, 0.039 , 0.0395,
       0.04  , 0.0405, 0.041 , 0.0415, 0.042 , 0.0425, 0.043 , 0.0435,
       0.044 , 0.0445, 0.045 , 0.0455, 0.046 , 0.0465, 0.047 , 0.0475,
       0.048 , 0.0485, 0.049 , 0.0495, 0.05  ])


In [4]: np.linspace(0,0.0077,100)
Out[4]:
array([0.00000000e+00, 7.77777778e-05, 1.55555556e-04, 2.33333333e-04,
       3.11111111e-04, 3.88888889e-04, 4.66666667e-04, 5.44444444e-04,
       6.22222222e-04, 7.00000000e-04, 7.77777778e-04, 8.55555556e-04,
       9.33333333e-04, 1.01111111e-03, 1.08888889e-03, 1.16666667e-03,
       1.24444444e-03, 1.32222222e-03, 1.40000000e-03, 1.47777778e-03,
       1.55555556e-03, 1.63333333e-03, 1.71111111e-03, 1.78888889e-03,
       1.86666667e-03, 1.94444444e-03, 2.02222222e-03, 2.10000000e-03,
       2.17777778e-03, 2.25555556e-03, 2.33333333e-03, 2.41111111e-03,
       2.48888889e-03, 2.56666667e-03, 2.64444444e-03, 2.72222222e-03,
       2.80000000e-03, 2.87777778e-03, 2.95555556e-03, 3.03333333e-03,
       3.11111111e-03, 3.18888889e-03, 3.26666667e-03, 3.34444444e-03,
       3.42222222e-03, 3.50000000e-03, 3.57777778e-03, 3.65555556e-03,
       3.73333333e-03, 3.81111111e-03, 3.88888889e-03, 3.96666667e-03,
       4.04444444e-03, 4.12222222e-03, 4.20000000e-03, 4.27777778e-03,
       4.35555556e-03, 4.43333333e-03, 4.51111111e-03, 4.58888889e-03,
       4.66666667e-03, 4.74444444e-03, 4.82222222e-03, 4.90000000e-03,
       4.97777778e-03, 5.05555556e-03, 5.13333333e-03, 5.21111111e-03,
       5.28888889e-03, 5.36666667e-03, 5.44444444e-03, 5.52222222e-03,
       5.60000000e-03, 5.67777778e-03, 5.75555556e-03, 5.83333333e-03,
       5.91111111e-03, 5.98888889e-03, 6.06666667e-03, 6.14444444e-03,
       6.22222222e-03, 6.30000000e-03, 6.37777778e-03, 6.45555556e-03,
       6.53333333e-03, 6.61111111e-03, 6.68888889e-03, 6.76666667e-03,
       6.84444444e-03, 6.92222222e-03, 7.00000000e-03, 7.07777778e-03,
       7.15555556e-03, 7.23333333e-03, 7.31111111e-03, 7.38888889e-03,
       7.46666667e-03, 7.54444444e-03, 7.62222222e-03, 7.70000000e-03])
In [5]: np.linspace(0,0.015,100)
Out[5]:
array([0.        , 0.00015152, 0.00030303, 0.00045455, 0.00060606,
       0.00075758, 0.00090909, 0.00106061, 0.00121212, 0.00136364,
       0.00151515, 0.00166667, 0.00181818, 0.0019697 , 0.00212121,
       0.00227273, 0.00242424, 0.00257576, 0.00272727, 0.00287879,
       0.0030303 , 0.00318182, 0.00333333, 0.00348485, 0.00363636,
       0.00378788, 0.00393939, 0.00409091, 0.00424242, 0.00439394,
       0.00454545, 0.00469697, 0.00484848, 0.005     , 0.00515152,
       0.00530303, 0.00545455, 0.00560606, 0.00575758, 0.00590909,
       0.00606061, 0.00621212, 0.00636364, 0.00651515, 0.00666667,
       0.00681818, 0.0069697 , 0.00712121, 0.00727273, 0.00742424,
       0.00757576, 0.00772727, 0.00787879, 0.0080303 , 0.00818182,
       0.00833333, 0.00848485, 0.00863636, 0.00878788, 0.00893939,
       0.00909091, 0.00924242, 0.00939394, 0.00954545, 0.00969697,
       0.00984848, 0.01      , 0.01015152, 0.01030303, 0.01045455,
       0.01060606, 0.01075758, 0.01090909, 0.01106061, 0.01121212,
       0.01136364, 0.01151515, 0.01166667, 0.01181818, 0.0119697 ,
       0.01212121, 0.01227273, 0.01242424, 0.01257576, 0.01272727,
       0.01287879, 0.0130303 , 0.01318182, 0.01333333, 0.01348485,
       0.01363636, 0.01378788, 0.01393939, 0.01409091, 0.01424242,
       0.01439394, 0.01454545, 0.01469697, 0.01484848, 0.015     ])





'''

