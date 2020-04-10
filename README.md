Temporary repository to reproduce the issue I'm seeing with xarray.

When I load up a netcdf file using this code, it will intermittently hang while saving the file.

I can reproduce this with different netcdf files, for example the [stearns_wharf.nc example](https://data.nodc.noaa.gov/thredds/catalog/ioos/sccoos/stearns_wharf/catalog.html?dataset=ioos/sccoos/stearns_wharf/stearns_wharf-2013.nc) from NCEI netCDF templates.

I've seen this with the following combos:

* xarray=0.14.1
* dask=2.9.1
* netcdf4=1.5.3

and 

* xarray=0.15.1
* dask=2.14.0
* netcdf4=1.5.3


---


Steps to reproduce:

Create environment:

```
conda env create -n xarray_reproduce --file requirements.txt 
conda activate xarray_reproduce
```

Run tests
```
# this script fails randomly, so try it a bunch of times until it fails
for i in {1..10}; do echo $i; python reproduce.py; done
```

Dump env info:
```
conda env export --no-builds > environment.yml
```
