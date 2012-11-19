"""
API for enzo_test

Author: Matthew Turk <matthewturk@gmail.com>
Affiliation: UCSD
Author: J.S. Oishi <jsoishi@gmail.com>
Affiliation: KIPAC/SLAC/Stanford
Author: Britton Smith <brittonsmith@gmail.com>
Affiliation: MSU
Homepage: http://yt-project.org/
License:
  Copyright (C) 2010-2011 Matthew Turk.  All Rights Reserved.

  This file is part of yt.

  yt is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from .runner import \
    RegressionTestRunner, \
    RegressionTestStorage, \
    clear_registry, \
    registry_entries

from .output_tests import \
    YTStaticOutputTest, \
    create_test

from .default_tests import \
    TestFieldStatistics, \
    TestAllProjections

from .xunit import \
    Xunit

from .halo_tests import \
    TestHaloCompositionHashHOP, \
    TestHaloCompositionHashFOF, \
    TestHaloCompositionHashPHOP

from .boolean_region_tests import \
    TestBooleanANDGridQuantity, \
    TestBooleanORGridQuantity, \
    TestBooleanNOTGridQuantity, \
    TestBooleanANDParticleQuantity, \
    TestBooleanORParticleQuantity, \
    TestBooleanNOTParticleQuantity

try:
    from .framework import AnswerTesting
except ImportError:
    raise
