# Meatless Munchies - Introduction

**Meatless Munchies** food delivery website is developed using Django Framework as the final project for the Code Institute Bootcamp.

> It is a takeaway places that specialises in **meat-free comfort/junk food**. Customer users can see images and descriptions of the food in the menu page, search through the items and order on the application. The customer side is streamlined and intuitive to navigate for people to order easily even after a night on the town. They are able to chose whether to pay via the paypal api or at the door when their food arrives. Staff users haveto log in and can see the total revenue and orders completed for the day as well as any undelivered orders and mark them as delivered.

You can view the live site here:- `IMPLEMENT THIS`

![mockup ~~~image of the website homepage on pc laptop phone and tablet~~~](assets/mockup.jpg)

----

## [Content](#content)
- [Meatless Munchies - Introduction](#Meatless-Munchies---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [Site Aims](#site-aims)
    - [Agile Methodology](#agile-methodology)
      - [Epics and User Stories](#epics-and-user-stories)
      - [Tasks](#tasks)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
      - [Navbar](#navbar)
      - [Hero Image](#hero-image)
      - [Destination Section](#destination-section)
      - [Footer](#footer)
    - [User Page](#user-page)
    - [About Page](#about-page)
    - [Blog Page](#blog-page)
      - [Blog Details](#blog-details)
      - [Blog Comments](#blog-comments)
    - [Register](#register)
    - [Login](#login)
    - [Logout](#logout)
    - [Destinations](#destinations)
    - [Search Button](#search-button)
    - [Alert Messages](#alert-messages)      
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Testing](#testing)
      - [Validation](#validation)
      - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfix Bugs](#unfix-bugs)
  - [Deployment](#deployment)
      - [Creating the Django project](#creating-the-django-project)
      - [Creating Heroku app](#creating-heroku-app)
      - [Set up Environment Variables](#set-up-environment-variables)
      - [Heroku deployment](#heroku-deployment)
      - [Final Deployment](#final-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Acknowledgement](#acknowledgement)

-----

# User Experience - UX

## Site Aims
* Meatless Munchies aims to provide a hearty and delicious late night takeaway food for vegetarians and vegans quickly and efficiently.
* The site should be easy to navigate for tired or intoxicated people.
* This site also aims to provide users with visually pleasing images and mouthwatering descriptions of the food.
* Meatless Munchies aims to fill a gap in the market of comfort food aimed at vegetarian and vegan people.
* Staff users are able to see the orders placed and mark them as delivered and delete orders.
* Customer users can place orders.
* Superusers can create orders, read the data, update if the orders have been paid for and delete orders.

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and Trello. Through the use of the Kanban board in Trello, the project was divided into a few different sections: 

* To Do - All the tasks were initially entered in the 'To Do' column.
* In Progress - During development they were moved into the 'In Progress' column to help focus on tasks in a planned order.
* Done - They were then moved into 'Done' once the development on them was complete. this gave a list reference to know if additions made werent considered in the beginning or were implemented wrongly.
* Testing- These held the testing protocols that were added as the project went along.

Please find my Kanban Board with my user stories

<img src="assets/kanban.PNG" width="500" height="300" alt="Kanban board">

## Epics and User Stories

Following Epics were created which were further developed into several User Stories.

### Epic 1- Website UI
Epic Goals for User- 
* A streamlined User Interface to get to the food and order with minimal hurdles.
* Obvious categories and "top picks of the week" to prevent too many decisions impeding orders.
* Easily know the site sells vegetarian and vegan food.
* Toggle buttons between veganism and vegetarianism and obvious indication of which items are which.
* Search bar for menu items.

#### Related User Stories:
* As a site user I can easily order food even when I am drunk or tired.
* As a site user I can see specific dishes that look tasty so I dont have to look at every dish to make a decision.
* As a site user I can know immediately that I am on the correct site and it is for vegans aswell as vegetarians.
* As a site user I can chose to only see vegan options if I cannot eat non-vegan options.
* As a site user I can use a search bar to search for a specific meal if I already know what I want.

### Epic 2- Staff usability
Epic Goals-
* Easy sign in page for the staff members
* No option for non-staff members to access the backend
* Upon signing in, the staff can see the dashboard with total revenue for the day and number of orders recieved
* Easy access to Update the delivered status of orders
* Removal, from the dashboard, of delivered orders to not clog up the site 

#### Related User Stories:
* As a staff user, I can login to see the orders dashbaord.
* As a site owner, I can prevent the general public from accessing to the dashboard.
* As a staff user, I can find the dashboard intuitively and select through the current orders.
* As a staff user, I can change the data on if the order is delivered.
* As a staff user, I want a clear and informative page that contains all the things I could want to know while working in a busy kitchen.

### Epic 3- Food menu Management
Epic Goals-
* Create/ Update / Read / Delete selected menu items as they come in and out of season.
* View them in the menu and make sure they look delicious.
* Approve and publish nutritional information.

#### Related User Stories:
* As a site owner, I can create planned food drafts so that they can be published on the launch of a new menu day.
* As a site owner, I have complete control over what foods are on the menu.
* As a site owner, I can add nutritional infromation and alergy notices.

## Tasks

The website development process closely followed CI's Django module "I Think Therefore I Blog". The Legion Scripts YouTube series "Building a Food Delivery Web App With Django and Python 3" also outlined some of the key tasks for projects similar to this one.

**Before Project Inception**

- Design ERD and Data 
- Create Repository in GitHub
- Create Project, Epics, User Stories and prepare Kanban Board

**Creation of Project in GitPod**

- Create the Django project. Check details in [deployment-section](#deployment)
- Create the "cafcafproj" Django project
- Create the "custapp" Django application
- Create the "cafapp" Django application
- Deploying app to Heroku - Details in [deployment](#deployment) section
- Create Database Models
	- Set up models.py file in "custapp" directory
- Create the "custapp" views
 - Index, About, Order
- Set up Templates
	- Create base.html, navigation.html, (Navbar) and footer.html (Footer) content, which gets extended to all the other template files
- Created "custapp" Database Models
  - Including menu item, order and category models
- Set up order, orderconfirmation and orderpayconfirmation templates
  - Adding things like modals in to allow the user to double check what they ordered
- Added views for Orderconfirmation and Orderpay
- Added PayPal API into website
- Install Allauth for sign in, sign up and sign out templates with-  pip3 install django-allauth 
- Implement no new staff users
- Implement bootstrap templates for login and logout pages	
  - Install crispy-forms to add styles to Django account templates with-  pip3 install crispy-bootstrap5
- Create views for "cafapp" (staff side)
  - Dashboard and OrderDetails
- Create templates for "cafapp"
  - Create order_details html and dashboard html
- Added template for menu view for "custapp" including a search feature
- Intensive Manual Testing and Validation checks of each page and codes written
- Final Deployment steps

-----

[Back to top](#content)

## Design

### Colours

Vegetarian and Vegan foods and events seem to have a very consistent theme of green with darkish brown. This is something I want to replicate as it gives the site a consistent and familiar feel. Hopefully instilling confidence in the user that food is cooked by people that love veggie and vegan food.

![Color Palette](assets/colour_scheme.png)


### Imagery

All the imagery is related to or pictures of meat-free food. Ideally making the users mouths water and intice them into ordering food.

### Wireframes

The wireframes for this projected were generated using Figma. 

<img src="assets/index.PNG" width="500" height="300" alt="Home page">
<img src="assets/About.PNG" width="500" height="300" alt="Information on the company">
<img src="assets/menu.PNG" width="500" height="300" alt="Place to view whats on the menu with search bar">
<img src="assets/order.PNG" width="500" height="300" alt="Where to place the orders and input the address">
<img src="assets/checkout.PNG" width="500" height="300" alt="portal to webpage api">
<img src="assets/dashboard.PNG" width="500" height="300" alt="staff side dashboard">

----

## Database Diagram

Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities Post, Author, Destination and Comment are shown in this diagram.

<img src="assets/DB.PNG" width="500" height="300" alt="ER Diagram">

[Back to top ⇧](#content)

----

# Features

## Home Page

The first impression of the site will be clean and professional with the hero image in the background suggesting food is the center of the operation. It has a card positioned at the center of the screen with a large centralised order button. For first time users there are few choices to be made to get to where they will probably want to go.

![Homepage](assets/features/home-page.jpg)

## Navbar

To keep a consistent site structure the nav bar is at the top of every page. This is the main way to navigate to parallel sections of the site as the main usage of the site will be linear. This declutters the options the user is faced with but still maintains the ease of access which is so crucial to the site.
The nav bar is collapsed on mobile and explicit on larger devices.

![Navbar](assets/features/navbar.jpg)

![Navbar](assets/features/nav-hamburger.jpg)

## Footer

The footer displays the copyright and a subtle login link for staff members. This is out of the way for most customers but still easily accessible for staff members.

![Navbar](assets/features/footer.jpg)

----

## About Page

Since the customer base is very ethical and choice conscious, it is very important to have an about section that explains who we are and what we aim to do. Additionally having this information there can instill confidence in the customers. While this page will often not be accessed by every user it is still crucial to display this information oepnly.

![About Us](assets/features/about-us-page1.jpg)

----

## Menu Page

If someone is wanting to try a new food this menu page is there to display everything offered and has a search bar to find what you're looking for quickly. Additionally this page will have allergy information and the main ingredients list for more niche denominations like lacto-ovo-vegetarians to decide whether they can eat it or not.

### Search Bar

To allow for fast search or searching for products related to other products.

![Menu](assets/features/menu.jpeg)

## Order Page

The order page displays the food in a linear fashion so that customers can decide which products they do or dont want with the address form at the bottom. This streamlines the ordering process so they can get their order sent quickly and hastle free.

## Checkout Page

This is where the paypal api button sits and shows an overview of the order including the food ordered and the total incase anything has been added or missed off by mistake. Again it is a very clean design to not distract from the utility of the website.

![No post message](assets/features/no-destination-post.jpg)

----

## Superuser

The superusers can log in through the staff portal (seen below) and can create, read, update and delete all of the orders and menu items.

[here](assets/features/admin-panel-post-model.jpg)

### Admin 'MenuItem' Model Management

On creating a new MenuItem the superuser can add a name, description, price, photo and category. This is then rendered on the menu and order page the next time it is loaded.

The admin site for post model appears as shown [here](assets/features/admin-panel-post-model.jpg).

### Admin 'Order' Model Management

Orders are generated by the user and saved down. They can be generated by the admin but in most use cases this is not what happens. The user submitting an order records what items they want and inputs their address. Automatically, the price is generated and the is-paid and is-delivered are set to false. The is-delivered can be changed by staff members via the dashboard when the order has been sent off.

The admin site for comment model appears as shown [here](assets/features/admin-panel-comment-model.jpg).

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt
* [JavaScript](https://www.javascript.org/)- To link up add the paypal api button.

### Django Packages

* [Gunicorn](https://gunicorn.org/)- As the server for Heroku. `please edit this`
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.

### Frameworks - Libraries - Programs Used

* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [Heroku](https://id.heroku.com)- Used to deploy the live project.
* [PostgreSQL](https://www.postgresql.org/)- Database used through heroku.
* [Figma](https://www.figma.com/)- To build the wireframes for the project.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.
* [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
* [Visual Studio Code](https://code.visualstudio.com/)- As a text editor.
-----

[Back to top ⇧](#content)

## Testing

### Validation

I used the following validation tools to validate HTML, CSS, PYTHON codes. Validation results below:  
- HTML using [W3C HTML validator](https://validator.w3.org/)
- CSS using [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
- Python via [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)

### Manual Testing

Testing has taken place continuously throughout the development of the project. With each feature being added then checked to be working before moving on. 
- Youtube videos [The Dumbfounds](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) for automated testing.

----

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| In navbar, the menu burger button did not appear | pls fix this jack :) |
| My images were not loading | I realised this was a mistake in the file paths and corrected it |
| Staff group didnt exist and I thought the allauth staff was this group | Created group through the admin panel |

## Future Implementation

* Undo button for is-delivered 
* A way to order multiple of one item

[Back to top ⇧](#content)


## Deployment

### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project:`django-admin startproject project_name .`.
* Create app: `python manage.py startapp app_name`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!

### 2. Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`(note: this must be either removed or set to 0 for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py
* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku, click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: 
```ALLOWED_HOSTS = ['<Heroku_app_name>.herokuapp.com', 'localhost']```
* Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Commit and push the code to the GitHub Repository.

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

### 6. Final Deployment
In the IDE:
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

----

[Back to top](#content)

# Credits

## Code

I followed the videos for Legion Script's how to build a food delivery app. 
I also supplemented my understanding with "Coding with Mosh"
The CI videos were not useful due to lack of explanation.


## Learning Resources

Youtube videos by [Legion Script](https://www.youtube.com/@LegionScript)
[W3CSchool](https://www.w3schools.com/django/)
Bootstrap documentation [Bootstrap](https://getbootstrap.com/docs/4.3/components/navbar/)
[Django Documentation](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)(For different quaries while doing project. For example query about models, fields, form widgets, auth and many more)
Youtube videos [The Dumbfounds](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) for automated testing.

## Content and Media

Images were taken from Pexels and Canva

## Acknowledgement

Special thanks to Rosemary Jones and Richey Malhotra for the emotional support along this horrible fucking readme. `Emotional Damage`

[Back to top](<#content>)
   
