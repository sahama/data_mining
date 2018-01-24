import math
import numpy
l = [10.6729017233248,10.7192672065069,10.4668264919524,10.6623796476102,10.3624783283431,10.3717902475263,10.8465367439193,10.2138787316649,10.4101933820285,10.2052039663541]

previous_channels_data = [[],[]] # if not clean replace with []
previous_clean_data = []

def XC(t,i):
    return 1 if previous_channels_data[i][t] else 0

def variance_norm(k, i):
    variance = numpy.var(k)
    makhraj_sum = 0
    makhraj_count = 0
    for i_t, t in enumerate(previous_clean_data):
        if XC(i_t, i):
            makhraj_sum += numpy.var(t)
            makhraj_count += 1
    return variance/(makhraj_sum/makhraj_count)


print(LOF(l))
