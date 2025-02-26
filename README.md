# About SCMS

A Github repository for documentation about the Beinecke Rare Book and Manuscript Library's Special Collections Metadata Services Unit (SCMS).

## What is SCMS

Special Collections Metadata Services (SCMS) provides a comprehensive, cross-collection, and service-centered approach to enabling and enhancing the discovery of Yale Library’s special collections through metadata services, data reporting and analysis, and special collections systems and tool management. 

## SCMS Metadata Services

SCMS provides the following services:

- __Metadata management__: remediation, creation, and enhancement of special collections metadata 
- __Data transformation__: migrations, mappings, data re-use 
- __Reporting and data analysis__
- __Tool and workflow support__: automation and process improvement 
- __ArchivesSpace support__: product ownership, application and user management 
- __Training, documentation, consultation__

These services are provided in multiple contexts. In some cases our work originates internally - e.g. SCMS staff identify and prioritize data problems and opportunities. In others, services are requested by other SCTS units, special collections departments, or repositories. Our services may also be provided as part of our participation on committees, advisory groups, task forces, or working groups. And finally, SCMS services may be provided to support cross-departmental projects, programs, or initiatives.

### Metadata management

Metadata management consists of the bulk remediation, creation, and enhancement of special collections metadata.  

#### Activities 

- Identify and prioritize metadata problems, opportunities, requests 
- Develop strategies for assessing and addressing metadata issues (e.g. data auditing, reporting) 
- Develop metadata project plans 
- Develop ETL-style workflows for managing metadata projects 
- Perform exploratory data analysis and reporting 
- Programmatically manipulate data 
- Develop and execute scripts to update metadata in systems of record 
- Communicate with stakeholders 
- Perform testing and quality assurance activities 
- Maintain and enhance tools, documentation, training materials 

#### Examples

- Identify and delete expired restriction dates
- Clean up controlled value lists in ArchivesSpace
- Update preferred citation notes for Divinity after library name change
- Add structured dates to ArchivesSpace records which previously only had free-text dates
- Add SNAC identifiers to agent records
- Add barcodes to location records
- Delete archival object records for materials which have been reprocessed

#### Stakeholders 

- Special collections metadata-creating departments and units: BRBL-TS: ADU, BDU, ACCU; Divinity Library, Music Library, Arts Library, YCBA, Peabody Museum (Archives) 
- DSCA 
- Cross-unit/departmental projects and committees 
- Archives Advisory Group (AAG) 
- YUL MSC 
- YUL Technical Services 
- Library IT 

### Data transformation

Data transformation services include data migrations and conversions, data re-use projects, and integrations with other systems.

#### Activities 

- Communicate with stakeholders to identify transformation projects/opportunities 
- Perform mapping/crosswalking activities 
- Develop strategies for handling handling data loss in the transformation process 
- Manage system integrations 
- Create requirements documents for use by developers 
- Act as liaison between stakeholders and developers 
- Create documentation 
- Reporting and exploratory data analysis 
- Develop programmatic data transformation tools 
- Plan and execute database migrations 
- Maintain and update existing data mappings and system integrations 
- Coordinate with product owners of other systems 

#### Examples

- Migrate YNHH data from Access database and Word documents to ArchivesSpace
- Migrate Acquisitions DBText database to ArchivesSpace
- Develop mappings between ArchivesSpace and Lux
- Develop mappings between ArchivesSpace and Metadata Cloud/DCS
- Convert architecture project index spreadsheets to ArchivesSpace records
- Convert GLAD box lists to ArchivesSpace records
- Convert Proquest-provided dissertation metadata to Elischolar and Voyager records
- Maintain Excel-to-EAD transformation tool
- Reassociation of data between Find-It/Ladybird and ArchivesSpace
- Integration of ArchivesSpace and Quicksearch
- Integration of ArchivesSpace and DCS

#### Stakeholders 

- Special collections metadata-creating units: BRBL-TS: ADU, BDU, ACCU, DSCA 
- Cross-unit/departmental projects and committees: UDAG, AAG, CHIT/Lux 
- YUL MSC
- Library IT 
- YUL Technical Services 
- Public Services and Operations 

### Reporting and data analysis

Reporting and data analysis activities can stand on their own or be provided as part of another service such as data management and transformation.

