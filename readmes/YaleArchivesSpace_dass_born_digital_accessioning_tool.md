# DASS Born Digital Accessioning Tool

Updated version of [born-digital-accessioner](https://github.com/ucancallmealicia/born-digital-accessioner).


## Workflow

1. DASS staff receive completed spreadsheet from technical services staff
2. DASS staff perform accessioning actions on born-digital materials and add event information to DASS spreadsheet
3. Every morning at 9am, the script checks the network folder and makes the updates for each spreadsheet. If the script encounters an error in a spreadsheet, it skips the rest of the rows and moves to the next sheet
4. Any errors are reported in an error log stored in `logs` folder
5. Spreadsheets for which all rows were successfully updated are moved to the `complete` folder
6. Spreadsheets which had an error are moved to the `errors` folder
7. Output spreadsheets containing newly-created URIs are created within the `outputs` folder
8. Backups are produced for all updated objects, and are stored in the `backups` folder


