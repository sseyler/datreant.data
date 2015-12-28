# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# datreant

"""
datreant.data --- basic data storage backends for datreant.limbs.Data
=====================================================================

"""
from .core import DataFile
from . import pydata, npdata, pddata
from . import tests

# attach limbs to datreant objects
from . import attach

__all__ = ['pydata', 'npdata', 'pddata']