# chit_archives_scripts

Repo to store CHIT-related work on archival and manuscript metadata reconciliation

## Requirements

* [`utilities`](https://github.com/ucancallmealicia/utilities) package for file processing and http utilities

## Survey

### Metadata schemas and controlled vocabularies for agents and subjects currently in use by YUL special collections and BRBL

#### Metadata schemas

ArchivesSpace metadata schemas for agents and subjects:

* [abstract_agent](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/abstract_agent.rb)
* [agent_person](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_person.rb)
* [agent_family](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_family.rb)
* [agent_corporate_entity](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_corporate_entity.rb)
* [agent_contact](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_contact.rb)
* [name_corporate_entity](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_corporate_entity.rb)
* [name_family](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_family.rb)
* [name_person](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_person.rb)
* [telephone](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/telephone.rb)
* [subject]
* [term]

ArchivesSpace documentation

* [Ruby YARD docs](http://archivesspace.github.io/archivesspace/doc/)
* [tech-docs](https://github.com/archivesspace/tech-docs)
* [API Docs](http://archivesspace.github.io/archivesspace/api/)


XML-based schemas:

* [EAC-CPF](https://eac.staatsbibliothek-berlin.de/schemata-and-tag-library/)
* [EAD 2002](https://www.loc.gov/ead/eadschema.html)
* [EAD 3](https://www.loc.gov/ead/EAD3taglib/index.html)

Example of JSON agent and subject records from ArchivesSpace

[agent_person](record_examples/agent_person.json)

[agent_corporate_entity](agent_corporate_entity.json)

[agent_family](agent_family.json)

[subject](subject.json)

[resource record with linked agents](resource_with_links.json)

Examples of collection-level EAD files with linked agents (exported from ArchivesSpace):

[EAD 2002](/record_examples/ead_2002.xml)

[EAD 3](/record_examples/ead_3.xml)

#### Controlled vocabularies

Agents

* Personal names, corporate names: [Library of Congress Name Authority File (LCNAF)](http://id.loc.gov/authorities/names.html)
* Family names: [Library of Congress Subject Headings (LCSH)](http://id.loc.gov/authorities/subjects.html)

Subjects

* [Art and Architecture Thesaurus (AAT)](https://www.getty.edu/research/tools/vocabularies/aat/index.html)

### Overview of previous reconciliation work performed on archival metadata

Deliverables:

* [Task Force Documentation](https://drive.google.com/drive/u/0/folders/0B7qoM_riUwnbMDBtZGpMZEQtbVk)
* [Task Force Final Report](https://docs.google.com/document/d/118o923PDYmTeP_0Xb74wxVUfTOzeLdKGQpdMCjnJf4Y/edit)
* [Task Force Future Recommendations](https://docs.google.com/document/d/1mz8-K8sjCxkx9wf8m6fNkBTQ9pM6F48qyfG9EELq9_I/edit)
* [Ruby app that parsed MARC fields and downloaded authority files](https://github.com/mark-cooper/authorizer)
* [ArchivesSpace authority record importer](https://github.com/lyrasis/aspace-importer)

## Work Plan

* Spring 2020 student [job description](https://docs.google.com/document/d/1C8zBbFWC9V2N3Hs4lHZyrkhrIebDun6eDEtnj39Y8ts/edit)

Preliminary task list:

* Reconcile agents and subjects with existing LCNAF and AAT URIs against Wikidata, SNAC, ULAN, VIAF others?
* Reconcile agents and subjects without existing LCNAF and AAT URIs against Wikidata (pulling LCNAF and other URIs from Wikidata where possible) - includes agents created since last reconciliation and potentially another round on agents which were not found in previous round (using OpenRefine, possibly)
* Edit and upload duplicate detection script to GH repo
* Create reports for use in reconciliation (i.e. will need to have links to finding aids side-by-side with agent records for manual review)
* Create instructions for authority reconciliation in OpenRefine
* Import of authority records into ArchiveSpace following previous processes
* Review of results
* Data audit of agent and subject records in ArchivesSpace (partially Python, partially OpenRefine)
* Cleanup of agent and subject records in ArchivesSpace
* De-duplication - should this happen before or after reconciliation. Or both?
* Planning for storage of additional URIs - no way in ArchivesSpace to store more than one
* Compare and remediate differences between ArchivesSpace and Voyager agent and subject records

## Reports from ArchivesSpace

* [Agents - people, all fields](/archivesspace_sql_queries/agent_person_data.sql)
* [Agents - corporate entities, all fields](/archivesspace_sql_queries/agent_corporate_entity_data)
* Agents - families, all fields
* All agent links
* All subjects, all fields
* All subject links
* All agents with URIs
* All agents without URIs
* All agents created since July 21, 2018 with URIs
* All agents created since July 21, 2018 without URIs
* All subjects created since July 21, 2018 with URIs
* All subjects created ince July 21, 2018 without URIs
* Counts?

## Data Sources

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)
* [id.loc.gov](http://id.loc.gov/)
* [Getty](https://www.getty.edu/research/tools/vocabularies/lod/)
* [SNAC](https://snaccooperative.org/?command=api_help)
* [VIAF](https://www.oclc.org/developer/develop/web-services/viaf.en.html)
* ArchivesSpace

## Resources to Consult

* [Questioning Authority](https://github.com/samvera/questioning_authority#what-does-this-do)
* [LD4P Lookup Service](https://lookup.ld4l.org/)
* [Metaphactory](https://www.metaphacts.com/product)
* [Wikidata Authority Control](https://www.wikidata.org/wiki/Wikidata:WikiProject_Authority_control)
* [Wikidata Data Access](https://www.wikidata.org/wiki/Wikidata:Data_access#MediaWiki_API)
* [Wikibase Data Model](https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON#Example_)
* [Extracting Data From Wikidata JSON](https://stackoverflow.com/questions/46383784/wikidata-get-all-properties-with-labels-and-values-of-an-item)
* [Example Workflow for Python-based SPARQL Queries](https://towardsdatascience.com/questions-96667b06af5)
* [Linking records back to Wikidata](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/393724/Dokumentation_P485_Import.pdf?sequence=1&isAllowed=y)
* [Wikidata Tools for Programmers](https://www.wikidata.org/wiki/Wikidata:Tools/For_programmers)
* [WikidataIntegrator](https://github.com/SuLab/WikidataIntegrator)
* [Extracting info from Wikidata responses, 1](https://stackoverflow.com/questions/38906932/how-to-programmatically-get-all-available-information-from-a-wikidata-entity)
* [Extracting info from Wikidata responses, 2](https://stackoverflow.com/questions/31266398/getting-readable-results-from-wikidata/31290824
)
