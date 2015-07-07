######################################
#    Created on Jun 11, 2015
#
#    @author: nqian
#
#    Module for all constants
######################################

from enum import Enum

class Plot(Enum):
    baseplot = 0
    backscattered = 1
    depolarized = 2
    vfm = 3

plot_type_enum = {'base_plot': Plot.baseplot,
                  'backscattered': Plot.backscattered,
                  'depolarized': Plot.depolarized,
                  'vfm': Plot.vfm}

HEIGHT = 665
WIDTH = 1265
CHILDWIDTH = 200
CHILDHEIGHT = 325
IMPORTWIDTH = 1000
IMPORTHEIGH = 500

BASE_PLOT = 0
BACKSCATTERED = 1
DEPOLARIZED = 2
VFM = 3

FILE_NAME = 0
COLOR = 1
ATTRIBUTES = 2
CUSTOM = 3

BASE_PLOT_STR = "base_plot"
BACKSCATTERED_STR = "backscattered"
DEPOLARIZED_STR = "depolarized"
VFM_STR = "vfm"

PLOTS = ["base_plot", "backscattered", "depolarized", "vfm"]

VERTICES = "vertices"
DATE = "date"

# READ ONLY
TAGS = ['aerosol', 'aerosol LC', 'clean continental', 'clean marine', 'cloud', 'cloud LC',
        'dust', 'polluted continental', 'polluted continental dust', 'polluted dust',
        'polluted marine', 'smoke', 'stratospheric layer']

TKXMID = 629.5
TKYMID = 314

LOG_FILENAME = 'log/CALIPSO_debug.log'
