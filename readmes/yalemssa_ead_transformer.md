# ead_transformer

A script to export, transform, and validate EAD 2002 or EAD3 files generated from ArchivesSpace.

## Requirements

* Python 3.7+
* `utilities` package: https://github.com/ucancallmealicia/utilities
* Saxon: https://gist.github.com/joewiz/f44a29c61ae23b16b478dfabe0fefbac
* EAD 2002 and EAD3 schematron and .xsd files
* Yale best practices EAD XSLT files

## Tutorial

The script takes a CSV of ArchivesSpace resource identifiers and repository identifiers as input. Configuration of API login information, transformation and schema paths, the path to Saxon, and inputs (CSV file, directory) is managed in a config.yml file which is located in the same directory as the script. After adding data to the config file, do:

```>>> python export_transform_validate_ead.py
```