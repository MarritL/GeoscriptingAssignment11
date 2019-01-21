#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 21-01-2019
def geocodePlacenameToCoordinates(placename):
    """ Get the coordinates of a specified location
    
    :placename: location to find the coordinates for
    :returns: location information
    """
    geolocator = Nominatim(user_agent="specify_random_user_agent")
    location = geolocator.geocode(placename)
    return location