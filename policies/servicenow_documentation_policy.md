# Documentation Policy 

## 1. ServiceNow 
### 1.1 Tags 
Upon Receiving the ticket, it should be added to the Visual Board and be given appropriate tags: 
- Request Type – What type of project is this? Data Transformation, Reporting, etc. 
- Effort Value – How complex is this project based off the initial request. 
- Priority Value – How high a priority is this project based off the initial request. 
- Origin Library – Which library is requesting this project. 
- System – What systems will be used in this project? Alma, ArchivesSpace, or Other. 

Upon completion of the ticket, add appropriate Tags to the RITM. Many of these tags can be copied from the tags given to the ticket on the visual task board, but should be updated to reflect the details of the project upon completion. For example, if a project was initially considered a low effort project but became complex over time, the tag on the ticket will be different from the tags on the card. 

The tags included should be: 
- Request Type – Migration, Transformation, Reporting, etc. 
- Effort Value – How complex was this project. 
- Priority Value – How high a priority was this project. 
- Origin Library – Which library requested this project. 
- System – What systems were used in this project? Alma, ArchivesSpace, or Other. 

#### Request Types 
- Data Remediation – Requires deletion or replacement of data in existing records. 
- Data Creation or Enhancement – Requires the creation of records or enhancement of existing fields. (e.g. Adding linked data to a subject heading rather than replacing it with a new heading) 
- Data Transformation – Migration or Mapping of data into a new format. 
- Reporting or Data Analysis – Providing reports or providing analysis of data. 
- Workflow or Tool Support – The creation, updating, or review of workflows or tools. 
- ArchivesSpace Support – Providing support to ArchivesSpace such as granting permissions, creating accounts, fixing errors, updating Archives at Yale, etc. 
- General Support – Anything that does not fit into the above categories. 

[See Request Types for more information.](../service_requests/request_types.md)

#### Effort Values 
- Low Effort – Any request that requires little or no specialized knowledge or skills. (e.g. Granting ArchivesSpace Permissions, Deleting records from a provided set of Alma MMS IDs or ArchivesSpace URIs, creating a simple report in Analytics or SQL that requires no advanced querying knowledge such as providing a list of archival object ids with titles, etc.) 
- Medium Effort – Any request that requires basic Metadata Specialist skills. Most requests should fall under this category. (e.g. Specialized Reports with advanced querying, Batch editing records, etc.) 
- High Effort – Any request that could provide a challenge or learning opportunities for a Metadata Specialist. (e.g. Creating complicated reports from messy data, Updating or Repairing an ArchivesSpace plugin, extracting data from an inaccessible resource, etc.) 

#### Priority Values 
- Low Priority – Work that has no specific timeline and can be completed at leisure. 
- Medium Priority – Work that needs to be addressed within two weeks and completed within a reasonable amount of time. 
- High Priority – Work that needs to be addressed and completed as soon as possible. 

[See Specialist Workflow for more information.](../workflows/servicenow_specialist_workflow.md)

### 1.2 Work Notes 
If discussions occur outside of the ticketing system (e.g., email, meetings, Teams messages, phone calls), a summary or copy of the relevant information should be added to the ticket work notes. 

The ticket should serve as the authoritative record of decisions, requirements, and project history. 

### 1.3 Attachments 
External links have a habit of breaking over time or requiring granted access. Whenever possible, files should be included as attachments on the ticket. If a user links to an external file, download a copy and attach it to the ticket for documentation purposes. 

When sending files to users, always attach the file on ServiceNow for documentation purposes. 

Try to include result files as attachments wherever possible. Keeping documentation on the ticket of things such as a csv with a list of all records altered and what changes were made is an important part of keeping good documentation. 

## 2. Project Documentation 
Tickets with brief low efforts – such as adding permissions in ArchivesSpace – do not require documentation. However, anything that involves writing a script or doing something complicated should be documented in our Github. Upon completion of a ticket, ensure proper tagging is applied for both simple and complex tickets, and then create documentation of the complex projects. Documentation should be filled out as detailed as possible; not every field is always applicable. 


And example of a project template: 
```
# TITLE 
Last updated on [DATE] by [NAME]. 
 
| Start Date | End Date | Contributors | Informed Stakeholders | 
| ---------- | -------- | ------------ | --------------------- | 
|            |          |              |                       | 
 
# Overview 
## Problem Statement 
Include statement of the problem and its impact. 
## Goals 
Describe the goals of the project and what outcomes are required to measure the success of the project. 
# Background 
Detailed Background of the project, data, and services. Include reasons why specific decisions were made. 
 
 
# Process 
- List steps here 
 
# Notes 
(Keep track of meetings and formal communication of the project. Also include any highlights in the project's progress such as roadblocks or changes in approach.) 
 
| Date | Highlight | Notes | 
| ---- | --------- | ----- | 
|      |           |       | 
 
# Review 
 
## Data Details 
Include details about the amount of records, shared traits, collection information, etc. 
## Communication 
Stakeholders and consultants contacted and any relevant comments. 
## Results 
Describe the outcome of the project and describe any relevant issues that arose. 
 
# References 
- List of relevant links 
```

### 2.1 Github 

SCMS uses Github to record our work. Every fiscal year a new project documentation repository is created to add documentation to. After completing your project documentation and gathering all your files, it should be uploaded to the current FY repository in its own folder. The project documentation should be written in Markdown and added as a README.md in your folder. 

Upon adding your folder, update the repositories main README file to include in the table a link to your documentation, the system(s) used, and a short description of the project. 

For ease of use, specialists can set up a project folder connected to the repository so they can push files directly from their computer without accessing the website and having to individually edit or upload each file. 
1. Navigate in terminal to the folder you wish to use then `git init`.
2. Next `git remote add origin git@github.com:Yale-DMAC/projects_fy27.git` or whatever the repo name currently is. Follow up with: `git remote set-url origin git@github.com:Yale-DMAC/projects_fy27.git` These will use your SSH key to connect the folder with the FY27 project repository. See https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent for guidance on setting up a SSH key in github. 
3. Always `git pull origin main` before pushing to ensure you are not erasing any updates from other users. 
4. `git add .` Will add every new change to a commit. 
5. `git commit –m “Message Here.”` will add your commit comment. Usually this will be something such as “Adding documentation for the YCBA instances update.” 
6. `git push origin main` will push the new commit into the repository. 

### 2.2 Clarity 
Testing using Yale’s LLM resource for documentation purposes has begun. Clarity boasts of privacy protection for sensitive data: 

This configuration assures that information you provide to the Clarity platform cannot appear in responses provided to other users of Clarity or to other AI model users. These features allow users to submit moderate and high-risk data to the Clarity platform which would pose an unacceptable privacy risk in other generative AI tools. 

Promising results have been obtained in creating documentation for the github by using Clarity by following these steps: 
1. Export Ticket – download a pdf copy of your ticket, this should include all communications and work notes visible on the ticket and any title or description information on the ticket. 
2. Upload to Clarity – Upload your ticket, the project documentation template, code scripts, and any other relevant files. 
3. Ask Clarity to write project documentation for you based on the template provided. 