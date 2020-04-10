import os
import uuid

import xarray as xr
import logging

def test_reproduce_xarray_issues():
    print("test start")
    mfd = xr.open_mfdataset(['dataset.nc'], combine='by_coords')
    p = os.path.join('tmp', 'xarray_{}.nc'.format(uuid.uuid4().hex))
    print(f"Writing data to {p}")
    mfd.to_netcdf(p)
    print("complete")
