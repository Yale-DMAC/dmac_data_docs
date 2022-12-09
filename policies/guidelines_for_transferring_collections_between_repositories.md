# Guidelines for Transferring Collections Between Repositories

## Originating repository responsibilities

### ArchivesSpace

*Note: Before proceeding, confirm that the staff member carrying out the following steps has at least view access and transfer permissions in both the originating and destination repositories. If you require this access, please consult with YAMS co-chairs.*

* Test resource transfer on DEV or TEST
* Once you’ve confirmed the transfer works in DEV or TEST, do the following in PROD:
	- Unpublish the resource record
	- Remove the EAD ID
	- Remove the EAD Location    	
	- Add the following information to the Immediate Source of Acquisition note: “Transferred from [originating repository], [year]”
	- Update the Processing Information note with the soon-to-be former call number
	- Transfer the resource record to the destination repository
	- In the originating repository, create a new resource record for the collection in order to keep a record of it having existed in the originating repository; add the former EAD ID and identifier to this new resource record; and suppress the record

### Orbis

* Suppress the bibliographic and holdings records from the OPAC
* Update the 561 note
* Add or update the 099 to indicate the former call number (e.g. Former call number: MS 464)
* Delete the item records, if necessary, and capture the barcodes for subsequent LSF deaccessioning, as noted under Physical transfer, below

### Physical transfer

* Notify destination repository that ASpace and Orbis work is complete
* Transfer materials to destination repository
* If items are shelved at the Library Shelving Facility, contact LSF staff to request the items be de-accessioned from LSF.

## Destination repository responsibilities

### Physical transfer 

* Accept materials from originating repository.
* Relabel the boxes to bring the boxes into line with destination repository local practice.
* If boxes were previously shelved at LSF, remove and replace the existing barcodes.

### Orbis

* Update the 039 ‡9: with the new EAD ID
* Update the 524 with the new preferred citation
* Update the 852 to final repository
* Update the 856/1 with the new finding aid handle
* Decide what to do with the any 856 external links (e.g. digital library links)
* Create a new Mfhd
* Transfer the item records from the former Mfhd to the new one (confirming that the permloc is correct), replace them with new item records, or delete them altogether if your practice is to manage items in ASpace, as appropriate
* Delete the former Mfhd
* Make whatever other changes are necessary to bring the record into line with destination repository local practice
* Unsuppress the record

### ArchivesSpace

* Add the new EAD ID 
* Update the resource identifier
* Update the Preferred Citation note
* Make whatever other changes are necessary to bring the finding aid into line with destination repository local practice
* If the material was at LSF, remove old barcodes from boxes and ASpace; re-barcode materials
* Publish the resource
* Once resource is published in ASpace, send new handle for the collection to Mark Custer, to update the old handle to redirect to the new finding aid
