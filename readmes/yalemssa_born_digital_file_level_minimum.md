# Born Digital File Level Minimum

Files to support creation and enhancement of born-digital description in ArchivesSpace to meet file-level minimum [standards](https://guides.library.yale.edu/c.php?g=934566&p=6736589) set by the YUL Born Digital Archives Working Group (BDAWG).

### What's in this repository

#### `bd_file_level_minimum.xlsm`

A template for creating and updating archival object records to meet born-digital file-level minimum standards.

#### `bd_file_level_minimum.py`

A script which creates or updates archival object records using the template above as input.

##### Requirements

* Python 3 (tested on 3.8, but will likely work with older versions)
* `requests` package

##### Preparing Inputs

The script takes the `bd_file_level_minimum` spreadsheet (saved as a .CSV file) as input. If creating new records, include the word 'create' in the filename of the spreadsheet. If updating records, include the word 'update'.

##### Tutorial

1. Enter your credentials and input/output paths to the included `condig.json` file
2. Open a Terminal or Prompt window
3. Navigate (`cd`) to the directory which contains the script
4. Enter `python bd_file_level_minimum.py` into the Terminal/Prompt and press Return
5. The script should begin running. Monitor the Terminal/Prompt for errors
6. When finished, check ArchivesSpace to view created or updated records

#### `bd_file_level_minimum.sql`

This report replicates the structure of the `bd_file_level_minimum.xslm` template, and can be used to retrieve existing data for enhancement. The report is also available in the TEST staff interface of ArchivesSpace (coming soon to PROD).

To make use of the drop-down values and data validation functions in the `bd_file_livel_minimum.xslm` template, you can either:
1. Copy and paste the data from the report into the template
2. Import the data into the template using the Data --> Get External Data --> Import Text File feature in Excel or other spreadsheet software

__NOTE__: It is unlikely (<1% of all archival objects, the majority of which are older, analog records), but possible, that more than one date, extent, or note (of any type) is associated with a single archival object. If this is the case, the values are concatenated in a single cell of the report. For instance, if there are two date records associated with a record, both values are included in the date_begin column, separated by a semicolon.

If you don't intend to change the value of the field containing multiple values, you can simply delete all of the values in the cell, leaving it empty.

If you do need to change the value of the field (again, this will happen infrequently), you should delete all the values in the cell and manually update the field as desired.

The extent columns (columns E-L) are the only exception to this. The spreadsheet allows for the creation or update of two extent values. If there is more than one extent value associated with a record, the second extent is populated in columns I-L. Additional extents are not included on the report (as of 2/15/2021 there is only 1 MSSA record with 3 extents).