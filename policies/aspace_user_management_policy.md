# Yale ArchivesSpace User Management Policy

## Introduction

This policy governs: 

* The creation, management, and deactivation of user accounts within ArchivesSpace
* The granting and revocation of privileges associated with each user account
* The authentication by which the user establishes a connection to their account

## Rationale

This approach to user groups gives the greatest possible flexibility to workers in repositories to assign and remove privileges as staff responsibilities change while still protecting the data in other repositories. These permissions atomize common work functions (creation, read access, update access, and delete) by record type (accessions, resources, containers, and records shared across repositories) and make clear which functions affect only the user’s repository and which affect all repositories. 

## Scope

This policy applies to all ArchivesSpace accounts at Yale University. This document includes statements on access control, privileges, authentication/password management, and the information required to request a user account.

## Access Control

* Access to ArchivesSpace will be primarily limited to users with Yale NetIDs who require access to the system for their work. Users external to Yale (e.g., consultants) may be granted access to the system on a case-by-case basis. 
* Access is managed separately for all three instances of ArchivesSpace at Yale: development (DEV), production (PROD), and test (TEST). Access to the TEST and DEV environments is managed on an as-needed basis.
* Certain software systems which are integrated with ArchivesSpace (i.e. Preservica, EAD export service) utilize user accounts to perform GET and POST requests against the ArchivesSpace API. These accounts are identified by the name of the service (i.e. preservicaprod, ead_export_service). 
* The YAMS co-chairs have system administrator permissions. Additional system administrator permissions may be granted on a case-by-case basis.
* The person enacting any change to a user account must be different from the person requesting the change.
* Accounts should never be deleted from the ArchivesSpace database; instead, when a user no longer requires access to the ArchivesSpace database, their account will be deactivated by removing any repository roles associated with that account.
* Repository managers are responsible for either deactivating user accounts themselves or alerting YAMS when staff or student workers are no longer active.
* Accounts will be reviewed annually by YAMS for inactive NetIDs to determine if any need to be deactivated. 
* Accounts may be re-activated -- but only after a request has been issued and approved by following the same procedures required for requesting a new account.

## Authentication/Password Management

For authentication to the Staff Interface, ArchivesSpace will use CAS for staff logins, thereby allowing most users to manage passwords externally.

For authentication to the API, users will have to use a local password. These can be set by the system administrator and will have to be reset by the same.

A system administrator account exists but is not used. That account’s password may be reset by a sysadmin if the account must be used.

Aside from administrative and API passwords, no other passwords should be assigned within the ArchivesSpace application.

## Guidance for Users

