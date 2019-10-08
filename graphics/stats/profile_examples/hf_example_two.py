#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import os, sys
import argparse

def do_plot(post = False) :

    data_vals = [100, 100]
    bkg_vals = [80, 100]
    sig_val = 20
    bkg_uncerts = [0.5, 0.14]
    if post :
        bkg_vals = [80, 100]
        bkg_uncerts = [0.136, 0.1]

    fig, ax = plt.subplots(1,1)
    ax.set_xticks([0.5, 1.5])
    ax.set_xticklabels(["Region 1", "Region 2"])
    ax.set_ylabel("Yield", horizontalalignment = "right", y = 1)
    ax.set_xlabel("")
    ax.set_xlim([0,2])
    ax.set_ylim([0,180])
    ax.tick_params(which = "both", direction = "in",
        top = True, right = True
    )

    # draw mc
    #ax.bar([0.5], bkg_vals[0], color = "#bb2a33",
    #    width = 1,
	#	label = "Bkg 1"
    #)
    ax.bar([0.5], 100, color = "#cccc65", width = 1, label = "Signal")
    ax.bar([0.5], bkg_vals[0], color = "#bb2a33",
        width = 1,
		label = "Bkg 1"
    )
    ax.bar([1.5], bkg_vals[1], color = "#286fb0",
        width = 1,
		label = "Bkg 2"
    )

    # draw mc error bars
    if not post :
        err_lo = bkg_vals[0] - bkg_uncerts[0] * bkg_vals[0]
        err_hi = bkg_vals[0] + bkg_uncerts[0] * bkg_vals[0]
        e_lo = np.array([err_lo, err_lo])
        e_up = np.array([err_hi, err_hi])
        x =  np.array([0,1])
        ax.fill_between(x, e_lo+20, e_up+20, hatch = "///",
            facecolor = "none", edgecolor = "k", linewidth = 0, zorder = 1e9)
    else :
        err_lo = bkg_vals[0] - bkg_uncerts[0] * bkg_vals[0]
        err_hi = bkg_vals[0] + bkg_uncerts[0] * bkg_vals[0]
        e_lo = np.array([err_lo, err_lo])
        e_up = np.array([err_hi, err_hi])
        x =  np.array([0,1])
        ax.fill_between(x, e_lo+20, e_up+20, hatch = "///",
            facecolor = "none", edgecolor = "k", linewidth = 0, zorder = 1e9)
        

    err_lo = bkg_vals[1] - bkg_uncerts[1] * bkg_vals[1]
    err_hi = bkg_vals[1] + bkg_uncerts[1] * bkg_vals[1]
    e_lo = np.array([err_lo, err_lo])
    e_up = np.array([err_hi, err_hi])
    x =  np.array([1,2])
    ax.fill_between(x, e_lo, e_up, hatch = "///",
        facecolor = "none", edgecolor = "k", linewidth = 0, zorder = 1e9)

    # draw data
    data_err = [10, 10]
    ax.plot([0.5, 1.5], data_vals, "ko",
		label = "Data",
		markersize = 8
	)
    ax.errorbar([0.5, 1.5], data_vals, yerr = data_err, xerr = 0,
        linestyle = "none",
        marker = "o",
        color = "k",
        markersize = 0,
		linewidth = 2
    )

	# legend
    ax.legend(loc = "upper right", frameon = False, prop = {"size" : 15})

    # labels
    label = "Pre-fit"
    if post :
        label = "Post-fit"
    ax.text(0.1, 160, label, size = 20, weight = "bold")
    ax.text(0.1, 150, "Bkg 1 Pre-fit Uncertainty: 50%", size = 10)

    fig.show()
    outname = "profile_ex_2_"
    if post :
    	outname += "post"
    else :
    	outname += "pre"
    outname += ".pdf"
    fig.savefig(outname, bbox_inches = "tight")
    x = input()

def do_pull() :

    bkg0 =   [0, 0.993]
    bkg1_0 = [0, 0.814]
    bkg1_1 = [0, 0.814]
    mu     = [1, 1.9]


    fig, ax = plt.subplots(1,1)
    ax.tick_params(which = "both", direction = "in",
        top = True, right = True
    )

    x_lims = [0, 4]
    y_lims = [-2, 3]
    ax.set_xlim(x_lims)
    ax.set_ylim(y_lims)
    ax.set_xlabel("")
    ax.set_ylabel(r"Post Fit $\theta$")
    ax.set_xticks([0.5, 1.5, 2.5, 3.5])
    ax.set_xticklabels(["Norm. Bkg 1", r"Norm. Bkg 2$_1$", r"Norm. Bkg 2$_2$", r"$\mu_{\mathrm{sig}}$"])

    x_vals = [0.5, 1.5, 2.5]
    y_vals = [bkg0[0], bkg1_0[0], bkg1_1[0]]
    y_errs = [bkg0[1], bkg1_0[1], bkg1_1[1]]

    ax.errorbar(x_vals, y_vals, yerr = y_errs, xerr = 0,
        linestyle = "none",
        color = "k",
        marker = "o",
        linewidth = 1,
        markersize = 6,
        capsize = 2
    )
    x_vals = [3.5]
    y_vals = [mu[0]]
    y_errs = [mu[1]]
    ax.errorbar(x_vals, y_vals, yerr = y_errs, xerr = 0,
        linestyle = "none",
        color = "r",
        marker = "o",
        linewidth = 1,
        markersize = 6,
        capsize = 2
    )

    # lines
    ax.plot(x_lims, [0,0], "r--")
    ax.plot(x_lims, [1,1], "b-")
    ax.plot(x_lims, [-1,-1], "b-")

    fig.show()
    fig.savefig("profile_ex_2_pulls.pdf", bbox_inches = "tight")
    x = input()

def main() :

    do_plot(post = False)
    do_plot(post = True)
    do_pull()

if __name__ == "__main__" :
    main()
