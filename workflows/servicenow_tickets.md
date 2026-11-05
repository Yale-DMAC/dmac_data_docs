# ServiceNow Tickets 

## 1. Anatomy of a Ticket 

**REQ** – The Request or Order. May be attached to multiple items or just one. 

**RITM** – The individual Items in a Request. A Requester may fill out the ServiceNow form multiple times and add them to their cart before submitting. By doing so, they will create multiple RITMs under a single REQ which is the complete order. Think of it as a REQ is the grocery cart and the RITMs are the individual items in the cart. 

**TASK** – The individual Tasks attached to an RITM. Staff can break an RITM into multiple parts to assign to different staff members or to track what parts of the project are completed.  

**INC** – Incident Responses are unique requests in that they require urgent attention. Typically these are used for when something is broken or in general is an emergency. However, all emailed requests are automatically made into Incident Responses due to the nature of the submission. These INCs will give daily reminders that the request has not been addressed. If these are not genuine incidents, then they should be converted into formal Requests when possible. 

Most requests we receive have one RITM and one task. But ServiceNow allows for structuring complex projects into manageable pieces. As an example, the request for a migration between databases could look something like: 

- REQ – Migrate DBText 
    - RITM 1 – Migrate CATACQ 
        - TASK 1 – Map CATACQ XML to ArchivesSpace 
        - TASK 2 – Clean up CATACQ XML data 
        - TASK 3 – Write migration code CATACQ data 
        - TASK 4 – Test migration 
        - TASK 5 – Migrate 
        - TASK 6 – Document	 
    - RITM 2 – Migrate ACQ 
        - TASK 1 – Map ACQ XML to ArchivesSpace 
        - TASK 2 – Clean up ACQ XML data 
        - TASK 3 – Write migration code for ACQ database 
        - TASK 4 – Test migration 
        - TASK 5 – Migrate 
        - TASK 6 – Document	 


## 2. Assigning Tickets 
1. Open the RITM. 
2. To Assign the entire ticket, click on the magnifying glass next to the ‘Assigned to’ field to locate the assignee’s NetID and select it. 
3. Next, assign the TASK as well. Scroll down to the bottom of the ticket where the ‘Catalog Tasks’ tab is located and click on the TASK you wish to assign. Click on the magnifying glass next to the ‘Assigned to’ field to locate the assignee’s NetID and select it. 
4. To break an RITM into multiple TASKs to assign different parts to Specialists, scroll to the bottom of the ticket where the ‘Catalog Tasks’ tab is located. Click on the ‘New’ button to add a new task. Enter a description of what that individual task will entail. Create as many TASKs as needed. 

## 3. Closing Tickets 
1. Open the RITM, and navigate to the bottom of the ticket where the ‘Catalog Tasks’ tab is located. Select the TASK you wish to close. Or just open the TASK directly from the main menu. 
2. Set the TASK status to ‘Closed Complete’. Make sure you are assigned to the TASK and not just the ticket to be able to close it properly. 
3. Once all TASKs are completed, the Ticket will automatically close itself. 

## 4. Communication and Work Notes 
**Work Notes** – Visible only to those who have staff access to ServiceNow. Those who submitted the ticket will not be able to see these notes. This is a good place to record information anyone looking at the ticket in the future will need to know. If you have external communications about this ticket, you should copy them in or summarize them in the Work Notes. 

**Additional Comments (Customer visible)** - These messages will be visible to the Requester and any watchers on the ticket. The message will also be sent as an email to anyone in SCMS and the Requester and watchers on the ticket. This is the preferred method of communication about any ticket as it keeps a record of any communications. 

**Attachments** – By selecting the paperclip button at the top of the ticket, you may add attachments to the ticket that Users can view and download. Use this to submit results to the user. If they request the files be delivered via email, make sure to also add them here. 

Users can see their tickets by accessing them at https://yale.service-now.com/it?id=my_items. On the ‘Activity Stream’ tab, the user can read messages and send responses. On the ‘Attachments’ tab they can add attachments or download existing attachments. Users can also add individuals to the Watch List toward the bottom of their ticket. 

## 5. Incident Responses 
To turn an Incident Response into a REQ, you will need to cancel the INC and create a new REQ that is linked to it. 

1. Open the INC and right click on the Incident number at the top of the ticket. 
2. Select ‘Create Request’ 
3. You will be redirected to the ServiceNow form, fill out the request in the form and make sure to fill out the contact name for the original Requester. 
4. This will create a REQ linked to the INC. 

## 6. Submitting Tickets for Others 

If you receive a request via email or in person, you should redirect the user to our ServiceNow form. 

If they are unable to fill out the form they can also email their request. 

It is important to encourage staff to submit a ticket themselves to avoid future requests being submitted this way. However, if you have a case where you have to submit a ticket for someone else, it is very simple. 

Fill out the form with the provided request information and in the ‘Contact Name’ field, select the Requester’s NetID. This should set them as the Requester; however, this doesn’t always work smoothly, and sometimes you will need to add them as the Requester in the REQ by selecting the magnifying glass in the ‘Requested For’ field and selecting their NetID. 

 