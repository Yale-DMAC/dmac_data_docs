# Kevin Roche John Dinkeloo Associates Data Re-use Process

## Process

1. Save project index .XLSX file as a CSV file. Delete all rows which refer to boxes already in ArchivesSpace
2. Run `process_spreadsheet.py` script against CSV file
3. Copy/past box numbers into Excel and run remove duplicates function
4. Add `repo_uri` and `box_type` fields to box number spreadsheet
5. Comment out relevant parts of `project_index_new.py` script and run to create containers (FIX THIS)
6. Run split titles through OpenRefine to extract dates, clean up
	- Keep original title
	- Extract dates (just split by comma)
	- Add index!
	- Run replace function to remove dates
	- Run find/replace in LibreOffice for punctuation, spaces, 'no date' etc.
7. Match box numbers and project numbers with URIs
8. Create new projects if needed, record URIs
9. Create archival objects with `project_index_new.py` script
	
  
## Notes

- Do all of this in ArchivesSpace TEST first, then repeat for production.

## Future Work

- Combine projects from same location with different job titles
- Separate projects that have multiple job numbers
- Re-order based on date, job number, or box number