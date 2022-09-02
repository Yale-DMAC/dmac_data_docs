# archivesspace-templates

Scripts for generating JSON and CSV templates for creation of records in ArchivesSpace.

## Requirements

* Python 3.4+
* ArchivesSpace 2.4+
* `ArchivesSnake` module

## Getting Started

To get templates for all record types:

```
$ cd /path/to/archivesspace_templates
archivesspace_templates $ python
Python 3.6.2 |Anaconda custom (x86_64)| (default, Sep 21 2017, 18:29:43)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import parse_schemas as ps
>>> template = ps.ASTemplates()
>>> all_schemas = template.all_schemas
>>> all_temps = template.parse_schemas(all_schemas)
>>> import pprint
>>> pprint.pprint(all_temps['date'])
{'begin': None,
 'calendar': ['gregorian', 'julian'],
 'certainty': ['approximate', 'inferred', 'questionable'],
 'date_type': ['bulk', 'inclusive', 'range', 'single'],
 'end': None,
 'era': ['bce', 'ce'],
 'expression': None,
 'jsonmodel_type': 'date',
 'label': ['agent_relation',
           'broadcast',
           'copyright',
           'creation',
           'deaccession',
           'digitized',
           'event',
           'existence',
           'issued',
           'modified',
           'other',
           'publication',
           'usage',
           'record_keeping']}
>>>
```
