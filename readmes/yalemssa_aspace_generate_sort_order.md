## aspace_generate_sort_order

A lightweight Python application to generate a custom sort order from ArchivesSpace. 

### What does this application do?

The application performs the following tasks on each row of a CSV report containing information about all archival objects within a given collection:

1. Retrieves the JSON record for the object
2. Extracts the `ancestor` array from the JSON and reverses it so that the collection-level record is first, etc.
3. Retrieves JSON for each ancestor, excluding the collection-level record, as resource records do not have position values
4. Extracts the `position` value from each ancestor and, if the position value is less than 5 digits in length, add leading zeros. The largest collection in ArchivesSpace has ~88000 records linked to it, meaning that even if the collection were totally flat there would not be a position value greater than 5 digits in length
5. Concatenate each position value to a string variable, with a dot after each position. The sort order will end up looking something like this: 00001.00027.00005.00435
6. Adds this position value in a new column in the input CSV file

### Requirements

- Running the executable file requires a Mac. You do not need to install Python or any other dependencies. You can just double-click on the file to run the script.
- Running the Python script requires Python 3.8+ and the `requests` and `rich` third-party libraries

### Tutorial

#### Generating the input file

This application takes the custom `All Archival Objects` report (CSV format) as input. This report is generated within the ArchivesSpace staff interface. To run this report: 

1. Click on the gear icon next to the repository name in the staff interface
2. Select `Reports` from the drop down
3. Click on the `All Archival Objects` report
4. Enter the call number of the collection in the `Call Number` box
5. Select `CSV` from the `Format` dropdown menu
6. Click `Start Job` to start the report job
7. When the report finishes, click the `Refresh Page` button
8. Click the `Download Report` link to download the report

#### Configuration settings

The application comes with a `config.json` file, which allows the user to specify ArchivesSpace login information and the path to the input CSV file.

Sample `config.json` formatting:

```
{
	"input_csv": "full/path/to/input_csv.csv",
	"aspace_api_url": "https://archivesspace.library.yale.edu/api",
	"aspace_username": "yourusername",
	"aspace_password": "yourpassword"
}
```

If the configuration file is not completed, the application will prompt the user for each of these inputs.

#### Running the application

Double click on the executable file to run the script. If the configuration file is complete, the script will begin immediately. If not the user will be prompted to enter the input file path and ArchivesSpace login data.

Depending on the number of archival objects associated with the collection, the script could take a while to run (test runs completed approximately 675 records per minute). A progress bar will appear which includes the number of records processed and the estimated time remaining.

#### Output

The application outputs a CSV file, and stores it in the same directory as the input file. The filename will be the same as the input file, with the addition of `_output` at the end of the filename - i.e. `full/path/to/input_csv_output.csv`

The output CSV file includes a new first column, `sort_order`, which stores the sort order that is generated during the process. The values in this column can be sorted within spreadsheet software, script, or other application as needed.

__NOTE:__ If sorting in spreadsheet software, it is important to specifically open the file as plain text. Many spreadsheet software applications will default to `General` format, which can cause leading zeros to be dropped from the sort order values. Obviously if this happens the sort order will not work properly.

If using Excel, follow these steps to ensure that the output file is opened in plain text:

1. Open a blank workbook in Excel
2. Select `Data > Get External Data > Import Text File...`
3. In Step 1 of the Text Wizard, select the `Delimited` radio button and press `Next >`
4. in Step 2, check the `Comma` box in the `Delimiters` menu
5. In Step 3, click on the first column to highlight it
7. Select the `Text` radio button in the Column data format menu
8. Click `Finish`
9. Select the `Existing sheet` radio button from the next menu and click `OK`
10. The spreadsheet will populate with the formatted data. To sort, click the `Data > Sort` button. 
11. In the sort menu, check the `My list has headers` button and select `sort_order` from the `Column` drop-down. Click `OK`.
12. You may receive a Sort Warning asking whether you should `Sort anything that looks like a number, as a number` or `Sort numbers and numbers stored as text separately`. Select `Sort numbers and numbers stored as text separately` and click `OK`
