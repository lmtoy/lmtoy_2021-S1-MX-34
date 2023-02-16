#! /usr/bin/env python
#
#   script generator for project="2021-S1-MX-34"
#

import os
import sys

try:
    lmtoy = os.environ["LMTOY"]
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2021-S1-MX-34"

on = {}

on["G12-42911"] = [ 98436, 98437, 98438, 98443, 98444, 98445, 98448,
                    98449, 98450, 98469, 98470, 98471, 98566, 98567,
                    98568, 98570, 98571, 98572, 98574, 98575, 98576,]

on["NGP-131281"] = [ 98607, 98608, 98609, 98612, 98613, 98614, 98616,
                     98617, 98618, 98620, 98621, 98622, 99850, 99851,
                     99852, 99854, 99855, 99856, 99858, 99979, 99980,
                     99981, 99983, 99984, 99985, 99987, 99988, 99989,
                     100388, 100389, 100390, 100392, 100393, 100394,]

pars1 = {}

pars1["G12-42911"] = ""
pars1["NGP-131281"] = ""

pars2 = {}

pars2["G12-42911"] = ""
pars2["NGP-131281"] = ""

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2)


#        1/1,3,3 are bad for all the series
#        3/5 was bad until Gopal reseated : on 5-may-2022 ?
pars1 = {}
pars1['G12-42911']  = "restart=1 badcb=1/1,3/3"
pars1['NGP-131281'] = "restart=1 badcb=1/1,3/3"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['G12-42911']  = ""
pars2['NGP-131281'] = ""

