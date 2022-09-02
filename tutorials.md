# Tutorials

A place to put DMAC tutorials

- [Getting Started with the ArchivesSpace API](#getting-started-with-the-archivesspace-api)
- [Guide to the ArchivesSpace Database](#guide-to-the-archivesspace-database)

---

## Getting Started with the ArchivesSpace API

This tutorial introduces the ArchivesSpace API by way of a common archival data cleanup task: updating container numbers. In the following sections you will learn how to:

* Set up a Python environment on your local computer
* Connect to the ArchivesSpace API
* Retrieve top container data for a collection
* Update top container indicators in bulk using a spreadsheet as input.

To get started, clone or download this repository.

Clone or download repo demo:

[![Demo](https://img.youtube.com/vi/FiHwYWIRurQ/hqdefault.jpg)](https://youtu.be/FiHwYWIRurQ)

### Requirements

* Miniconda (Python 3.7+)
* Access to ArchivesSpace API and/or MySQL database
<!-- * `aspace_tools` package -->

### Why Miniconda?

While many computers come with Python built-in, it is often many versions behind the latest release. Installing or upgrading Python packages in the system installation of Python can also cause unexpected conflicts and errors within existing programs. It is highly recommended that you use a virtual environment to avoid these issues.

There are many varieties of virtual environments, each with their own benefits and drawbacks. Anaconda and Miniconda are frequently used by those-who-work-with-data (including archivists!), and they come with frequently-used data processing packages preinstalled. Miniconda is a lightweight version of Anaconda, and both are based on `conda`. A good intro to `conda` can be found [here](https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307).

### Installing Miniconda

* If you already have the full version of Anaconda, [uninstall](https://docs.anaconda.com/anaconda/install/uninstall/) it
* [Download](https://docs.conda.io/en/latest/miniconda.html) Miniconda
* Click on the installer and follow the on-screen setup instructions. Store the program in your home directory (i.e. `C:\Users\your_username\Miniconda3`, `/Users/your_username/Miniconda3`). On Windows, if you choose, per the installer's recommendations, not to add Miniconda to your PATH, you will need to use the Anaconda Prompt or Anaconda Powershell to interact with the interpreter and run scripts from the command line. The Mac installer should automatically make Miniconda your default Python installation.
* After the program is installed, click on the Windows start menu and open the Anaconda Prompt or Anaconda Powershell. If using a Mac, open a Terminal window.
<!-- * To further check your installation, type `echo $PATH` into the prompt. You should see some Miniconda-related directories.
 -->

Download and install Miniconda demo:

[![Demo](https://img.youtube.com/vi/YLwgOZwZUO4/hqdefault.jpg)](https://youtu.be/YLwgOZwZUO4)

Open the Anaconda Prompt or Terminal and enter `python`. This will open the interactive Python interpreter. To check the location of your Python installation, enter `import sys`. Then, enter `sys.executable`. You should see the path to your Miniconda Python executable. To close the Python interpreter and return to the prompt, enter `quit()`.

To see what Python packages are currently installed, type `conda list` into the prompt. You should see that `requests` is already installed. If it is not, enter `conda install requests` into the Anaconda prompt.

On a Mac you can also type `which python` into the Terminal to make sure that you are using the Miniconda distribution.

Start Python, check distribution demo:

[![Demo](https://img.youtube.com/vi/8SqU1DUBndA/hqdefault.jpg)](https://youtu.be/8SqU1DUBndA)

### Running Python scripts from the command line; imports

In addition to typing Python commands into the interactive interpreter, you can also run `.py` files from the Anaconda Prompt or Terminal, and you can import the code from .py files into the interactive interpreter or into other .py files. To run the `hello_world.py` file, open the Anaconda Prompt or Terminal and enter the following:

```
#on a Mac this should be something like cd /Users/your_username/path/to/api_environment_setup/demo_files
$ cd C:\Users\your_username\path\to\api_environment_setup\demo_files
demo_files $ python hello_world.py

...stuff happens...

demo_files $
```

Running scripts from the command line demo:

[![Demo](https://img.youtube.com/vi/eZvzANBTap8/hqdefault.jpg)](https://youtu.be/eZvzANBTap8)

### Connecting to ArchivesSpace via `requests`

To connect to the ArchivesSpace API, you first need to enter your credentials into the `config.json` file included in the `demo_files` directory. Then open the Anaconda Prompt/Powershell or Terminal (be sure that you are still in the `demo_files` directory before you open the interpreter) and do the following:

```
demo_files $ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda custom (64-bit) on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
>>> import requests
>>> import archivesspace_login as as_login
>>> api_url, headers = as_login.login()
Login successful!
>>> api_url
https://archivesspace.university.edu/api
>>> headers
LONGSTRINGOFNUMBERSANDLETTERSREPRESENTINGAUTHKEY
```

The `import archivesspace_login as as_login` line imports the `archivesspace_login.py` file into the Python interpreter. This file contains a `login()` function which you can run to log in to the API. The API URL and the authentication key are stored in the `api_url` and `headers` variables so that they can be used in other parts of the script.

Connect to ArchivesSpace API demo:

[![Demo](https://img.youtube.com/vi/ehBSp4aLx-s/hqdefault.jpg)](https://youtu.be/ehBSp4aLx-s)

If your login credentials are invalid you should be prompted to enter them again into the interpreter. If your login credentials were accepted, you can send your first API request - to retrieve a top container JSON record - by entering the following into the Python interpreter:

```
>>> import pprint
>>> top_container_uri = '/repositories/12/top_containers/239815'
>>> top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
>>> pprint.pprint(top_container_json)
{'active_restrictions': [],
 'barcode': '39002102377802',
 'collection': [{'display_string': 'Rights and Wrongs records',
                 'identifier': 'MS 1821',
                 'ref': '/repositories/12/resources/4869'}],
 'container_locations': [],
 'container_profile': {'ref': '/container_profiles/113'},
 'create_time': '2016-10-14T19:31:11Z',
 'created_by': 'cconnoll',
 'display_string': 'Box 153D: Series 4 [39002102377802]',
 'ils_holding_id': '6879939',
 'indicator': '153D',
 'is_linked_to_published_record': True,
 'jsonmodel_type': 'top_container',
 'last_modified_by': 'amd243',
 'lock_version': 7,
 'long_display_string': 'MS 1821, Series 4, Box 153D [39002102377802], video '
                        'Beta',
 'repository': {'ref': '/repositories/12'},
 'restricted': True,
 'series': [{'display_string': 'Programs, 1993-1996',
             'identifier': '4',
             'level_display_string': 'Series',
             'publish': True,
             'ref': '/repositories/12/archival_objects/2012461'}],
 'system_mtime': '2019-10-29T12:53:50Z',
 'type': 'Box',
 'uri': '/repositories/12/top_containers/239815',
 'user_mtime': '2018-09-28T13:04:43Z'}

```

You will notice that the JSON response corresponds to the fields and values that you see when you look at this record in the staff interface.

Top containers and all other "top level" ArchivesSpace records can be accessed via the API by unique URIs, which correspond with their database identifiers (a very brief overview of "top level" records and the AS data model can be found in the second section of this [article](https://journal.code4lib.org/articles/14443), or [here](https://github.com/archivesspace/tech-docs/blob/backend_docs/architecture/backend/database.md)). Top containers are scoped to repositories, and so the URI also includes the repository number, for instance `/repositories/12/top_containers/32918`. See the ArchivesSpace API documentation for more detailed explanations of how URIs and other parameters are formulated.

Retrieve single record demo:

[![Demo](https://img.youtube.com/vi/3PF1sYrnfCM/hqdefault.jpg)](https://youtu.be/3PF1sYrnfCM)

### Updating a single top container indicator

JSON objects are treated essentially like Python [dictionaries](https://realpython.com/python-dicts/), which means that Python comes with a variety of built-in ways to manipulate the data that comes from ArchivesSpace.

Updating top container indicators (changing box numbers) is straightforward, as the indicator field is non-repeatable string value that is located at the top level of the record (i.e. it is not nested in a list or other dictionary).

To update an existing top container indicator, open a Python interpreter session (be sure you are in the `demo_files` directory) and execute the following code:

```
>>> top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
>>> top_container_json['indicator'] = '26'
>>> post_record = requests.post(f"{api_url}/{top_container_uri}", headers=headers, json=top_container_json).json()
>>> print(post_record):
{'status': 'updated', 'lock_version': 8, 'id': 239185, uri': '/repositories/12/top_containers/239815'}
>>>
```

Update single record demo:

[![Demo](https://img.youtube.com/vi/WyFmrgu48fU/hqdefault.jpg)](https://youtu.be/WyFmrgu48fU)

### Preparing data for bulk upload

You can update ArchivesSpace data in bulk with Python using a spreadsheet as input. To update a top container indicator you only need the URI of the top container and the new box number. However, you may also want to include the old box number in your spreadsheet so that you can keep track of the previous value while preparing your data and to have a record if something goes wrong.

#### Retrieving top container data via MySQL

The easiest way to retrieve existing data from ArchivesSpace and prepare it for update is via the MySQL database. Retrieving data from the API is often slower, and it takes extra processing to manipulate the JSON response into the spreadsheet formats that many archivists rely on use to create and update archival description. Here is a sample query for retrieving top container indicators for two series within a single collection:

```
select DISTINCT CONCAT('/repositories/', tc.repo_id, '/top_containers/', tc.id) as uri
	, tc.indicator as old_box_number
from archival_object ao
left join archival_object ao2 on ao2.id = ao.parent_id
left join archival_object ao3 on ao3.id = ao2.parent_id
left join instance on instance.archival_object_id = ao.id
left join sub_container sc on sc.instance_id = instance.id
left join top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
left join top_container tc on tclr.top_container_id = tc.id
LEFT JOIN enumeration_value ev2 on ev2.id = tc.type_id
where ao.root_record_id = 11718
and tc.id is not null
ORDER BY CAST(tc.indicator AS UNSIGNED)
```

After running this query you can export the results as a CSV. Open the file and add a column called 'new_box_number'. Then you can fill in the column with the new box number. Save the CSV file.

#### Retrieving top container data via the API

There are also a few ways to retrieve top container data via the API. This are especially useful if you do not have access to the ArchivesSpace database. The most efficient method for retrieving all top containers in a collection is to use the [`repositories/:repo_id/top_containers/search`](http://archivesspace.github.io/archivesspace/api/#search-for-top-containers) endpoint. To retrieve a list of top containers for a given resource, import your modules and enter the following into the Python interpreter:

```
>>> resource_uri = '/repositories/12/resources/11718'
>>> query = f'{{"query":{{"jsonmodel_type": "field_query", "field": "collection_uri_u_sstr", "value": "{resource_uri}", "literal":true}}}}'
>>> tc_search = requests.get(api_url + "/repositories/12/top_containers/search?filter=" + query, headers=headers).json()
>>> tc_data = [[item['id'], item['json']['indicator']] for item in tc_search['response']['docs']
                if `response` in tc_search]
>>> pprint.pprint(tc_data)

```

The full version of this code is saved in the `retrieve_top_container_data.py` file so it can be run from the Anaconda Prompt or Terminal. It will output a spreadsheet with two columns: the top container URI will be in the first column and the current box number will be in the second column. It will also have a third column "new_box_number", where you can enter the new box numbers.

Retrieve containers demo:

[![Retrieve Containers Demo](https://img.youtube.com/vi/kpy3wE37y-4/hqdefault.jpg)](https://youtu.be/kpy3wE37y-4)

Update numbers in spreadsheet demo:

[![Fix Numbers Demo](https://img.youtube.com/vi/oC3A3WxmulU/hqdefault.jpg)](https://youtu.be/oC3A3WxmulU)

**NOTE**: There is a [`/repositories/:repo_id/resources/:id/top_containers`](http://archivesspace.github.io/archivesspace/api/#get-top-containers-linked-to-a-published-resource-and-published-archival-ojbects-contained-within) endpoint which retrieves similar data, but it is very slow when run against a large resource, as it essentially just loops through all of the archival object records and pulls top container data. It also, as of version 2.7.1, is a bit buggy.

### Updating top container indicators in bulk

Opening your CSV file and using it to update multiple top container indicators takes only a few more lines of code than the example above which updates a single indicator. To perform the update, import your modules, connect to the ArchivesSpace API, and execute the following code in a Python interpreter (change the file path formulation to `/Users/username/path/to/file` if using a Mac):

```
>>> with open('C:\\Username\\Path\\To\\File.csv', 'r', encoding='utf-8') as csvfile:
...		csvreader = csv.reader(csvfile)
...		next(csvreader, None)
...		for row in csvreader:
...			top_container_uri = row[0]
...			new_box_number = row[2]
...			try:
...				top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
...				top_container_json['indicator'] = new_box_number
...				post_record = requests.post(f"{api_url}/{top_container_uri}", headers=headers, json=top_container_json).json()
...				print(post_record)
...			except:
...				print(traceback.format_exc())
...				continue
...
<OUTPUT>
>>>
```

The full version of this code is also saved in the `update_top_container_indicator.py` file so it can be run from the Anaconda Prompt. Be aware that this code requires that the top container URI be in the first column of the spreadsheet, the old box number in the second column, and the new box number in the third.

Updating containers in bulk demo:

[![Demo](https://img.youtube.com/vi/yB1Et5EcW20/hqdefault.jpg)](https://youtu.be/yB1Et5EcW20)

### Creating and updating subrecords

#### Updating folder numbers

Updating folder numbers in ArchivesSpace uses a different process than updating box numbers. Sub-container information is stored in instance subrecords in archival object or resource records. This means that the records cannot be accessed directly via their own URIs, but rather via the URI of the archival object or resource record to which they are linked. 

Below is an example of an archival object JSON record with two instances. One of these instances has a `sub_container` subrecord, which is where folder numbers are stored. Note that some fields have been removed for the sake of clarity.

```
{'create_time': '2015-06-01T19:16:49Z',
 'created_by': 'admin',
 'dates': [{'begin': '1991-08-14',
            'create_time': '2015-06-01T19:16:49Z',
            'created_by': 'admin',
            'date_type': 'single',
            'expression': '1991 August 14',
            'jsonmodel_type': 'date',
            'label': 'creation',
            'last_modified_by': 'admin',
            'lock_version': 0,
            'system_mtime': '2018-02-09T20:28:50Z',
            'user_mtime': '2015-06-01T19:16:49Z'}],
 'display_string': 'Beinecke, William S., 1991 August 14',
 'extents': [],
 'instances': [{'create_time': '2015-06-01T19:16:49Z',
                'created_by': 'admin',
                'instance_type': 'mixed_materials',
                'is_representative': False,
                'jsonmodel_type': 'instance',
                'last_modified_by': 'admin',
                'lock_version': 0,
                'sub_container': {'create_time': '2015-06-01T19:16:49Z',
                                  'created_by': 'admin',
                                  'indicator_2': '5',
                                  'jsonmodel_type': 'sub_container',
                                  'last_modified_by': 'admin',
                                  'lock_version': 0,
                                  'system_mtime': '2015-06-01T19:16:49Z',
                                  'top_container': {'ref': '/repositories/12/top_containers/96186'},
                                  'type_2': 'folder',
                                  'user_mtime': '2015-06-01T19:16:49Z'},
                'system_mtime': '2015-06-01T19:16:49Z',
                'user_mtime': '2015-06-01T19:16:49Z'}],
 'jsonmodel_type': 'archival_object',
 'last_modified_by': 'admin',
 'level': 'file',
 'parent': {'ref': '/repositories/12/archival_objects/815180'},
 'publish': True,
 'repository': {'ref': '/repositories/12'},
 'resource': {'ref': '/repositories/12/resources/2623'},
 'system_mtime': '2021-05-04T18:12:01Z',
 'title': 'Beinecke, William S.',
 'uri': '/repositories/12/archival_objects/815185',
 'user_mtime': '2015-06-01T19:16:49Z'}
```

The `get_folder_numbers.sql` and `update_sub_container_indicator.py` files can be used together to retrieve and update archival object instance records.

##### Retrieving folder data via MySQL

Run the `get_folder_numbers.sql` query in an SQL client to retrieve folder numbers for a given collection or series. Add the new folder number in column H.

##### Running the `update_sub_container_indicator.py` file

Run the `update_sub_container_indicator.py` script using the same process

<!-- ## Creating and updating notes -->

<!-- scope and content notes -->

<!--

One challenge in working with ArchivesSpace JSON objects is that they are frequently nested. It is helpful to keep the following in mind:

* subrecords are usually repeatable and are contained in lists
* many records are linked to other records via URI refs, which are stored as nested dictionaries.

## Creating and updating ArchivesSpace data in bulk via the API

The obvious advantage of the ArchivesSpace API is that it enables users to create and update ArchivesSpace records in bulk. The primary input for these bulk updates are CSV spreadsheet files. An example file which might be used to update multiple archival objects  

## Retrieving ArchivesSpace data with MySQL

<-- ## Using the `aspace_tools` package to perform CRUD actions against the API and database-->

### Safety Tips

Creating and updating records via the ArchivesSpace API is fast and convenient, but can be dangerous. There is no undo button, and problems can have cascading effects. In order to prevent errors that may take significant effort to identify and remedy, please follow these guidelines:

* When running any updates against the API, have another staff member review your:
	* Input data
	* Code
	* Test output
* __ALWAYS__ run your updates in TEST or DEV before running in production
* Keep all JSON backups, log files, input data, and code. Organize your files by project/task. Document any and all actions you take. Due to the lack of an "edit history" in ArchivesSpace, it can be difficult to trace the source of data quality issues.

### Helpful Resources

* ArchivesSpace API [Documentation](http://archivesspace.github.io/archivesspace/api/)
* RealPython [Python Data Types](https://realpython.com/python-data-types/)
* RealPython [An Effective Python Environment: Making Yourself at Home](https://realpython.com/effective-python-environment/)
* RealPython [Running Python Scripts](https://realpython.com/run-python-scripts/)
* RealPython [Python Dictionaries](https://realpython.com/python-dicts/)
* RealPython [Introduction to Python](https://realpython.com/learning-paths/python3-introduction/) learning path
* [Setting up a miniconda environment](https://medium.com/dunder-data/anaconda-is-bloated-set-up-a-lean-robust-data-science-environment-with-miniconda-and-conda-forge-b48e1ac11646)
* [Python for Archivists](https://practicaltechnologyforarchives.org/issue7_wiedeman/)

---

## Working with the ArchivesSpace Database

The ArchivesSpace database stores all data that is created within an ArchivesSpace instance. As described in other sections of this documentation, the backend code - particularly the model layer and `ASModel_crud.rb` file - uses the `Sequel` database toolkit to bridge the gap between this underlying data and the JSON objects which are exchanged by the other components of the system.

Often, querying the database directly is the most efficient and powerful way to retrieve data from ArchivesSpace. It is also possible to use raw SQL queries to create custom reports that can be run by users in the staff interface. Please consult the [Custom Reports](../../customization/reports.md) section of this documentation for additional information on creating custom reports.

<!-- .See this [plugin](link-to-plugin) for an example. Also  -->

It is recommended that ArchivesSpace be run against MySQL in production, not the included demo database. Instructions on setting up ArchivesSpace to run against MySQL are [here](../../provisioning/mysql.md).

The examples in this section are written for MySQL. There are many freely-available tutorials on the internet which can provide guidance to those unfamiliar with MySQL query syntax and the features of the language.

**NOTE**: the documentation below is current through database schema version 129, application version 2.7.1.

### Database Overview

The ArchivesSpace database schema and it's mapping to the JSONModel objects used by the other parts of the system is defined by the files in the `common/schemas` and `backend/models` directories. The database itself is created via the `setup-database` script in the `scripts` directory. This script runs the migrations in the `common/db/migrations` directory.

The tables in the ArchivesSpace database can be grouped into several general categories:
  * [Main record tables](#Main-record-tables)
  * [Supporting record tables](#Supporting-record-tables)
  * [Subrecord tables](#Subrecord-tables)
  * [Relationship/linking tables](#Relationship-tables)
  * [Enumeration tables](#Enumerations)
  * [User, setting, and permission tables](#User-setting-and-permission-tables)
  * [Job tables](#Job-tables)
  * [System tables](#System-tables)


  One way to get a view of all tables and columns in your ArchivesSpace instance is to run the following query in a MySQL client:

  ```
  SELECT TABLE_SCHEMA
    , TABLE_NAME
    , COLUMN_NAME
    , ORDINAL_POSITION
    , IS_NULLABLE
    , COLUMN_TYPE
    , COLUMN_KEY
  FROM INFORMATION_SCHEMA.COLUMNS
  #change the following value to whatever your database is named
  WHERE TABLE_SCHEMA Like 'archivesspace'
  ```

Additionally, a BETA version of an [ArchivesSpace data dictionary](https://github.com/archivesspace/data-dictionary-initial) has been created by members of the ArchivesSpace development team and the ArchivesSpace User Advisory Council Reports team.

### Main record tables

These tables hold data about the primary record types in ArchivesSpace. Main record types are distinguished from subrecords in that they have their own persistent URIs - corresponding to their database identifiers/primary keys - that are resolvable via the staff interface, public interface, and API. They are distinguished from supporting records in that they are the primary descriptive record types that users will interact with in the system.

All of these records, except archival objects, can be created independently of any other record. Archival object records represent components of a larger entity, and so they must have a resource record as a root parent. See the [parent/child relationships](#Parent-Child-Relationships-and-Sequencing) section for more information about the representation of  hierarchical relationships in the database.

A few common fields occur in several main record tables. These similar fields are defined by the parent schemas in the `common/schemas` directory:

| Column Name | Tables |
|----------------|--------|
| `title`        | `accession`, `archival_object`, `digital_object`, `digital_object_component`, `resource`
| `identifier`/`component_id`/`digital_object_id`   | `accession`, `resource`/`archival_object`, `digital_object_component`/`digital_object`
| `other_level`  | `archival_object`, `resource`
| `repository_processing_note` | `archival_object`, `resource`

<!-- Booleans -->

All of the main records have a set of fields which store boolean values (`0` or `1`) that indicate whether the records are published in the public user interface, suppressed in the staff interface, or have some kind of applicable restriction. The exception to this is the `repository` table, which does not have a restriction boolean, but does have a `hidden` boolean. The `accession` table has multiple restriction-related booleans. See the section below for more information about boolean fields.

Beginning in version 2.6.0, the main record tables (and some supporting records - see below) also contain fields which hold data about archival resource keys (ARKs) and human-readable URLs (slugs):

| Column Name | Tables |
|----------------|--------|
`slug`           | `accession`, `archival_object`, `digital_object`, `digital_object_component`, `repository`, `resource`
| `external_ark_url` | `archival_object`, `resource`

Also stored in these and all other tables are enumeration values, foreign keys which correspond to database identifiers in the `enumeration_value` table, which stores controlled values. See enumeration section below for more detail.

All subrecord data types - i.e. dates, extents, instances - relating to a main or supporting record are stored in their own tables and linked to main or supporting records via foreign key references in the subrecord tables. See subrecord section below for more detail.

The remaining data in the main record tables is text, and is unique to each table:

| TABLE_NAME               | COLUMN_NAME                   | IS_NULLABLE | COLUMN_TYPE   | COLUMN_KEY |
|--------------------------|-------------------------------|-------------|---------------|------------|
| `accession`               | `content_description`           | YES         | text          |            |
| `accession`                | `condition_description`         | YES         | text          |            |
| `accession`                | `disposition`                   | YES         | text          |            |
| `accession`                | `inventory`                     | YES         | text          |            |
| `accession`                | `provenance`                    | YES         | text          |            |
| `accession`                | `general_note`                  | YES         | text          |            |
| `accession`                | `accession_date`                | YES         | date          |            |
| `accession`                | `retention_rule`                | YES         | text          |            |
| `accession`                | `access_restrictions_note`      | YES         | text          |            |
| `accession`                | `use_restrictions_note`         | YES         | text          |            |
| `archival_object`          | `ref_id`                        | NO          | varchar(255)  | MUL        |
| `digital_object_component` | `label`                         | YES         | varchar(255)  |            |
| `repository`               | `repo_code`                     | NO          | varchar(255)  | UNI        |
| `repository`               | `name`                          | NO          | varchar(255)  |            |
| `repository`               | `org_code`                      | YES         | varchar(255)  |            |
| `repository`               | `parent_institution_name`       | YES         | varchar(255)  |            |
| `repository`               | `url`                           | YES         | varchar(255)  |            |
| `repository`               | `image_url`                     | YES         | varchar(255)  |            |
| `repository`               | `contact_persons`               | YES         | text          |            |
| `repository`               | `description`                   | YES         | text          |            |
| `repository`               | `oai_is_disabled`               | YES         | int           |            |
| `repository`               | `oai_sets_available`            | YES         | text          |            |
| `resource`                 | `ead_id`                        | YES         | varchar(255)  |            |
| `resource`                 | `ead_location`                  | YES         | varchar(255)  |            |
| `resource`                 | `finding_aid_title`             | YES         | text          |            |
| `resource`                 | `finding_aid_filing_title`      | YES         | text          |            |
| `resource`                 | `finding_aid_date`              | YES         | varchar(255)  |            |
| `resource`                 | `finding_aid_author`            | YES         | text          |            |
| `resource`                 | `finding_aid_language_note`     | YES         | varchar(255)  |            |
| `resource`                 | `finding_aid_sponsor`           | YES         | text          |            |
| `resource`                 | `finding_aid_edition_statement` | YES         | text          |            |
| `resource`                 | `finding_aid_series_statement`  | YES         | text          |            |
| `resource`                 | `finding_aid_note`              | YES         | text          |            |
| `resource`                 | `finding_aid_subtitle`          | YES         | text          |            |

<!-- arguably top contsainers should be here, or digital objects should be in the supporting records -->

### Supporting record tables

Like the main record types listed above, supporting records can also be created independently of other records, and are addressable in the staff interface and API via their own URI. However, they are primarily meaningful via their many-to-many linkages to the main record types (and, sometimes, other supporting record types). These records typically provide additional information about, or otherwise enhance, the primary record types. A few supporting record types - for instance those in the `term` table - are used to enhance other supporting record types.

| Supporting module tables          |         Linked to        |
|-----------------------------------|--------------------------|
| `agent_corporate_entity`          |
| `agent_family`                    |
| `agent_person`                    |
| `agent_software`                  |
| `assessment`                      |
| `classification`                  | `accession`, `resource`
| `classification_term`             | `classification`, `accession`, `resource`
| `container_profile`               | `top_container`
| `event`                           |
| `location`                        |
| `location_profile`                | `location`
| `subject`                         | `resource`, `archival_object`
| `term`                            | `subject`
| `top_container`                   |
| `vocabulary`                      | `subject`, `term`
| `assessment_attribute_definition` | `assessment_attribute`, `assessment_attribute_note`

<!-- is this the appropriate place for the assessment attribute def? Vocabulary? -->

### Subrecord tables

<!-- link to ### Nested records section of the backend readme -->

Subrecords must be associated with a main or supporting record - they cannot be created independently. As such, they do not have their own URIs, and can only be accessed via the API by retrieving the top-level record with which they are associated. In the staff interface these records are embedded within main or supporting record views. In the API subrecord data is contained in arrays within main or supporting records.

The various subrecord types do have their own database tables. In addition to data specific to the subrecord type, the tables also contain foreign key columns which hold the database identifiers of main or supporting records. Subrecord tables must have a value in one of the foreign key fields. Some subrecords can have another subrecord as parent (for instance, the `sub_container` subrecord has `instance_id` as its foreign key column).

Subrecords exist in a one-to-many relationship with their parent records, so a record's `id` may appear multiple times in a subrecord table (i.e. when there are two dates associated with a resource record).

It is important to note that subrecords are deleted and recreated upon each save of the main or supporting record with which they are associated, regardless of whether the subrecord itself is modified. This means that the database identifier is deleted and reassigned upon each save.

| Subrecord tables              | Foreign keys |
|-------------------------------|--------------
| `agent_contact`               | `agent_person_id`, `agent_family_id`, `agent_corporate_entity_id`, `agent_software_id`
| `date`                        | `accession_id`, `deaccession_id`, `archival_object_id`, `resource_id`, `event_id`,             `digital_object_id`, `digital_object_component_id`, `related_agents_rlshp_id`, `agent_person_id`, `agent_family_id`, `agent_corporate_entity_id`, `agent_software_id`, `name_person_id`, `name_family_id`, `name_corporate_entity_id`, `name_software_id`
| `extent`                      | `accession_id`, `deaccession_id`, `archival_object_id`, `resource_id`, `digital_object_id`, `digital_object_component_id`
| `external_document`           | `accession_id`, `archival_object_id`, `resource_id`, `subject_id`, `agent_person_id`, `agent_family_id`, `agent_corporate_entity_id`, `agent_software_id`, `rights_statement_id`, `digital_object_id`, `digital_object_component_id`, `event_id`
| `external_id`                 | `subject_id`, `accession_id`, `archival_object_id`, `collection_management_id`, `digital_object_id`, `digital_object_component_id`, `event_id`, `location_id`, `resource_id`
| `file_version`                | `digital_object_id`, `digital_object_component_id`
| `instance`                    | `resource_id`, `archival_object_id`, `accession_id`
| `name_authority_id`           | `name_person_id`, `name_family_id`, `name_software_id`, `name_corporate_entity_id`
| `name_corporate_entity`       | `agent_corporate_entity_id`
| `name_family`                 | `agent_family_id`
| `name_person`                 | `agent_person_id`
| `name_software`               | `agent_software_id`
| `note`                        | `resource_id`, `archival_object_id`, `digital_object_id`, `digital_object_component_id`, `agent_person_id`, `agent_corporate_entity_id`, `agent_family_id`, `agent_software_id`, `rights_statement_act_id`, `rights_statement_id`
| `note_persistent_id`          | `note_id`, `parent_id`
| `revision_statement`          | `resource_id`
| `rights_restriction`          | `resource_id`, `archival_object_id`
| `rights_restriction_type`     | `rights_restriction_id`
| `rights_statement`            | `accession_id`, `archival_object_id`, `resource_id`, `digital_object_id`, `digital_object_component_id`, `repo_id`
| `rights_statement_act`        | `rights_statement_id`
| `sub_container`               | `instance_id`
| `telephone`                   | `agent_contact_id`
| `user_defined`                | `accession_id`, `resource_id`, `digital_object_id`
| `ark_name`                    | `archival_object_id`, `resource_id`
| `assessment_attribute_note`   | `assessment_id`
| `assessment_attribute`        | `assessment_id`
| `lang_material`               | `archival_object_id`, `resource_id`, `digital_object_id`, `digital_object_component_id`
| `language_and_script`         | `lang_material_id`
| `collection_management`       | `accession_id`, `resource_id`, `digital_object_id`
| `location_function`           | `location_id`

<!-- appropriate place for collection management and deaccession stuff? what about location function? all the rights statement stuff? Is there a specific thing that defines a subrecord as a subrecord? -->

### Relationship tables

These tables exist to enable linking between main records and supporting records. Relationship tables are necessary because, unlike subrecord tables, supporting record tables do not include foreign keys which link them to the main record tables.

Most relationship tables have the `_rlshp` suffix in their names. They typically contain just the primary keys for the tables that are being linked, though a few tables also include fields that are specific to the relationship between the two record types.

| Relationship/linking tables         | Tables linked |
|-------------------------------------|-------------
| `assessment_reviewer_rlshp`         | `assessment` to `agent_person`
| `assessment_rlshp`                  | `assessment` to `accession`, `archival_object`, `resource`, or `digital_object`
| `classification_creator_rlshp`      | `classification` to `agent_person`, `agent_family`, `agent_corporate_entity`, or `agent_software`
| `classification_rlshp`              | `classification` or `classification_term` to `resource` or `accession`
| `classification_term_creator_rlshp` | `classification_term` to `agent_person`, `agent_family`, `agent_corporate_entity`, or `agent_software`
| `event_link_rlshp`                  | `event` to `accession`, `resource`, `archival_object`, `digital_object`, `digital_object_component`, `agent_person`, `agent_family`, `agent_corporate_entity`, `agent_software`, or `top_container`. Also includes the `role_id` table, which can be joined with the `enumeration_value` table to return the event role (source, outcome, transfer, context)
| `instance_do_link_rlshp`            | `digital_object` to `instance`
| `linked_agents_rlshp`               | `agent_person`, `agent_software`, `agent_family`, or `agent_corporate_entity` to `accession`, `archival_object`, `digital_object`, `digital_object_component`, `event`, or `resource`. Also includes the `role_id` and `relator_id` tables, which can be joined with the `enumeration_value` table
| `location_profile_rlshp`            | `location` to `location_profile`
| `owner_repo_rlshp`                  | `location` to `repository`
| `related_accession_rlshp`           | Links a row in the `accession` table to another row in the `accession` table. Also includes fields for `relator` and relationship type.
| `related_agents_rlshp`              | `agent_person`, `agent_corporate_entity`, `agent_software`, or `agent_family` to other agent tables, or two rows in the same agent table. Also includes fields for `relator` and `description`, and the type of relationship.
| `spawned_rlshp`                     | `accession` to `resource`. This contains all linked accession data, even if the resource was not spawned from the accession record.
| `subject_rlshp`                     | `subject` to `accession`, `archival_object`, `resource`, `digital_object`, or `digital_object_component`
| `surveyed_by_rlshp`                 | `assessment` to `agent_person`
| `top_container_housed_at_rlshp`     | `top_container` to `location`. Also includes fields for `start_date`, `end_date`, `status`, and a free-text `note`.
| `top_container_link_rlshp`          | `top_container` to `sub_container`
| `top_container_profile_rlshp`       | `top_container` to `container_profile`
| `subject_term`                      | `subject` to `term`
| `linked_agent_term`                 | `linked_agents_rlshp` to `term`

<!-- is the assessment definition thing a linking table - it pretty much only has foreign keys

Same question about one of the rights restriction tables - can't remember which one right now.
 -->

 It is not always obvious which relationship tables will provide the desired results. For instance, to get a box list for a given resource record, enter the following query into a MySQL editor:

 ```
 SELECT DISTINCT    CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) as resource_uri
    , resource.identifier
    , resource.title
    , tc.barcode as barcode
    , tc.indicator as box_number
 FROM sub_container sc
 JOIN top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
 JOIN top_container tc on tclr.top_container_id = tc.id
 JOIN instance on sc.instance_id = instance.id
 JOIN archival_object ao on instance.archival_object_id = ao.id
 JOIN resource on ao.root_record_id = resource.id
 #change to your desired resource id
 WHERE resource.id = 4556
 ```

 Sometimes numerous relationship tables must be joined to retrieve the desired results. For instance, to get all boxes and folders for a given resource record, including any container profiles and locations, enter the following query into a MySQL editor:

 ```
 SELECT CONCAT('/repositories/', tc.repo_id, '/top_containers/', tc.id) as tc_uri
    , CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) as resource_uri
    , CONCAT('/repositories/', resource.repo_id) as repo_uri
    , CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as ao_uri
    , resource.identifier AS resource_identifier
    , resource.title AS resource_title
   , ao.display_string AS ao_title
   , ev2.value AS level
   , tc.barcode AS barcode
    , cp.name AS container_profile
    , tc.indicator AS container_num
   , ev.value AS sc_type
   , sc.indicator_2 AS sc_num
 from sub_container sc
 JOIN top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
 JOIN top_container tc on tclr.top_container_id = tc.id
 LEFT JOIN top_container_profile_rlshp tcpr on tcpr.top_container_id = tc.id
 LEFT JOIN container_profile cp on cp.id = tcpr.container_profile_id
 LEFT JOIN top_container_housed_at_rlshp tchar on tchar.top_container_id = tc.id
 JOIN instance on sc.instance_id = instance.id
 JOIN archival_object ao on instance.archival_object_id = ao.id
 JOIN resource on ao.root_record_id = resource.id
 LEFT JOIN enumeration_value ev on ev.id = sc.type_2_id
 LEFT JOIN enumeration_value ev2 on ev2.id = ao.level_id
 #change to your desired resource id
 WHERE resource.id = 4223

 ```
 <!-- Mention the CONCAT function for creating URIs -->

### Enumerations

All controlled values used by the application - excluding tool-tips and frontend/public display values and the values that are stored a few of the supporting record tables (see below) - are stored in a table called `enumeration_values`. Controlled values are organized into a variety of parent enumerations (akin to a set of distinct controlled value lists) which are utilized by different record and subrecord types. Parent enumeration data is stored in the `enumeration` table and is linked by foreign key in the `enumeration_id` field in the `enumeration_value` table. In the record and subrecord tables, enumeration values appear as foreign keys in a variety of foreign key columns, usually identified by an `_id` suffix.

ArchivesSpace comes with a standard set of controlled values, but most of these are modifiable by end-users via the staff interface and API. However, some values in the `enumeration_value` table are read-only - these values define the terminology and data types used in different parts of the application (i.e. the various note types).

Enumeration IDs appear as foreign keys in a variety of database tables:

| table_name                 | column_name                        | enumeration_name                           |
|----------------------------|------------------------------------|--------------------------------------------|
| `accession`                | `acquisition_type_id`              | accession_acquisition_type
| `accession`                | `resource_type_id`                 | accession_resource_type
| `agent_contact`            | `salutation_id`                    | agent_contact_salutation
| `archival_object`          | `level_id`                         | archival_record_level
| `collection_management`    | `processing_priority_id`           | collection_management_processing_priority
| `collection_management`    | `processing_status_id`             | collection_management_processing_status
| `collection_management`    | `processing_total_extent_type_id`  | extent_extent_type_id
| `container_profile`        | `dimension_units_id`               | dimension_units
| `date`                     | `calendar_id`                      | date_calendar
| `date`                     | `certainty_id`                     | date_certainty
| `date`                     | `date_type_id`                     | date_type
| `date`                     | `era_id`                           | date_era
| `date`                     | `label_id`                         | date_label
| `deaccession`              | `scope_id`                         | deaccession_scope
| `digital_object`           | `digital_oject_type_id`            | digital_object_digital_object_type
| `digital_object`           | `level_id`                         | digital_object_level
| `event`                    | `event_type_id`                    | event_event_type
| `event`                    | `outcome_id`                       | event_outcome
| `extent`                   | `extent_type_id`                   | extent_extent_type                       
| `extent`                   | `portion_id`                       | extent_portion                           
| `external_document`        | `identifier_type_id`               | rights_statement_external_document_identifier_type                              
| `file_version`             | `checksum_method_id`               | file_version_checksum_methods                             
| `file_version`             | `file_format_name_id`              | file_version_file_format_name                           
| `file_version`             | `use_statement_id`                 | file_version_use_statement                             
| `file_version`             | `xlink_actuate_attribute_id`       | file_version_xlink_actuate_attribute                            
| `file_version`             | `xlink_show_attribute_id`          | file_version_xlink_show_attribute                           
| `instance`                 | `instance_type_id`                 | instance_instance_type  
| `language_and_script`      | `language_id`                      |               
| `language_and_script`      | `script_id`                        |                 
| `location`                 | `temporary_id`                     | location_temporary              
| `location_function`        | `location_function_type_id`        | location_function_type              
| `location_profile`         | `dimension_units_id`               | dimension_units            
| `name_corporate_entity`    | `rules_id`                         | name_rule                 
| `name_corporate_entity`    | `source_id`                        | name_source                
| `name_family`              | `rules_id`                         | name_rule              
| `name_family`              | `source_id`                        | name_source               
| `name_person`              | `name_order_id`                    | name_person_name_order            
| `name_person`              | `rules_id`                         | name_rule              
| `name_person`              | `source_id`                        | name_source               
| `name_software`            | `rules_id`                         | name_rule                
| `name_software`            | `source_id`                        | name_source             
| `repository`               | `country_id`                       | country_iso_3166            
| `resource`                 | `finding_aid_description_rules_id` | resource_finding_aid_description_rules        
| `resource`                 | `finding_aid_language_id`          |               
| `resource`                 | `finding_aid_script_id`            |                  
| `resource`                 | `finding_aid_status_id`            | resource_finding_aid_status             
| `resource`                 | `level_id`                         | archival_record_level               
| `resource`                 | `resource_type_id`                 | resource_resource_type               
| `rights_restriction_type`  | `restriction_type_id`              | restriction_type               
| `rights_statement`         | `jurisdiction_id`                  |                
| `rights_statement`         | `other_rights_basis_id`            | rights_statement_other_rights_basis                
| `rights_statement`         | `rights_type_id`                   | rights_statement_rights_type                
| `rights_statement`         | `status_id`                        |                 
| `rights_statement_act`     | `act_type_id`                      | rights_statement_act_type               
| `rights_statement_act`     | `restriction_id`                   | rights_statement_act_restriction              
| `rights_statement_pre_088` | `ip_status_id`                     | rights_statement_ip_status                
| `rights_statement_pre_088` | `jurisdiction_id`                  |                 
| `rights_statement_pre_088` | `rights_type_id`                   | rights_statement_rights_type               
| `sub_container`            | `type_2_id`                        | container_type                 
| `sub_container`            | `type_3_id`                        | container_type           
| `subject`                  | `source_id`                        | subject_source                 
| `telephone`                | `number_type_id`                   | telephone_number_type               
| `term`                     | `term_type_id`                     | subject_term_type              
| `top_container`            | `type_id`                          | container_type          

<!-- need to add some rlshp tables which have enums -->

To translate the enumeration ID that appears in the record and subrecord tables, join the `enumeration_value` table. The table can be joined multiple times if there are multiple values to translate, but you must use an alias for each table. For example:

```
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as ao_uri
  , ao.display_string as ao_title
  , date.begin
  , date.end
  , ev.value as date_label
  , ev2.value as date_type
  , ev3.value as date_calendar
FROM archival_object ao
LEFT JOIN date on date.archival_object_id = ao.id
LEFT JOIN enumeration_value ev on ev.id = date.label_id
LEFT JOIN enumeration_value ev2 on ev2.id = date.date_type_id
LEFT JOIN enumeration_value ev3 on ev3.id = date.calendar_id
```

**NOTE**: `container_profile`, `location_profile`, and `assessment_attribute_definition` records are similar to the records in the `enumeration_value` table in that they store controlled values which are referenced by other parts of the system. However, they differ in that they have their own tables and are addressable via their own URIs.

### User, setting, and permission tables

These tables store user and permissions information, user/repository/global preferences, and RDE and custom report templates.

| Table name                        | Description                                                    |
|-----------------------------------|----------------------------------------------------------------|
| `custom_report_template`          | Custom report templates
| `default_values`                  | Default values settings
| `group`                           | Data about permission groups created by each repository
| `group_permission`                | Links the permission table to the group table
| `group_user`                      | Links the group table to the user table
| `oai_config`                      | Configuration data for OAI-PMH harvesting
| `permission`                      | All permission types that can be assigned to users
| `preference`                      | User preference data
| `rde_template`                    | RDE templates
| `required_fields`                 | Contains repository-defined required fields
| `user`                            | User data

### Job tables

These tables store data related to background jobs, including imports.

| Table name                        | Description                                                    |
|-----------------------------------|----------------------------------------------------------------|
| `job`                             | All jobs which have been run in an ArchivesSpace instance.
| `job_created_record`              | Records created via background jobs
| `job_input_file`                  | Data about input files used in background jobs
| `job_modified_record`             | Data about records modified via background jobs

### System tables

These tables track actions taken against the database (i.e. edits and deletes), system events, session and authorization data, and database information. These tables are typically not referenced by any other table.

| Table name                        | Description                                                    |
|-----------------------------------|----------------------------------------------------------------|
| `active_edit`                     | Records being actively edited by a user. Read-only system table
| `auth_db`                         | Authentication data for users. Read-only system table
| `deleted_records`                 | Records deleted in the past 24 hours. Read-only system table
| `notification`                    | Notifications stream. Read-only system table
| `schema_info`                     | Contains the database schema version. Read-only system table.
| `sequence`                        | The value corresponds to the number of children the archival object has - 1. Read-only system table
| `session`                         | Recent session data. Read-only system table
| `system_event`                    | System event data. Read-only system table

<!--  these are subrecords -->
<!-- | subnote_metadata |
| rights_statement_pre_088  | -->

### Parent-Child Relationships and Sequencing

#### Repository-scoped records

Many main and supporting records are scoped to a particular repository. In these tables the parent repository is identified by a foreign key which corresponds to the database identifier in the `repository` table:

| Column name    | Description                              | Example | Found in
|---------------|------------------------------------------|---------|-------
`repo_id`       | The database ID of the parent repository | `12` | `accession`, `archival_object`, `assessment`, `assessment_attribute_definition`, `classification`, `classification_term`, `custom_report_template`, `default_values`, `digital_object`, `digital_object_component`, `event`, `group`, `job`, `preference`, `required_fields`, `resource`, `rights_statement`, `top_container`

#### Parent/child relationships

Hierarchical relationships between other records are also expressed through foreign keys:

| Column name    | Description                              | Example |PK Tables| Found in
|---------------|-------------------------------------------|---------|---------|-------
`root_record_id`| The database ID of the root parent record | `4566` |`resource`, `digital_object`, `classification`| `archival_object`, `digital_object_component`, `classification_term`
`parent_id`     | The database ID of the immediate parent record. This is used to identify parent records which are of the same type as the child record (i.e. two archival object records). The value will be NULL if the only parent is the root record. | `1748121` |`archival_object`, `classification_term`, `digital_object_component`| `archival_object`, `classification_term`, `digital_object_component`, `note_persistent_id`
`parent_name`   | The database ID or URI, and the record type of the immediate parent | `144@archival_object`, `root@/repositories/2/resources/2` | `resource`, `archival_object`, `classification`, `classification_term`, `digital_object`, `digital_object_component`| `archival_object`, `classification_term`, `digital_object_component`

Beginning with MySQL 8, you can recursively retrieve all parents of an archival object (or all archival objects linked to a resource) by running the following query:

```
WITH RECURSIVE ao_path AS
  (SELECT ao1.id
    , ao1.display_string
    , ao1.component_id
    , ao1.parent_id
    , ev.value as `ao_level`
    , 1 as level
   FROM archival_object ao1
   LEFT JOIN enumeration_value ev on ev.id = ao1.level_id
   WHERE ao1.id = <your ao id>
   <!-- to get all trees for a resource change to: WHERE ao1.root_record_id = <your root_record_id> -->
   UNION ALL
   SELECT ao2.id
    , ao2.display_string
    , ao2.component_id
    , ao2.parent_id
    , ev.value as `ao_level`
    , ao_path.level + 1 as level
   FROM ao_path
   JOIN archival_object ao2 on ao_path.parent_id = ao2.id
   LEFT JOIN enumeration_value ev on ev.id = ao2.level_id)
   SELECT GROUP_CONCAT(CONCAT(display_string, ' ', ' (', CONCAT(UPPER(SUBSTRING(ao_level,1,1)),LOWER(SUBSTRING(ao_level,2))), ' ', IF(component_id is not NULL, CAST(component_id as CHAR), "N/A"), ')') ORDER BY level DESC SEPARATOR ' > ') as tree
   FROM ao_path;

```

To retrieve all children (MySQL 8+):

To retrieve both parents and children (MySQL 8+):

To retrieve all parents of a record in MySQL 5.7 and below, run the following query:

```
SELECT (SELECT GROUP_CONCAT(CONCAT(display_string, ' (', ao_level, ')') SEPARATOR ' < ') as parent_path
        FROM (SELECT T2.display_string as display_string
                    , ev.value as ao_level
              FROM (SELECT @r AS _id
                        , @p := @r AS previous
                        , (SELECT @r := parent_id FROM archival_object WHERE id = _id) AS parent_id
                        , @l := @l + 1 AS lvl
                    FROM ((SELECT @r := 1749840, @p := 0, @l := 0) AS vars,
                            archival_object h)
                           WHERE @r <> 0 AND @r <> @p) AS T1
              JOIN archival_object T2 ON T1._id = T2.id
              LEFT JOIN enumeration_value ev on ev.id = T2.level_id
              WHERE T2.id != 1749840
              ORDER BY T1.lvl DESC) as all_parents) as p_path
     , ao.display_string
     , CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri
FROM archival_object ao
WHERE ao.id = 1749840
```

To retrieve all children of a record (MysQL 5.7 and below):

```
```

#### Sequencing

The ordering of records in a `resource`, `classification`, or `digital_object` tree is determined by the `position` field. The position field is also used to order values in the `enumeration_value` and `assessment_attribute_definition` tables:

| Column name    | Description                              | Example |Found in
|---------------|------------------------------------------|---------|-------
`position` | The position of the archival object under the immediate parent | `168000` | `enumeration_value`, `assessment_attribute_definition`, `classification_term`, `digital_object_component`, `archival_object`


### Boolean fields

Many records and subrecords include fields which contain integers (`0` or `1`) corresponding to boolean values.

|  Boolean fields      | Description    | Found in |
|----------------------|----------------|----------|
| `publish`            |                | `subnote_metadata`, `file_version`, `external_document`, `accession`, `classification`, `agent_person`, `agent_family`, `agent_software`, `agent_corporate_entity`, `classification_term`, `revision_statement`, `repository`, `note`, `digital_object`, `digital_object_component`, `archival_object`, `resource`
| `suppressed`         |                | `accession`, `archival_object`, `assessment_reviewer_rlshp`, `assessment_rlshp`, `classification`, `classification_creator_rlshp`, `classification_rlshp`, `classification_term`, `classification_term_creator_rlshp`, `digital_object`, `digital_object_component`, `enumeration_value`, `event`, `event_link_rlshp`, `instance_do_link_rlshp`, `linked_agents_rlshp`, `location_profile_rlshp`, `owner_repo_rlshp`, `related_accession_rlshp`, `related_agents_rlshp`, `resource`, `spawned_rlshp`, `surveyed_by_rlshp`, `top_container_housed_at_rlshp`, `top_container_link_rlshp`, `top_container_profile_rlshp`
| `restrictions_apply` |                | `accession`, `archival_object`

<!-- NEED TO ADD the restriction field here - the resource and dig ob recs have it -->
<!-- also add the hidden field in repo and the multiple restrictions in accession -->
<!-- I think this is good to mention because these are editable via the API but also have their own endpoints. So they are a little different. Should also mention that they are bools in the API docs. -->

### Read-Only Fields

Several system generated, read-only fields appear across many tables. These include database identifiers, timestamps that track record creation and modification, and fields that record the username of the user that created and last modified the each record.

|   Most common read-only fields | Description |
|--------------------------------|------------------------------------|
| `id` (primary key)             | Database identifier for each record
| `system_mtime`                 | The last time the record was modified by the system
| `created_by`                   | The user that created a record
| `last_modified_by`             | The user that last modified a record
| `user_mtime`                   | The time that a record was last modified by a user
| `create_time`                  | The time that a record was created
| `lock_version`                 | This field is incrementally updated each time a record is updated. This provides a method of tracking updates and managing near-simultaneous edits by different users.
| `json_schema_version`          | The JSON schema version
| `aspace_relationship_position` | The position of a linked record in a list of other linked records
| `is_slug_auto`                 | A boolean value that indicates whether a slug was auto-generated
| `system_generated`             | A boolean value that indicates whether a field was system-generated
| `display_string`               | A system-generated field which concatenates the title and date fields of an archival object record

**NOTE**: for subrecord tables these fields may hold unexpected data - because subrecords are deleted and recreated upon each save of a main or supporting record, their create and modification times will also be recreated and will not reflect the original creation date of the subrecord itself. For resource records, the timestamp only records the time that the resource itself was modified, not the last time any of its components were modified.

<!-- ## Querying the ArchivesSpace Database -->


