"""
May 12th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.01.00
# fun_coordinate.py  -  this program has the function to create a coordinate surface.
### this program is only available on FieldView ###

from fv import *

# scalartype: U,V,W-VELOCITY, PRESSUER, etc...
# axis: Cutting axis -> X, Y, Z
# position: Cutting position (can use "min" & "max")
def fun_createCOORD(scalartype, axis, position):
    # define coordinate surface table
    coord_table = {
        "dataset": 1,
        "scalar_func": scalartype,
        "axis": axis,
        axis + "_axis": {"current": position},
        "display_type": "constant_shading",
    }

    # create coordinate surface
    create_coord(coord_table)


if __name__ == "__main__":
    from fun_loadUNS import fun_loadUNS
    filepath = "./rect_duct_001.uns"
    fun_loadUNS(filepath)
    fun_createCOORD("u-velocity", "Z", 0.0127)