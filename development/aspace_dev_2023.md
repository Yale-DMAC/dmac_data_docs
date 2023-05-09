# ArchivesSpace Development FY 2023

This document describes updates to Yale's instance of ArchivesSpace that are happening as part of the FY2023 development cycle.

## Upgrade to ArchivesSpace 3.3.1

The most significant change to the system in this cycle is the upgrade to ArchivesSpace 3.3.1 from version 2.7.1. Yale's core ArchivesSpace differs somewhat from the core code in 3.3.1 - primarily due to the single-scroll view - and so must be rebased with the new version prior to the upgrade. This upgrade process began in January 2023 and will be completed on Tuesday, June 30, 2023.

### What's new in ArchivesSpace 2.8-3.3.1?

The official release notes for all ArchivesSpace versions can be found [here](https://github.com/archivesspace/archivesspace/releases). Each release contains many bug fixes and new features. The most relevant changes for Yale staff are outlined below.

#### Agent Model redesign


From release notes:

> This release "Centers around changes to the agents module of ArchivesSpace 
> to make it more standards-compliant with EAC-CPF and the MARCXML format for 
> authority data, enabling deeper and richer description of people, families, 
> and corporate entities, their relationships to each other and their 
> relationships to materials held outside ArchivesSpace. This work is the 
> result of a community specification involving the participation of many 
> users across the ArchivesSpace community, mostly notably Cory Nimer, Sue 
> Luftschein, and Brad Westbrook. Through this work new fields and sub-records
> have been added to the agents schema, and staff and public interface views, 
> imports, exports, and auxiliary functionality like agent merging have all 
> been updated. There is also a new Light mode, which provides the option for 
> users to continue to work with agent records in the staff interface in a 
> pared down view that is similar to that of ArchivesSpace versions prior to  
> this one."

[![Webinar](https://img.youtube.com/vi/SRLfUR6_6bA/hqdefault.jpg)](https://youtu.be/SRLfUR6_6bA)

Policies surrounding usage of the new agents model at Yale are still being developed. For the time being, continue to follow the current [Agents and Subjects Best Practices](https://dmac-data-docs.readthedocs.io/en/latest/policies/agents_and_subjects_best_practices.html) when creating new agent records or updating existing records. YAMS/DMAC/AAG will provide additional guidance as policies surrounding its usage are developed.

The only exception is the placement of the authority ID (e.g. LCNAF URI). In previous ArchivesSpace versions, the authority ID was entered into the Authority ID field in the first name form subrecord of an agent record. In the new version, this ID should be entered into the Record ID subrecord. The upgrade process will include a migration of all existing authority IDs to this field, so no retrospective cleanup is necessary. 

Please also note that the LCNAF plugin will be disabled in Yale's ArchivesSpace instance, as some of the mappings will need to be customized to conform to Yale's descriptive standards.

#### User account management

Non-admin users can now manage their own accounts - you no longer have to contact YAMS to change your password!

Additionally, it is now possible for ArchivesSpace admins and repository managers to mark users as 'inactive' with a single click, which will ease the process of removing permissions for staff and students who are no longer employed by Yale Special Collections. 

The user management module is now sortable by name or username, which facilitates quick lookup of staff accounts.

#### Container Management Updates

A few notable updates to the container management module include:

- Subcontainer barcodes
- Merge top containers
- Bulk top container indicator update
- Top container CSV export

#### Link accessions to archival objects

In prior versions of ArchivesSpace it was only possible to link accession records to resource records. This new feature (3.3.0) permits users to link accession records to archival objects. It is also possible to spawn an archival object from an accession record.

#### Spreadsheet importer

Beginning in ArchivesSpace v2.8, the spreadsheet importer plugin is available in the core code. Yale did not use the plugin, instead relying on the Excel-EAD Oxygen transformation process for spreadsheet ingest.

In addition to creating new records, this importer update permits users to update existing archival objects with top containers. 

YAMS is still developing guidelines surrounding the use of this feature, so please do not use the feature in production until further training and policy information is provided.

#### Search updates - Local and Core

1. Change stemmer from Krovetz stemmer to SnowballPorterFilterFactory stemmer
2. Repository records associated with archival object and resource records are no longer indexed. This reduces the number of false positive results - e.g. searching for 'Wall' previously returned all Beinecke records, as '120 Wall Street' is part of the Beinecke repository record.
3. Searching within collection now configurable
4. Agent contact data no longer being indexed
5. Allow narrowing of PUI search by multiple values within the same facet
6. Solr params apply to the PUI in the same way as they do in the SUI
7. Optimizations to improve speed
8. Better search-by-URI
9. More fields excluded from index in core code
10. Built-in apostrophe handling
11. Advanced date search fine-tuning
12. Update full record exclusions

#### Staff interface search, browse, and sort preferences

1. Limit top containers by location in top container search page
2. Browse locations by repository
3. Top container CSV export
5. Add URI to list of fields that can be displayed in search/browse preferences
6. Display indicator that top container has restricted material
7. Many new options for displaying browse and search results in SUI

#### Assorted other changes affecting staff users

__Bug Fixes__

- Facets are now retained in the PUI - date filters, container filters, etc.
- PR 1928: Ordered records data loss
- Fix for `Database integrity constraint conflict: Java::JavaSql::SQLIntegrityConstraintViolationException: Duplicate entry '1836494@archival_object-500' for key 'archival_object.uniq_ao_pos` error (ANW-1020)
- Linking issues in subject and agent records (ANW-73)
- Prevent loss of agent contact details - if a user without permission to view contacts updates a record containing contact records then that data is lost.

__Features__

- New metadata rights declaration subrecord
- Add languge and script of description fields to accession
- Add langmaterial subrecord to accession
- Numerous mapping changes and bulk import fixes
- Many accessibility enhancements to PUI and SUI
- PR 1934: Make file_size_bytes a bigint

#### Notable infrastructure updates

As of ArchivesSpace version 3.2.0, embedded Solr has been removed and external Solr is required. More information about the move to external Solr can be found [here](https://archivesspace.org/archives/7151)

From the release notes:

> Due to some needed accessibility improvements for the public interface, some
> relatively minor styling changes have been made to views in some places.
> This may impact plugins used for styling these areas. Check plugins used to
> theme the public interface to determine if you need to make any changes 
> locally to preserve your desired styling.

#### API changes

The following API endpoints have been removed in version 3.3.1:

```
Endpoint.get_or_post('/search/subjects')
Endpoint.get('/repositories/:repo_id/resources/:id/tree')
Endpoint.get('/repositories/:repo_id/digital_objects/:id/tree')
Endpoint.get('/repositories/:repo_id/classifications/:id/tree')
Endpoint.get('/repositories/:repo_id/archival_contexts/softwares/:id.xml')
Endpoint.get('/repositories/:repo_id/archival_contexts/softwares/:id.:fmt/metadata')
```

Please contact DMAC/YAMS if any of these API changes impact your integrations with ArchivesSpace.

#### Config Changes

One config change supports the enabling/disabling of new custom reporting functionality:

`AppConfig[:enable_custom_reports] = true `

Two config changes support the enabling/disabling of search-within-collection sidebar:

```
AppConfig[:pui_search_collection_from_archival_objects] = false
AppConfig[:pui_search_collection_from_collection_organization] = false
```

## Yale-Specific Updates

### Digital materials tab

- Archival objects will now only appear in the Digital Materials tab if they have a published digital object attached. This will exclide any records from the list which have only a Preservica link.
- Now possible to sort Digital Materials results by "collection order" - e.g. their position in the archival hierarchy.

### Importer update: validation of controlled values

You may have noticed that our controlled value lists get messy over time. This is because when importing an EAD file, if a controlled value that is not already in the list is present in the EAD file, that value is added to the database.

### Other updates to note

Updates to child_publisher so internal notes created by the Preservica sync are not published when using the publish all feature.

### Digital Object information passed to Aeon

