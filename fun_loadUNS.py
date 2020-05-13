"""
May 12th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.01.00
# fun_loadUNS.py  -  this program has the function the UNSfile load to Field View.
### this program is only available on FieldView ###

from fv import *

def fun_loadUNS(filepath):
    print(filepath + " now loading ...")
    #define data input table
    data_input_table = {
        "data_format": "unstructured",
        "input_parameters": {
            "name": filepath,
            "options": {
                "input_mode": "replace",
                "transient": "on"
            },
        }
    }

    # call function to read dataset
    read_dataset(data_input_table)


if __name__ == "__main__":
    filepath = "./fvAVE_WM2DsmallP1_res10.uns"
    fun_loadUNS(filepath)