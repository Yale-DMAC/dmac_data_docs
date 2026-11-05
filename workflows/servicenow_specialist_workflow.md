# Request Ticket Workflow 

## 1. Ticket Assignment 

Tickets should be reviewed and assigned within 14 calendar days of submission. 

Upon Receiving the ticket, it should be added to the Visual Board and be given appropriate tags: 
- Request Type – What type of project is this? Data Transformation, Reporting, etc. 
- Effort Value – How complex is this project based off the initial request. 
- Priority Value – How high a priority is this project based off the initial request. 
- Origin Library – Which library is requesting this project. 
- System – What systems will be used in this project? Alma, ArchivesSpace, or Other. 

[See Documentation Policy for more information.](../policies/servicenow_documentation_policy.md)

Upon assignment, the assigned Specialist should contact the requester through the ticketing system to acknowledge receipt of the request and confirm that work is being evaluated. This helps ensure Requesters know their ticket has not been overlooked. 

Assigned Specialists should be assigned on the RITM and TASK tickets as soon as they have accepted the ticket. This prevents e-mails from being sent to everyone any time an update is made to the ticket, keeps the new tickets category clean, and preserves valuable metrics. 

### Add Ticket to Visual Task Board 
1. Find the RITM of the new Request and select the checkbox next to it. 
2. In the top right, select the ‘Actions on selected rows’ drop-down menu. 
3. Select ‘Add to Visual Task Board’ from the drop-down menu. 
4. On the ‘All Boards’ tab, select ‘SCMS Tickets’ board. 
5. The ticket will appear in the ‘Not yet prioritized’ lane in the Task Board. 
6. Open the Task board and click on the ticket’s card. 
7. In the right panel of the card, select the ‘Labels’ tab. 
8. Add the appropriate labels mentioned above. 

### Assigning the Ticket 
1. Open the RITM. 
2. To Assign the entire ticket, click on the magnifying glass next to the ‘Assigned to’ field to locate the assignee’s NetID and select it. 
3. Next, assign the TASK as well. Scroll down to the bottom of the ticket where the ‘Catalog Tasks’ tab is located and click on the TASK you wish to assign. Click on the magnifying glass next to the ‘Assigned to’ field to locate the assignee’s NetID and select it. 
4. To break an RITM into multiple TASKs to assign different parts to specialists, scroll to the bottom of the ticket where the ‘Catalog Tasks’ tab is located. Click on the ‘New’ button to add a new task. Enter a description of what that individual task will entail. Create as many TASKs as needed. 
5. In the Visual Task Board, drag the ticket’s card into the appropriate Specialist lane. 
6. Click on the card, in the right panel select the ‘Assignee’ tab. 
7. Ensure the Specialist is assigned on the Task Board task as well as the actual RITM and TASK. 

[See ServiceNow Tickets for more information.](./servicenow_tickets.md)

## 2. Request Confirmation 
Before beginning work, the assigned Specialist should review the request and restate their understanding of the request within the ticket. 

The confirmation should include: 
- The Specialist's understanding of the request 
- Any assumptions being made 
- Any questions or areas requiring clarification 

Requesters should be given an opportunity to confirm the requirements or correct any misunderstandings before significant work begins. 

If the Requester has selected the option to meet before work begins, the Specialist should send a meeting invite to discuss the project. 

Send a meeting invite with:  
- Purpose: confirm scope/requirements   
- Prep requested: any files/access/record examples they can bring 

## 3. Investigation and Planning 
The assigned Specialist should evaluate the request and determine: 
- Scope of work 
- Required resources or dependencies 
- Estimated timeline 
- Any additional information needed from the requester 

Use this information to set or update the priority and effort values. 

Expected timelines should be communicated to the Requester as early as possible. 

“Based on the current scope, I estimate this project will take approximately [timeline]. If anything changes, I’ll update you immediately.” 
 
Note: Be generous with your timeline. Requesters will be pleased if a project is completed earlier than expected. If you are unsure how long it will take to complete the project, break the project into smaller parts and let them know how long you expect the part you are working on to take. 

## 4. Work Documentation and Communication 
Specialists should provide updates throughout the lifecycle of the request, particularly when: 
- Significant work has been completed 
- Timelines change 
- Additional information is required 
- Issues or blocks are encountered 

If discussions occur outside of the ticketing system (e.g., email, meetings, Teams messages, phone calls), a summary or copy of the relevant information should be added to the ticket work notes.  
- Date of communication and who participated 
- Summary of discussion 
- Any files or links referenced 

The ticket should serve as the authoritative record of decisions, requirements, and project history.  

[See ServiceNow Tickets for more information.](./servicenow_tickets.md)

## 5. Completion and Review 
Upon completion of the requested work, the specialist should: 
- Describe the work that was completed 
- Communicate any limitations, follow-up actions, or known issues 
- Provide a csv of updated records where applicable for the Requester to review 
- Ask the Requester to confirm that the request has been satisfactorily resolved 
 
Whenever practical, Requesters should be given an opportunity to review the completed work before the ticket is closed. Providing a list of updated records and how they were updated brings visibility to the Specialist’s work and keeps a record of what was covered in the project. 

## 6. Ticket Closure 
Once the requester has confirmed that the request has been completed, or after a reasonable period without further feedback (two weeks or more), the specialist may close the ticket. 
1. If there is no response after two weeks, comment with the following:  
    - “Closing this ticket as Completed after [2 weeks] without a response. If anything else is needed, please submit a new request.” 
2. Select the TASK at the bottom of the ticket 
3. Ensure the TASK is assigned to you then select ‘Closed Complete’ as the status 
4. Save and the entire Ticket will be closed unless there are other open TASKs 
5. In the Visual Task Board, move the card to the Completed lane. 

Specialists should ensure that all tickets are closed once they have received confirmation that the ticket has been completed. This keeps ticket categories clean and preserves valuable metrics. 

[See ServiceNow Tickets for more information.](./servicenow_tickets.md)

## 7. Project Documentation 
Upon completion, project documentation should be added to the appropriate GitHub repository when applicable. Simple tasks such as adding permissions do not require documentation, but anything requiring a script should be included. 

Documentation may include: 
- Scripts and code 
- Background information 
- Problem statements and Goals 
- Process Taken 
- Who was communicated with 
- Dates of testing and execution 
- The results of the project 

Documentation should be sufficient to allow future staff to understand, maintain, or reproduce the work. 

[See Documentation Policy for more information.](../policies/servicenow_documentation_policy.md) 

## 8. Ticket Tagging 
Upon completion of the ticket, add appropriate Tags to the RITM. Many of these tags can be copied from the tags given to the ticket on the Visual Task Board but should be updated to reflect the details of the project upon completion. For example, if a project was initially considered a low effort project but became complex over time, the tag on the ticket will be different from the tags on the card. 

The tags included should be: 
- Request Type – Migration, Transformation, Reporting, etc. 
- Effort Value – How complex was this project. 
- Priority Value – How high a priority was this project. 
- Origin Library – Which library requested this project. 
- System – What systems were used in this project? Alma, ArchivesSpace, or Other. 

To add tags to the RITM: 
1. Find the RITM of the new Request and open it. 
2. On the top right of the ticket, select the ‘...’ 
3. Select the ‘Add Tag’ option in the menu. 
4. Enter the appropriate tags. 

[See Documentation Policy for more information.](../policies/servicenow_documentation_policy.md)