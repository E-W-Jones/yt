# EWJ: Taken almost verbatim from unyt - however this is essentially the same as yt.units.physical_constants.
# Which in the original issue I had already identified as a replacement
# Unless of course, yt.units is going to be gotten rid of...
# In which case we keep this
from unyt import unyt_quantity as _unyt_quantity  # noqa EWJ: Ignore error for now, delete if we actually don't end up using it
from unyt.unit_registry import default_unit_registry as _default_unit_registry
from unyt.unit_systems import add_constants as _add_constants

_add_constants(globals(), registry=_default_unit_registry)
# This PR actually gets rid of amu_cgs elsewhere: https://github.com/yt-project/yt/pull/4722/changes/dd9625125e2af262b55c686abab1bbfbc19f494c
# amu_cgs == _unyt_quantity(1.0, "amu").in_cgs()

"""
# Small script that checks all the imports I found through either searching repo for physical_constants imports or pytest are either accounted for, or defines a new form to use
import yt.utilities.physical_constants as ytc
import unyt
from unyt import unyt_quantity

assert ytc.amu_cgs == unyt_quantity(1, "amu").in_cgs()

const_names = ["gravitational_constant_cgs", "G", "mu_0", "boltzmann_constant_cgs", "c", "speed_of_light", "speed_of_light_cgs", "clight", "hcgs", "kboltz", "kb", "mh", "me", "mp", "mass_hydrogen_cgs"]
for name in const_names:
    assert getattr(ytc, name) == getattr(unyt, name)
"""
