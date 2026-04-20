# EAD Export

## What Does It Do?
Pulls [the EAD3? for?] new(?) and newly published [ASpace] collections and repurposes it in 2 ways:
1. Puts the EAD itself in a public GitHub repo
	+ pulls EAD data via the ArchivesSpace API every night
	+ amends the exported EAD
	+ puts a copy in Yale’s ArchivesSpace GitHub organization
1. Transforms the EAD into PDF finding aids and puts them in a world-accessible web location, allowing them to be reached from Archives at Yale webpages by those researchers who prefer that style of discovery (a non-trivial group)
	+ transforms it into PDFs, and
	+ places the PDFs into a folder on the server.
1. Runs a report created by LIT that collates data issues.
1. As part of those processes, emails a defined list of addresses if there are errors running the application or errors in the ArchivesSpace data that prevent in part or whole creating EAD3 files or finding aids.

## Where Is It?

1. The servers are on Yale infrastructure. Access is restricted to a defined list of netids.
	1. `yul-eadexport-tst1.library.yale.edu` / `yul-eadexport-tst1.library.yale.internal`
	1. `yul-eadexport-prd1.library.yale.edu` / `yul-eadexport-prd1.library.yale.internal`
	1. For possible information archeology: the former server was named as13dev.library.yale.edu
1. Public EAD3 [GitHub repo](https://github.com/YaleArchivesSpace/Archives-at-Yale-EAD3)
1. Public [PDF finding aids](https://ead-pdfs.library.yale.edu/) Note: This root directory view is never publicly linked. It's not prohibited, but there's nothing particularly secret about it either.
	+ The prod server runs a webserver, just to spell that out

## What's It Made Of?

1. [Open source ArchivesSpace plugin](https://github.com/YaleArchivesSpace/ead_export_addon.git)
1. [Open source application](https://github.com/hudmol/archivesspace_export_service)
	+ Including a SQLite internal db
1. Java 1.8
1. API-only account in ArchivesSpace instances
1. Application key from the GitHub repository
1. Additional management cron jobs and other management scripts that handle running the application on a schedule, exporting the EAD3 documents to GitHub, and transforming and moving the PDF finding aids

## Who Maintains It?

For now the following is the skinny list of people who have access to the bits and bytes:
+ Alicia Detelich, DMAC
+ Christy Bailey-Tomecek, DSCA
+ Trip Kirkpatrick, Library IT
+ Rick Aliwalas, Library IT

These addresses receive an email if there are issues in running the application, or if there are data errors that require one. Alison and Steelsen receive it in a backstop capacity. This list is contained in the `eadexport.sh` file for the former reason and in the `eadexport_report.sh` file for the latter.
+ [christy.tomecek@yale.edu](mailto:christy.tomecek@yale.edu)
+ [alicia.detelich@yale.edu](mailto:alicia.detelich@yale.edu)
+ [trip.kirkpatrick@yale.edu](mailto:trip.kirkpatrick@yale.edu)
+ keith.boyd-carter@yale.edu
+ steelsen.smith@yale.edu
+ alison.clemens@yale.edu

### What maintenance is needed?

*Most Important:* If any test run needs to be done, even on the Test server, testers need to be sure all pieces are pointing to testing options so that tests don't overwrite the public EAD3 repository, for instance, and don't foul up the currency of PDF finding aids.

When necessary, someone needs to ensure
+ The export service gets shut down and restarted properly,
	+ `sudo systemctl restart eadexport`  
	OR
	+ `sudo systemctl stop eadexport`
	+ `sudo systemctl start eadexport`  

	AND
	+ `sudo systemctl status eadexport`
+ The webserver gets shut down and restarted properly, and
+ The appropriate firewall rules get generated and activated after restart so the PDFs will be world-readable.
+ This person as of the last edit to this text was Keith Boyd-Carter in LIT
+ But the person responsible for supporting ArchivesSpace more broadly will be responsible to YAMS et al. for comms and effecting the above even if they aren’t mashing the buttons.

PDF finding aids are not deleted by the service. If we want to delete (not update/replace, fully delete), that's a manual process.

## How Do I Get the Secret Handshake?

Talk to one of the authenticated people in the order listed. Once you are cleared, there's a Box document with the credentials, access throttled by YAMS chair[s] and/or Tech Lead for Special Collections, Library IT.

Once you have that, `ssh -l [your netid] yul-eadexport-tst1.library.yale.internal` or to the Prod server, as appropriate.
Switch to being the eadexport user as needed: `sudo su - eadexport`

### Testing the EAD Export Application

1. SSH to server
1. check settings in `/home/eadexport/exporter_app/config/config.rb` and `/home/eadexport/exporter_app/config/jobs.rb`
	+ The former should have
		+ Credentials that match what they should be
		+ `aspace_backend_url: 'https://testarchivesspace.library.yale.edu/api'`
		+ Handle information pointing to ITS's test entry
			```
			handle_wsdl_url: 'http://linktest.its.yale.edu/ypls/webservices?wsdl',
			handle_user: '10079.1/FA',
			handle_credential: [see ASpace credentials repository]
			handle_prefix: '10079.1/fa',
			handle_group: '10079.1/FA',
			handle_base: 'https://puitestarchivesspace.library.yale.edu',
			```
	+ The latter should have a small number of repo jobs and a github job.
		+ The GitHub job should have
			+ `:jobs_to_merge` entry in the `:task_parameters` entry, with a value of an array containing the repo job names
			+ `:git_remote` entry with a value of  `git@github.com:YaleArchivesSpace/Archives-at-Yale-EAD3-Test.git`
1. Check that `/home/eadexport/eadexport_report.sh` is only going to send emails summarizing the work to the right people
1. Ditto `/home/eadexport/eadexport.sh`
1. Cron stuff? How do the files get converted to PDF? When/how do the Finding Aids get put in a world-readable share? (Which is [https://ead-pdfs.library.yale.edu](https://ead-pdfs.library.yale.edu).)

## Where Can I Read More?

Access not guaranteed to any of these.

+ [Word Doc in LIT Sharepoint](https://yaleedu.sharepoint.com/sites/library.it.teams2/Shared%20Documents/(AMS)%20Archival%20Management%20Systems/Tech_Lead_Documentation/Management_and_Projects.docx?web=1)
+ [Google doc from migration time](https://docs.google.com/document/d/1e_QhZAPbeuFijZ6JW6bvt9M70LoGb-BwcVFrSY00Og8/edit#)
+ [YAMS Documentation on S/W that Integrates with ASpace](https://docs.google.com/document/d/1cOlvR1narvXfrWrQoC4QqvgFgpmtWQi0fyE_2Gkfszo/edit)

