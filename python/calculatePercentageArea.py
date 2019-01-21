#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 21-01-2019

def calculatePercentageArea(GDF1, GDF2):
    """calculate the area of the water per parcel 
    
    """
    intersection = gpd.overlay(GDF1, GDF2, how = 'identity') # or other?
    print(intersection.head())
    
    # todo: some calculation