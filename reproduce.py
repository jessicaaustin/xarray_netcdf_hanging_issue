import os
import sys
import uuid

import xarray as xr


def reproduce_xarray_issues():
    print("run start")
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    try:
        for i in range(50):
            # NOTE: if you set lock=False then this runs fine every time
            # Setting lock=None causes it to intermittently hang
            with xr.open_mfdataset(['dataset.nc'], combine='by_coords', lock=None) as mfd:
                p = os.path.join('tmp', 'xarray_{}.nc'.format(uuid.uuid4().hex))
                print(f"Writing data to {p}")
                mfd.to_netcdf(p)
        print("complete")
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    reproduce_xarray_issues()
