#! /usr/bin/env python
#
#   script generator for project="2021-S1-UM-11"
#

import os
import sys

project="2021-S1-UM-11"

#        obsnums per source (make it negative if not added to the final combination)
#  initial test cases are J113833 and J132227 (where the J was accidentally dropped from the name)
on = {}
on['G12-42911']  = [98436, 98437, 98438, 98443, 98444, 98445, 98448, 98449, 98450,
                    98469, 98470, 98471, 98566, 98567, 98568, 98570, 98571, 98572,
                    98574, 98575, 98576,
                    ]


on['NGP-131281'] = [98607, 98608, 98609, 98612, 98613, 98614, 98616, 98617, 98618,
                    98620, 98621, 98622, 99850, 99851, 99852, 99854, 99855, 99856,
                    99858, 99979, 99980, 99981, 99983, 99984, 99985, 99987, 99988, 99989,
                    100388, 100389, 100390, 100392, 100393, 100394,
                    ]


#        common parameters per source on the first dryrun (run1, run2)
#        1/1,3,3 are bad for all the series
#        3/5 was bad until Gopal reseated : on 5-may-2022 ?
pars1 = {}
common1="admit=0 restart=1 badcb=1/1,3/3"
pars1['G12-42911']  = ""
pars1['NGP-131281'] = ""

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
common2="admit=0 restart=1 srdp=1"
pars2['G12-42911']  = ""
pars2['NGP-131281'] = ""



# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument -- deprecated
def getargs3(obsnum):
    """ search for <obsnum>.args
    """
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        args = ""
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
        return args
    else:
        return ""

#        specific parameters per obsnum will be in files <obsnum>.args -- deprecated
pars3 = {}
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        pars3[o] = getargs3(o)

#        obsnum.args is alternative single file pars file to set individual parameters
pars4 = {}
if os.path.exists("obsnum.args"):
    lines = open("obsnum.args").readlines()
    for line in lines:
        if line[0] == '#': continue
        w = line.split()
        pars4[int(w[0])] = w[1:]
        print('PJT',w[0],w[1:])

def getargs(obsnum):
    """ search for <obsnum> in obsnum.args
    """
    args = ""
    if obsnum in pars4.keys():
        print("PJT2:",obsnum,pars4[obsnum])
        for a in pars4[obsnum]:
            args = args + " " + a
    return args

run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run1b = '%s.run1b' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run1b, "w")

fp4 = open(run2,  "w")
fp5 = open(run2a, "w")

#                           single obsnum
n1 = 0
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 %s %s" % (o,s,pars1[s], pars2[s], getargs(o))
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1" % (o,s,pars1[s])
        cmd3 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 %s" % (o,s,pars2[s], getargs(o))
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        fp3.write("%s\n" % cmd3)
        n1 = n1 + 1

#                           combination obsnums
n2 = 0        
for s in on.keys():
    obsnums = ""
    n3 = 0
    for o1 in on[s]:
        o = abs(o1)
        if o1 < 0: continue
        n3 = n3 + 1
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d/%d] :' % (s,n3,len(on[s])), obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd5 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp4.write("%s\n" % cmd4)
    fp5.write("%s\n" % cmd5)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1a)
print(run2)
print(run1b)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))

