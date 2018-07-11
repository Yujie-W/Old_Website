#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:59:13 2018

@author: yujie
"""

from numpy import exp,linspace
from pylab import figure

k = 0.4
x = linspace(0,20,1001)
y = k**2.0 * x * exp(-1.0*k*x)

fig0 = figure(figsize=(6,4),dpi=100)
ax0  = fig0.add_subplot(1,1,1)
ax0.plot(x,y)
ax0.set_xlabel("Annual Money Left (10000 Yuan)")
ax0.set_ylabel("Probability")

m = x
sale = exp(-1.0*k*m) * (k*m+1)

fig1 = figure(figsize=(6,4),dpi=100)
ax1  = fig1.add_subplot(1,1,1)
ax1.plot(m,sale)
ax1.set_xlabel("Annual Cost (10000 Yuan)")
ax1.set_ylabel("Probability of Purchase")

c1 = 0.1
c2 = 0.05
c3 = 0.0

prof1 = (m-c1) * sale
prof2 = (m-c2) * sale
prof3 = (m-c3) * sale

print( m[list(prof1).index(max(prof1))] )
print( m[list(prof2).index(max(prof2))] )
print( m[list(prof3).index(max(prof3))] )
print( sale[list(prof1).index(max(prof1))] )
print( sale[list(prof2).index(max(prof2))] )
print( sale[list(prof3).index(max(prof3))] )

fig2 = figure(figsize=(6,4),dpi=100)
ax2  = fig2.add_subplot(1,1,1)
ax2.plot(m,prof1, label="1000 Yuan")
ax2.plot(m,prof2, label="500 Yuan")
ax2.plot(m,prof3, label="0 Yuan")
ax2.set_xlabel("Annual Cost (10000 Yuan)")
ax2.set_ylabel("Annual Sale Profit (10000 Yuan per person)")
ax2.set_ylim(0,2.5)
ax2.legend(loc="upper right")
