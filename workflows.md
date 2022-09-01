# Workflows

DMAC workflow and process documentation

- [Copy Order Fulfillment for Digitally-Available Material](#copy-order_fulfillment)
- [Processing Electronic Theses and Dissertations](#processing-electronic-theses-and-dissertations)

---

## Copy Order Fulfillment

This document outlines the process for fulfilling patron requests for already-digitized materials (not including born-digital or MADID materials). 

The bulk of the document provides instructions on how to run a report in the ArchivesSpace staff interface which retrieves data about all digitally-available material in a given collection(s). The report will be used to identify requested materials that have already been digitized, and to facilitate the automated fulfillment of patron requests for those materials.

This document also provides guidance on sending files to patrons once the automated portion of the fulfillment process is complete.

__Initiating a copy order for existing files__

1. Ensure that the patron is registered in Aeon and has signed the user agreement
2. Create an order in Quickbooks and generate an order number
3. Add the patron’s name (Last, First), Aeon username, request date, invoice number, and institutional affiliation to a new row in the [Patron Reprographics](https://docs.google.com/spreadsheets/d/1ZovIjgmJdrMIFLGVqF0PONpwd0kdZcQgW9L22TCI9Cc) spreadsheet

__Running the ArchivesSpace report__

4. Open the ArchivesSpace staff interface. Click on the gear icon and select ‘Reports’ from the drop-down menu

    ![Step 4](./_images/copy_order_fulfillment/step4.png)

5. Select the ‘Copy Order Fulfillment’ report from the menu

    ![Step 5](./_images/copy_order_fulfillment/step5.png)


6. Enter the call number, select ‘CSV’ from the format drop-down menu, and click ‘Start Job’. If the patron requests materials from multiple collections, enter each call number separated by a comma and a space (i.e MS 466, MS 56)

    ![Step 6](./_images/copy_order_fulfillment/step6.png)


7. The report will start running. Depending on the size of the collection and the number of digitally-available items this may take a moment.

    ![Step 7](./_images/copy_order_fulfillment/step7.png)


8. When the job is finished, click ‘Refresh Page’

    ![Step 8](./_images/copy_order_fulfillment/step8.png)

9. Click on the ‘Download Report’ link under the ‘Files’ section to download the report

    ![Step 9](./_images/copy_order_fulfillment/step9.png)


	[Sample report output](https://drive.google.com/file/d/1BqtJeSIS8pVBoXwFIplEbVRj2I-bPBfm/view)

	The report will be downloaded as a .CSV file to your browser’s default download location (usually the ‘Downloads’ folder).

__Using the report to select digitized files for download__

10. Open the report

	Navigate to your Downloads folder and open the report. The filename will be something like `job_9999_digital_object_preservica_links_2021-02-19.csv`. The report can be opened by any spreadsheet software (Excel, Google Sheets, etc.).

11. Select files to download

	The report should contain sufficient information (i.e. Archives at Yale URL in column B, title of archival object in column E, physical container information in column F) to identify a digitized record that has been requested by a patron.

	If there are many digitized records on the report, it may be difficult to visually identify the relevant files. If this is the case, hit `CTRL-F` within your spreadsheet software to launch the search bar (in Excel this will appear on the top right-hand side of the window).

	There are a few different search methods for finding relevant files in the report. To search for files, you can copy and paste one of the following from your browser into the spreadsheet search bar:

	- The URL

	![Step 11](./_images/copy_order_fulfillment/step11.png)

	- 	The component title

	![Step 11a](./_images/copy_order_fulfillment/step11a.png)

	- 	The digital object title(s) from the staff interface

	![Step 11b](./_images/copy_order_fulfillment/step11b.png) 

	Once the relevant files have been identified, mark an `X` in column A of the rows that contain the files to be downloaded. The automated download process will use the values in this column to select files for download.

	_Note on AV files_: Some AV files won’t appear on the report because a presentation manifestation (access file) doesn’t exist in preservica, rather just a preservation manifestation (a lossless, large file, such a .wav). If you find this is the case, please contact the manager of public services.

12. Save the report

	Save the edited report as a new file using the ‘Save As…’ function in the ‘File’ menu of your spreadsheet software, with the naming convention `customerlastnameCustomerfirstname-ordernumber.csv` (i.e. `doeJohn-2787.csv`). The order number is the Quickbooks order number assigned to the patron.

	The file should automatically save as a CSV, but if Excel attempts to save it as an XLSX file you can select Comma Separated Values (CSV) from the File Format dropdown in the ‘Save As’ prompt.

	The report should be saved to the following network drive location: `\\wcsfs00.its.yale.internal\libraryit-807001-ics\MSSA\mssaArrangementAndDescription\Copy_Orders_From_Preservica\orders\_new_`

__Sending Download Links to Patrons__

13. Locate the output of the Yale Box upload process

	Every Thursday morning at 9:15am, a process will run which will download the selected files in each spreadsheet from Preservica, package them into zip files (with the same naming convention as the report - i.e. `doeJohn-2787.zip`), and upload these zip files to Yale Box. The upload process will create a public Box link that expires after 10 days.

	This process will create two outputs to facilitate sending emails from the Aeon client notifying patrons that their order is complete and providing them with the Box link so they may download their files.

	The first output is a file, entitled `orders_to_send_2021-04-08` (with the date being the date that the report was generated), that is stored in the following location: `\\wcsfs00.its.yale.internal\libraryit-807001-ics\MSSA\mssaArrangementAndDescription\Copy_Orders_From_Preservica\orders`

	This report contains relevant patron information taken from the Patron Reprographics Spreadsheet, plus the Box links that were created during the upload process.

	The second output is a text file containing a template for the email that will be sent to the patron manually in Aeon. The files follow the same naming convention as other files created during this process (doeJohn-2787.txt). The template files are stored in `\\wcsfs00.its.yale.internal\libraryit-807001-ics\MSSA\mssaArrangementAndDescription\Copy_Orders_From_Preservica\emails\to_send`

14. Send the files

	To send the Box link to the patron, open the Aeon client. Using the shared link report, enter the patron’s Aeon username. This will open up their profile in the Aeon client. Click on the Email tab, then select `MSSA-SendingFilesViaEFT` from the New Email drop-down. 

	To complete the template, either copy/paste the text from the email template text file, or enter the relevant information (order number, Box link, your name) directly into the template.

	Be sure to update the subject line with the patron’s order number before sending the email.

15. Update the Patron Reprographic spreadsheet

	After sending the emails, check the box in column J of the [Patron Reprographics](https://docs.google.com/spreadsheets/d/1ZovIjgmJdrMIFLGVqF0PONpwd0kdZcQgW9L22TCI9Cc) spreadsheet to indicate that the order is complete.

	A script will periodically clean up the files in the `Copy_Orders_From_Preservica` directory, so there is no need for staff members to manually delete or move any files.

---

## Processing Electronic Theses and Dissertations

This document describes a workflow for processing electronic theses and dissertations from the Graduate School of Arts and Sciences.

__Receipt of Records from Proquest__

Students submit their dissertations electronically to the Graduate School of Arts and Sciences. After acceptance, these dissertations are sent electronically to Proquest for processing and ingest into the Proquest Theses and Dissertations Online database.

In the course of processing, Proquest creates three types of metadata for each dissertation:

1. A provider-neutral MARCXML file
2. A Proquest XML metadata file
3. An XLSX file with some additional information about each dissertation.

After Proquest processes and ingests the dissertations into their system, they send PDF copies of each dissertation, along with the metadata files noted above, to a Manuscripts and Archives drive via FTP.

__Extract Metadata from Proquest Files, Ingest into EliScholar__

After receiving the files from Proquest, MSSA staff run Python scripts which organize the files and extract metadata from the Proquest XML into the BePress .XLS template for bulk ingestion into EliScholar.

After records are ingested into EliScholar, a report can be generated from the EliScholar interface which includes the EliScholar URL for each thesis or dissertation. This report is matched up with the publication numbers and Proquest identifiers for each item via a Python script, and the report with the URLs and publication numbers/identifiers is sent to RDS. Adding the publication numbers/identifiers allows RDS staff to make the connection between the EliScholar URL and the MARCXML record which is ingested into Voyager.

__Modify Proquest MARCXML, Ingest into Voyager__

The following changes are made to the MARCXML records provided by Proquest in order to comply with YUL cataloging practices:

- Fixed fields:
	- Add 006: =006  m\\\\\o\\d\\\\\\\\
	- Add 007: =007  cr\|n|
	- Add 008/7-10: [year of publication]
	- Add 008/15-17: ctu = place of publication
	- Add 008/23: o = online
	- Add 008/24: m = thesis
- Modify 040 to 040  \\$aCtY$beng$erda$epn$cCtY
- Add to 100: ,$e author before final period.
- Modify 260 to 264 \1 $a[New Haven, Connecticut] :$bYale University,$c [keep date]
- Update 300 \\ “1 online resource”; expand abbreviations (p. to pages)
- 336 \\ $atext$btxt$2rdacontent
- 337 \\ $acomputer$bc$2rdamedia
- 338 \\ $aonline resource$bcr$2rdacarrier
- Add 380 \\ $aDissertations, Academic$2 lcsh
- Modify 502 $aThesis (Ph.D.)--Yale University, date. to 502  \\$bPh.D.$cYale University$d date.
- Delete 506 restrictions notes from original record.
- Add 506 \\ $3Proquest dissertation:$aAccess is restricted by licensing agreement$5CtY
- Add 506 \\ $3EliScholar dissertation:$aAccess is available to the Yale community$5CtY
- Add 655 \7$a Academic theses.$2lcgft
- Delete 690 and 790; delete 590 with school code
- Modify 720 advisor name to 700 $a…,$edegree supervisor.
- 710 2\ Add ,$e degree granting institution.
- Add 710 2\ $aYale University.$b[Department].
- Add 730 0\ $3Proquest dissertation$aDissertations & Theses @ Yale University.$5CtY
- Add 830 \0$3EliScholar dissertation$aYale Graduate School of Arts and Sciences Dissertations.$5CtY
- If record ingested from MarcEdit into Voyager, we may need to add an 852 for ProQuest dissertation and an 852 for EliScholar dissertation
- After discussion, just going to create a single 852
- Update 856 40 $3 Proquest thesis
- 856 ProQuest links require proxy prefix (https://yale.idm.oclc.org/login?URL=)
- Add 856 40 $3 EliScholar thesis
- 856 EliScholar links are open to the world, no proxy or authentication required.
- Add punctuation to 246: =264  \1$a[New Haven, Connecticut]:$bYale University,$c2021
- Remove =546  \\$aEnglish
- =500  \\$aSource: Dissertations Abstracts International, Volume: 83-02, Section: A to =588  \\$aDescription based on Dissertations Abstracts International, Volume: 83-02, Section: A.
- Add a comma before $e in 700: ex. =700  1\$aAlexander, Jeffery,$edegree supervisor.
- Change the period before $e to a comma in 710. Ex. change: =710  2\$aYale University.$bPsychology.$edegree granting institution. To =710  2\$aYale University.$bPsychology,$edegree granting institution.
- Add 590 to embargoed records indicating length of embargo and that patron should contact BRBL staff for access

These modifications are made to the MARCXML record via a MarcEdit file and a Python script which is stored on Google Colaboratory and run by RDS staff during processing. The Python script also adds the provided EliScholar URLs to the 856 field for each record. Once the records are modified the MARCXML is ingested into Voyager.

__Ingest into Preservica, Voyager Sync__

The process of ingesting files into Preservica is still being determined, and rollout depends on the in-process upgrade of Preservica to v6. Upon upgrade, the Preservica-Voyager sync will become active, and theses and dissertations which are ingested into Preservica will have Preservica links added to the 583 field in the MARC record for each thesis or dissertation.