#### Activities

- Communicate with stakeholders to identify required data elements 
- Develop and execute queries across multiple systems 
- Develop tools to synthesize data from disparate systems 
- Perform exploratory data analysis and manipulation 
- Present requested information to stakeholders 
- Develop and maintain tools enabling staff to self-run reports 
- Perform regular data auditing and quality assurance 
- Leverage data to support decision making 
- Document and share data analysis tools with professional community

#### Examples

- Report on Papyri records in order to facilitate migration to DCS, additional physical processing, and patron research
- Report of University Archives materials stored at off-site storage
- Report of all acquisitions in the last 5 years
- Reporting to support Special Collections backlog project
- Reports plugin: report of all containers in a given location
- Reports plugin: report of all materials in a given collection that are digitized and in Preservica and/or DCS

#### Stakeholders

- BRBL-TS: ADU, BDU, ACCU 
- DSCA 
- BRBL Administration 
- Public Services and Operations 
- YUL Technical Services 
- Library IT 
- Cross-department/unit committees and projects 
- Digital Preservation Services 

### Tool and workflow support

#### Activities

- Communicate with stakeholders re: workflow needs 
- Identify opportunities for workflow improvements or automation tools 
- Planning, testing, and prototyping of tools and workflows 
- Scripting and tool development 
- Write user and technical documentation, train staff on new workflows 
- Maintain and share tools

#### Examples

- Workflow for automated processing of electronic dissertations
- Copy order fulfillment process for previously digitized materials
- Box and folder labeling process
- Workflow support for Digital Accessioning Service
- LSF barcode search tool
- Reassociation project

#### Stakeholders

- BRBL-TS: ADU, BDU, ACCU 
- Public Services and Operations 
- Digital Preservation Services (DPS) 
- DSCA

### ArchivesSpace Product Ownership and Support

#### Activities

- Policy development surrounding usage of ArchivesSpace (in consultation with advisory groups, MSC, SCSC)
- Triage staff and patron support requests 
- Administration - manage passwords, permissions, account creation 
- Troubleshooting - reporting and resolving system problems (in collaboration with service owner)
- Manage parts of the external development process 
	- Gather user feedback and prioritize development work 
	- Write user stories 
	- Meet with external developers 
	- Test application upgrades, features, plugins, bug fixes 	
	- Coordinate and manage implementations 
	- Maintain plugins on Yale Github accounts 
	- Low effort development work 
- Training and documentation (in collaboration with advisory groups and service owner)
- Manage hosting (in collaboration with service owner)
	- Recommend and manage infrastructure improvements to the hosting environment 
	- Generate Docker images 
- Communicate system changes to stakeholders and provide training 
- Serve as ArchivesSpace representatives on library- or university- wide projects

#### Stakeholders

- All ArchivesSpace staff users 
- Public Services and Operations 
- BRBL Tech Services 
- Archives Advisory Group (AAG) 
- YUL Technical Services 
- Library IT 
- Preservation and Conservation Services 
- Lyrasis (hosting provider) 
- Hudson Molonglo (primary contract developers) 

## How to Update This Documentation

This documentation is generated by Sphinx from scripts, spreadsheets, and various .RST and .MD files within the documentation Github repository.

### Spreadsheets

The spreadsheets are stored in the `_files` directory. The spreadsheets include list of current Yale ArchivesSpace plugins, a list of current DMAC-related Github repositories, lists of completed, active, recurring, and future projects, and a list of ArchivesSpace data that is subject to data auditing protocols. 

The Github repository and plugins spreadsheets are generated via the `get_repo_data.py` script. The project and data auditing spreadsheets are created manually, and are then converted into a table by the Sphinx documentation generator.

### Github Readmes

The `get_repo_data.py` script also pulls in all READMEs from DMAC-related Github repositories, and stores them in the `readmes` directory of the documentation. 

### Other Readmes

Separate directories exist in which policy, workflow, and tutorial documentation can be added. These documents should be .MD files. 

Each directory has a corresponding .RST file in the main directory, which pulls in all of the files which are in the directories and displays them in the generated documentation.

### Building the Docs

To update the documentation, you can edit the files in the repository, and then push your changes to the dmac_data_docs Github repository. The documentation will automatically re-build. 








