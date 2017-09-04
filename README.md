## Synopsis

This is a Neurodata without borders package, designed to work as part of the FFBO system, and alongside a neuroarch database, for physiological data.

## Usage

This module will work along side a neuroarch database, which will contain the uniqueID (or path) of each nwb data file.

This module with enable the following methods, given a data file:

1. Validate it is a nwb file, as per the specifications
2. Retrieve the file metadata: description, time, datasets contained, size, etc
3. Retrieve the entire file
4. Retrieve a single dataset
5. Retrieve a slice of a single dataset
6. Retrieve a downsampled version of a dataset


## Execution

TODO:
    


## Installation

the package can be cloned, and installed using python setup.py install. The package will require the core NWB python-api, which you can find [here](https://github.com/NeurodataWithoutBorders/api-python/tree/master/nwb)
