# MSSA MADID Reassociation Project Plan

**January 2022**

This document provides an overview of MSSA’s plan for reassociating descriptive metadata from ArchivesSpace with MADID digital images in the Digital Collections System (DCS). This work is required by the [YUL Digital Collections System Policy](https://yaleedu.sharepoint.com/sites/YULITSC9/Documents%20Open%20to%20YUL/Forms/AllItems.aspx?id=%2Fsites%2FYULITSC9%2FDocuments%20Open%20to%20YUL%2FApprovedPolicies%2FPolicy%5FDigitalCollectionsSystem%5FFinal%5F10082020%2Epdf&parent=%2Fsites%2FYULITSC9%2FDocuments%20Open%20to%20YUL%2FApprovedPolicies).

## Reassociation Scenarios

### Fully digitized, single image

One MADID image associated with an archival object, and that image is a 1:1 representation of the intellectual content of the archival object

**61** total MADID images

#### Solution

This is the easiest, but also an unlikely, scenario. The OIDs and URIs of these images can be copied from the reassociation spreadsheet into a batch process template and updated in bulk.

### Fully digitized, multiple images

Multiple MADID images associated with a single archival object, and the combined images represent the full intellectual content of the archival object

**30** total MADID images

#### Solution

Combine these images under a single parent in DCS, and link that parent to the archival object. 

**OR**

Create new archival objects for each image? These may be a good candidate for creating new objects, since they are complete representations of the ArchivesSpace record. However, our current practices do not usually include item-level description (except for AV), so this may not be the best approach.


### Partial digitization, single image

One MADID image associated with an archival object, but that that image is not a full representation of the intellectual content of the archival object

**3531** total MADID records


#### Solution

Link the parent record to the ArchivesSpace record. Do not create individual ArchivesSpace child records for each image. 

### Partial digitization, multiple images

Multiple MADID images associated with a single archival object, but the combined images are not a full representation of the intellectual content of the archival object

**7746** total MADID records

#### Solution

Combine these images under a single parent in DCS, and link that parent to the archival object. Do not create individual ArchivesSpace child records for each image.

### Other Scenarios

#### Purple

Problem with the Ladybird record. [what does this mean? Mostly no notes on these]

**2757** total MADID records

#### Blue

Some question about it which prevents reassociation. Some of these are marked as ‘may warrant additional description in ArchivesSpace’

**3301** total MADID records

#### Red

Cannot be found in ArchivesSpace or Orbis. About ~40 of these were not marked as ‘cannot be found’, but did not have an ArchivesSpace URL in the spreadsheet.

**643** total MADID records

## Reassociation Procedures

Reassociation work happens via the management app and the ArchivesSpace API. Procedures for each scenario are below. Reassociation can proceed iteratively, in batches, based on the various scenarios. This will allow reassociation to move forward while the remaining issues (i.e. the records highlighted in various colors on the MADID spreadsheet) are resolved.

### Associate existing DCS record with existing ArchivesSpace record

Using the ‘Update Parent Objects’ template in the DCS management app, list ArchivesSpace URIs alongside the image OID (also include ‘aspace’ in the ‘source’ column), and then run the batch process using the completed template as input.

### Create a new parent in DCS and associate children

First, create the new parent objects via the ‘Create Parent Objects’ batch process. Then update the parent objects with the correct ArchivesSpace URI via the ‘Update Parent Objects’ batch process. Finally, use the ‘Reassociate Child OIDS’ batch process to associate the images with the new parent.

Note: need to determine exactly how this works. How are the OIDs assigned in the ‘Create Parent Objects’ template?

### Create new records in ArchivesSpace, associate those with existing DCS records

This can be done via the ArchivesSpace API. In cases where additional description is warranted, data can be taken from the MADID spreadsheet and transformed into valid ArchivesSpace records. These ArchivesSpace URIs can then be listed alongside the image OID, and then reassociated via the ‘Update Parent Objects’ batch process in the DCS management app

## Questions

* Are there any MADID images that should be removed from DCS?
    * Possibly partial publications, depending on existence of fully digitized pub
* Is there any data in Ladybird that we want to add to existing ArchivesSpace records?
    * Data that can be added to DCS child records: caption, maybe dimensions (though image size is in pixels); copyright
    * What to do about genre/form terms. May be a question for a larger group, including Mark C.
    * Where should this data be added if individual records are not created in Aspace - if parent objects are created in DCS, with multiple MADID images as children, can any of the data that is in individual MADID records be aggregated and added to the ArchivesSpace record? For instance, if there are 10 MADID images combined under a single parent and linked to an archival object, and there are 5 unique genre/form terms associated with those images, could the genre/form terms be linked as subject to the associated ArchivesSpace record?
* Any way to determine how much of the material is digitized without calling back every box?
    * Generate report of number of boxes/barcodes; may want to call these back

## Data

* **[MADID spreadsheet](https://docs.google.com/spreadsheets/d/15xYPCTwMx3F5H_q20100_-RkiCS9noNXf9VNBetLN_Y/edit) - working document; make all changes to this document**
* [MADID Spreadsheet](https://docs.google.com/spreadsheets/d/1BBXhRiLAO55sOVxgqlb6hLOB8L1UO4CFqaxS38NEfUU/edit) (original)
    * Question: seem to be a lot more images here than are actually part of the MADID collection. Why is this? Should I match up with just the OIDS from what is actually in DCS?
* [Report](https://docs.google.com/spreadsheets/d/1LOrpc9-wbzVGkDYH7Bv5lFp1rCvryKsClmj7c8wd7AI/edit#gid=1699582303): Archival objects with more than 50 MADID images. Can create new parents for these
* [DCS Management App](https://collections.library.yale.edu/management)
* [MSSA objects in DCS](https://collections.library.yale.edu/catalog?f%5Brepository_ssi%5D%5B%5D=Manuscripts+and+Archives)

## References

* [YUL Digital Collections System Policy](https://yaleedu.sharepoint.com/sites/YULITSC9/Documents%20Open%20to%20YUL/Forms/AllItems.aspx?id=%2Fsites%2FYULITSC9%2FDocuments%20Open%20to%20YUL%2FApprovedPolicies%2FPolicy%5FDigitalCollectionsSystem%5FFinal%5F10082020%2Epdf&parent=%2Fsites%2FYULITSC9%2FDocuments%20Open%20to%20YUL%2FApprovedPolicies)
* [Digital Collections Initiative FAQs](https://yaleedu.sharepoint.com/:b:/r/sites/YULDCSAG/Documents%20Open%20to%20YUL/Reference/DCIP_FAQs_20200921.pdf?csf=1&web=1&e=iHyq4r)
* [Reassociation Project Instructions](https://docs.google.com/document/d/1T3GH0iVQWYRTe3bdRy0mxxsNhMfyfHJFtbVYQW9lzpc/edit)
* [MADID-to-Find-It Migration Documentation](https://docs.google.com/document/d/1R1zi4VT4AfgIwaWrb9En0TnavVnxLNi5AyP5CkgkN5M/edit)
* [Digital Collections System Data Model](https://docs.google.com/document/d/1Ho4uKCjaAk7zel_izCS4D0ZkGkVAKiYA/edit?rtpof=true)
* [Metadata Cloud Mappings](https://metadata-api.library.yale.edu/metadatacloud/public/index.html)