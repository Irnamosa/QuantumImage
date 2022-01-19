import numpy as np


def get_bin(x,n):
    return format(x, 'b').zfill(n)

def coord2bool(i,j,N):
    '''
    (i,j) entry in NxN matrix
    0<= i,j <= N-1
    '''
    pad = len(get_bin(N*(N-1)+(N-1),0))
    
    return get_bin(N*i+j, pad)

def populate(counts, N):
    '''
    populate counts with states that yielded 0 shots
    '''
    for i in range(2**N):
        bnry = "{0:b}".format(i).zfill(N)
        if bnry not in counts:
            counts[bnry] = 0
    
    return counts