"""
May 13th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.01.00
# FLOWS_pointprobe.py  -  this program probes some points in FLOWS.
### this program is only available on FieldView ###

from fun_loadUNS import fun_loadUNS
from fun_coordinate import fun_createCOORD
from fun_pointprobe import fun_culPPROBE
import os
import re


### Parameter
## FLOWS file parameter
unsfile = "F:/mizu_data/WM-2D/smallP7/res11/movieWM2DsP7P0001.uns"
start_number = 1
end_number = 3
# file_numdigit: NUmber of digits for UNS file numbering
file_numdigit = 4

## point probe parameter
pointlist = "F:/mizu_data/fieldview/WM_test_plot.txt"
outfilename = "WM_test_out.txt"
# scalartype: scalar type to probe("PRESSUR", "U,V,W-VELOCITY", etc...)
scalartype = "U-VELOCITY"


### function
def fun_basename(path, filetype):
    basename = os.path.basename(path)
    basename = basename.rstrip("." + filetype)
    basename = re.sub(r"\d\d+", "", basename)
    directoryname = os.path.split(path)[0] + "/"
    return basename, directoryname

def fun_callnumber(Snumber, Enumber, digit):
    numlist = []
    for num in range(Snumber, Enumber + 1):
        number = str(num)
        if len(number) < digit:
            notenough = digit - len(number)
            for zero in range(notenough):
                number = "0" + number
        elif len(number) > digit:
            print("ERROR: Wrong digit definition ...")
            return
        numlist.append(number)
    return numlist

def main(unsfile, pointlsit, scalartype, outfilename):
    fun_loadUNS(unsfile)
    fun_culPPROBE(pointlist, scalartype, outfilename)

### main
uns_base, uns_dir = fun_basename(unsfile, "uns")
numlist = fun_callnumber(start_number, end_number, file_numdigit)

tmp_base, out_dir = fun_basename(pointlist, "txt")
outpath = out_dir + outfilename

for i in numlist:
    unspath = uns_dir + uns_base + i + ".uns"
    print(uns_base + i + " Now doing ...")
    main(unspath, pointlist, scalartype, outpath)

print("Successfull!!")