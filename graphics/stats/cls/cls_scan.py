#!/bin/env python

import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
import glob
import sys, os
from cycler import cycler
from seaborn import color_palette
N = 8
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.hsv(np.linspace(0,1,N)))

#plt.rcParams["axes.prop_cycle"] = cycler(color = "cool")

scan_dir = "cls_scans/"

def main() :

    all_scan_files = glob.glob("%s/*.log" % scan_dir)

    x_vals = []
    uncert_vals = []
    for f in all_scan_files :
        name = f.split("/")[-1]
        sob = float(name.split("_")[4])
        x_vals.append(sob)
        uncert = float(name.split("_")[6].replace(".log",""))
        if uncert not in uncert_vals :
            uncert_vals.append(uncert)

    data = {} # { uncert val : y_vals }
    for uv in uncert_vals :
        data[uv] = []

    x_vals = sorted(list(set(x_vals)))
    uncert_vals = sorted(uncert_vals)

    fig, ax = plt.subplots(1,1)
    ax.set_xlabel("S / B", horizontalalignment = "right", x = 1, size = 16)
    ax.set_ylabel(r"CL$_{\mathrm{s}}$", horizontalalignment = "right", y = 1, size = 16)
    ax.tick_params(which = "both", direction = "in",
            top = True, right = True
    )

    x_lo, x_hi = 0.2, 1.5
    y_lo, y_hi = 0, 0.7
    ax.set_xlim([x_lo, x_hi])
    ax.set_ylim([y_lo, y_hi])
    ax.plot([x_lo, x_hi], [0.05, 0.05], "r--", zorder = 1e-9)
    
    points_found = []
    for uncert_val in uncert_vals :
        y_vals = []
        for sob_val in x_vals :
                for f in all_scan_files  :
                    name = f.split("/")[-1]
                    sob = float(name.split("_")[4])
                    if sob != sob_val : continue
                    uncert = float(name.split("_")[6].replace(".log",""))
                    if uncert != uncert_val : continue

                    p = (uncert_val, sob_val)
                    if p in points_found : continue
                    with open(f, "r") as infile :
                        for line in infile :
                            line = line.strip()
                            if not line : continue
                            if "CLs" not in line : continue
                            if "CLb" in line : continue
                            if "CLsplusb" in line : continue
                            #print("(%.2f, %.2f) = %s" % (sob_val, uncert_val, line))
                            cls_val = float(line.split("=")[-1].split("+/-")[0])
                            y_vals.append(cls_val)
                            points_found.append(p)
                            data[uv].append(cls_val)
        x_new = np.linspace(x_lo, x_hi, 300)
        smoothed = spline(x_vals, y_vals, x_new)
        ax.plot(x_new, smoothed, label = "%.0f%%" % (100*uncert_val))

        #ax.plot(x_vals, y_vals, label = "%.2f" % uncert_val)
    ax.legend(loc = (0.4,0.2), frameon = False,
            title = "Background Systematic",
            fontsize = 12,
            title_fontsize = 14
    )

    ax.text(0.81, 0.56, r"$N_{\mathrm{background}} = 20$", size = 16)
    ax.text(0.85, 0.62, r"$N_{\mathrm{observed}} = 20$", size = 16)
    
    fig.savefig("cls_bkguncert_scan.pdf", bbox_inches = "tight")
    fig.show()
    x = input()
            
        

if __name__ == "__main__" : 
    main()
