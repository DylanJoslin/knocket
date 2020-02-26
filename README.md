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

 ### static folder
 This folder stores all of the static content such as images and css. Keep your files here, and in a django template you have to do two things to load them:
 1. Include `{% load static %}` at the top of your html file
 2. Call the file by using the format `{% static 'type/file.type' %}`. For example, for loading css you would write `href="{% static 'css/styles.css' %}"`.

 ## Creating a Virtual Environment
 You wont be able to run any django functions without installing it into a virtual environment. There are a few steps involved in that:
 1. Install pip on your machine by opening terminal and entering  `sudo easy_install pip`.
 1. Install virtualenv on your machine by running `sudo /usr/bin/easy_install virtualenv`
 1. Create a folder that will hold your django environment called 'Environments'
 1. In terminal, navigate to the 'Environments' folder you created, and run `virtualenv django`
 1. To start your virtual environment, run `source django/bin/activate`
    - You can tell it is working when you see (django) above your command line
 1. Several packages will need to  be installed. Run these commands to install them:
    - `pip install numpy`
    - `pip install pytz`
    - `pip install Pillow`
    - `pip install django`
  1. Now, to start running your server and using django, in terminal navigate to the project folder (which is probably in your github directory if you downloaded the project from Dylan's github). Once inside if you type the command `ls` you should see all of the files in the project, including manage.py. 
  1. In terminal run the command `python manage.py runserver` and you should be able to go to localhost:8000 in your browser to view the website.
  In the future, when you want to run the server again you will need to be in your virtualenv first. Follow step 5 again to achieve this.
 
 
 ## Django, Useful Functions
 - `python manage.py runserver`
   - Launches the local server, which is run on localhost:8000 in your browser
 - `python manage.py startapp <app_name> `
   - Creates a new app in the project, such as users and home
 - `python manage.py makemigrations` AND `python manage.py migrate`
   - Needs to be run after creating a new app or model. I think this updates the database. 

## Final Notes
If you're working on Django templates, you'll have to install the Django Templates plugin in VS Code. When you do, you lose html snippets in Django Templates, which is annoying. You can get them back by pressing cmd+shift+p on mac, or ctr+shift+p on windows, and type settings. Open the settins JSON file, and add this bit to it to get the snippets back: 
`"emmet.includeLanguages": {
        "django-html": "html"
    }
`

It's possible you might need to install some extra plugins into your virtual environment. If that's the case and you need help, just text Tristan

## Working with SASS/SCSS

To start working with SASS in this project you'll need to do two things:
1. Download the live sass compiler through visual studio code.
2. Go to your settings: cmd+shift+p on mac, or ctr+shift+p then search "open settings" and enter. This should open a settings.json file. Add the piece of code below to that settings.json file.

`
"liveSassCompile.settings.formats": [
        {
          "format": "expanded",
          "extensionName": ".css",
          "savePath": "~/../css"
        }
      ],
`

This ensures that SASS is compiling the css in the right directory.