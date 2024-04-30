# Refreshing Data in Test and Dev from Prod

## General Workflow

From time to time, it's beneficial to sync up the data between Prod and Test. Here's the basic procedure for doing that:
1.	Undertake a superficial comparison to see if anything's structurally different (plugin versions, db versions, etc.) in origin instance and target instance, following up as appropriate if there is.
1.	Confer with Lyrasis about any date restrictions 
1.	Set an intended date (only non-Lyrasis restriction is that it should work well with any plugin deployments or configuration changes) 
1.	Request to members of Archives Advisory Group (AAG) to inquire in their units whether anyone has work in Test that needs to complete, with response within 10 days 
1.	Request to AAG members to be available for QA on sync date 
1.	Message to yulaspace mailing list about the same time with the same core message, alerting people to a date no less than 3 weeks in the future (2 might be preferable, but also might be tight in case someone's on vacation) and requesting responses within 10 days 
1.	Presuming no material objections, reminder message to yulaspace a week before 
1.	Lyrasis executes on the planned date, AAG members need to do light QA to look for anything broken
	+	After copy happens, run the Background Job named "Preservica Data Deleter" (see below for that process)
1.	Announce to yulaspace that it's complete


## What data will be changed, in a Refresh? 

(taken from [a Digital Preservation Services Google Doc](https://docs.google.com/document/d/11z83QJHG4chuFLaZuQpCVhpQwuTbdZ7IrLCiCIWbcjA/edit#heading=h.48whbe3haivu))

All ASpace records in all repositories within a particular instance will be replaced by data from the Production instance. Any records/data/changes that was specific to a particular instance (ie ASpaceDev or ASpaceTest) will be overwritten. 
Once the Refresh is complete in the ASpace instance, YAMS admins will then run the Preservica data deleter plugin in the ASpace instance that has just been overwritten with ProdASpace data. This plugin removes all links to Preservica from the ASpace instance. The reason this step is required is that the ProdASpace records that have been written to the refreshed ASpace instance contain links to the ProdDPS instance - ie, DevASpace records now contain links to items in ProdDPS. Running the plugin deletes all of these incorrect URLs, so that the refreshed ASpace instance can then resume with sync workflows to the corresponding DPS instance. (ie so that DevASpace can resume sync with DevDPS, and TestASpace to TestDPS.)

## Running the Preservica Data Deleter

1. Log in to the appropriate instance of ArchivesSpace (it does not matter which repository)
1. Next to the repository name below the header area, click the gear icon
1. Choose "Background Jobs"
1. Look for the "Create Job" button and click it
1. Choose "Preservica Data Deleter"
1. Read the page
1. Click "Start Job" without checking the box or entering a confirmation string to execute a dry run of the job 
1. To actually delete data, check the "Delete preservica data?" checkbox and enter a confirmation string as explained on the page.
1. You can wait or step away. Finished (successful and unsuccessful) jobs show up on [the Background Jobs listing page](https://testarchivesspace.library.yale.edu/jobs) (link is to TEST)