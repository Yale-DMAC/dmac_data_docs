# ArchivesSpace-to-Excel Guide 

## Columns Used in Creating Finding Aids

For description of subordinate components only. Enter collection-level description directly into ArchivesSpace and use this guide for entering data at any level of description below the collection level.

To hide columns in Excel, highlight one or more columns and right click, then choose **Hide**. Unhide them the same way (choose columns on either side of the hidden column/s and click **Unhide**). To add a row, highlight a row and right click, then choose **Insert**; the new row will be inserted above it.

<table>
  <tr>
   <td><strong>A</strong>
   </td>
   <td>level number
   </td>
   <td>Use Arabic numerals (1-12 only) to indicate the level of hierarchy described in Column D
   </td>
  </tr>
  <tr>
   <td><strong>B</strong>
   </td>
   <td>level type
   </td>
   <td>Use drop-down menu for choices that name the level indicated in Column A. Will be auto-populated as <strong>File</strong> if left blank.
   </td>
  </tr>
  <tr>
   <td><strong>C</strong>
   </td>
   <td>unitid
   </td>
   <td>Series level only, when <strong>Series</strong> is selected in Column B – use Arabic numerals and only insert numeral, not “Series 1.”
   </td>
  </tr>
  <tr>
   <td><strong>D</strong>
   </td>
   <td>title
   </td>
   <td>Free text for titling Series, Subseries, and Headings, or File titles, etc., at the level indicated in Columns A-C
   </td>
  </tr>
  <tr>
   <td><strong>E</strong>
   </td>
   <td>date expression
<p>
dates in this column will display in finding aid but are not machine-actionable
   </td>
   <td>Only use this field when you need to add a *textual date* that cannot be represented in columns F-H alone, such as <strong>undated</strong> or <strong>Easter 1942</strong> or anything with <strong>circa </strong>or question marks. When you use this column also add actual date values (for <strong>Easter 1942</strong>, you would enter <strong>1942</strong> in column F, and optionally <strong>4</strong> in column G, and <strong>5</strong> in column H). For two dates separated by a comma (<strong>1912, 1929</strong>) see directions on page 4.
   </td>
  </tr>
  <tr>
   <td><strong>F</strong>
   </td>
   <td>year begin
<p>
date is machine-actionable
   </td>
   <td>Enter a start year (<strong>YYYY</strong>) for <span style="text-decoration:underline;">inclusive</span> span dates in a Series or folder, a bracketed date, and a single-date folder (e.g., <strong>1920</strong> May 2). Single-folder dates entered in columns F-H will auto-display normally in the finding aid (1920 May 2).
   </td>
  </tr>
  <tr>
   <td><strong>G</strong>
   </td>
   <td>month begin
   </td>
   <td>Use for single-date folders: enter Arabic numeral for month
   </td>
  </tr>
  <tr>
   <td><strong>H</strong>
   </td>
   <td>day begin
   </td>
   <td>Use for single-date folders: enter Arabic numeral for day
   </td>
  </tr>
  <tr>
   <td><strong>I</strong>
   </td>
   <td>year end
<p>
date is machine-actionable
   </td>
   <td>Enter an end year (<strong>YYYY</strong>) for <span style="text-decoration:underline;">inclusive</span> span dates 
   </td>
  </tr>
  <tr>
   <td><strong>J</strong>
   </td>
   <td>month end
   </td>
   <td>Infrequently used, so hide this column. You can use this field if you’d like, if you have exact begin and ends dates (e.g., 1920-01-15 – 1927-04-02).
   </td>
  </tr>
  <tr>
   <td><strong>K</strong>
   </td>
   <td>day end
   </td>
   <td>Infrequently used, so hide this column. You can use this field if you use column J.
   </td>
  </tr>
  <tr>
   <td><strong>L</strong>
   </td>
   <td>bulk year begin
<p>
date is machine-actionable
   </td>
   <td>Series level only – enter the start year (<strong>YYYY</strong>) for <span style="text-decoration:underline;">bulk</span> span dates 
   </td>
  </tr>
  <tr>
   <td><strong>M</strong>
   </td>
   <td>bulk month begin
   </td>
   <td>Infrequently used, so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>N</strong>
   </td>
   <td>bulk day begin
   </td>
   <td>Infrequently used, so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>O</strong>
   </td>
   <td>bulk year end