Getting access to ArchivesSpace requires following the User Account Creation steps as outlined in the YAMS LibGuide: [Yale Archival Management Systems Committee: User Account Creation](https://guides.library.yale.edu/c.php?g=296249&p=4694567)

In order for the user to be assigned roles within the system, she must follow the above guidelines to create her account. These steps are necessary in order for the username (the user’s NetID) to be present in the system and for her repository manager to assign her roles.

The second step is for the repository manager to give that user access to whichever user groups the repository manager deems appropriate. All groups are additive and access must be explicitly granted to each group.

For instance, if you want a user to be able to create accessions AND resources, you must add that user to both the “Create, read, and update accessions and top containers” group and the “Create, read and update resources and top containers” group. A user can be assigned to a group by entering her NetID in the “Members” field of a group. This step must be repeated for each group that a user will be assigned to.

Multiple user groups may also be assigned to a user by selecting their username under Manage Users, then selecting Edit Groups. User groups can be added or removed by checking and unchecking the check boxes next to each user group. See the [User Groups at Yale](#user-groups-at-yale) section of this document for definitions and permissions associated with each group.

## Guidance for Assigning Permissions

### Repository managers internal to the repository

Repository managers generally have the following permissions within their repository:

* Assessments -- Create, read, update and delete assessment records
* Create-accessions -- Create, read, and update accessions and top containers
* Create-digital-object -- Create, read and update digital objects
* Create-events -- Create, read and update event records
* Create-resources -- Create, read and update resources and top containers
* Delete-records -- Delete records from this repository
* Import-jobs -- Initiate and cancel an import job
* Manage-top-containers -- Delete or bulk update top containers in this repository
* Merge-records -- Merge records from this repository
* Repository-managers -- Manage a repository (manage locations, user groups, department codes, user access)
* Subject-agent -- Create, read, merge, update and delete subject or agent records (affects all repositories)
* Suppress-records -- Suppress records from this repository
* Transfer-distinct-records -- Transfer distinct records across a repository
* View-records -- View (non-suppressed) records in this repository
* View-suppressed-records -- View suppressed records in this repository
* Vocabulary-classification -- Create, read, update and delete vocabulary or classification terms (affects all repositories)

### Archivist staff members internal to the repository

Archivist staff members generally have the following permissions within their repository:

* Assessments -- Create, read, update and delete assessment records
* Create-accessions -- Create, read, and update accessions and top containers
* Create-digital-objects -- Create, read and update digital objects
* Create-events -- Create, read and update event records
* Create-resources -- Create, read and update resources and top containers
* Delete-records -- Delete records from this repository
* Import-jobs -- Initiate and cancel an import job
* Manage-top-containers -- Delete or bulk update top containers in this repository
* Merge-records -- Merge records from this repository
* Subject-agent -- Create, read, merge, update and delete subject or agent records (affects all repositories)
* View-records -- View (non-suppressed) records in this repository
* View-suppressed-records -- View suppressed records in this repository
* Vocabulary-classification -- Create, read, update and delete vocabulary or classification terms (affects all repositories)

### Technical services support staff members internal to the repository

Technical services support staff members generally have the following permissions within their repository:

* Assessments -- Create, read, update and delete assessment records
* Create-accessions -- Create, read, and update accessions and top containers
* Create-digital-objects -- Create, read and update digital objects
* Create-events -- Create, read and update event records
* Create-resources -- Create, read and update resources and top containers
* Delete-records -- Delete records from this repository
* Import-jobs -- Initiate and cancel an import job
* Manage-top-containers -- Delete or bulk update top containers in this repository
* Merge-records -- Merge records from this repository
* Subject-agent -- Create, read, merge, update and delete subject or agent records (affects all repositories)
* View-records -- View (non-suppressed) records in this repository
* Vocabulary-classification -- Create, read, update and delete vocabulary or classification terms (affects all repositories)

### Staff members internal to the repository without data entry responsibilities

Non-technical services staff members generally have the following permissions within their repository:

* View-records -- View (non-suppressed) records in this repository

The following additional permissions may also be added in some instances, if the staff member requires these permissions for their work and has received proper training:

* Create-accessions -- Create, read, and update accessions and top containers 
* Create-digital-objects -- Create, read and update digital objects 
* Create-events -- Create, read and update event records 
* Create-resources -- Create, read and update resources and top containers

### Student staff members in the repository

Student staff members generally have the following permissions within their repository:

* Create-events -- Create, read and update event records
* Create-resources -- Create, read and update resources and top containers
* Manage-top-containers -- Delete or bulk update top containers in this repository
* View-records -- View (non-suppressed) records in this repository

### Staff members external to the repository

In some cases, staff members at Yale have repository permissions for repositories outside of their home repository. For example, as noted above, the YAMS co-chairs have system administrator permissions. In some cases, staff members in one repository or department require permissions in another repository. Such permissions are granted by the repository managers on a case-by-case basis and are documented by YAMS in a spreadsheet of who has which exceptional permissions and why. YAMS periodically audits that list against the Account Manager.

## User Groups at Yale

User groups at Yale are comprised of a set of functions that a user can perform. These functions are hard-coded into the application and not changeable. This means that although we have a great deal of flexibility in assigning permissions as sets of these hard-coded functions, there are some options that are simply not available. For instance, the “view records” function gives a user permission to view all non-suppressed records in a repository. At this time, there is no option to only let users see a single record type (e.g., only accessions or only resources).

### Yale User Permission Groups

**Create, read, update and delete assessment records**
assessments*

X create/update assessment records
X delete assessment records

\*BRBL only as of 6/2020

**Manage a repository (manage locations, user groups, department codes, user access)**
*repository-managers*

X manage this repository (change groups and other settings)
X create and run a background job
X cancel a background job

**Transfer the entire contents of a repository**
*transfer-contents*

X transfer the entire contents of a repository

**Transfer distinct records across a repository**
*transfer-distinct-records*

X transfer major record types between repositories

**Create, read, and update accessions and top containers**
*create-accessions*

X create/update accessions in this repository
X view the records in this repository
X create/update top container records

**Create, read and update resources and top containers**
*create-resources*

X create/update resources in this repository
X view the records in this repository
X create/update top container records
X delete/bulk update top container records \*BRBL
X manage RDE templates

**Create, read and update digital objects**
*create-digital-objects*

X create/update digital objects in this repository
X view the records in this repository

**Create, read and update event records**
*create-events*

X create/update event records in this repository
X view the records in this repository

**Create, read, update and delete container profile records (affects all repositories)**
*container-profiles*

X create/update/delete container profile records

**Suppress records from this repository**
*suppress-records*

X suppress the major record types in this repository
X view suppressed records in this repository

**Delete records from this repository**
*delete-records*

X delete event records in this repository
X delete the major record types in this repository
X delete/bulk update top container records

**Delete or bulk update top containers in this repository**
*manage-top-containers*

X  delete/bulk update top container records

**Merge records from this repository**
*merge-records*

X merge the major record types in this repository

**View suppressed records in this repository**
*view-suppressed-records*

X view suppressed records in this repository

**View (non-suppressed) records in this repository**
*view-records*

X view the records in this repository

**Initiate and cancel an import job**
*import-jobs*

X create/update resources in this repository \*BRBL only
X view the records in this repository \*BRBL only
X initiate import jobs
X cancel an import job
X merge the major records types in this repository \*BRBL only
X create and run a background job
X cancel a background job

**Create, merge, update and delete subject or agent records (affects all repositories)**
*subject-agent*

X create/update/delete subject records
X create/update/delete agent records
X merge agent/subject records

**Create, update and delete vocabulary or classification terms (affects all repositories)**
*vocabulary-classification*

X create/update classifications and classification terms
X delete classifications and classification terms
X create/update/delete vocabulary records

### Custom User Permission groups

**Printed Acquisitions**
*Printed-Acq*

X create/update accessions in this repository
X create/update event records in this repository
X view the records in this repository
X initiate import jobs
X cancel an import job

\*BRBL only

**Student workers**
*MusicLibraryStudentStaff*

X create/update resources in this repository
X view the records in this repository
X create and update top container records

\*Music only

**Delete/Cancel/Transfer permissions not explicitly specified in other groups**
*higher_level_permissions*

X transfer the entire contents of a repository
X delete event records in this repository
X transfer major record types between repositories
X view suppressed records in this repository
X create/update classifications and classification terms
X delete classifications and classification terms
X cancel an import job
X merge the major record types in this repository

\*Fortunoff_Testimonies only

### User Permission Groups provided in ArchivesSpace by Default

**System Administrator**

Has all read/write and functional permissions for all repositories sharing the ArchivesSpace installation.

**Advanced Data Entry users of the [Repo name] repository**
repository-advanced-data-entry*

X create/update accessions in this repository
X create/update resources in this repository
X create/update digital objects in this repository
X create/update event records in this repository
X view the records in this repository
X initiate import jobs
X create/update/delete subject records
X create/update/delete agent records
X create/update/delete vocabulary records
X create/update top container records
X delete/bulk update top container records
X create/update/delete container profile records
X create/update/delete location profile records
X create and run a background job


**Archivists of the [Repo name] repository**
*repository-archivists*

X create/update accessions in this repository
X create/update resources in this repository
X create/update digital objects in this repository
X create/update event records in this repository
X view the records in this repository
X initiate import jobs
X create/update/delete subject records
X create/update/delete agent records
X create/update/delete vocabulary records
X create/update top container records
X delete/bulk update top container records
X create/update/delete container profile records
X create/update/delete location profile records
X create and run a background job

**Basic data entry users of the [Repo name] repository**
*repository-basic-data-entry*

X create/update accessions in this repository
X create/update resources in this repository
X create/update digital objects in this repository
X view the records in this repository
X create and run a background job

**Managers of the [Repo name] repository**
*repository-managers*

X manage this repository
X create/update accessions in this repository
X create/update resources in this repository
X create/update digital objects in this repository
X create/update event records in this repository
X suppress the major record types in this repository
X delete the major record types in this repository
X view the records in this repository
X initiate import jobs
X create/update/delete subject records
X create/update/delete agent records
X create/update/delete vocabulary records
X create/update top container records
X delete/bulk update top container records
X create/update/delete container profile records
X manage RDE templates
X create/update/delete location profile records
X create and run a background job
X cancel a background job

**Project managers of the [Repo name] repository**
*repository-project-managers*

X create/update accessions in this repository
X create/update resources in this repository
X create/update digital objects in this repository
X create/update event records in this repository
X suppress the major record types in this repository
X delete the major record types in this repository
X view the records in this repository
X initiate import jobs
X create/update/delete subject records
X create/update/delete agent records
X create/update/delete vocabulary records
X merge agent/subject records
X create/update top container records
X delete/bulk update top container records
X create/update/delete container profile records
X create/update/delete location profile records
X create and run a background job
X cancel a background job

**Viewers of the [Repo name] repository**
*repository-viewers*

X view the records in this repository

5/2015; revised 12/2018; revised 6/2020
