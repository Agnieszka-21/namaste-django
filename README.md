# Namaste Yoga Studio

## Introduction

Namaste Yoga Studio is a web application for a fictional yoga studio in Dublin offering group classes in various styles of yoga. Any user can access the most important information about the studio - its location, opening hours, weekly class schedule, as well as a detailed description of each class which includes a teacher's bio, characteristics of the yoga style taught in the class, and who it is suitable for. Users interested in reserving their spot in a class can sign up in order to create an account, and after logging in they are able to book any classes. They can also see their upcoming booked classes, update or cancel their bookings, as well as update their personal profile by adding/changing/removing a profile picture, their date of birth, and information on recent or chronic injuries.

This is the fourth Portfolio Project for the Code Institute's Diploma Course in Full Stack Software Development (E-commerce Applications). The application is built in Django using Python, HTML, CSS, and JavaScript. It provides role-based permissions for users to interact with data in a PostgreSQL database. It includes user authentication, email validation, and CRUD functionality for User Profiles and Bookings.

![Screenshot of the application on multiple devices](add link)

## Table of Contents

...
Add table of contents

## UX

### The Strategy Plane

General description...

#### The Site's Ideal User
- Adults who want to attend in-studio yoga classes, whether they are new to yoga or a seasoned practicioner
- Adults who are interested in trying yoga for the first time, whether it's to de-stress, improve their mobility and flexibility, or as a workout routine
- Elderly people who are looking for gentle full-body workouts
- Expectant mothers and new mothers who want to be healthier

#### Site Goals
- To inform users about the studio's offerings, class schedule and different styles of yoga
- To provide an easy way for users to book a class up to 4 weeks in advance so that they can plan ahead and ensure their spot in a class where the number of participants is limited
- To give users the possibility of cancelling their booking or changing the date of their booked class easily and quickly
- To provide users with the opportunity to create a personal profile and share information on their chronic or recent injuries (if applicable), so that yoga teachers at the studio can deliver classes that satisfy clients

#### Epics
...

#### User Stories


### The Scope Plane

**Features planned include:**
- ...
  

### The Structure Plane

#### User Story ...
...

#### Acceptance Criteria
...

#### Implementation
...

#### User Story...
...
#### Acceptance Criteria
...


#### Opportunities arising from User Stories

#### Implementation
...


### The Skeleton Plane

#### Wireframe mock-ups
...

#### Database schema
...



### The Surface Plane

#### Design
...

#### Typography
...

#### Images
...

## Features
...


## Future Enhancements

...
- More stories could be added as further instances of the class Story to provide a wider range of topics and to keep users entertained for longer, also encouraging them to return to the application multiple times.



## Testing

### Testing Overview

...
Continuous testing was an integral part of the development process. I used numerous print statements, which were removed as specific features reached their desired shape and functionality. The statements helped me understand which exact details were accessed via API in the online dictionary, how my functions influenced one another, and what information I had to gather in order to print clear messages for the user. Testing multiple word inputs, as well as the behavior of the application in response to them was an important step in the development of a refined and reliable input validation process. While there is still potential for further enhancements, I ensured to handle any and all errors that I encountered, and took great care to handle various word inputs in a way that prevents mistakes as much as possible, at the same time allowing for a lot of variety without restricting the user in their choice of word inputs. Tests were conducted mainly in my development environment, and once results were positive, they were re-checked within the live application after it was deployed to Heroku.

### Manual Testing

While testing every single functionality as I was creating and refining it was essential to progressing with this project, I also applied a more structured approach to testing once everything seemed to work correctly in order to double-check the code's behavior and ensure that I handled any possible scenarios to avoid any issues. The table below documents this more structured approach, where I tested any and all possible functionalities as well as likely user inputs in [the live version of the app](link...).


| Functionality being tested | Expected Outcome | Actual Outcome | Result (pass/fail) |
| :------------------- | :--------------- | :------------- | :-------------------- |



### Validator Testing

