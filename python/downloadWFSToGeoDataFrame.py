#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Anne-Juul Welsink and Marrit Leenstra
# Date: 21-01-2019

#import libraries
import json
from owslib.wfs import WebFeatureService
import geopandas as gpd

def downloadWFSToGeoDataFrame(url, version, bbox, typename):
    """Download a WFS from a given url
    
    :url: urlstring where WFS is located
    :version: WFS version to download
    :bbox: boundingbox (xmin, xmax, ymin, ymax)
    :typename: key:value pair needed on national georegister website to download 
               certain WFS    
    :returns: GDF: geodataframe with requested data
    """
    MapWFS = WebFeatureService(url=url, version = version)
    response = MapWFS.getfeature(typename=typename, bbox=bbox, maxfeatures=100, 
                                 outputFormat='json', startindex=0)
    data = json.loads(response.read())
    GDF = gpd.GeoDataFrame.from_features(data['features'])
    return GDF
