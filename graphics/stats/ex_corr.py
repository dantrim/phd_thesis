#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys, os

def example_1() :

    fig, ax = plt.subplots(1,1)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    data_grid = {
        (0,0) : 0,
        (0,1) : 0,
        (0,2) : 1,
        (1,0) : -0.5,
        (1,1) : 1,
        (1,2) : 0,
        (2,0) : 1,
        (2,1) : -0.5,
        (2,2) : 0
    }
    bw = 1
    bins = np.arange(0, 4, bw)
    ax.tick_params(which = "both", direction = "out")
    ax.set_xticks(bins[:-1]+0.5*bw)
    ax.set_yticks(bins[:-1]+0.5*bw)
    ax.set_xticklabels(["Norm. Bkg 1", r"Norm. Bkg 2$_1$", r"Norm. Bkg 2$_2$"])
    ax.set_yticklabels([r"Norm. Bkg 2$_2$", r"Norm. Bkg 2$_1$", "Norm. Bkg. 1"],
        rotation = 50)
    #sys.exit()

    x_vals = []
    y_vals = []
    w_vals = []
    for dp, w in data_grid.items() :
        x, y = dp
        x_vals.append(x)
        y_vals.append(y)
        w_vals.append(w)


    h, x, y, im = ax.hist2d(x_vals, y_vals, bins = bins, weights = w_vals)
    cbar = fig.colorbar(im)
    cbar.set_label("NP Correlation", horizontalalignment = "right", y = 1)

    for dp, w in data_grid.items() :
        ax.text(dp[0]+0.4 * bw, dp[1]+0.45 * bw, r"$\mathbf{%.2f}$" % float(w), color = "w")

    fig.show()
    fig.savefig("np_corr_ex_1.pdf", bbox_inches = "tight")
    x = input()

def example_2() :

    fig, ax = plt.subplots(1,1)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    data_grid = {
        (0,0) : -0.97,
        (0,1) : 0,
        (0,2) : 0,
        (0,3) : 1,
        (1,0) : 0,
        (1,1) : -0.5,
        (1,2) : 1,
        (1,3) : 0,
        (2,0) : 0,
        (2,1) : 1,
        (2,2) : -0.5,
        (2,3) : 0,
        (3,0) : 1,
        (3,1) : 0,
        (3,2) : 0,
        (3,3) : -0.97
        
    }
    bw = 1
    bins = np.arange(0, 5, bw)
    ax.tick_params(which = "both", direction = "out")
    ax.set_xticks(bins[:-1]+0.5*bw)
    ax.set_yticks(bins[:-1]+0.5*bw)
    ax.set_xticklabels(["Norm. Bkg 1", r"Norm. Bkg 2$_1$", r"Norm. Bkg 2$_2$", r"$\mu_{\mathrm{sig}}$"])
    ax.set_yticklabels([r"$\mu_{\mathrm{sig}}$", r"Norm. Bkg 2$_2$", r"Norm. Bkg 2$_1$", "Norm. Bkg. 1"],
        rotation = 50)
    #sys.exit()

    x_vals = []
    y_vals = []
    w_vals = []
    for dp, w in data_grid.items() :
        x, y = dp
        x_vals.append(x)
        y_vals.append(y)
        w_vals.append(w)


    h, x, y, im = ax.hist2d(x_vals, y_vals, bins = bins, weights = w_vals)
    cbar = fig.colorbar(im)
    cbar.set_label("NP Correlation", horizontalalignment = "right", y = 1)

    for dp, w in data_grid.items() :
        ax.text(dp[0]+0.4 * bw, dp[1]+0.45 * bw, r"$\mathbf{%.2f}$" % float(w), color = "w")

    fig.show()
    fig.savefig("np_corr_ex_2.pdf", bbox_inches = "tight")
    x = input()

if __name__ == "__main__" :

    #example_1()
    example_2()
