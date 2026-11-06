# Guides for Specific Record Types 


| Header 1 | Header 2 | Header 3 |
| :---     | :---:    | ---:     |
| Left     | Center   | Right    |
| Text     | Text     | Text     |


This guide was designed as a starting point for anyone requesting the creation or enhancement of specific record types in bulk. We will work with you no matter how much starting information you have available. However, if you are unsure what to include in your request, please consider the following: 

General Guidelines
===================

- Please avoid placing any important information in locations such as comments on an excel sheet. Information from non-machine readable locations are difficult to extract and add up to weeks of extra work. Whenever possible, keep information within columns in the spreadsheet. 
- Avoid assuming we know which repository you are working in. A link to your record does not work if we are not in the correct repository. This can involve extra time trying to make educated guesses and switching to different repositories to test whether the link will work. Giving us the link and informing us it is in MSSA is very helpful. 
- URIs (/repositories/11/resources/203) are the most helpful way to provide a quick link to the record you are referring to. This can be found in the Archives at Yale URL, or on the ArchivesSpace Record information. This includes the Repository id for us so we do not need to guess which repository you are working in. 

Top Containers 
===============

When requesting the creation of Top containers and Instances, consider the following fields: 
- Archival Object ID (required) – The ID number of the archival object the top container shall be attached to. If your container will be attached to multiple AOs, there should be a line for each object along with the appropriate sub-container information in the child and grandchild fields. The barcode, location, indicator, and type of the top container should be identical for each AO attached to that top container. 
- Barcodes – Should be a unique identifier. 
- Indicator (required)– What is the number or unique identifier of the box, folder, slide, etc. 
- Child/Grandchild Indicator – Does the Instance have sub-identifiers? (e.g. Box 1 Folder 13 Slide 22) When supplying this information, ensure you indicate which archival object they should be attached to. 
- Locations – From the Locations list, select where your top container exists. 
- Repository (required) – The repository the top container will belong to (e.g. BRBL, YCBA, Music, etc.) 
- Type (required)– Select the Top container type from a list of Controlled Values. If the value you need is not included, you can submit an official request to add a new value to the list. 
- Child/Grandchild Type – If you have any child or grandchildren please include types for them as well. 

When submitting your request, consider the following table as a guide. Indicate the Archival Object ID in which Repository you wish to attach an instance to. If you wish to use the same Top Container but different Child and Grandchild information, make sure the barcodes, locations, type and indicator information match on both lines. If a field is not required, then it can be left blank in cases where there is no relevant information – such as a Top Container not needing a location or a grandchild. 

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1
   * - AO ID
     - Repo
     - Barcode
     - Location
     - Indicator
     - Type
     - Child Indicator
     - Child Type
     - Grandchild Indicator
     - Grandchild Type
   * - 3878066
     - BRBL
     - 312987
     - 
     - 12
     - Box
     - 3
     - Folder
   * - 3878067
     - BRBL
     - 312987
     - 
     - 12
     - Box
     - 6
     - Folder
     - 21
     - Slide
   * - 3878066
     - BRBL
     - 312458
     - SML, B57-A [82181, Drawer: 23]
     - 3
     - Box

Digital Objects 
================

When requesting the creation of digital objects, consider the following fields: 
- Archival Object ID (required) – The ID number of the archival object the digital object shall be attached to. If your DO will be attached to multiple AOs, they should be included in a single cell separated by a delimiter such as ‘;’ 
- Identifier – The unique identifier of the digital object, this can be the external ID of the digital object, such as the preservica id. 
- Repository (required) – The repository the digital object will belong to (e.g. BRBL, YCBA, Music, etc.) 
- Title (required) – The title will be what the digital object displays as. Sometimes this may be the same as the URL but can also be a name or description of the object. 
- URL (required) – This is the link that is used to connect to the digital resource. Should be in the typical url format of `http://`. If your DO has multiple URLs attached to it, they should be included in a single cell separated by a delimiter such as ‘;’ 

Other fields may be included as needed (such as dates and notes), just add additional columns to your spreadsheet to reflect these additional fields. If a field is not listed as required, you can leave a cell empty to indicate that the field should be left blank on the Digital Object. 
+-------+------+------+-----------+--------------+
| AO ID | Repository | Title | Idenitfier | URL |
|=======|=======|=======|=======|=======|
| 349811 | Music | 2 songs op. 34 | oid: 110879 | https://collections.library.yale.edu/manifest/32456; https://collections.library.yale.edu/catalog/9874 |
+-------+------+------+-----------+--------------+
| 367821; 367822; 367823 | MSSA | Name and address cards – by state | 4d5a45876-3087c-4567-87ed-e867 | https://preservica.library.yale.edu/explorer/explorer.html#7545678edg |
+-------+------+------+-----------+--------------+

