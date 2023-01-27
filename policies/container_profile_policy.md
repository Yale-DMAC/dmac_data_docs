# Container Profile Records

## Functional Overview

Container profiles are associated with top containers, and provide information about the physical container in which archival materials are housed. With this data, we can calculate how much space a collection occupies.

![alt_text](images/image1.png "image_tooltip")

## Associating an existing container profile with a top container record

## Creating a container profile

On the main toolbar, click Plug-ins and select Manage Container Profiles.

In the upper right corner of the Container Profiles main page, click Create Container Profile.

Enter the following information 

* **Name** - A descriptive name for the container type. Since this value must be unique, we also include a summary of the container’s dimensions in parentheses. See below for guidance on general name types for container profiles.
* **Dimension units** - The unit of measurement used to measure the dimensions of a container. Container profile dimensions are always measured in inches.  
* **Extent Dimension** – The dimension of a container used to measure linear extent. Width is always used to measure linear extent at Yale. 
* **Depth**, **Height**, and **Width** measurements of the container. When measuring a container, you should always round up to the nearest whole inch.
    * Depth represents the distance from the front of the shelf to the back of the shelf.
    * Height represents the distance from the bottom of the box upwards.
    * Width is the edge of the container that faces out on the shelf.
        * For flat boxes, the long edge is measured as width. 
        * For containers in which materials are stored upright (i.e. archive boxes, record cartons, card boxes, etc.), the edge facing the front of the shelf (often the short edge) is measured as width.
        * For two-dimensional containers (folders of any size), the long side should be measured as width and the height should be measured as 0.5 inches.

Click Save Container Profile.

## Rules for creating container profiles

* Permission to create container profiles is given at the discretion of repository managers.
* Container profiles are shared across all repositories. 
* Container profiles for most standard-sized, commercially-produced containers used in Yale repositories have already been created in ArchivesSpace. Before creating a new container profile for a standard-sized box, please search the existing container profiles to confirm that it doesn’t already exist.
* **All containers are measured to the nearest inch on each side.** This means that there may be two different containers of relatively different sizes that belong to the same container profile. Since the goal of container profiles is to give a ballpark estimate of the size of our holdings, these marginal differences are acceptable.
* Container profiles refer to the boxes in which materials are stored. In some cases, container profile names may refer to a particular material or carrier type. Keep in mind, however, that in all cases, the container profile name has nothing to do with the materials therein. 
* Example: A set of earrings may be kept in a 5-inch audiocassette box. Never assume that the container profile name refers to the box’s contents.

## Container profile names

In order to minimize the possible proliferation of names, we've decided on a small group of name types. When creating a container profile, please use a name type from this list. If no value on this list describes the container that you would like to create a profile for, please contact the [Yale Archival Management Systems Committee](http://guides.library.yale.edu/archivesspace/members). 

* flat box
* card box
* film can
* square tube
* folder
    * n.b. -- a folder of any size should be referred to as a folder (including broadside, folio folder, etc.) Because of the uniqueness constraint, a folder’s name should include its width and depth dimensions. There’s no need to include its height dimension, since all folders are assigned a default height of 0.5 inches.
* records carton

## Container profiles for custom-made boxes

Many Yale repositories use custom-made boxes to house oddly-sized or shaped materials that won’t fit safely into standard-sized containers. In order to prevent an unmanageable proliferation of container profiles in ArchivesSpace, a single set of uniform container profiles for custom boxes has been created. These container profiles correspond approximately to the most common types and dimensions of custom boxes used in Yale repositories. They are as follows:

* Custom box [vertical octavo, 1" wide] (1" w x 10" h x 9" d) 
* Custom box [vertical octavo, 3" wide] (3" w x 10" h x 9" d)
* Custom box [vertical quarto, 1" wide] (1" w x 15" h x 13" d)
* Custom box [vertical quarto, 3" wide] (3" w x 15" h x 13" d)
* Custom box [flat, 12" wide] (12" w x 3" h x 10" d)
* Custom box [flat, 18" wide] (18" w x 3" h x 14" d)
* Custom box [flat, 24" wide] (24" w x 3" h x 20" d)
* Custom box [flat, 30" wide] (30" w x 3" h x 24" d)
* Custom box [flat, 36" wide] (36" w x 3" h x 30" d)
* Custom box [flat, 42" wide] (42" w x 3" h x 36" d)

## Rules for assigning container profiles to custom containers

* For containers smaller than 42 inches in width, round up to the next closest size container.
* For containers larger than 42 inches in width, assign "Custom box (flat, 42" wide) (42" w x 3" h x 36" d)"
* If none of the custom container profiles meet your guidelines, please contact the Yale Archives Management Systems Committee before creating a new custom box container profile.

## Strategies for searching, browsing, and choosing container profiles

* When searching for a container profile in a typeahead field (for example, in the Create Top Container window), look for words in bold text in your search results. When an exact match for your search term(s) is found in a record, that term will appear in bold.
* Using the Browse feature provides you with a greater number of tools for finding container profile records. To browse for a container profile from the Create Top Container Window, open the drop-down menu next to the typeahead and click on Browse. Some tips for browsing top container records:
    * In the search field in the top left corner of the Browse window, you can use quotation marks to search for an exact phrase. If you use the correct container profile name (example: “archive half legal”), this will make your search more accurate and greatly reduce your search results.
    * On the left side of the browser window, you can browse containers according to their height, width, or depth dimensions (but not all three at the same time). Click on the link next to the desired dimension and measurement to see all container profile records for boxes that include that dimension.