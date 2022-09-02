# location-search

A simple command line tool for searching ArchivesSpace locations by barcode. Returns a CSV containing data about each container found in the provided location(s).

## Requirements

* Python 3.7+
* `requests` module
* `utilities` module
* ArchivesSpace 2.4+

## Installation

* Clone or download repository
* Open a Terminal or Powershell window and do:

```
$ cd /Users/username/path/to/repository
$ pip install .
```

## Tutorial

The main lookup function can be run by calling the `lookup` command followed by one or more location barcodes, which can be scanned directly into the CLI using a barcode reader. The output of the command will print to the console and write to an outfile. Barcodes should be separated by a single space.

The script will look in the user's home directly to find a configuration file with login information and a path to an output CSV file. A template config.yml file can be found in this repository.

Example usage:

```
$ lookup 81053
Login successful!
['/repositories/2/top_containers/3', '39002137016797', 'MS 5, Series 2, Box 4 [39002137016797], Paige 15', 'MS 5', 'Valuable Records', '/repositories/2/resources/2848', 'BDL, B1 [81053, Range: 1, Section: C, Shelf: 3]', '/locations/3']
['/repositories/2/top_containers/4', '39002137016789', 'MS 5, 2, Box 5 [39002137016789], Paige 15', 'MS 5', 'Valuable Records', '/repositories/2/resources/2848', 'BDL, B1 [81053, Range: 1, Section: C, Shelf: 3]', '/locations/3']
$
```

