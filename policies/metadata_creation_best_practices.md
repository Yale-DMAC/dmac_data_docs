# Proposed Best Practices for ArchivesSpace Metadata Creation
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