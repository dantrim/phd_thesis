#!/bin/env python

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.ticker as ticker
import numpy as np
import sys, os

N = 9
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.hsv(np.linspace(0,1,N)))

def higgs_br(which = "bb") :

    br_dict = {
        "bb" : 0.5809
        ,"tautau" : 0.06256
        ,"mumu" : 0.0002171
        ,"cc" : 0.0284
        ,"gg" : 0.08180
        ,"gamgam" : 0.00227
        ,"zgam" : 0.001541
        ,"ww" : 0.2152
        ,"zz" : 0.02641
    }

    return br_dict[which]

def x_idx(which = "bb") :

    br_idx = {
        "bb" : 0
        ,"ww" : 1
        ,"gg" : 2
        ,"tautau" : 3
        ,"cc" : 4
        ,"zz" : 5
        ,"gamgam" : 6
        ,"zgam" : 7
        ,"mumu" : 8
    }

    return br_idx[which]

def y_idx(which = "bb") :

    br_idx = {
        "bb" : 8
        ,"ww" : 7
        ,"gg" : 6
        ,"tautau" : 5
        ,"cc" : 4
        ,"zz" : 3
        ,"gamgam" : 2
        ,"zgam" : 1
        ,"mumu" : 0
    }

    return br_idx[which]

def br_name(which = "bb") :

    names = {
        "bb" : r"$bb$"
        ,"ww" : r"$WW$"
        ,"gg" : r"$gg$"
        ,"tautau" : r"$\tau \tau$"
        ,"cc" : r"$cc$"
        ,"zz" : r"$ZZ$"
        ,"gamgam" : r"$\gamma \gamma$"
        ,"zgam" : r"$Z \gamma$"
        ,"mumu" : r"$\mu \mu$"
    }
    return names[which]

def main() :

    higgs_decays = ["bb", "ww", "gg", "tautau", "cc", "zz", "gamgam", "zgam", "mumu"]
    n_bins = len(higgs_decays)
    data = {}

    bbbb_br = higgs_br("bb") * higgs_br("bb")
    vals = []
    for i in range(n_bins) :
        for j in range(n_bins) :
            if j < i : continue
            bin_tuple = tuple((x_idx(higgs_decays[i]), y_idx(higgs_decays[j])))
            hh_br = higgs_br(higgs_decays[i]) * higgs_br(higgs_decays[j])
            val = hh_br / bbbb_br
            vals.append(val) 
            data[bin_tuple] = val
            #print("({},{}) --> ({},{})".format(higgs_decays[i], higgs_decays[j], x_idx(higgs_decays[i]), y_idx(higgs_decays[j])))


    vals = list(set(vals))
    min_val = min(vals)
    fig, ax = plt.subplots(1,1)
    labels = [br_name(x) for x in higgs_decays]
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels[::-1])
    ax.tick_params(which = "both", direction = "in", length = 0)
    bw = 1
    bins = np.arange(0,len(higgs_decays)+1, bw)
    ax.set_xticks(bins[:-1]+0.5 * bw) #, minor = True)
    ax.set_yticks(bins[:-1]+0.5 * bw) #, minor = True)
    ax.set_xticks(bins[:-1], minor = True)# +0.5 * bw)
    ax.set_yticks(bins[:-1], minor = True)# +0.5 * bw)

    x_vals = []
    y_vals = []
    w_vals = []
    for dp, w in data.items() :
        x, y = dp
        x_vals.append(x)
        y_vals.append(y)
        w_vals.append(w)

    h, x, y, im = ax.hist2d(x_vals, y_vals, bins = bins,
        weights = w_vals,
        cmin = min_val,
        #cmap = plt.cm.hsv(np.linspace(0,1,N))
        #cmap = "YlGnBu",
        #cmap = "YlOrRd",
        cmap = "jet",
        norm = LogNorm()
    )
    cbar = fig.colorbar(im)
    cbar.set_label("Branching fraction relative to 4b",
		horizontalalignment = "right",
		y = 1,
		size = 14
	)
#    ax.xaxis.set_major_formatter(ticker.NullFormatter())
#    for tick in ax.xaxis.get_minor_ticks() :
#        tick.label1.set_horizontalalignment("center")

    ax.grid(which = "minor", alpha = 0.8)
    #ax.set_ylabel("Larger BR", horizontalalignment = "right", y = 1)

	# bbbb
    ax.text(0.16, 8.6, r"100%", size = 7, weight = "bold", color = "white")
    ax.text(0.14, 8.33, r"(34%)", size = 7, weight = "bold", color = "white")
    #ax.text(0.25, 7.41, r"13%", size = 6, weight = "bold", color = "white")

	# bbww
    ax.text(0.25, 7.6, r"38%", size = 7, weight = "bold", color = "white")
    ax.text(0.14, 7.33, r"(13%)", size = 7, weight = "bold", color = "white")

	## wwww
    ##ax.text(1.25, 7.41, r"5%", size = 8, weight = "bold", color = "white")
    #ax.text(1.25, 7.6, r"14%", size = 7, weight = "bold", color = "white")
    #ax.text(1.19, 7.33, r"(5%)", size = 7, weight = "bold", color = "white")

	# bbtautau
    #ax.text(0.27, 5.41, r"4%", size = 8, weight = "bold", color = "white")
    ax.text(0.25, 5.6, r"11%", size = 7, weight = "bold", color = "white")
    ax.text(0.21, 5.33, r"(4%)", size = 7, weight = "bold", color = "white")

	# bbyy
    #ax.text(0.20, 2.41, r"<1%", size = 8, weight = "bold", color = "k")
    ax.text(0.20, 2.58, r"0.4%", size = 7, weight = "bold", color = "k")
    ax.text(0.11, 2.33, r"(0.1%)", size = 7, weight = "bold", color = "k")

    #fig.show()
    fig.savefig("hh_br.eps", bbox_inches = "tight")
    fig.savefig("hh_br.pdf", bbox_inches = "tight")
    #x = input()
    

    

if __name__ == "__main__" :
    main()
