# ArchivesSpace API Best Practices

## Purpose of This Guide

Introduce YUL ArchivesSpace users to best practices and guidelines surrounding usage of the ArchivesSpace API. Provide tips for safely performing operations against the API.

## Target audience

YUL ArchivesSpace users with YUL-focused API training.

## Resources for Getting Started

- Github repository for API training: https://github.com/yalemssa/api_environment_setup
- Introduction to Metadata Power Tools for the Curious Beginner (by Maureen Callahan, SAA 2015): https://docs.google.com/presentation/d/1Pqs5_J6C9y6-Nw-QJ0rCrnkugUEianYdqCNNHhXYpJc/edit#slide=id.gc63ed3508_0_0

## Be Aware of the Risks of Using the API

- There is no undo button
- There is no edit history
- It is easy to overwrite and delete data
- Can unknowingly make many mistakes very quickly

## What our systems and policies do to identify and prevent problems

- MySQL database is read-only (though it is not possible to limit access by repository)
- API access is scoped to individual user permissions - users can only do things via the API that they can do in the staff interface
- The JSONModel schema contains numerous constraints on data entry which are enforced by the API. These can be extended or modified via a plugin (e.g. [yale data rules](https://github.com/YaleArchivesSpace/yale_data_rules)
- The API performs a number of additional data [validations](https://github.com/archivesspace/archivesspace/blob/master/common/validations.rb) before creating or updating records. These can be extended or modified via a plugin.
	- For example, API updates will fail if a user tries to add an enumeration value which is not already in the database (this is NOT true when importing EAD files via the Background Jobs interface - improperly formed enumeration values are added to the database)
- The lock version function prevents users from updating the a record simultaneously
- 3 YUL ArchivesSpace instances - PROD, TEST, DEV - with [business rules](https://docs.google.com/document/d/17UDqjo2P49esTpbl8W5c_xnXFGZOfp0ft2LMFmmXqEg) for each
- Periodic data auditing and reporting

## What users must do to prevent problems

- Write effective code
	- Think like a machine - they only do exactly what you tell them to
- Understand the ArchivesSpace data model
- Understand where the data you want to update is situated within that model
- Test all updates in DEV or TEST (preferred) before running in production (REQUIRED)
- Build in ways to make sure that you are actually running against DEV or TEST - print out the URL in your code, ask the user to confirm, etc.
- Review results, preferably with reports rather than just eyeballing
- Peer review. Have a colleague look at your:
	- Code
	- Input data
	- Results
- Document all actions taken against ArchivesSpace records. Add comments to code, write detailed README files. 
- Keep all:
	- JSON backups
	- Input data
	- Scripts
- Organize scripts and data by project/task
