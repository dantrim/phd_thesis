#!/bin/env python

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import scipy.integrate as integrate

def main() :

    fig, ax = plt.subplots(1,1)
    ax.tick_params(which = "both", direction = "in",
        top = True, right = True
    )

    norm = stats.norm(0,1)
    ymin = 5e-4
    ymax = 5
    xmin = 0.1
    xmax = 30

    x_ticks = [0.5]
    x_ticks_ = np.arange(0, xmax+35, 5)
    for x in x_ticks_ :
        x_ticks.append(x)
    ax.set_xticks(x_ticks)

    x = np.arange(xmin, xmax, 0.05)
    ax.plot(x, stats.chi2.pdf(x, df=1), color = "b", lw = 1, label = "B")
    med_b = stats.chi2.median(df = 1)
    ax.plot( [med_b, med_b], [ymin, ymax], "k--", lw = 1, alpha = 0.75)
    ax.text(0.7, 3.2, "B Median", rotation = 90, alpha = 0.7)

    print("med_b = %.5f" % med_b)
    nc = 1.7
    ax.plot(x,  stats.ncx2.pdf(x, df=1, nc=nc), "r",lw = 1, label = r"S+B ($S \sim B$)")
    med = stats.ncx2.median(df = 1, nc = nc)
    ax.plot( [med, med], [ymin, ymax], "k--", lw = 1, alpha = 0.75)
    ax.set_xlim([xmin,xmax])
    #ax.set_ylim([0, 2])
    ax.set_ylim([ymin, ymax])
    ax.set_yscale('log')

    ax.text(2.1, 3.2, "S+B Median", rotation = 90, alpha = 0.7)

    ax.set_xlabel(r"$q_{\mu}$", horizontalalignment = "right", x = 1,
        size = 15
    )
    ax.set_ylabel("Probability Density", horizontalalignment = "right", y = 1,
        size = 15,
    )

    # legend
    ax.legend(loc = "best", frameon = False,
        fontsize = 15
    )

    fig.show()
    x = input()
    fig.savefig("qmu_dist_small_s.pdf", bbox_inches = "tight")

if __name__ == "__main__" :
    main()
