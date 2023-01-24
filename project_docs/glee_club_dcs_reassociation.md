# Glee Club Records: Data Reassociation

Project plan for reassociation of Glee Club images with ArchivesSpace metadata records

## Problem Statement

There are over 4,000 digitized Glee Club images in the Yale University Library Digital Collections System (YUL-DCS). These images use the old Ladybird database as their metadata source. This means that the images in YUL-DCS have no connection to their associated ArchivesSpace records. 

Per the new metadata policy for the YUL-DCS, all digitized images must have a 1:1 relationship with a metadata record in a system of record (ArchivesSpace, Voyager). The outcome of this project will be the addition of ArchivesSpace URIs to Glee Club images in YUL-DCS.

## Project Plan

In order to reconcile the Glee Club ArchivesSpace metadata with DCS records, perform the following steps in order:


### Step 1: Request Glee Club boxes

We will need to compare the images in the physical boxes with the digitized images on the YUL-DCS website, and so must call back all Glee Club boxes to perform the review. Alicia will do this 


### Step 2: Compare contents of box with DCS images, record URI of match in spreadsheet


## Student Worker Instructions

Instructions for matching Glee Club records in Aspace/the real world with images in the YUL Digital Collections System (DCS)

### Outcome

Add container and URI data to DCS records so that they can be reconciled with ArchivesSpace.


### Supplies

* Glee Club boxes (on shelf in B-50)
* Computer
* Reconciliation [spreadsheet](https://docs.google.com/spreadsheets/d/1jiiwc_xuE5Xoj45fVrNn527vOhg4VjJduLToZlk6FbI)
* Digital collections system (DCS) URL: [https://collections.library.yale.edu](https://collections.library.yale.edu/) 
* Archives at Yale (AAY) URL: [https://archives.yale.edu](https://archives.yale.edu) 


### Instructions

1. Pick a box to start working on
2. Locate the ArchivesSpace data for the box in the aspace_data tab of the spreadsheet
3. Locate the DCS data for the box in the dcs_data tab of the spreadsheet.
4. Right-click on one of the DCS URLs for the box, and open in a new tab
5. There are several different reconciliation scenarios, depending on the data present in DCS or Find-It:
    * DCS/Find-It records have an accession number, box number, and folder number
        * This is not common, but is easy to reconcile. Add the ArchivesSpace URI to the DCS tab in the ‘aspace_uri’ column.
    * DCS/Find-It records have an accession number and box number, but no folder number
        * This is the most common and the next-easiest scenario to reconcile. In these cases, add the folder number and corresponding ArchivesSpace URI to the DCS spreadsheet.
    * DCS/Find-It records have no accession number, but have a box number
        * This is more difficult, as it may require looking in multiple “box 10s” for the image.
    * DCS/Find-It records have an accession number, but no box number
        * This is also potentially difficult, as it may require looking in multiple boxes in the same accession
    * DCS/Find-It records have no container info
        * Skip for now
6. Using the information from the DCS tab, attempt to locate the original image in the physical box.
    * The images are individually cataloged in DCS, while they are described at a more aggregate level in ArchivesSpace. This means that the same ArchivesSpace URI may apply to numerous DCS images.
    * Sometimes multiple individual records in DCS are actually part of the same document - for instance, single pages of a pamphlet. If an image cannot be found, check pamphlets and other bound items within a folder for the image.
7. Once found, refer to the aspace_data spreadsheet to locate the ArchivesSpace URI for the item
8. Depending on the scenario, add any missing information (accession number, box number, folder number) + the ArchivesSpace URI, to the DCS spreadsheet.
9. If the record cannot be found, or there is some other issue, make a note in the notes column of the DCS tab of the spreadsheet.
10. Right-click on the next DCS URL and repeat steps 5-9

## Notes on Data

There are two projects in Ladybird for the Glee Club - part of MADID and on its own. The Glee Club collection has different OIDs than MADID. It seems like only the MADID images were migrated to DCS, not the Glee Club version. Unfortunately there also seems to be different metadata for the Glee Club collection than the MADID Glee Club images. Though it does seem like the MADID images are correct, and there may be some mismatched images in the Glee Club collection. For instance:

This is a Glee Club collection record: [https://findit.library.yale.edu/catalog/digcoll:4243116](https://findit.library.yale.edu/catalog/digcoll:4243116). The image is not of the cover, as it states in the title. 

This is the corresponding MADID collection record: [https://findit.library.yale.edu/catalog/digcoll:4351009](https://findit.library.yale.edu/catalog/digcoll:4351009). The image does appear to be of the cover. This is what was migrated to DCS: [https://collections.library.yale.edu/catalog/10535547](https://collections.library.yale.edu/catalog/10535547) 

Might be worth it to try and match up the two different collections using titles, accession numbers, etc.