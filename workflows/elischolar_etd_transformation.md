# Dissertation Data Transformation Workflow

This document describes the process for transforming ProQuest-provided dissertation metadata and full-text PDF links into a spreadsheet that can be ingested into EliScholar, and a MARCXML file that can be ingested into Voyager.

## Review data provided by ProQuest

ProQuest sends the following data to the MSSA shared drive via FTP transfer:
1. Zip files for each dissertation, which contain a PDF copy of the dissertation and an XML metadata file. Each file includes the submitter's last name and an identification number.
2. Excel file with a list of dissertations. This includes the ProQuest ID number, which is different from the identifier in the .zip files. Sometimes multiple Excel files are included, separated by the month that the records were processed by ProQuest.
3. A MARCXML file which includes data about each dissertation. Sometimes ther are multiple files separated by month of processing
4. PDF copies of each dissertation are also transferred to a different folder on the drive. These use the ProQuest ID number as the title.

Note that not all data provided by ProQuest is from GSAS - some MPH and MD dissertations are also included, which are not part of this workflow.

## Prepare data provided by ProQuest for ingest into EliScholar and Voyager

1. Copy all files from the MSSA shared drive onto a local drive. Put all of the `etd_admin_XXXXXX.zip` files into a folder separate from the other data.
2. Run the `extract_zip_files` function in the `process_files.py` script against the folder of .zip files. This will extract all .pdf and .xml files into a new folder entitled `extracted_files`. The files will be organized into subfolders for each submission.
3. Run the `create_submission_directories` function in the `process_files.py` script, which will move the PDF and ProQuest XML file for each submission into separate folders.
4. Review the provided Excel spreadsheet. Remove any rows from previous semesters (sometimes they get included erroneously if they are from the same year) and any rows that are for MD or MPH degrees. Save as a new .CSV file.
5. Run the `prep_data_for_elischolar.py` script against the folder of extracted files. This will generate a .XLS spreadsheet that can be ingested into EliScholar.
6. Run the `copy_select_files` function in the `process_files.py` script to copy all unembargoed dissertations to the MSSA Alt Finding Aids server.
7. Navigate to the EliScholar admin interface and select Manage Dissertations
8. Select Batch Upload Excel from the menu on the left-hand side of the page
9. Upload the file by selecting Choose File, choosing the file, and then clicking Upload
10. The upload may take a long time. An email will be sent when the upload is complete. If there are any errors, fix and re-upload

### Notes on transformation in Step 5

1. Embargoed dissertations are identified in the ProQuest XML and the Excel spreadsheet. If there is an embargo listed in the XML, the full text URL will not be added to the .XLS template
2. A few of the department names provided by ProQuest do not exactly match the list 
in EliScholar, which is based on the official names provided by GSAS (e.g. Biomedical Engineering in the XML, Biomedical Engineering (ENAS) in Elischolar). These department names are translated via the `prep_data_for_elischolar.py` script.
3. Sometimes there are multiple departments listed in the XML, but only one can be used in EliScholar. Review the spreadsheet prior to ingest and use only the primary department.

## Prepare data provided by ProQuest for Ingest into Voyager

1. Run the `extract_marc_xml_files` and `reassemble_marc_xml_file` functions in the `process_files.py` script on the provided MARCXML file to generate a new MARCXML which contains only the GSAS dissertations from the semester that is being processed. This file will be delivered to RDS for Voyager ingest.
2. After the dissertations are ingested into EliScholar, run a report from EliScholar (Administrator Report in the admin interface) which includes the EliScholar URLs for each submission.
3. Run the `match_data` function in the `process_files.py` script to match the publication number, ProQuest ID number, title, author, and embargo information from the ProQuest Excel file (converted to CSV) with the EliScholar URL report. This will contain all the information that RDS needs to add the EliScholar URLs and embargo information to the MARCXML file
4. Deliver the EliScholar report and MARCXML file to RDS for ingest into Voyager