<p>
date is machine-actionable
   </td>
   <td>Series level only – enter the end year (<strong>YYYY</strong>) for <span style="text-decoration:underline;">bulk</span> span dates 
   </td>
  </tr>
  <tr>
   <td><strong>P</strong>
   </td>
   <td>bulk month end
   </td>
   <td>Not currently used at Yale so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>Q</strong>
   </td>
   <td>bulk day end
   </td>
   <td>Not currently used at Yale so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>R</strong>
   </td>
   <td>instance type
   </td>
   <td>Will be auto-populated as <strong>Mixed Materials</strong> (only choice for Yale) so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>S</strong>
   </td>
   <td>container 1 type 
   </td>
   <td>Top container – will be auto-populated as <strong>Box</strong> so leave blank and hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>T</strong>
   </td>
   <td>container profile
   </td>
   <td>Top container size should only be assigned in ASpace, so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>U</strong>
   </td>
   <td>barcode
   </td>
   <td>Currently added in ASpace (Voyager at BRBL), so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>V</strong>
   </td>
   <td>container 1 value
   </td>
   <td>Add top container number here (that is, the “circulating” box/folder/frame/item that has the bar code attached to it)
   </td>
  </tr>
  <tr>
   <td><strong>W</strong>
   </td>
   <td>container 2 type
   </td>
   <td>Will be auto-populated as <strong>Folder</strong> if left blank, so hide this column or choose another type from drop-down
   </td>
  </tr>
  <tr>
   <td><strong>X</strong>
   </td>
   <td>container 2 value
   </td>
   <td>For folder numbers – a technique is being worked out so that staff can auto-number folders
   </td>
  </tr>
  <tr>
   <td><strong>Y</strong>
   </td>
   <td>container 3 type
   </td>
   <td>Not generally used at Yale so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>Z</strong>
   </td>
   <td>container 3 value
   </td>
   <td>Not generally used at Yale so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>AA</strong>
   </td>
   <td>extent number
   </td>
   <td>Use Arabic numeral
   </td>
  </tr>
  <tr>
   <td><strong>AB</strong>
   </td>
   <td>extent value
   </td>
   <td>Use drop-down menu
   </td>
  </tr>
  <tr>
   <td><strong>AC</strong>
   </td>
   <td>generic extent
   </td>
   <td>Series level only – use for container descriptions in columns AA and AB [e.g., (<strong>3 boxes</strong>)]
   </td>
  </tr>
  <tr>
   <td><strong>AD</strong>
   </td>
   <td>generic physdesc
   </td>
   <td>Series-level only – use when necessary for non-standard descriptions (e.g., 6 ceramic cats); hide this column 
   </td>
  </tr>
  <tr>
   <td><strong>AE</strong>
   </td>
   <td>origination
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AF</strong>
   </td>
   <td>bioghist
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AG</strong>
   </td>
   <td>scope and content note
   </td>
   <td>Enter descriptive text at any level
   </td>
  </tr>
  <tr>
   <td><strong>AH</strong>
   </td>
   <td>arrangement note
   </td>
   <td>Generally only used at Series level
   </td>
  </tr>
  <tr>
   <td><strong>AI</strong>
   </td>
   <td>access restrictions
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>AJ</strong>
   </td>
   <td>phystech
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AK</strong>
   </td>
   <td>physloc (location note)
   </td>
   <td>Formerly used for “Stored in OV” but now put the container number in Column V and hide this column 
   </td>
  </tr>
  <tr>
   <td><strong>AL</strong>
   </td>
   <td>use restrictions
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>AM</strong>
   </td>
   <td>language code
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AN</strong>
   </td>
   <td>langmaterial note
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AO</strong>
   </td>
   <td>other finding aid
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AP</strong>
   </td>
   <td>custodhist
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AQ</strong>
   </td>
   <td>acqinfo
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AR</strong>
   </td>
   <td>appraisal
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AT</strong>
   </td>
   <td>originalsloc
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AU</strong>
   </td>
   <td>alternative form available
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AV</strong>
   </td>
   <td>related material 
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AW</strong>
   </td>
   <td>separated material
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>AX</strong>
   </td>
   <td>preferred citation
   </td>
   <td>Hide this column
   </td>
  </tr>
  <tr>
   <td><strong>AZ</strong>
   </td>
   <td>control access headings
   </td>
   <td>Hide this column unless needed
   </td>
  </tr>
  <tr>
   <td><strong>BA</strong>
   </td>
   <td>component @id)
   </td>
   <td>Hide this column    
   </td>
  </tr>
  <tr>
   <td><strong>BB</strong>
   </td>
   <td>dao Link
   </td>
   <td>Currently added in ASpace, so hide this column 
   </td>
  </tr>
  <tr>
   <td><strong>BC</strong>
   </td>
   <td>dao Title
   </td>
   <td>Currently added in ASpace, so hide this column  
   </td>
  </tr>
  <tr>
   <td><strong>BD</strong>
   </td>
   <td>system ID
   </td>
   <td>Hide this column. The cells are populated with the ArchivesSpace URI fragment for the archival object. Those values are only added during the “EAD3-to-Excel” transformation scenario, in case someone wants to use those values for subsequent ArchivesSpace API updates.
   </td>
  </tr>
