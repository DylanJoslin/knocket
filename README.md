# Indigenous Storytelling
Welcome to our official git repo for our project! If you're working on a specific section of the website, please create a new branch of the project before making any changes, that way we don't change the master file before we're sure that we're happy with our changes. 
 
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

 ## static folder
 This folder stores all of the static content such as images and css. Keep your files here, and in a django template you have to do two things to load them:
 1. Include `{% load static %}` at the top of your html file
 2. Call the file by using the format `{% static 'type/file.type' %}`. For example, for loading css you would write `href="{% static 'css/styles.css' %}"`.
 
 
 ## Django, Useful Functions
 - python manage.py runserver
   - Launches the local server, which is run on localhost:8000 in your browser
 - python manage.py startapp <app_name> 
   - Creates a new app in the project, such as users and home
 - python manage.py makemigrations AND python manage.py migrate
   - Needs to be run after creating a new app or model. I think this updates the database. 

## Final Notes
If you're working on Django templates, you'll have to install the Django Templates plugin in VS Code. When you do, you lose html snippets in Django Templates, which is annoying. You can get them back by pressing cmd+shift+p on mac, or ctr+shift+p on windows, and type settings. Open the settins JSON file, and add this bit to it to get the snippets back: 
`"emmet.includeLanguages": {
        "django-html": "html"
    }
`

It's possible you might need to install some extra plugins into your virtual environment. If that's the case and you need help, just text Tristan

