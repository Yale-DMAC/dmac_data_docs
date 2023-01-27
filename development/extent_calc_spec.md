# User Story: Extent Calculator

As an archivist, I would like the option of calculating the linear footage and number of top containers (from within the resource record) for collection level and series/accession archival objects based on top container records associated with the archival objects.

If some top containers associated with the archival objects do not have container profiles, the calculation should be aborted and an error message given.

If the calculation is successful, then it should display in a separate window and I should then have the option to save that calculation as a new extent subrecord.

When a new extent subrecord is created, this is where the calculated data should go:

- The Portion should = Whole.
- The Number should = sum of extent measurements, based on extent depth, for all top containers within that resource/archival_object's hierarchy (if any top container is related to multiple archival_objects or resources, the extent should still be calculated as if it's the whole box...  the processor can edit this later, if need be).
- The Type should = “linear feet” if the top container dimension units is "inches". (perhaps this conversion should be a configurable list on the application level.  e.g. let's say I want to ignore the extent dimension value and have cubic meters display.  for our purposes, though, we’ll always want “linear feet” to be the Extent Type).
- The Container summary should = "(# containers)" (where container can be our generic "container type 1" value, which should be a configurable list for other users of the plugins. For us, though, this should suffice...  just like "linear feet" should suffice for the Extent Type).
- The Physical Details and Dimensions fields should be left blank.

These extent subrecords should be behave like any other in ASpace.  In other words, adding a new one should not delete existing records, and archivists should be able to edit and delete them as needed.

February 2015