...
I utilized the Code Institute's [Python Linter](https://pep8ci.herokuapp.com/) in order to check my Python files. No errors were reported - screenshots are linked here:
- [run.py](https://github.com/Agnieszka-21/madlibs/blob/main/assets/screenshots/mad_runpy_validator.png)
- [adj_list_ly_ending.py](https://github.com/Agnieszka-21/madlibs/blob/main/assets/screenshots/mad_adj_with_ly_validator.png)

### Notable Bugs

...


## Technologies Used

### Python 
...

#### os
...

#### sys
...

#### ...
...

#### ...
...

#### requests
...
This module (specifically the requests.get functionality) makes it possible to work with the dictionary API in the word input validation process by allowing to send HTTP requests to a specified URL...

### Django

### Heroku

### PostgreSQL

### JavaScript

### Bootstrap (version...)

### Font Awesome

### CSS

### Jinja/Django templating language

### HTML


### Packages Used

### Resources Used


## Deployment

The application has been deployed via Heroku.

This program was developed using a [template from the Code Institute](https://github.com/Code-Institute-Org/p3-template)...

In order to deploy the application to Heroku I followed the following steps:
- Sign up or log in to Heroku.
- On the main Heroku dashboard page select "Create new app".
- Give the project a unique name (mad-libs-grammar), select a suitable region, and click "Create app". This will create the app in Heroku and bring you to the Deploy tab.
- Switch to the Settings tab. 
- In the "Config Vars" section click the "reveal config vars" button.
- In the KEY input field enter "PORT" (all capitals), in the VALUE field next to it enter "8000", and then click the "Add" button to the right. This config var is required because we are using the Code Institute's template.
- Add one more config var, with the KEY "API_KEY_SERVICE" and the VALUE that is the API key used to access the dictionary. Click "Add".
- In the section "Buildpacks" click the "Add buildpack" button and select "python". Confirm by clicking the button "Add buildpack". Then click the button "Add buildpack" once again and select "nodejs". Confirm ("Add buildpack").
-  The order of these buildpacks is important. If you added nodejs before python, you can easily rearrange this with a drag-and-drop.
-  Scroll up to the top of the page and switch to the Deploy tab. 
-  In the "Deployment Method" section choose the "GitHub" button. Follow the next steps (if any) as prompted to connect your GitHub account. In the "Connect to GitHub" section that appears, choose your account, enter the name of your repository, and select "Search".
-  Once your GitHub repo is connected to the Heroku app, scroll down to the section "Automatic deploys".
-  Confirm that the correct branch of the repo is selected in the drop-down box, and select "Enable Automatic Deploys". Whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app.
-  Alternatively, you can use the option "Manual deploys" (for this projects, I used the "automatic deploys" option that allowed me to see changes I made to the app as I developed it).
-  Heroku will now build the app for you. Once the process is completed, you will see the message "Your app was successfully deployed", and a link to the app where you can visit the live site.
  

## Cloning and forking the repository

...
In order to clone the GitHub repository use the following link:
- [link](link)

In order to fork the GitHub repository:
- Go to [link](link)
- In the top menu choose the option "Fork"


## Credits

The following tutorials, articles, documentation and media were used to create this web application.

### Code

...
- The function clear_terminal is based on the code from an article on the forum [geeksforgeeks.org](https://www.geeksforgeeks.org/clear-screen-python/). Link included also in the run.py file.


### Content

...
- [Yoga Dublin's website](https://www.yogadublin.com/) was an inspiration to build a functional, aesthetically pleasing webpage that could be used by a real-world yoga studio. Descriptions of yoga styles as well as teachers' bios were copied from the Yoga Dublin's website and adapted for the needs of this projects (e.g. shortened, paraphrased, and any names have been changed)
- Images...


## Acknowledgements

I would like to express my sincere gratitude to my mentor, Matt Bodden, whose suggestions and practical advice have been invaluable. I am also grateful for the help of the team of tutors who supported me when I felt stuck and whose insights and tips ensured I could progress with the project.
