#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

from matplotlib import pyplot as plt
from matplotlib.patches import Patch

def visualize(parcels, selectedParcels, water, parcelsWater):
    """ Plot parcels on the WUR campus, parcels of interest, water areas on the WUR campus, and water areas on parcels of interest.
    
    :parcels: parcels on the campus of Wageningen University
    :selectedParcels: user-defined parcels of interest
    :water: water areas on the WUR campus
    :parcelsWater: intersection between water areas on the WUR campus and parcels of interest.
    """
    f, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title("Water areas on parcels of interest on the WUR campus")
    parcels.plot(ax=ax, color='grey', linewidth=0.3, edgecolor='black')
    selectedParcels.plot(ax = ax, color = 'grey', edgecolor = 'red')
    water.plot(ax=ax, color='blue', linewidth=0.3, edgecolor='black') 
    parcelsWater.plot(ax=ax, color='orange', linewidth=0.3, edgecolor='black')                      
    
    ParcelPatch = Patch(color='grey', label='Parcel')
    SelectedPatch = Patch(color='red', label='Selected Parcels')
    WaterPatch = Patch(color='blue', label='Water')
    parcelsWaterPatch = Patch(color='orange', label='Parcels with water')
    plt.legend(handles=[ParcelPatch, SelectedPatch, WaterPatch, parcelsWaterPatch])
    ax.set_facecolor("white")
    plt.axis('equal');
    plt.show()                     
                           

