 Specification for the construction of “series” titles in ArchivesSpace


[TOC]





## Overview



* The goal is to combine the following 4 different components into a single, composite display string for series-level archival objects:
    * level of description;
    * series component unique identifier;
    * series title;
    * series creation date sub records (inclusive/single)  
* Additionally, any dates added to the composite string should be filtered out of the unordered list of dates that display below the title on the context of the ~~archival-object landing pages and on the~~ single-scroll view.
* Ideally, this would happen in both the staff and public interface.  In the public interface, this composite string should be used wherever an archival object currently displays (e.g. title, context-tree view, single-scroll view, search-result page, etc.) 
* Even more ideally, the part of this process that covers titles and dates (REQ 7 - 13) could be copied for how ArchivesSpace currently creates the “display string” data attribute for all archival objects. Right now, those display strings only include the first date.

For Yale, a series is defined as:

An archival object that must have a resource record as a parent (not as a grandparent or any other type of ancestor), as long as that archival object meets one of the two following criteria:



1. level = “series”
2. level = “otherlevel”  


## Requirements

_For the first two components of the composite string (i.e. the level and the component unique identifier):_


### REQ 1:

When criteria 1 is met (i.e. level=”series”), “Series“ will precede the identifier.


### REQ 2:

Furthermore, if the archival object “component unique identifier” consists of Arabic numbers only, then those numbers should be converted to Roman numerals (which can be done with the “Romanize” module currently in place,[ https://github.com/YaleArchivesSpace/aspace_yale_pui/blob/master/public/models/romanize_series_identifier.rb](https://github.com/YaleArchivesSpace/aspace_yale_pui/blob/master/public/models/romanize_series_identifier.rb)).  


### REQ 3:

When criteria 2 is met (i.e. level=”otherlevel”), no text should precede the identifier. 


### REQ 4:

Furthermore, the otherlevel “component unique identifier” will be displayed as is, without any transformation.


### REQ 5:

In both cases, if there is no “component unique identifier”, then the level name should be omitted from the composite string. 


### REQ 6:

In cases where the level name is not omitted, then the component unique identifier should be appended with a colon and a space (e.g. “: “).

_For the third component of the composite string (i.e. the title):_


### REQ 7:

The title should be taken directly from the archival object “title”.  


### REQ 8:

If there is at least one creation date with a type of inclusive or single associated with that archival object, then a comma and a space should be applied after the title (e.g. “, “)


### REQ 9:

Contrary to REQ 8, if the title is blank, then the comma and a space separator must be omitted.


### REQ 10:

When the title ends with a double quote, then the comma should be inserted before the double quote, and still end with an extra space (e.g. “,” “).

_For the fourth component of the composite string (i.e. the creation dates that are either inclusive or single):_


### REQ 11:

Only date sub records with a type of inclusive or single should be appended at the end.  The order that they are in may be retained (in other words, there is no need to sort the date sub records).  


### REQ 12:

Each date sub record should be concatenated together with a comma and a space.  


### REQ 13:

As usual, if the date sub record has a date expression, then that value should be used.  If there is no date expression, then the begin and end date values should be combined with an em dash or a hyphen.


### REQ 14:

Creation dates added to the composite string should be filtered out of the unordered list of dates that display below the title on the context of the ~~archival-object landing pages and on~~ the single-scroll view.


## Examples


### Example 1

level=“series”

component unique identifier=1

title=“Correspondence”

creation date1 (inclusive) begin=1900

creation date1 (inclusive) end=1950

creation date2 (single) expression=1965 Easter

composite series string should be:

Series I: Correspondence, 1900-1950, 1965 Easter


### Example 2

level=“otherlevel”

otherlevel=“accession”

component unique identifier=“2015-A-etc”

title=“Transcripts”

creation date1 (inclusive) expression=“2000-2010, undated”

composite series string should be:

Accession 2015-A-etc: Transcripts, 2000-2010, undated


### Example 3

level=”series”

component unique identifier=5

creation date1(inclusive) expression=19th century

composite series string should be:

Series V: 19th century


### Example 4

level=”series”

title=”Restricted Fragile”

creation date1(inclusive) expression=2000-2011

creation date2(single) begin=2015

Composite series string should be:

Restricted Fragile, 2000-2011, 2015


### Example 5

level=”series”

component unique identifier=3

title=”Something that ends with a “double quote””

creation date1(inclusive) expression=1970-2008

Composite series string should be:

Series III: Something that ends with a “double quote,” 1970-2008


## Screenshots 

(so that we can consider such changes holistically, rather than just as a series-level composite string)



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


I took the dates out in this case, but I’m not actually advocating for that in this view.  

…
