from openeo.udf import XarrayDataCube
import xarray as xr
from github import Github
import rioxarray
from git_access import git_access_token
from datetime import datetime as dt
import time

#####
# This script is an example of how the data could be prepared before being handed as an input to the the run_cwl_url process.
# The input will be some data, often a raster data cube, but any data type is supported.
# This data will then be placed in an accessible location, either on a remote server (here we use GitHub) or locally on the server, 
# and the location of the file will be returned as a string. 
#####

## This function is called automatically when a function is run via the run_UDF process on openEO.
def apply_datacube(cube: XarrayDataCube, context: dict):
    xarrayTest = cube.to_array()
    access_token = "please_insert_token"
    url = create_file(xarrayTest, access_token)
    return url

## This function creates a netcdf file, uploads it to a GitHub repository and returns the url location.
def create_file(cube: xr.DataArray, access_token: str):
    g = Github(access_token)
    repo = g.get_repo('tjellicoe-tpzuk/openEO_read-write')
    outfile = cube.to_netcdf()
    timeNow = time()[-6:]
    fileName = f"openEO_output_{timeNow}"
    repo.create_file(f'data/{fileName}.nc', 'upload tif', outfile, branch='main')
    #print(repo)
    url = "https://raw.githubusercontent.com/tjellicoe-tpzuk/openEO_read-write/main/data/" + fileName + ".nc"
    return url

## This is a function to be used locally for testing of this function, as the runtime required to run this function is not 
## currently supported on openEO.
if __name__ == "__main__":
    geotiff_path_red = "/home/tjellicoe/Documents/EOEPCA-and-OPENEO/useful scripts/B01.tif"

    xarrayTest = rioxarray.open_rasterio(geotiff_path_red).to_dataset('band').to_dataarray()
    print(dt.now().strftime("%y-%m-%d"))
    create_file(xarrayTest, git_access_token)