"""
May 12th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.01.00
# fun_pointprobe.py  -  this program has the function to culculete a point probe.
### this program is only available on FieldView ###

from fv import *
import numpy as np
from fun_coordnate import fun_createCOORD

# load point list
def fun_loadLIST(listpath):
    pointlist = np.loadtxt(listpath)
    return pointlist


def fun_culPPROBE(listpath, scalartype, outname):
    # load point list
    print("Now loadinf point list ...")
    pointlist = fun_loadLIST(listpath)
    X = pointlist[0, 0]
    Y = pointlist[0, 1]
    Z = pointlist[0, 2]

    # create coordinate surface
    print("Now creating coordnaite surface ...")
    fun_createCOORD(scalartype, "X", X)
    fun_createCOORD(scalartype, "Y", Y)    
    fun_createCOORD(scalartype, "Z", Z)

    # create output file (header)
    fp_output = open(outname, "a")
    header = "X Y Z " + scalartype + "\n"
    fp_output.writelines(header)
    
    for row in pointlist:
        # 1: X, 2: Y, 3: Z
        point = {1: row[0], 2: row[1], 3: row[2]}

        # check same position
        if row[0] != X and row[1] != Y and row[2] != Z:
            print("Now creating coordnaite surface ...")
            fun_createCOORD(scalartype, "X", row[0])
            fun_createCOORD(scalartype, "Y", row[1])
            fun_createCOORD(scalartype, "Z", row[2])

        probeout = probe_current_functions(point)
        pscalar = probeout.get("scalar")
        pkey = pscalar.get("func")
        pvalue = pscalar.get("value")
        print("key: " + str(pkey) + ", " + "value: " + str(pvalue))
        
        datalist = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(pvalue) + "\n"
        fp_output.writelines(datalist)
        
        # memory X, Y, Z position
        X = row[0]
        Y = row[1]
        Z = row[2]

    fp_output.close()

if __name__ == "__main__":
    from fun_loadUNS import fun_loadUNS
    filepath = "./rect_duct_001.uns"
    fun_loadUNS(filepath)
    listpath = "./test_plot.txt"
    scalartype = "u-velocity"
    outname = "./test_out.txt"
    fun_culPPROBE(listpath, scalartype, outname)