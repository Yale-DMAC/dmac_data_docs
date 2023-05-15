# Yale ArchivesSpace Upgrade Guide

This document describes the process for upgrading Yale's production instance of ArchivesSpace

## Testing Checklist

ArchivesSpace upgrade testing is managed by the Yale Archival Management Systems Committee (YAMS). Testing should begin at least 6-8 weeks prior to the desired upgrade date. The spreadsheet used for testing can be found [here](https://docs.google.com/spreadsheets/d/1RdYJtq4dWk35Kt6osg-ncAU70CfqyOpSGHbTdvU6W4c).

### Integrations

It is very important to test all integrations with Yale's ArchivesSpace. A list of integrations is as follows:

- Preservica
- Aviary
- ICE
- LSF Tool
- Aeon
	- Web interface integration
	- Client add-on
- Nightly EAD export
- Metadata Cloud
	- Digital Collections System (DCS)
	- Quicksearch

When testing begins, YAMS will notify the product owner of each system which is integrated with ArchivesSpace of all changes which may affect the integration. This gives the product owners time to resolve any issues which may be caused by the upgrade.

## Process for Indexing Production Database on Lyrasis QA Server

Due to the size of Yale's ArchivesSpace database and the fact that Yale uses the ArchivesSpace public interface, when a full re-index is required it is necessary to begin this indexing process several days before performing the production upgrade. This eliminates any Archives at Yale downtime due to indexing. Each step in the indexing process is described below.

### Create a new ArchivesSpace image from Github and push to Docker Hub. 

See the [Yale ArchivesSpace Custom Build Workflow](https://dmac-data-docs.readthedocs.io/en/latest/development/aspace_custom_build_workflow.html) document for instructions on how to do this.

### Update the `aspace_deployment` repository

The `YaleArchivesSpace/aspace_deployment` repository contains Yale's custom configuration information - a list of plugins, YAML translation files, and custom `config.rb` settings. 

#### Ensure that the aspace_deployment repository is using the correct list of plugins

Upgrading ArchivesSpace requires that Yale's plugins also be updated to be compatible with the new version of the core code. 

#### Ensure that the aspace_deployment repository contains the correct translation files

#### Ensure that the aspace_deployment repository contains all necessary configration options

### Import the database copy to the QA server's MySQL instance

### Run the database migrations against the database

### Start the indexer

## Indexing Configuration

The PUI indexer can run out of memory when processing large records. This will cause the indexer to restart the indexing for the repository that it was currently working on. To prevent this, update the `config.rb` file with the following settings:

```
# Staff Indexer Settings
AppConfig[:indexer_records_per_thread] = 4
AppConfig[:indexer_thread_count] = 25
AppConfig[:indexer_solr_timeout_seconds] = 900

# PUI Indexer Settings
AppConfig[:pui_indexer_enabled] = true
AppConfig[:pui_indexing_frequency_seconds] = 30
AppConfig[:pui_indexer_records_per_thread] = 15
AppConfig[:pui_indexer_thread_count] = 1
```

## Resources

- [ArchivesSpace Technical Documentation: Upgrading](https://archivesspace.github.io/tech-docs/administration/upgrading.html)
- [Yale ArchivesSpace Custom Build Workflow](https://dmac-data-docs.readthedocs.io/en/latest/development/aspace_custom_build_workflow.html)
- [Yale ArchivesSpace testing spreadsheet](https://docs.google.com/spreadsheets/d/1RdYJtq4dWk35Kt6osg-ncAU70CfqyOpSGHbTdvU6W4c)
- [ArchivesSpace deployment repository](https://github.com/YaleArchivesSpace/aspace-deployment)