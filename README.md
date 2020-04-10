Temporary repository to reproduce the issue I'm seeing with xarray.

When I load up a netcdf file with a certain structure, it will intermittently hang while saving the file. I believe it's something about the file structure, but I haven't figured out what. 

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

Run test. Fails intermittently, but will typically happen after just a few attempts.
```
for i in {1..50}; do echo $i; pytest -s xarray_reproduce_test.py; done
```

Dump env info:
```
conda env export --no-builds > environment.yml
```

Dataset info:
```
$ ncdump -h dataset.nc
netcdf dataset {
dimensions:
	time = 298 ;
	z = 1 ;
variables:
	int time(time) ;
		time:units = "seconds since 1970-01-01T00:00:00Z" ;
		time:calendar = "gregorian" ;
		time:axis = "T" ;
	double z(z) ;
		z:units = "m" ;
		z:positive = "up" ;
		z:axis = "Z" ;
	double value(time, z) ;
		value:_FillValue = -9999. ;
	ubyte qc_agg(time, z) ;
		qc_agg:_FillValue = 2UB ;
	uint64 qc_tests(time, z) ;
		qc_tests:_FillValue = 0ULL ;
	uint64 dummy_var(time, z) ;
		dummy_var:_FillValue = 0ULL ;

// global attributes:
		:title = "feed_1000045_raw" ;
		:feed_id = 1000045LL ;
		:device_id = 1000128LL ;
		:station_id = 100006LL ;
}
```