Locations 
==========

When requesting the creation of Location records, consider the following fields: 
- Building (required) – The name of the building. 
- Area, Floor, Room – These fields can be used to expand the specific physical location details beyond just a building name. 
- Barcode (required if classification or coordinates are not used) – A unique barcode that represents the location as an identifier. 
- Classification Number (required if barcode or coordinates are not used) – A unique call number that represents the location as an identifier. 
- Coordinate Indicator 1 (required if barcode or classification are not used) – A unique number or phrase that represents the location as an identifier. 
- Coordinate Label 1 (required if Coordinate Indicator is used) – A label that represents the Coordinate Indicator, such as Room or Drawer or Shelf. 
- Top Container ID (required) – Provide the ID or IDs of the Top Containers these locations should be attached to. If you wish to attach a location to multiple Containers, they should be included in a single cell separated by a delimiter such as ‘;’ 

Locations will display as Building, Floor, Room, Area [Unique indicator]. So a location of SML on floor 2 in Room 150-A and a coordinate label and indicator of Drawer 15 would display as: ‘SML, 2, 150-A [Drawer: 15]’. 
+-------+------+------+-----------+--------------+---------+-------+
| Building | Floor | Room | Barcode | Coordinate Label | Coordinate Indicator | Top Container ID |
|=======|======|======|===========|==============|=========|=======| 
| 344 Winchester - Beinecke Tech Services | | C243 | 3418990 | | | | 71832; 718986 | 
+-------+------+------+-----------+--------------+---------+-------+
| SML | 2 | 150-A | | Drawer | 15 | 79823 |
+-------+------+------+-----------+--------------+---------+-------+

Agents 
=======

When requesting the creation of Agent records, consider the following fields: 
- Agent Type (required) – This field is used to indicate the type of agent. Either Person, Family, Corporate, or Software. 
- Archival Object (required) – The ID number of the archival object the agent shall be attached to. If your agent will be attached to multiple AOs, they should be included in a single cell separated by a delimiter such as ‘;’ 
- Family Name (required for Family Agents) – The main name of Family Agents. 
- Name Order – By default this is set to Indirect Name Order. Used for Person Agents, it determines whether a name will display as Indirect Order: surname first (Doe, John), or Direct Order: surname second (John Doe). 
- Primary Part of Name (Required for Person or Corporate Agents) – This is either the Person Agent’s Surname, or the Corporate Agent’s Business Name. 
- Repository (required) – The repository of the archival object the agent will be attached to (e.g. BRBL, YCBA, Music, etc.) 
- Rest of Name – For Person Agents, only the surname should be included in the Primary Part of Name. There are also individual fields for titles, suffixes, and dates. Rest of Name should be typically used for any other naming details such as first and middle names. 
- Software Name (required for Software Agents) – The main part of the name in Software Agents. This should be the title of software. Information for versions and manufacturers should be separated from this into their individual fields. 

With Agents the Main Name (Primary Part of Name, Family Name, Software Name) will display first, other title related fields (Rest of Name, Version and Manufacturer fields, dates, etc.) will display afterwards. So a Primary Name: Smith, Rest of Name: John James, with Dates: 1956-, will display by default as ‘Smith, John James, 1956-’. To alter this, you can indicate a Direct Name Order (‘John James Smith, 1956-’) instead of the default Indirect Name Order (‘Smith, John James, 1956-’). 

+-------+------+------+-----------+--------------+---------+-------+
| AO ID | Repo | Type | Main Name | Rest of Name | Version | Dates |
|=======|======|======|===========|==============|=========|=======| 
| 45678; 45679 | BRBL | Person | Smith | John James | | 1956- |
+--------------+------+--------+-------+------------+-+-------+
| 45239 | Arts | Software | Painterly | | 2.3.7 | |
+--------------+------+--------+-------+------------+-+-------+
| 451290 | Medical | Corporate | B. F. Paulson & Co. | | | |
+--------------+------+--------+-------+------------+-+-------+

Controlled Values 
==================

Values such as dimensions and container labels found in drop down menus that need updating should consider the following: 
- Action – Indicate the action that needs to be taken, such as Remove, Add, or Change. 
- Value Type – What type of value you wish to see updated, such as dimension units and container values.  
- Value Change – List the value that needs to be added, changed, or removed. 
- Value Merge – If you are requesting a value to be removed, sometimes records are actively using the value. Please indicate what value these records should be changed to. 
+--------------+------+--------+-------+
| Value Type | Action | Value Change | Value Merge |
|=======|======|======|===========|
| Dimension Units | Remove | ft. | feet |
+--------------+------+--------+-------+
| Container labels | Add | Drawer | |
+--------------+------+--------+-------+
