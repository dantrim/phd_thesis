#!/bin/env python

from math import sqrt

# fermion masses taken from PDG: http://pdglive.lbl.gov

higgs_vev = 246 # GeV

fermion_masses = { # GeV
    "electron" : 0.000511
    ,"muon" : 0.1057
    ,"tau" : 1.777
    ,"up" : 0.0022
    ,"down" : 0.00467
    ,"charm" : 1.27
    ,"strange" : 0.093
    ,"bottom" : 4.18
    ,"top" : 172.9
}

gev_to_mev = 1e3

def mass_to_yukawa(mass) :
    return sqrt(2) * mass / higgs_vev

def main() :

    leptons = ["electron", "muon", "tau"]
    quarks = ["up", "down", "charm", "strange", "top", "bottom"]

    print 55 * "-"
    print "Leptons:"
    for l in leptons :
        mass = fermion_masses[l]
        print "%15s: %.6f --> %4f" % (l, mass, mass_to_yukawa(mass))
    print 55 * "-"
    print "Quarks:"
    for l in quarks :
        mass = fermion_masses[l]
        print "%15s: %.6f --> %4f" % (l, mass, mass_to_yukawa(mass))


if __name__ == "__main__" :
    main()
