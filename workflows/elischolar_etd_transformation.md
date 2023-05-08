# EliScholar Data Transformation Workflow

This document describes the process for transforming ProQuest-provided dissertation metadata and full-text PDF links into a spreadsheet that can be ingested into EliScholar.

## Review data provided by ProQuest

ProQuest sends the following data to the MSSA shared drive via FTP transfer:
1. Zip files for each dissertation, which contain a PDF copy of the dissertation and an XML metadata file. Each file includes the submitter's last name and an identification number.
2. Excel file with a list of dissertations. This includes the ProQuest ID number, which is different from the identifier in the .zip files. Sometimes multiple Excel files are included, separated by the month that the records were processed by ProQuest.
3. A MARCXML file which includes data about each dissertation. Sometimes ther are multiple files separated by month of processing
4. PDF copies of each dissertation are also transferred to a different folder on the drive. These use the ProQuest ID number as the title.

Note that not all data provided by ProQuest from GSAS - some MPH and MD dissertations are also included, which are not part of this workflow

## Prepare data provided by ProQuest for ingest into EliScholar

1. Copy all files from the MSSA shared drive onto a local drive. Put all of the `etd_admin_XXXXXX.zip` files into a folder separate from the other data
2. Run the `process_files.py` script against the folder of .zip files. This will extract all .pdf and .xml files into a new folder entitled `extracted_files`. The files will be organized into subfolders for each submission.
3. Run the `process_files.py` script against the MARCXML file, which will extract each individual MARC record into the submission folders.
4. Review the provided spreadsheet. Remove any rows from previous semesters (sometimes they get included erroneously if they are from the same year) and any rows that are for MD or MPH degrees. Save as a new .CSV file.
5. Run the `prep_data_for_elischolar.py` script against the folder of extracted files. This will generate a spreadsheet that can be ingested into EliScholar
