#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt, cosh, sinh
import sys, os

def main() :

    avg_b_lifetime = 1.6 # ps
    avg_c_lifetime = 1 # ps

    b_hadron_mass = 5.5 # GeV
    c_hadron_mass = 2 # GeV

    pos_b_20 = 0.275

    ps_to_s = 1 * 10 ** (-12)
    speed_of_light = 3.08 * 10 ** 8 # m/s
#
#    l_width = 0.01 # cm
#    l_values = np.arange(0, 1.2 + l_width, l_width)
#    mp_width = 0.001
#    mp_values = np.arange(mp_width, 0.4 + mp_width, mp_width)
#
#    #mp_width = 0.1
#    #mp_values = np.arange(mp_width, 20 + mp_width, mp_width)
#
#
#    X, Y = np.meshgrid(l_values, mp_values)
#    # convert to m
#    #Z = (X/100) * Y / speed_of_light
#    Z = (X/100) * (1.0 / Y) / speed_of_light
#    #Z/=100
#    print(Z[0])
#
#    # convert to ps
#    Z *= (1 * 10 ** 12)
#    fig, ax = plt.subplots()
#    ax.tick_params(axis = "both", which = "both", labelsize = 12, direction = "in",
#        labelleft = True, bottom = True, top = True, left = True)
#    im = ax.imshow(Z,
#        extent = (l_values[0], l_values[-1], mp_values[0], mp_values[-1]),
#        origin = "lower",
#        aspect = "auto"
#    )
#    ax.grid(which = "both", lw = 0.5, color = "k")
#    cbar = fig.colorbar(im)
#    cbar.ax.tick_params(length = 0)
#    cbar.set_label(r"$\tau$ [ps]", horizontalalignment = "right", y = 1)
#    fig.show()
#
#    ax.set_xlabel(r"Decay Length [cm]", horizontalalignment = "right", x = 1)
#    ax.set_ylabel(r"$m_0 / p_T$", horizontalalignment = "right", y = 1)
#
#    levels = [avg_c_lifetime, avg_b_lifetime]
#    cont = ax.contour(X,Y,Z, levels = levels, colors = "k", linestyles = "dashed", labels = ["C", "B"])
#    #ax.clabel(cont, inline = 1, fmt = "%.2f")
#    ax.clabel(cont, inline = 1, fmt = { avg_c_lifetime : "C (1 ps)", avg_b_lifetime : "B (1.6 ps)" }, manual = True) #manual_locations)
#    fig.show()
#    x = input()
        

    pt_m_width = 0.1 # GeV
    pt_m_values = np.arange(0, 65 + pt_m_width, pt_m_width)
    t_width = 0.01 # ps
    t_values = np.arange(0, 2.0 + t_width, t_width)


    X, Y = np.meshgrid(t_values, pt_m_values)
    Z = Y * (speed_of_light * (X * ps_to_s))
    # convert Z to cm
    Z *= 100

    fig, ax = plt.subplots()
    ax.tick_params(axis = "both", which = "both", labelsize = 12, direction = "in",
        labelleft = True, bottom = True, top = True, left = True)
    im = ax.imshow(Z,
        extent = (t_values[0], t_values[-1], pt_m_values[0], pt_m_values[-1]),
        origin = "lower",
        aspect = "auto"
    )
    ax.grid(which = "both", lw = 0.5, color = "k")
    cbar = fig.colorbar(im)
    cbar.ax.tick_params(length = 0)
    cbar.set_label(r"Decay Length [cm]", horizontalalignment = "right", y = 1)

    ax.plot([avg_b_lifetime, avg_b_lifetime], [pt_m_values[0], pt_m_values[-1]], "w--", lw = 1)
    ax.set_xlabel(r"Lifetime, $\tau$ [ps]", horizontalalignment = "right", x = 1)
    ax.set_ylabel(r"$p_T$ / $m$", horizontalalignment = "right", y = 1)
    pt_vals = [20, 50, 100, 175, 250, 300]
    for pt in pt_vals :
        name = "$%d$ GeV" % int(pt)
        pt_m = pt / b_hadron_mass
        ax.plot( avg_b_lifetime, pt_m, "ro", markersize = 2.5)
        ax.text( 1.02 * avg_b_lifetime, pt_m - 8 * pt_m_width, name, size = 9)
    ax.text(0.95 * avg_b_lifetime, 0.2, "B", color = "white", rotation = 90)

    #ax.plot([avg_c_lifetime, avg_c_lifetime], [pt_m_values[0], pt_m_values[-1]], "w--", lw = 1)
    ##pt_vals = [5, 10, 20, 50, 80]
    #for pt in pt_vals[:3] :
    #    name = "$%d$ GeV" % int(pt)
    #    pt_m = pt / c_hadron_mass
    #    ax.plot( avg_c_lifetime, pt_m, "ro", markersize = 2.5)
    #    ax.text( 1.02 * avg_c_lifetime, pt_m - 8 * pt_m_width, name, size = 9)
    #ax.text(0.92 * avg_c_lifetime, 0.2, "D", color = "white", rotation = 90)

    levels = [0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.3]
    cont = ax.contour(X, Y, Z, levels = levels, colors = "k", linestyles = "dashed", linewidths = 1)
    ax.clabel(cont, inline = 1, fmt = "%.2f cm", fontsize = 8,  manual = True)

    fig.show()

    x = input()
        

if __name__ == "__main__" :
    main()
