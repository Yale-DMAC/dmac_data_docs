# Yale ArchivesSpace Upgrade Guide

This document describes the process for upgrading Yale's production instance of ArchivesSpace

## Testing Checklist

### Core Code

### Customizations to Core

### Plugins

### Integrations

## Indexing on the Lyrasis QA server

### Make a copy of the ArchivesSpace production database.

### Create a new ArchivesSpace image from Github and push to Docker Hub. 

See the [Yale ArchivesSpace Custom Build Workflow] (https://dmac-data-docs.readthedocs.io/en/latest/development/aspace_custom_build_workflow.html) document for instructions on how to do this.

### Ensure that the aspace_deployment repository is using the correct list of plugins

### Ensure that the aspace_deployment repository contains the correct translation files

### Ensure that the aspace_deployment repository contains all necessary configration options

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
- [Yale ArchivesSpace Custom Build Workflow] (https://dmac-data-docs.readthedocs.io/en/latest/development/aspace_custom_build_workflow.html)
- [Yale ArchivesSpace testing spreadsheet](https://docs.google.com/spreadsheets/d/1RdYJtq4dWk35Kt6osg-ncAU70CfqyOpSGHbTdvU6W4c)
- [ArchivesSpace deployment repository](https://github.com/YaleArchivesSpace/aspace-deployment)