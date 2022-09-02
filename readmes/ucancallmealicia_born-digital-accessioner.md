# born-digital-accessioner

A simple graphical user interface to create or update archival object records and create associated event records _en masse_ via the ArchivesSpace API. Written for [Yale Digital Accessioning Service (DAS)](https://guides.library.yale.edu/c.php?g=300384&p=3593184) workflows.

## Requirements
* Python 3.4+
* `requests` module
* ArchivesSpace 2.1+

## Quick Start

```
$ cd /Users/username/file/path
$ git clone https://github.com/ucancallmealicia/born-digital-accessioner
$ cd born-digital-accessioner
$ python born-dig-accessioner.py
``` 

__COMING SOON:__ .exe and .app versions with all dependencies packaged into a single file or directory.

## Tutorial

The Born Digital Accessioner was designed to support the following workflow:

1. During physical processing of archival collections, archivists from special collections repositories across Yale document all digital media items in the DAS spreadsheet template.
2. Repository staff send the physical media and completed template to the Digital Accessioning Service. 
3. DAS staff perform assorted preservation actions, and add the type of action, the outcome, and the date performed to each row of the DAS spreadsheet template.
4. DAS staff ingest the DAS spreadsheet into the Born Digital Accessioner, which either updates existing ArchivesSpace archival object records for the born digital materials, or creates new ones. In either case, event records are also created for each of the preservation actions performed by the Digital Accessioning Service.

### Step 1: Connect to ArchivesSpace

Logs the user into ArchivesSpace. The following data is accepted:

* __ArchivesSpace URL:__ the URL for the ArchivesSpace staff interface. The Born Digital Accessioner automatically appends `/api` to the end of the URL, which conforms to Yale’s URL formatting. Comment out lines 218 - 221 and uncomment line 222 to remove this appendage.
* __ArchivesSpace Username:__ the ArchivesSpace username of the Born Digital Accessioner user. This is the user that will be designated as the Authorizor of any event records created by the program.
* __ArchivesSpace Password:__ the ArchivesSpace password of the Born Digital Accessioner user.

Clicking the 'Connect!' button will submit login information. 

### Step 2: Select Input CSV

Allows the user to select the DAS spreadsheet template from a file menu by pressing the ‘Select File’ button. The path to the selected file will display in the interface.

### Step 3: Choose Action

The user chooses an action by clicking either the ‘Create records’ or ‘Update records’ buttons.

Sometimes repository staff will have already created archival object records in ArchivesSpace for born-digital materials. In these cases, the ArchivesSpace URL of each existing object should be listed on the DAS spreadsheet. Users click the 'Update Records' button to add metadata to these records, and to create event records related to DAS preservation actions.

If archival objects records don't already exist, the ArchivesSpace URL of the parent archival object record under which child archival objects records will be created should be listed on each row of the DAS spreadsheet. Users click the 'Create Records' button to create these new child records and their associated event records.

__NOTE:__ Archival object records can be created or updated even if no event data is present.

### Step 4: Review Outputs

Once the script finishes, the user can review various outputs. The total number of archival object records created or updated, the total number of create/update attempts, and the amount of time the program took to run will appear at the bottom of the interface.

Additionally, three buttons on the right-hand side of the interface allow users to perform the following actions:

* __Open Output File:__ All URIs for newly-created records are appended to the data from the original spreadsheet and written to an output CSV. Any records which do not update are written to the output CSV without any URIs. This button will open the output CSV file in the user's default spreadsheet program.
* __Open Log:__ Opens a detailed program log, which tracks the program's actions and documents errors.
* __Open in ArchivesSpace:__ If creating new records, this button will open the parent record in ArchivesSpace. If updating existing records, this button will open the last record updated in ArchivesSpace. 

### Tips

* To clear all data (i.e. login information, file selection, outputs), press the 'Clear Inputs' button at the bottom of the interface
* To view the Help page, select _File > Help_ from menu bar
* To download a blank copy of the DAS spreadsheet template, select _File > Template_ from menu bar
* To quit the program, select _File > Exit_ from menu bar

## Troubleshooting

### Data Issues

The most common cause of errors is invalid data entered into the DAS spreadsheet template, such as:

* Incorrect formatting of extent types and events (requires the database value)
* Data in the wrong column
* Missing data
* Typos

Most of the time, when the program encounters an error it will move onto the next record without stopping, but this is not always the case. Check the log file if the program stops during execution.

### Bugs

If your data looks good and you’re still having issues, check the program log for detailed error reporting. If you find a bug please submit an issue!

## Questions?

[Email me](mailto:alicia.detelich@yale.edu)
