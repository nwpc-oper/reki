import io

import pandas as pd
import numpy as np


SHORT_NAME_TABLE_CONTENT = """
short_name,discipline,parameterCategory,parameterNumber
ACPCP,0,1,10
ALBDO,0,19,1
APCP,0,1,8
ASNOW,0,1,29
BLI,0,7,1
CAPE,0,7,6
CDCC,0,6,22
CIN,0,7,7
CLWMR,0,1,22
DEPR,0,0,7
DPT,0,0,6
DZDT,0,2,9
EPOT,0,0,3
GRLE,0,1,32
GUST,0,2,22
HCDC,0,6,5
HFLUX,2,0,24
HGT,0,3,5
HLCY,0,7,8
HPBL,0,3,18
ICMR,0,1,23
KX,0,7,2
LCDC,0,6,3
LHTFL,0,0,10
MCDC,0,6,4
NCPCP,0,1,9
NLWRF,0,5,5
NSWRF,0,4,9
NSWRFCS,0,4,11
PLI,0,7,0
PRES,0,3,0
PRMSL,0,3,1
PTYPE,0,1,19
PWAT,0,1,3
RELD,0,2,13
RELV,0,2,12
RETOP,0,16,3
RH,0,1,1
RI,0,7,12
RWMR,0,1,24
SHWINX,0,7,13
SNMR,0,1,25
SNOD,0,1,11
SPFH,0,1,0
SX,0,7,5
TCDC,0,6,1
TCIWV,0,1,64
TCOLI,0,1,70
TCOLW,0,1,69
TMAX,0,0,4
TMIN,0,0,5
TMP,0,0,0
TOTALX,0,7,4
UGRD,0,2,2
ULWRF,0,5,4
UPHL,0,7,15
USWRF,0,4,8
VGRD,0,2,3
VIS,0,19,0
VWSH,0,2,25
"""


def get_short_name_table():
    f = io.StringIO(SHORT_NAME_TABLE_CONTENT)
    df = pd.read_table(
        f,
        header=0,
        sep=",",
    )
    return df


SHORT_NAME_TABLE = get_short_name_table()
