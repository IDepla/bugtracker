# Rationale.

The application is a bug tracker with an api. 

Strategy draft:

- User journey: the landing page is a 'login page', from login the user is transfered in the 'list of open bugs'. In this page, the user can create a new bug (which will be automatically open), execute some actions such as assign bugs, close bugs, access the API page, access  the bug (detail) page, access the user (detail) page. In the deails page the user will be able to modify fields, or other actions, such as assigning people to bugs (in the 'bug detail' page).

- The system entities are two, user and bug. User can extend the authentication account, so we reuse a part of the django infra. It is not specified what the users will use to authenticate, the design choice is by email. We drop all the management actions: change password and so on. We remain with create account through the admin site, and from client side a basic account management: login, modify some fields, change password.

- the bug entity has a few fields: the states implemented are 'Open' and 'Closed'; it is linked to the user representing these actions: creation, closing, assignment. While creation and closing are done by a single user, assignment could be to more than one. That summarizes in two foreign keys and one many to many.

- you can use the admin site to add new accounts, it removes the bother to validate and test emails/accounts. Only the administrator can add accounts.

- the system exposes an API. We can exploit the API to deliver the actions, so the system on deployment could be composed by: API server, WEB server, web server static content. The three webservers can be meshed using a proxy and routing by path. On development these parts can be served directly from one server.  

- databases: the system actions are simple, any db would be ok. Option is to use sqlite for development and move to postgres for deployment. Given the expected actions, there is no incompatibility.

- containers: two environment, development and deployment. development could also be dropped and just use localhost and sqlite. I'm working alone and I'm not planning to have other developers.

- testing plan: 
we drop the structural testing for the front-end, that's kept as a technical debt. 
The testing necessary includes a test for each operation on the models.



- get the application working,  
- containerize
- split