</table>

## Formatting available

Any text that is colored red will be encoded as a “title” in EAD and will display in an italic font in YFAD (but will be underlined in a PDF). You can also, if needed, emphasize text with **bold**, _italics_, <span style="text-decoration:underline;">underline</span>, etc.

To add a unique header to a bioghist or scope and content note (at any level), put the header information in 14-point font at the very start of the cell and hit [**ALT Enter**] **once** to begin the text.  

To create multiple paragraphs in notes, hit [**ALT Enter**] **two times** to provide paragraph separators.  

Example:

<table>
  <tr>
   <td><strong>level number</strong>
   </td>
   <td><strong>level type</strong>
   </td>
   <td><strong>bioghist</strong>
   </td>
   <td><strong>scope and content note</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>series
   </td>
   <td>John Livingston (1750–1822)  \
John Livingston was born in New York City, one of the twelve children of Robert Livingston Jr. (1708-1790), the third and last Lord of Livingston Manor, and his wife Maria Thong Livingston (1711-1765). An aide-de-camp to General George Clinton during the Revolutionary War, John Livingston was engaged in land speculation in the Hudson River Valley and upstate New York. 
   </td>
   <td>Series I consists of papers of the earliest members of the family to reside at Oak Hill, John Livingston and his son Herman, accompanied by a group of the Livingston family's land and legal records.  \
 \
John Livingston's papers comprise one folder of miscellaneous correspondence and financial documents to or referring to him; the latter includes a letter from Elkanah Watson. Additional material concerns Livingston's involvement in the New York Genesee Company of Adventurers, documenting the activities of Caleb Benton, Oliver Phelps, Peter Ryckman, and the Indians Joseph Brant and The Infant, among others, along the Pre-Emption Line in the area of Canadesaga (now Geneva), New York. 
   </td>
  </tr>
</table>


## Other tips

* For ease of navigation in a long spreadsheet you can color-code entire rows (for example, to delineate a series-level row) or columns. Select the row or column, right-click, and choose a “fill color” (the tipped bucket) from the formatting box that pops up above. You can also use a larger point size for a row (such as a Series title) or column (such as A) as long as it’s <span style="text-decoration:underline;">not</span> 14 point.
* To move an existing row(s), highlight it, right click, choose **Cut**; choose the row <span style="text-decoration:underline;">below</span> where you want to insert the cut row, right click, and choose **Insert Cut Cells**. 
* The spell-check feature is found on the far left under the REVIEW tab.

## Level-0 Rows

If you have a folder date that is not a range—such as **1912, 1929**—encode the two dates separately. To do that, add another row below the title level and set the new row level in column A equal to **0** (zero). 

Example:

<table>
  <tr>
   <td><strong>A</strong>
   </td>
   <td><strong>B</strong>
   </td>
   <td><strong>C</strong>
   </td>
   <td><strong>D</strong>
   </td>
   <td><strong>E</strong>
   </td>
   <td><strong>F</strong>
   </td>
   <td><strong>I</strong>
   </td>
  </tr>
  <tr>
   <td><strong>level number</strong>
   </td>
   <td><strong>level type</strong>
   </td>
   <td><strong>unitid</strong>
   </td>
   <td><strong>unittitle</strong>
   </td>
   <td><strong>date expression</strong>
   </td>
   <td><strong>year begin</strong>
   </td>
   <td><strong>year end</strong>
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>file
   </td>
   <td>
   </td>
   <td>Simpson, Robert  
   </td>
   <td>
   </td>
   <td>1912
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>1929
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>file
   </td>
   <td>
   </td>
   <td>Smith, Catherine Jones
   </td>
   <td>
   </td>
   <td>1908
   </td>
   <td>1937
   </td>
  </tr>
</table>

You can also use level-0 rows for any other values that need to repeat within a single level of description. For example, rather than making two levels of description in YFAD because the material being described spans two boxes, you can group that information by adding a new row, setting its column A equal to 0, and then filling in a value in column V. 

Revised October 30, 2015
