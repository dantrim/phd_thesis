#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

class Lumi :
    def __init__(self, number, year, month, day, lumi) :
        self.number = number
        self.year = year
        self.month = month
        self.day = day
        self.lumi = lumi # pb

    def __eq__(self, other) :
        return self.year == other.year and self.month == other.month and self.day == other.day

def main() :

    lumi_shifts = []
    lumi_id = -1
    years = { 2016 : 0, 2017 : 1, 2018 : 2 }
    shift_lumi = {}
    shift_keys = {}
    shift_key_vals = []

    with open("lumi_dantrim.txt", "r") as infile :
        for line in infile :
            line = line.strip()
            if line.startswith("#") : continue
            if "YEAR" in line : continue
            fields = line.split()
            year = int(fields[0])
            month = int(fields[1])
            day = int(fields[2])
            lumi = float(fields[3])
            key_str = "%d_%d_%d" % (year, month, day)
            lc = Lumi(lumi_id, years[year], month, day, lumi)
            if key_str in shift_lumi :
                shift_lumi[key_str] += lumi
            else :
                shift_lumi[key_str] = lumi
                lumi_id += 1
                shift_keys[lumi_id] = key_str
                shift_key_vals.append(lumi_id)
            lumi_shifts.append(lc)

    print("found %s shifts" % len(shift_lumi))

    x_vals = shift_key_vals
    y_vals = []
    for lid in shift_key_vals :
        key = shift_keys[lid]
        y_vals.append(shift_lumi[key])
    y_vals = np.cumsum(y_vals)

    plt.plot(x_vals, y_vals, "r-")
    plt.show()
    x = input()

if __name__ == "__main__" :
    main()
