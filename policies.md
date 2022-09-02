# Policies

Policies and best practices for special collections metadata managed by DMAC and YAMS.

- [ArchivesSpace API Best Practices](#archivesspace-api-best-practices)
- [Best Practices for ArchivesSpace Metadata Creation](#best-practices-for-archivesspace-metadata-creation)
- [Agents and Subjects Best Practices](#agents-and-subjects-best-practices)
- [Conditions Governing Access Notes for Born-Digital Material](#conditions-governing-access-notes-for-born-digital-material)

## ArchivesSpace API Best Practices

__Purpose of This Guide__

Introduce YUL ArchivesSpace users to best practices and guidelines surrounding usage of the ArchivesSpace API. Provide tips for safely performing operations against the API.

__Target audience__

YUL ArchivesSpace users with YUL-focused API training.

__Resources for Getting Started__

- Github repository for API training: https://github.com/yalemssa/api_environment_setup
- Introduction to Metadata Power Tools for the Curious Beginner (by Maureen Callahan, SAA 2015): https://docs.google.com/presentation/d/1Pqs5_J6C9y6-Nw-QJ0rCrnkugUEianYdqCNNHhXYpJc/edit#slide=id.gc63ed3508_0_0

__Be Aware of the Risks of Using the API__

- There is no undo button
- There is no edit history
- It is easy to overwrite and delete data
- Can unknowingly make many mistakes very quickly

__What our systems and policies do to identify and prevent problems__

- MySQL database is read-only (though it is not possible to limit access by repository)
- API access is scoped to individual user permissions - users can only do things via the API that they can do in the staff interface
- The JSONModel schema contains numerous constraints on data entry which are enforced by the API. These can be extended or modified via a plugin (e.g. [yale data rules](https://github.com/YaleArchivesSpace/yale_data_rules)
- The API performs a number of additional data [validations](https://github.com/archivesspace/archivesspace/blob/master/common/validations.rb) before creating or updating records. These can be extended or modified via a plugin.
	- For example, API updates will fail if a user tries to add an enumeration value which is not already in the database (this is NOT true when importing EAD files via the Background Jobs interface - improperly formed enumeration values are added to the database)
- The lock version function prevents users from updating the a record simultaneously
- 3 YUL ArchivesSpace instances - PROD, TEST, DEV - with [business rules](https://docs.google.com/document/d/17UDqjo2P49esTpbl8W5c_xnXFGZOfp0ft2LMFmmXqEg) for each
- Periodic data auditing and reporting

__What users must do to prevent problems__

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

---

## Proposed Best Practices for ArchivesSpace Metadata Creation
December 10, 2018

__Introduction__

With the move into the ArchivesSpace Public User Interface (Archives at Yale) and its direct link to the Staff User Interface, it is important to address standardization for metadata creation and updates by repositories. Therefore, we are proposing the creation of best practices for metadata creation for ArchivesSpace for several common record and subrecord types that are generally mandatory for inclusion in an ArchivesSpace record.

__Categories and Proposals__

*Dates*

Date sub records currently contains both structured date fields (begin and end), and a free text date field (expression). Data retrieval in ArchivesSpace functions the best with structured data rather than the free text. Therefore, we propose the following:
In cases where dates are clearly known to at least the year, the structured begin and end dates must be filled out. In cases where there is a single year, the date only needs to be added to the begin date field. The free text field does not need to be filled out and in any future data auditing and correction, we will not add any date data to the free text field.

In cases where the date is estimated (circa dates, dates with a question mark), the approximate date will be put into the structured date fields. In the free text field, the date will be inputted with the appropriate modifier. For example, if the date is estimated to be 1924-1926, the structured begin field will read 1924, the structured end field will read 1926, and the free text field will read "circa 1924-1926." Modifiers like "circa" should be fully spelled out rather than abbreviated.

In cases where the data is unknown/cannot be estimated to a specific date range, it should be estimated to the dates of the collection. For example, if a collection is dated 1945-1990, the begin date would be 1945, the end date would be 1990, and the expression field would read "circa 1945-1990."
The Certainty, Era, and Calendar fields do not need to be filled out and we will not address those fields in any data auditing and correction.

*Container types*

Container types allows for researchers to quickly determine the storage format of the materials. This should not be confused with container profiles—the profiles will contain most of the necessary information a researcher or staff member would need to identify physical storage in detail. The container type default for a top container should be set to "Box". The exceptions are microfilm, which will receive the type "reel," folio folders and similar which will receive the type “folder,” and books, which will receive the type "volume."

*Identifiers*

Both accession records and resource records contain identifiers. Accession records' identifiers are formatted automatically in ArchivesSpace. Resource records are free text and contain four fields. We propose that all identifier parts are placed in the first field rather than split across them, although dividers/punctuation choice can be maintained by repository preference. An example using Fortunoff records would be placing "HVT-0001" all together in one field, manually adding the hyphen as we prefer that usage. Meanwhile, Manuscripts and Archives would prefer a space, which looks like "MS 2025," all in the first field.

*Note labels*

A proposal for note labels was circulated in AMDECO in December 2017. We will restate these in this document. In previous systems as well as in ArchivesSpace, we can add our own labels to title notes instead of the default names for the note fields. While some notes, such as General, will necessarily have labels to explain their purpose and other note labels have specific repository policy like the Beinecke's biographical notes using the subject's name as a title, many of the listed notes have had labels over the years that do not have an apparent reason for them to be used over another similar label. We feel the differing labels could cause confusion for users. For instance, it could make researchers unsure if one collection's summary is different from another collection's description of the papers. This could also be tricky for Conditions Governing Access and Conditions Governing Use. Since ArchivesSpace note fields are heavily based on Describing Archives: A Content Standard (DACS) for their naming and all repositories would easily have that available to them for future creation of description, we advise that the labels on all notes except General (<odd>), Biographical (<bioghist>), Associated Materials, Related Materials, or Copy and Version Identification (<relatedmaterial>), and any other notes with compelling policy reasons for variation, are deleted and the PUI defaults to the ArchivesSpace supplied label.

*Note boilerplates for access and use of collections*

A proposal for boilerplates was circulated in AMDECO in December 2017. We will restate these in this document. Collection materials across repositories often had many variations on how to express levels of access and use. While some of these notes include information about repository policy, e.g. Manuscripts and Archives' restriction on listening to A/V masters, the Music library's information about making appointments to view the collection, most of these variations are simply personal or repository word choice. We feel that this could be confusing to researchers using the ArchivesSpace PUI. We also feel, given the unification of all our repositories in our public facing content, it would be advisable to use a common boilerplate. The most common restriction language for materials where there are no qualifiers ("open with permission," "open by appointment," "open for research, except for [specific material]") is "The materials are open for research." We advise that this be the boilerplate in use.

*Agents and subjects*

YAMS has already created a document for Agents and Subjects best practices. We recommend continuation of its use.

*Extent types*

After the controlled value list for extent type receives its final clean-up/remediation, the extent types present on the list should be deferred to as much as possible, with the "See Container Summary" type rarely, if ever used.

*Controlled value lists*

Repository managers cannot add to any controlled value lists without proposing the value to YAMS first for their approval. (Example: Extent type, container profile.)

---

## Agents and Subjects Best Practices

TBD

---

## Conditions Governing Access Notes for Born-Digital Material

This document proposes a procedure for creating file-level access notes for born-digital materials.

__Background__

Facilitating access to born-digital materials described in ArchivesSpace is one of the highest priorities for YAMS and YUL in 2020-2021. YAMS has contracted with HM to develop several features which will permit users to request born-digital materials for reading room use via Archives at Yale and Aeon. As part of the development process, members of the ASC advisory group indicated that public services staff who are processing these requests will need a way to identify the materials as being born-digital, as requests for born-digital materials require special processes to fulfill. 

Currently, most units add a RestrictedFragile local access restriction type to file- or series-level born-digital records in ArchivesSpace. However, this restriction type is also applied to materials that are not born-digital, and so cannot be used by staff users of Aeon to identify born digital materials.

In 2021 YAMS approved a request for the addition of a new local access restriction type, BornDigital, which will be added to born digital records at the most appropriate level of description, adhering to DACS descriptive requirements. This new restriction type will be consumed by Aeon and displayed in the ItemInfo8 field, indicating to staff that the material is born digital.

__Proposed Process__

*Case 1: Born-digital access note does not exist*

Some born-digital materials do not currently have access notes. In these cases, a new note should be created at the appropriate level, with the BornDigital local access restriction type and a text note.

If the collection contains an entire series or other grouping of computer files (i.e. Dworkin), where all children are born-digital, then the local access restriction type and access note text can be applied at the series level, and the local access restriction type will be inherited by all of the children. If the entire collection is born-digital, the restriction type and note can be added at the collection level.

Proposed note text, adapted from MSSA: “As a preservation measure, original materials may not be used. Digital access copies will be provided for use.”

“As a preservation measure, original computer files may not be used. Digital access copies must be provided for use.”

*Case 2: Born-digital access note already exists*

In some cases access notes have already been added to born-digital materials at the appropriate level. For instance, this record. In these cases the BornDigital local access restriction should be added to these existing notes, replacing the RestrictedFragile restriction type.

This case only applies to the retroactive updates. Going forward, processors will add the standard note text at the appropriate level when describing born-digital material.

__Documentation/Maintenance__

Processors will be responsible for creating these access notes during description.

YAMS will periodically run reports to identify born-digital materials which do not have access notes

If approved by BDAWG and AMDECO, this procedure will be added to YUL’s Born Digital Archival Description Guidelines and the YUL ArchivesSpace User Manual. YAMS will announce the new procedure via yulaspace, and each repository liaison will reach out to their units to coordinate the changes.
