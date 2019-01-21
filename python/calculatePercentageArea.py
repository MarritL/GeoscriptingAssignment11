#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 21-01-2019

import geopandas as gpd

def calculatePercentageArea(GDF1, GDF2):
    """calculate the area of the water per parcel 
    
    :GDF1: first geodataframe
    :GDF2: second geodataframe
    return: intersecting areas
    """
    intersection = gpd.overlay(GDF1, GDF2, how = 'intersection')
    return intersection
