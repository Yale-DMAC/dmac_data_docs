# Processing Electronic Theses and Dissertations

This document describes a workflow for processing electronic theses and dissertations from the Graduate School of Arts and Sciences.

## Receipt of Records from Proquest

Students submit their dissertations electronically to the Graduate School of Arts and Sciences. After acceptance, these dissertations are sent electronically to Proquest for processing and ingest into the Proquest Theses and Dissertations Online database.

In the course of processing, Proquest creates three types of metadata for each dissertation:

1. A provider-neutral MARCXML file
2. A Proquest XML metadata file
3. An XLSX file with some additional information about each dissertation.

After Proquest processes and ingests the dissertations into their system, they send PDF copies of each dissertation, along with the metadata files noted above, to a Manuscripts and Archives drive via FTP.

## Extract Metadata from Proquest Files, Ingest into EliScholar

After receiving the files from Proquest, MSSA staff run Python scripts which organize the files and extract metadata from the Proquest XML into the BePress .XLS template for bulk ingestion into EliScholar.

After records are ingested into EliScholar, a report can be generated from the EliScholar interface which includes the EliScholar URL for each thesis or dissertation. This report is matched up with the publication numbers and Proquest identifiers for each item via a Python script, and the report with the URLs and publication numbers/identifiers is sent to RDS. Adding the publication numbers/identifiers allows RDS staff to make the connection between the EliScholar URL and the MARCXML record which is ingested into Voyager.

## Modify Proquest MARCXML, Ingest into Voyager

The following changes are made to the MARCXML records provided by Proquest in order to comply with YUL cataloging practices:

- Fixed fields:
	- Add 006: =006  m\\\\\o\\d\\\\\\\\
	- Add 007: =007  cr\|n|
	- Add 008/7-10: [year of publication]
	- Add 008/15-17: ctu = place of publication
	- Add 008/23: o = online
	- Add 008/24: m = thesis
- Modify 040 to 040  \\$aCtY$beng$erda$epn$cCtY
- Add to 100: ,$e author before final period.
- Modify 260 to 264 \1 $a[New Haven, Connecticut] :$bYale University,$c [keep date]
- Update 300 \\ “1 online resource”; expand abbreviations (p. to pages)
- 336 \\ $atext$btxt$2rdacontent
- 337 \\ $acomputer$bc$2rdamedia
- 338 \\ $aonline resource$bcr$2rdacarrier
- Add 380 \\ $aDissertations, Academic$2 lcsh
- Modify 502 $aThesis (Ph.D.)--Yale University, date. to 502  \\$bPh.D.$cYale University$d date.
- Delete 506 restrictions notes from original record.
- Add 506 \\ $3Proquest dissertation:$aAccess is restricted by licensing agreement$5CtY
- Add 506 \\ $3EliScholar dissertation:$aAccess is available to the Yale community$5CtY
- Add 655 \7$a Academic theses.$2lcgft
- Delete 690 and 790; delete 590 with school code
- Modify 720 advisor name to 700 $a…,$edegree supervisor.
- 710 2\ Add ,$e degree granting institution.
- Add 710 2\ $aYale University.$b[Department].
- Add 730 0\ $3Proquest dissertation$aDissertations & Theses @ Yale University.$5CtY
- Add 830 \0$3EliScholar dissertation$aYale Graduate School of Arts and Sciences Dissertations.$5CtY
- If record ingested from MarcEdit into Voyager, we may need to add an 852 for ProQuest dissertation and an 852 for EliScholar dissertation
- After discussion, just going to create a single 852
- Update 856 40 $3 Proquest thesis
- 856 ProQuest links require proxy prefix (https://yale.idm.oclc.org/login?URL=)
- Add 856 40 $3 EliScholar thesis
- 856 EliScholar links are open to the world, no proxy or authentication required.
- Add punctuation to 246: =264  \1$a[New Haven, Connecticut]:$bYale University,$c2021
- Remove =546  \\$aEnglish
- =500  \\$aSource: Dissertations Abstracts International, Volume: 83-02, Section: A to =588  \\$aDescription based on Dissertations Abstracts International, Volume: 83-02, Section: A.
- Add a comma before $e in 700: ex. =700  1\$aAlexander, Jeffery,$edegree supervisor.
- Change the period before $e to a comma in 710. Ex. change: =710  2\$aYale University.$bPsychology.$edegree granting institution. To =710  2\$aYale University.$bPsychology,$edegree granting institution.
- Add 590 to embargoed records indicating length of embargo and that patron should contact BRBL staff for access

These modifications are made to the MARCXML record via a MarcEdit file and a Python script which is stored on Google Colaboratory and run by RDS staff during processing. The Python script also adds the provided EliScholar URLs to the 856 field for each record. Once the records are modified the MARCXML is ingested into Voyager.

## Ingest into Preservica, Voyager Sync

The process of ingesting files into Preservica is still being determined, and rollout depends on the in-process upgrade of Preservica to v6. Upon upgrade, the Preservica-Voyager sync will become active, and theses and dissertations which are ingested into Preservica will have Preservica links added to the 583 field in the MARC record for each thesis or dissertation.

