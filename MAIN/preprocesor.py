# -*- coding: utf-8 -*-
"""
This module contains functions to preprocess the input files to compute
a Finite Element Analysis.

"""
from __future__ import division, print_function
import numpy as np


def readin(folder=""):
    """Read the input files"""
    nodes = np.loadtxt(folder + 'nodes.txt', ndmin=2)
    mats = np.loadtxt(folder + 'mater.txt', ndmin=2)
    elements = np.loadtxt(folder + 'eles.txt', ndmin=2, dtype=np.int)
    loads = np.loadtxt(folder + 'loads.txt', ndmin=2)

    return nodes, mats, elements, loads

def proini(nodes, mats, elements, loads):
    """Extract problem parameters
    from nodes, elements, mats and loads
    arrays.

    Returns
    -------
    ne : Number of elements.
    nn : Number of nodes.
    nm : Number of material profiles.
    nl : Number of point loads

    """
    ne = elements.shape[0]
    nn = nodes.shape[0]
    nm = mats.shape[0]
    nl = loads.shape[0]

    return ne, nn, nm, nl


def echomod(nodes, mats, elements, loads, folder=""):
    """Create echoes of the model input files"""
    np.savetxt(folder + "KNODES.txt", nodes, fmt='%5.2f', delimiter=' ')
    np.savetxt(folder + "KMATES.txt", mats, fmt='%5.2f', delimiter=' ')
    np.savetxt(folder + "KELEMS.txt", elements, fmt='%d', delimiter=' ')
    np.savetxt(folder + "KLOADS.txt", loads, fmt='%5.2f', delimiter=' ')
