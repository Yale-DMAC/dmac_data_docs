# MSSA Copy Order Fulfillment

Scripts to support an MSSA workflow for fulfilling copy orders for already-digitized materials.

## What's included

* `preservica_file_picker.py`: a lightweight Python console application to download files from Preservica.
* `package_files.py`: Packages folders into a .zip archive file
* `get_spreadsheet_data.py`: Gets patron reprographics data from Google Sheets API
* `create_shared_links.py`: uploads .zip files to Yale Box, creates a shared public link which expires after 10 days, returns a report containing patron name, Aeon username, order number, and box link.
* `update_spreadsheet_data.py`: Updates patron reprographics data via Google Sheets API
* `generate_email_template.py`: Generates boilerplate email text to send to patron using report from `create_shared_links.py`
* `clean_directories.py`: Moves or deletes files and folders after files are sent
* `constants.py`: utility file to hold console app styling data
* `config/config.json`: user config settings
* `config/service_account.json`: Placeholder for Google API config file

## Proposed workflow

1. Public Services staff receive a request from a researcher for digitized materials
2. Public Services staff ensures customer is registered in Aeon and signs the user agreement
3. Public Services staff fill out tracking spreadsheet and create Quickbooks order
4. Public Services staff run the ‘Preservica Access Copy Links’ [report](https://github.com/YaleArchivesSpace/yale-archivesspace-reports/blob/add_report/backend/model/digital_object_preservica_links.rb) in the ArchivesSpace staff interface to retrieve all Preservica digital content links for one or more collections
5. Public services staff review the report and mark, in the first row, any files that should be downloaded and sent to the patron
6. Public services staff save the CSV file as a new file into a “hot folder” on a network drive; the file should be named with the patron’s last name and order number separated by hyphens (i.e. customerlastname-ordernumber.csv)
7. At the end of each day a script runs from an MSSA/YAMS server which zips and shares the files via an expiring Yale Box link. The script returns a report, stored in the same folder, containing the request date, patron name, Aeon username, order number, and institutional affiliation for each request
8. Digitization staff send emails to patrons from Aeon containing Box links

