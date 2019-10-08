#!/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def main() :

    fig, ax = plt.subplots(1,1)
    ax.set_xlabel("x", horizontalalignment = "right", x = 1)
    ax.set_ylabel("Probability Density", horizontalalignment = "right", y = 1)
    ax.tick_params(which = "both", direction = "in", right = True, top = True)
    x_vals = np.arange(-10, 10, 0.001)

    do_log = False

    x_lo, x_hi = 0, 6
    y_lo, y_hi = 0, 0.45
    line_hi = 0.4 * y_hi
    if do_log :
        y_lo = 1e-9
        y_hi = 10
        line_hi = 0.35
        text_loc = 0.6

    ax.set_xlim([x_lo, x_hi])
    ax.set_ylim([y_lo, y_hi])
    ax.plot(x_vals, norm.pdf(x_vals, 0, 1), "r-")
    ax.plot([0, 0], [y_lo, y_hi], "k--", alpha = 0.2, lw = 1)

    ax.plot([1.64, 1.64], [y_lo, line_hi], "k-")
    ax.plot([3, 3], [y_lo, line_hi], "k-")
    ax.plot([5, 5], [y_lo, line_hi], "k-")

    text_hi = 1.1 * line_hi
    if do_log :
        text_hi = 1.2 * line_hi

    ax.text(1.65, text_hi, "Z = 1.64")
    ax.text(3,    text_hi, "Z = 3")
    ax.text(5,    text_hi, "Z = 5")

    if do_log :
        ax.set_yscale("log")

    fig.savefig("pval_sig_lin.pdf", bbox_inches = "tight")
    #fig.show()
    #x = input()


if __name__ == "__main__" :
    main()
