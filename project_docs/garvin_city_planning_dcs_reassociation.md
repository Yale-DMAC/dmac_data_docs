# Garvin City Planning Image Collection: DCS Reassociation

## Reassociation Plan

Due to the limited amount of descriptive metadata in ArchivesSpace, as compared to the extensive “hierarchy” in Find-It, propose to migrate Garvin hierarchical metadata data from Ladybird into ArchivesSpace, and associate the newly-created ArchivesSpace records with parent records in DCS. 

This will require the creation of new archival objects in ArchivesSpace, followed by an update of Garvin parent records in DCS to include the URIs of the newly-created ArchivesSpace objects and change the metadata source to ArchivesSpace. It will not be necessary to combine any existing DCS child OIDs under new parents, and the Garvin child objects in DCS have already been grouped under their parents.

## Process Overview

1. Extract report of Garvin metadata from DCS via ‘export all parent objects by admin set’ batch process
2. Extract report of Garvin metadata from Ladybird database
3. Using the `oid` and `_oid` (parent) columns in Ladybird report of Garvin parent records, generate a nested JSON file which contains the full hierarchy, including OIDs
4. Using the JSON file, recursively create archival object records in ArchivesSpace. Record the new ArchivesSpace URIs and the OIDs on a spreadsheet
5. Match the newly-created URIs with DCs parent records
6. Use the spreadsheet to update parent objects in DCS with ArchivesSpace URIs

## Metadata Overview

### Garvin Reports Folder

[Link to report folder](https://drive.google.com/drive/folders/1UOoK_wRyZ5rsY34AZrhKrY-eZyBGie1_?usp=sharing) 

### Garvin Data in Ladybird

[Collection page](https://findit.library.yale.edu/catalog/digcoll:4089284)

[All records in find-it](https://findit.library.yale.edu/?f%5Bdigital_collection_sim%5D%5B%5D=Garvin+City+Planning+Image+Collection&search_field=all_fields&utf8=%E2%9C%93 

Total number of published records on the front end of Find-It: **17733**. This includes parent records without associated images.

### Garvin Data in ArchivesSpace

[Current collection record (unpublished)](https://archivesspace.library.yale.edu/resources/11636#tree::resource_11636)

Revised collection, based on Ladybird metadata: 

[Resource record, TEST staff interface](https://testarchivesspace.library.yale.edu/resources/12498) 

[Resource record, TEST public interface](https://puitestarchivesspace.library.yale.edu/repositories/5/resources/12498)

### Issues

* Some cleanup needed. For instance, moving records which are listed under the heading ‘other’.
* May need to reconcile the physical containers that are listed in the original Garvin collection with the new records. There was no data about physical containers stored in Ladybird

## Garvin Data in DCS

[All Arts records in production (including theater photos)](https://collections.library.yale.edu/catalog?f%5Brepository_ssi%5D%5B%5D=Robert+B.+Haas+Family+Arts+Library+Special+Collections) 

[Reassociated Garvin Records in UAT](https://collections-uat.library.yale.edu/catalog?f%5Bcollection_title_ssi%5D%5B%5D=Garvin+City+Planning+Image+Collection+%5BDCS+TESTING%5D+%28VRC+1990+TEST%29&f%5Brepository_ssi%5D%5B%5D=Robert+B.+Haas+Family+Arts+Library+Special+Collections) 

### Issues

* Some records are not yet available in DCS: at least 850 parent OIDs have some kind of problem. These will be deleted and ingested via Goobi after the ArchivesSpace metadata is updated (this is required for Goobi ingest)

## Questions

* Any obvious reasons not to proceed this way? Suggestions on alternatives? Other things I haven’t considered?
* Where did the description in Find-It originate?
* What is the physical situation of Garvin? Does the hierarchy at all reflect the physical organization of the collection? What is the relationship of the images in Find-It/Ladybird to the current ArchivesSpace resource record?
* Any additional background on this collection that would be helpful?

<!-- ## Garvin Zenhub Tickets

Migration ticket: [https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1807](https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1807)  

Reassociation ticket: [https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1967](https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1967) 

Review of issues in production: [https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1929](https://app.zenhub.com/workspaces/yul-dc-5e50083561915b11fc9e5850/issues/yalelibrary/yul-dc/1929)  -->
