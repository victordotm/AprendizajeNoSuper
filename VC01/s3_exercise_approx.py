#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:50:55 2018

@author: momo
"""

import numpy as np
import itertools as itt


pX=[]
pX.append( np.array([0.3,0.7]) )
pX.append( np.array([[0.4,0.1],[0.6,0.9]]) )
pX.append( np.array([[0.2,0.5],[0.8,0.5]]) )
pX.append( np.array([[0.3,0.2],[0.7,0.8]]) )
pX.append( np.array([[0.4,0.5,0.7,0.2],[0.6,0.5,0.3,0.8]]) )
pX.append( np.array([[0.1,0.4],[0.9,0.6]]) )


def prob_rule(x,pX) :
    return (pX[0][x[0]]* pX[1][x[1],x[0]]* pX[2][x[2],x[0]]* 
            pX[3][x[3],x[1]]* pX[4][x[4],x[1]*2+x[2]]* pX[5][x[5],x[2]])




#x=[1,0,1,1,0,1]
#x = np.round(np.random.rand(6)).astype(int)
#print(x)


np.random.seed(15485863)

e=[1,0,-1,-1,-1,-1]

nsamples = 10000

mat = np.round(np.random.rand(nsamples,len(e))).astype(int)
for i in range(len(e)):
    if (e[i] >= 0):
        mat[:,i]=e[i]


p_vect = [prob_rule(mat[i,],pX) for i in range(nsamples)]
h_vect = np.ones(nsamples)*1./2**4
s_vect = p_vect/h_vect

#x_3=0
print sum(s_vect[mat[:,2] == 0])/sum(s_vect)
print sum(s_vect[mat[:,2] == 1])/sum(s_vect)



pr0=0.
pr1=0.
for x in itt.product(range(2), repeat=3):
    largex0 = np.concatenate([np.array(e[0:2]),np.array([0]),np.array(x)])
    pr0+=prob_rule(largex0,pX)
    largex1 = np.concatenate([np.array(e[0:2]),np.array([1]),np.array(x)])
    pr1+=prob_rule(largex1,pX)
#    print(largex)
#    1,0,1+x
    
 #   print(np.array(x))

print [pr0/(pr0+pr1),pr1/(pr0+pr1)]

