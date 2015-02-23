#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Turn earthquake RDF objects into earthquake python objects
"""

__author__ = "Marc Tim Thiemann"
__copyright__ = "Copyright 2015"
__credits__ = ["Marc Tim Thiemann"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""
__date__ = "February 2015"
__status__ = "Development"

import sys
sys.path.insert(1,'../../../CoreConceptsPy')
sys.path.insert(1, '../../../CoreConceptsRDF')
from earthquake import *
from RDFReader import *

rdf = RDFReader()
earthquakes = rdf.read('test.rdf', format="xml")

for x in range(0,3):
    print earthquakes[x].latitude
    print earthquakes[x].longitude
    print earthquakes[x].place
    print earthquakes[x].atTime
    print earthquakes[x].magnitude
