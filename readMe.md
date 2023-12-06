## All JSON files here are created as extensions to those found in the git repo [here](https://github.com/eodcgmbh/openeo-processes/tree/7044771f54525f6b613a8fc065f5f7d688eeca35)

### Regex has been developed and testing using the web-app [here](https://regex101.com/r/wApQYM/1). Most of the regex pattern expressions here are just first attempts and need to be expanded to ensure accurate definitions.

### How to use this repository

Once you have the repo cloned, all code should be executed in a virtual environment running Python 3.9(.18). To create a virtual environment called `venv` run `virtualenv -p /usr/bin/python3.9 venv`. To star the virtual environment run `source venv/bin.activate`. Then install the required packages by running `pip install -r reuqirements.txt`. Now you are free to start running any of the Python scripts as you please. Note that some scripts may need updating to use different file paths for your own local files, as well as updating any GitHub tokens, for example in the [cwl_preparation.py](https://github.com/tjellicoe-tpzuk/openeo_processes_update/cwl_preparation.py) script you must add your own GitHub token to upload the selected file to your own GitHub repo.
