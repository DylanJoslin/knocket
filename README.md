# Indigenous Storytelling
 
 ## Apps
 
 ### storytelling_prototype
 This is the base that the website is built off of. the urls.py file here links to many of the other apps. This also stores the settings.py file that needs to be updated when new apps are created
 
 ### home
 The home app renders the map on the home page. It also includes the pages for resources, about, and events. The base.html template is also stored here, which most other pages will keep as part of their framework.
 
 ### users
 The users app handles the creation of new profiles. This is where students will go to register and log in. This also has to profile template where students will be able to view posts they have made and manage them. By default, students do not have permission to upload or view content, they must be approved by a teacher first.
 
 ### stories
 **This hasn't been built yet**. This will be where students are sent when they follow the map to view videos from their peers. 
 
 ### administration
 **This hasn't been built yet** This will be where teachers and admins can change the access level of students so that they can begin viewing and posting content. 
 
 
 ## Django, Useful Functions
 - python manage.py runserver
   - Launches the local server, which is run on localhost:8000 in your browser
 - python manage.py startapp <app_name> 
   - Creates a new app in the project, such as users and home
 - python manage.py makemigrations AND python manage.py migrate
   - Needs to be run after creating a new app or model. I think this updates the database. 

