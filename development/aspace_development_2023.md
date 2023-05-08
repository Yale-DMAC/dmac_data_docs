# ArchivesSpace Development FY 2023

This document describes updates to Yale's instance of ArchivesSpace that are happening as part of the FY2023 development cycle.

## Upgrade to ArchivesSpace 3.3.1

The primary change to the system in this cycle is the upgrade to ArchivesSpace 3.3.1 from version 2.7.1. Yale's core ArchivesSpace differs somewhat from the core code in 3.3.1 - primarily due to the single-scroll view - and so must be rebased with the new version prior to the upgrade. This upgrade process began in January 2023 and will be completed on Tuesday, June 30, 2023.

### What's new in ArchivesSpace 3.3.1?

The official release notes for all ArchivesSpace versions can be found [here](https://github.com/archivesspace/archivesspace/releases). Each release contains many bug fixes and new features. The most relevant changes for Yale staff are outlined below.

#### Agent Model redesign

ArchivesSpace v3 introduces a major redesign of the agents data model, in an effort to be more compliant with the EAC-CPF standard for describing people, families, and corporate entities. Many new subrecords and fields are now included in agent records. For additional information on the new fields, please see this webinar produced by Lyrasis: 

[![Webinar](https://img.youtube.com/vi/SRLfUR6_6bA/hqdefault.jpg)](https://youtu.be/SRLfUR6_6bA)

Policies surrounding usage of the new agents model at Yale are still being developed. For the time being, continue to follow the current [Agents and Subjects Best Practices](https://dmac-data-docs.readthedocs.io/en/latest/policies/agents_and_subjects_best_practices.html) when creating new agent records or updating existing records. YAMS/DMAC/AAG will provide additional guidance as policies surrounding its usage are developed.

The only exception is the placement of the authority ID (e.g. LCNAF URI). In previous ArchivesSpace versions, the authority ID was entered into the Authority ID field in the first name form subrecord of an agent record. In the new version, this ID should be entered into the Record ID subrecord. The upgrade process will include a migration of all existing authority IDs to this field, so no retrospective cleanup is necessary. 

Please also note that the LCNAF plugin will be disabled in Yale's ArchivesSpace instance, as some of the mappings may need to be customized to conform to Yale's descriptive standards.

#### User account management

Non-admin users can now manage their own accounts - you no longer have to contact YAMS to change your password!

Additionally, it is now possible for ArchivesSpace admins and repository managers to mark users as 'inactive', which will ease the process of removing permissions for staff and students who are no longer employed by Yale Special Collections. 

#### Container Management Updates

A few notable updates to the container management module include:

- Subcontainer barcodes
- Merge top containers
- Bulk top container indicator update


#### Link accessions to archival objects

In prior versions of ArchivesSpace it was only possible to link accession records to resource records. This new feature permits users to link accession records to archival objects.

#### Spreadsheet importer

Beginning in ArchivesSpace v2.8, the spreadsheet importer plugin is available in the core code. Yale did not use the plugin, instead relying on the Excel-EAD Oxygen transformation process for spreadsheet ingest.

YAMS is still developing guidelines surrounding the use of this feature, so please do not use the feature in production until 

#### Search updates

1. Repository records associated with archival object and resource records are no longer indexed. This reduces the number of false positive results - e.g. searching for 'Wall' previously returned all Beinecke records, as '120 Wall Street' is part of the Beinecke repository record.

#### Assorted other changes affecting staff users

- BUG FIX: facets are now retained in the PUI
- BUG FIX: Ordered records data loss

#### Notable infrastructure updates

- External Solr

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

The following API endpoints have been added to version 3.3.1:

Please contact DMAC if any of these API changes impact your integrations with ArchivesSpace.


#### Config Changes

## Yale-Specific Updates

### Import/Export updates

You may have noticed that our controlled value lists get messy over time. This is because when importing an EAD file, if a controlled value that is not already in the list is present in the EAD file, that value is added to the database.

### Plugin Changes

Updates to child_publisher so internal notes created by the Preservica sync are not published when using the publish all feature.


