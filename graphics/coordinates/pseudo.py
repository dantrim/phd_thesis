#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt, cosh, sinh
import sys, os

def rapidity_from_pseudo(mass, pt, ps) :

    num_0 = sqrt(mass*mass + pt*pt*cosh(ps)*cosh(ps))
    num_1 = pt * sinh(ps)
    num = num_0 + num_1
    den = sqrt(mass*mass + pt*pt)
    return log(num/den)

def rapidities_from_mop(mop, ps) :

    num = sqrt( mop*mop + cosh(ps)*cosh(ps) ) + sinh(ps)
    den = sqrt( mop*mop + 1)
    return log(num/den)

def rap_mop_arr(mop_arr, ps_arr) :

    num = np.sqrt( np.power(mop_arr, 2) + np.power(np.cosh(ps_arr), 2) )
    den = np.sqrt( np.power(mop_arr, 2) + np.ones(mop_arr.size) )
    return num / den

def main() :

    #pseudos = np.arange(0, 8, 0.1)
    #masses = np.arange(0, 4500, 500)
    #pt = 50 # GeV

    #fig, ax = plt.subplots(1,1)

    #for im, m in enumerate(masses) :
    #    name = "%d GeV" % int(m)
    #    ax.plot(pseudos, [rapidity_from_pseudo(m, pt, x) for x in pseudos],
    #        label = name)

    #fig.show()
    #ax.legend(loc = "best", frameon = False)
    #x = input()

    mop_bin_width = 0.01
    mop_values = np.arange(0, 1 + mop_bin_width, mop_bin_width)
    eta_bin_width = 0.03
    eta_values = np.arange(0, 3 + eta_bin_width, eta_bin_width)

    X, Y = np.meshgrid(mop_values, eta_values)
    Z1 = np.sqrt( np.power(X, 2) + np.power(np.cosh(Y), 2)) + np.sinh(Y)
    Z2 = np.sqrt( np.power(X, 2) + np.ones(X.shape))
    Z = np.log(Z1/Z2)
    #Z = X/Z

    #print(Y.shape)
    #print(Y[0:2])
    #print(Z.shape)
    for i in range(Y.shape[0]) :
        eta_vals = Y[i]
        rap_vals = Z[i]
        print(eta_vals[0])
        print(rap_vals[0])
        #diffs = (rap_vals - eta_vals) / rap_vals
        diffs = eta_vals / rap_vals
        Z[i] = diffs
        #Z[i] = Z[i] / Y[i]
        #print(Z[i])
        #sys.exit()

    z_plot = Z

    fig, ax = plt.subplots()#1,1)
    ax.tick_params(axis = "both", which = "both", labelsize = 12,
        direction = "in",
        labelleft = True, bottom = True, top = True, left = True)
    im = ax.imshow( z_plot[1:], 
            extent = (mop_values[0], mop_values[-1], eta_values[0], eta_values[-1]),
            origin = "lower",
            aspect = "auto")
    ax.grid(which = "both", lw = 0.5, color = "k")
    cbar = fig.colorbar(im)
    cbar.ax.tick_params(length = 0)
    cbar.set_label(r"$\eta$ / $y$", horizontalalignment = "right", y = 1)
    fig.show()
    levels = [1.01, 1.05, 1.1, 1.15, 1.2, 1.25,  1.30, 1.5, 2, 3]
    cont = ax.contour(X,Y, z_plot, levels = levels, colors = "k", linestyles= "dashed")
    ax.clabel(cont, inline = 1, fmt = "%.2f")

    ax.set_xlabel(r"Mass / $p_{T}$ [GeV]", horizontalalignment = "right", x = 1)
    ax.set_ylabel(r"$\eta$", horizontalalignment = "right", y = 1)
    x = input()

    fig.savefig("eta_vs_rap.pdf", bbox_inches = "tight")

if __name__ == "__main__" :
    main()
