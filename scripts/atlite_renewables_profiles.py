""" Build power generation timeseries with Atlite (https://github.com/FRESNA/atlite/)
"""

import atlite

import pandas as pd

from datapackage_utilities import building
from shapely.geometry import Point
from scipy import sparse

poi = Point(8.925556, 54.621389)  # location of Bordelum

filepath = building.download_data(
    'sftp://atlite.openmod.net/home/atlite/cutouts/eu-2014.zip', unzip_file='eu-2014/')

cutout = atlite.Cutout(name='eu-2014/', cutout_dir=filepath)

# determine grid cell index containing the point geometry
index = [i for i, g in enumerate(cutout.grid_cells()) if g.intersects(poi)]

# https://github.com/FRESNA/atlite/blob/master/examples/build_city_heat_demand.py
matrix = sparse.csr_matrix(([1], ([0], index)), shape=(1, len(cutout.grid_coordinates())))

df = pd.DataFrame()
df['wind-onshore-Bordelum-profile'] = cutout.wind(
    matrix=matrix, turbine='Vestas_V112_3MW').squeeze(drop=True).to_series()

df['solar-Bordelum-profile'] = cutout.pv(
    matrix=matrix, panel='KANENA', orientation='latitude_optimal').squeeze(
        drop=True).to_series()

building.write_sequences('generator-profiles.csv', df)
