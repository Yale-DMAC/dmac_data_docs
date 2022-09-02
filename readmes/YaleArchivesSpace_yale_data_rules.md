# yale_data_rules

Plugin to enforce data entry rules on YUL ArchivesSpace instances.

## The Rules

### Dates

Structured 'begin' and 'end' date values must conform to the following rules:

* YYYY-MM-DD, YYYY-MM, or YYYY format
* Maximum length of 10 characters
* Month values cannot be larger than '12'
* Day values cannot be larger than '31'
* Month and day values less than '10' and year values less than '1000' must contain a leading '0' - i.e. '06', '0900'.
