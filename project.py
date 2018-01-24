import math
import numpy
l = [10.6729017233248,10.7192672065069,10.4668264919524,10.6623796476102,10.3624783283431,10.3717902475263,10.8465367439193,10.2138787316649,10.4101933820285,10.2052039663541]

previous_channels_data = [[],[]] # if not clean replace with []
previous_clean_data = []

# k is new data from all channels
# finally k will add to previous_channels_data

def XC(t,i):
    return 1 if previous_channels_data[i][t] else 0

def variance_norm(k, i):
    variance = numpy.var(k[i])
    makhraj_sum = 0
    makhraj_count = 0
    for i_t, t in enumerate(previous_clean_data):
        if XC(i_t, i):
            makhraj_sum += numpy.var(t)
            makhraj_count += 1


    if not makhraj_count == 0:
        makhraj = makhraj_sum/makhraj_count
    else:
        makhraj = 1

    return variance/makhraj

def f_H(k,i,j):
    abs(variance_norm(k,i) - variance_norm(k,j))

def f_L(k,i,j):
    variance_norm_i = abs(variance_norm(k,i))
    variance_norm_j = abs(variance_norm(k,j))

    if variance_norm_i >= variance_norm_j:
        f = variance_norm_i/variance_norm_j
    else:
        f = variance_norm_j / variance_norm_i
    return f

def d(k, i, j):
    return max(variance_norm(k,i) - variance_norm(k,j))


print(LOF(l))
