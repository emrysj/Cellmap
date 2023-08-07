# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:47:01 2023

@author: ukejon
"""

import geopandas
import pandas
import matplotlib as plt
import numpy
import subprocess
import shapely

#%%

Cells = geopandas.read_file('C:/QPath_DESI/QUPathTest11.geojson')

#Test = geopandas.read_file('C:/QPath_DESI/1200773-e122cf709898c09758aecfef349964a8d73a83f3/sample.json')

#%%



Cell1 =  Cells.loc[2]

Cell1M = Cell1.loc['measurements']

Cell1T = Cell1.loc['objectType']
Cell1ID = Cell1.loc['id']

Cell1G = Cell1.loc['geometry']

#%%



Area1=Cell1M.get("Cell: Area")
Circ1=Cell1M.get("Cell: Circularity")  
Ecc1=Cell1M.get("Cell: Eccentricity")

CellSI = pandas.DataFrame({"Area": [Area1],
                           "Circularity" : [Circ1],
                           "Eccentricity": [Ecc1]})



#%%

for x in range(2,239):
    
    Cell1 =  Cells.loc[x]
    Cell1M = Cell1.loc['measurements']
    Area1=Cell1M.get("Cell: Area")
    Circ1=Cell1M.get("Cell: Circularity")  
    Ecc1=Cell1M.get("Cell: Eccentricity")
     
   
    Row = pandas.DataFrame({"Area": [Area1],
                           "Circularity" : [Circ1],
                           "Eccentricity": [Ecc1]})
    CellSI = CellSI.append(Row,ignore_index=True)
    
    #%%
    
CellSI.plot("Eccentricity","Circularity", kind='scatter')
   
   # ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

  #%%
  

subprocess.run('C:/HDI/lib/maldichrom.exe -d "C:/QPath_DESI/p8_fsb_newslide4_cropped.raw" -p "C:/HDI/process/ROI_5Cell1raw.txt" -w "C:/QPath_DESI/Cell4.raw"', shell=True)

  #%%


s= geopandas.GeoSeries(Cell1['geometry'])



  #%%




