# Namaste Yoga Studio


## Introduction

Namaste Yoga Studio is a web application for a fictional yoga studio in Dublin. Anyone can access information regarding opening hours, the studio's location, class schedule, a detailed description of each class as well as each teacher's bio. Moreover, users interested in taking classes at the studio can sign up for an accout that allows them to book classes, manage their bookings (update and cancel), and also manage their user profile.

This is the fourth Portfolio Project for the Code Institute's Diploma Course in Full Stack Software Development (E-commerce Applications). The application is built in Django using Python, HTML, CSS, and JavaScript. It provides role-based permissions for users to interact with data in a PostgreSQL database. It includes user authentication, email validation, and CRUD functionality for User Profiles and Bookings.

[View the live website here](https://namaste-yoga-studio-d494d1aeeada.herokuapp.com/)

![Screenshot of the application on multiple devices](add link)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.


## Table of Contents

...
Add table of contents


## UX

### The Strategy Plane

Namaste Yoga Studio is a web application for a fictional yoga studio in Dublin offering group classes in various styles of yoga. Any user can access the most important information about the studio - its location, opening hours, weekly class schedule, as well as a detailed description of each class which includes a teacher's bio, characteristics of the yoga style taught in the class, and who it is suitable for. Users interested in reserving their spot in a class can sign up in order to create an account, and after logging in they are able to book any classes. They can also see their upcoming booked classes, update or cancel their bookings, as well as update their personal profile by adding/changing/removing a profile picture, their date of birth, and information on recent or chronic injuries.

#### The Site's Ideal User
- People who want to attend in-studio yoga classes, whether they are new to yoga or a seasoned practicioner
- People who are interested in trying yoga for the first time, whether it's to de-stress, improve their mobility and flexibility, or as a workout routine
- Elderly people who are looking for gentle full-body workouts
- Expectant mothers and new mothers who want to be healthier

#### Site Goals
- To inform users about the studio's offerings, class schedule and different styles of yoga
- To provide an easy way for users to book a class up to 4 weeks in advance so that they can plan ahead and ensure their spot in a class where the number of participants is limited
- To give users the possibility of cancelling their booking or changing the date of their booked class easily and quickly
- To provide users with the opportunity to create a personal profile and share information on their chronic or recent injuries (if applicable), so that yoga teachers at the studio can deliver classes that satisfy clients

#### Iterations (GitHub Milestones)
Since the project was created using the Agile approach, both planning and prioritizing accordingly was essential.

The work on this project has been divided into 3 iterations, each lasting 3 weeks. This made the entire process easier to manage and helped track progress as well as decide on the priorities at each stage.

- Iteration 1 - ended on Aug 25, 2024
- Iteration 2 - ended on Sept 15, 2024
- Iteration 3 - ended on Oct 6, 2024

You can see the iterations with their details, including User Stories that were finished in each iteration, [here](https://github.com/Agnieszka-21/namaste-django/milestones).

#### Epics

This project is based on the following 9 epics:
- [#34 Set up Django and Deploy Early](https://github.com/Agnieszka-21/namaste-django/issues/34)
- [#1 View the Class Schedule and Relevant Details on the Website](https://github.com/Agnieszka-21/namaste-django/issues/1)
- [#31 Create and Maintain a User Account](https://github.com/Agnieszka-21/namaste-django/issues/31)
- [#38 Create and Manage a Class Schedule](https://github.com/Agnieszka-21/namaste-django/issues/38)
- [#32 Book Classes, View and Manage Bookings](https://github.com/Agnieszka-21/namaste-django/issues/32)
- [#39 Inform, Ask, and Listen to the Clients](https://github.com/Agnieszka-21/namaste-django/issues/39)
- [#20 Create, Manage, and Delete Staff Accounts](https://github.com/Agnieszka-21/namaste-django/issues/20)
- [#15 Use a Staff Account to Teach with Ease and Clarity](https://github.com/Agnieszka-21/namaste-django/issues/15)
- [#47 Ensure the Code is Ready for Production](https://github.com/Agnieszka-21/namaste-django/issues/47)

These epics were split into User Stories to help manage the work on this project. All these and more details can be found in the project's [kanban board](https://github.com/users/Agnieszka-21/projects/2/views/1?sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Labels).

#### User Stories

Here are the User Stories resulting from the 9 epics

1. Set up Django and Deploy Early
- [#35 Install Django and supporting libraries](https://github.com/Agnieszka-21/namaste-django/issues/35)
- [#36 Secure sensitive data - API keys and secret keys](https://github.com/Agnieszka-21/namaste-django/issues/36)
- [#37 Deploy the project to Heroku](https://github.com/Agnieszka-21/namaste-django/issues/37)

2. View the Class Schedule and Relevant Details on the Website
- [#2 View class schedule](https://github.com/Agnieszka-21/namaste-django/issues/2)
- [#3 View a specific class in detail](https://github.com/Agnieszka-21/namaste-django/issues/3)
- [#4 View teacher's bio](https://github.com/Agnieszka-21/namaste-django/issues/4)
- [#30 View the studio's location(s)](https://github.com/Agnieszka-21/namaste-django/issues/30)
- [#42 View the studio's opening hours](https://github.com/Agnieszka-21/namaste-django/issues/42)
- [#43 View the studio's social media accounts](https://github.com/Agnieszka-21/namaste-django/issues/43)

3. Create and Maintain a User Account
- [#5 Create a User (Client) account](https://github.com/Agnieszka-21/namaste-django/issues/5)
- [#6 Log in to the User account](https://github.com/Agnieszka-21/namaste-django/issues/6)
- [#7 Log out of the User account](https://github.com/Agnieszka-21/namaste-django/issues/7)
- [#8 Manage the User (Client) account](https://github.com/Agnieszka-21/namaste-django/issues/8)
- [#9 Delete a User (Client) account](https://github.com/Agnieszka-21/namaste-django/issues/9) - see Future Enhancements
- [#41 Sign in to the User account with a social media login](https://github.com/Agnieszka-21/namaste-django/issues/41) - see Future Enhancements

4. Create and Manage a Class Schedule
- [#23 Create a class schedule](https://github.com/Agnieszka-21/namaste-django/issues/23)
- [#25 Manage a class schedule](https://github.com/Agnieszka-21/namaste-django/issues/38) 
- [#24 View all data related to classes and bookings](https://github.com/Agnieszka-21/namaste-django/issues/24)

5. Book Classes, View and Manage Bookings
- [#10 Book a class](https://github.com/Agnieszka-21/namaste-django/issues/10)
- [#11 Cancel a booked class](https://github.com/Agnieszka-21/namaste-django/issues/11)
- [#12 Join a waitlist](https://github.com/Agnieszka-21/namaste-django/issues/12) - see Future Enhancements
- [#13 Add a profile photo in My Account](https://github.com/Agnieszka-21/namaste-django/issues/13)
- [#28 Class cannot be booked because it is already full](https://github.com/Agnieszka-21/namaste-django/issues/28)
- [#33 View personal bookings](https://github.com/Agnieszka-21/namaste-django/issues/33)
- [#45 Edit a future booking (change date)](https://github.com/Agnieszka-21/namaste-django/issues/45)

6. Inform, Ask, and Listen to the Clients
- [#22 Ensure each client signs a waiver](https://github.com/Agnieszka-21/namaste-django/issues/22)
- [#40 Ask client for a review of a class they attended](https://github.com/Agnieszka-21/namaste-django/issues/40) - see Future Enhancements

7. Create, Manage, and Delete Staff Accounts - see Future Enhancements

8. Use a Staff Account to Teach with Ease and Clarity - see Future Enhancements

9. Ensure the Code is Ready for Production
- [#46 Create automated tests to ensure the code is working as expected](https://github.com/Agnieszka-21/namaste-django/issues/46)
- [#48 Create a comprehensive README.md file](https://github.com/Agnieszka-21/namaste-django/issues/48)
- [#49 Deploy the final version of the application to Heroku](https://github.com/Agnieszka-21/namaste-django/issues/49)
- [#50 Run manual tests on the deployed app](https://github.com/Agnieszka-21/namaste-django/issues/50)

#### Story Points
Each User Story was given a label that specifies the number of story points in order to measure/estimate in a predictive way how much time is needed for completing the User Stories as compared to one another. The simplest User Stories were given just 1 story point, the ones that needed a little more attention 2 story points, then 4 for the ones that required even more attention, and 8 for the most complex features and functionalities.

MORE ON THE POINTS - show that must-haves were below 60%!!!!!!!!!!!!!!!!!!

#### MoSCoW Prioritization

Each User Story has been marked with one of these labels:
- must-have,
- should-have,
- could-have,
- won't have.
Using these labels allowed for a clear understanding of what needs to be prioritized in terms of necessary features, and what is simply optional or can be added later as a nice-to-have functionality.


### The Scope Plane

**Features planned include:**
- User Profile - Create, Read, Update and Delete
- Bookings - Users can create, read, update and delete their upcoming booked classes
- Users can login to their account
- Users can logout of their account
- Users can reset their password if they forget it
- Users need to be registered and logged in to book scheduled classes, access their user account, see their bookings (upcoming classes only), update and cancel their bookings, as well as as view and/or update their user profile (additional information like the date of birth, chronic/recent injuries, a profile image)
  
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

__Home page__
The home page provides the user with a clear understanding as to the purpose of the site. There is a clear call to action for the user to check out the studio's class schedule, with a button in the center of the hero section that links directly to the Schedule page. The hero section also includes a photograph of a yoga studio space and a welcome message, creating a friendly, inviting mood for the website. Underneath the hero section, there is a Google map, the studio's address, and its opening hours. The welcome message is clearly visible to the user when they first arrive at the site regardless of the device they are using. There is also a navigation bar at the top of the page with the menu, and a footer including social media link - these 2 elements are visible on all pages.

![wireframe of the current page - large screen](link)

__Schedule page__
The schedule page contains a banner image, a call to action heading, and a list of all weekly group classes offered by the studio. Each listed class is shown as a card, presenting the most important information. The title of each class is a clickable link that leads to a detail page for that specific class, should the user be interested in booking the class or simply finding out more.

![wireframe of the current page - large screen](link)

__Schedule detail pages__
Each class listed on the schedule page leads to its own page where user can find a detailed description of the yoga style taught in the class, recommendations regarding who this class is suitable or not suitable for, as well as information regarding the location (which room in the studio), start time, weekday, and duration. Next to the teacher's name, there is also a "Show bio" link which opens a model with the teacher's bio. 

![wireframe of the current page - large screen](link)

__My profile__
This page can be accessed only if user is logged in. Each user can see here the information they provided when signing up (first name, last name, email address), a profile image (default or their own), and their profile information. There is also an "Edit profile" button which leads to another page which contains a form, allowing the user to update their profile data.

__My bookings__
This page can be accessed only if user is logged in. It lists the user's booked classes, but only the ones that have not started yet. The reason for this is that each booking can be updated or cancelled up to the moment of the start of each specific class booked by the user. Each booking is shown as a card that lists the most important details that help clearly identify the booked class, with 2 buttons: "Edit booking" and "Cancel booking". These buttons lead to a new page each where the user can take action as they wish.

If the user has no upcoming classes booked, the page shows a button with a call to action - "Book your next class", redirecting the user to the Schedule page.

__Wireframes for mobile devices__
Wireframes were also produced for each major page for mobile devices since the intention was to make the site fully responsive so that regardless of the user's device size, it will display accordingly. These wireframes were created before the ones for large screens (because of the mobile-first approach to design) and therefore depict an earlier version of the project, which evolved with time as the development process was progressing.

You can find the mobile wireframes here:
- [Homepage mobile wireframe](link)
- [Schedule page mobile wireframe]()
- [Schedule page continuation - class list mobile wireframe](link)
- [Schedule detail mobile wireframe](link)
- [User profile mobile wireframe](link)

#### Database schema

A few custom models were predicted to be required when building the site. Built-in Django AllAuth with its User model was applied for the user authentication system, removing the need to build a custom User model. However, a custom Profile model was required in order to gather and maintain additional information like a profile image uploaded by the user, as well as information on their date of birth and recent or chronic injuries - if they wished to add these. These 2 models were used throughout the User Profiles app.

In the Schedule app, there are more custom models, some of them linked to the User model. The Yoga Styles and Style Description are simple models which simply define options to choose from for the Group Class model that stores information on the weekly group classes. The "title" column uses the Yoga Style model as its Foreign Key, while the "description" column has the same relationship to the Style Description model. Further details are declared as choices for a CharField or an IntField, or directly (e.g. for the datetime field - "first class" column, or the "image" column - CloudinaryField upload).

The next two models, Repeated Event and Event Occurrence, are a result of using the Django-Eventtools library, which was applied to create specific datetimes for each weekly class, needed for the Booking model and the Specific Group Class model.

The Booking model has Group Class and User models as its Foreign Keys (for the "chosen class" column, and the "client" column). It gathers and maintains information regarding each specific booking, including whether or not it was cancelled, and storing a cancellation reason based on how the booking was cancelled.

The Specific Group Class model is directly connected only to the User model (many-to-many relationship to stor a list of participants' names for each specific class). However, through the use of suitable logic in views, it "inherits" indeirectly information regarding the "specific title" column from the Group Class, and for the "specific datetime" column from the Django-Eventtools models (datetime chosen by user on the book class page).

You can see the models and the relationships between them in the following database schema, created using the [drawSQL app](https://drawsql.app/).

![Database schema](link)


### The Surface Plane

#### Design
...

#### Typography
...

#### Images
...

## Features
...

__Sign up page__
The Sign Up option in the navigation menu is shown when user is not logged in. This page presents a sign up form, allowing the user to create an account and therefore access further features.

__Log in page__
The Log In option in the navigation menu is shown when user is not logged in. This page presents a log in  form, allowing the user to log into their account and access further features.

__Log out page__
The Log Out option in the navigation menu is shown when user is logged in. This page asks for a log out confirmation, allowing the user to log out of their account and keep their personal data safe.


## Future Enhancements

While the following User Stories have not been applied as they have been deemed unnecessary for an MVP, they present a wide range of potential enhancements that could be added to the project in the future.

- [#9 Delete a User (Client) account](https://github.com/Agnieszka-21/namaste-django/issues/9) - so that User (Client) can remove their account once they are sure they are not going to need it anymore (e.g. because of moving to a different area)
- [#44 Contact the studio (send a message) through a contact form](https://github.com/Agnieszka-21/namaste-django/issues/44) - so that User (Client) can easily contact the studio, get their questions answered etc.
- [#14 Buy a membership/class Bundle inside My Account](https://github.com/Agnieszka-21/namaste-django/issues/14) - so that User (Client) can purchase a suitable offer from the comfort of their home anytime they want
- [#12 Join a Waitlist](https://github.com/Agnieszka-21/namaste-django/issues/12) - so that User (Client) who could not book a class that was already full gets notified when a place opens up, giving them a chance to attend
- [#41 Sign into the User account with a social media login](https://github.com/Agnieszka-21/namaste-django/issues/41) - so that User (Client) can use existing login details from their social media account for the ease of access
- [#40 Ask clients for a review of a class they attended](https://github.com/Agnieszka-21/namaste-django/issues/40) - so that the studio/admin can get feedback and act on it for better results as a business

Applying the epic [#20 Create, Manage, and Delete Staff Accounts](https://github.com/Agnieszka-21/namaste-django/issues/20) would be a further enhancement. This epic consists of the following User Stories:
- [#21 Create a staff account for each teacher](https://github.com/Agnieszka-21/namaste-django/issues/21) - so that each teacher has a personal staff account with suitable permissions.
- [#26 Delete a staff account](https://github.com/Agnieszka-21/namaste-django/issues/26) - so that an admin can remove a staff account when a teacher decides to leave the studio as their workplace
- [#27 Edit a staff account (as an admin)](https://github.com/Agnieszka-21/namaste-django/issues/27) - so that a professional-looking profile image and bio can be uploaded, checked and made accessible on the website by an admin who takes care of the website

Building on that epic, applying the epic [#15 Use a Staff Account to Teach with Ease and Clarity](https://github.com/Agnieszka-21/namaste-django/issues/15) would improve the user experience for any teachers/instructors working for the studio and give them more control over their work hours. The epic contains the following User Stories:
- [#16 Log into a Staff (Teacher) Account](https://github.com/Agnieszka-21/namaste-django/issues/16)
- [#29 View Your Teaching Schedule](https://github.com/Agnieszka-21/namaste-django/issues/29)
- [#19 Check Clients In When Teaching a Class](https://github.com/Agnieszka-21/namaste-django/issues/19) - which could be helpful to let teachers see the clients' name, their profile picture and information regarding chronic/recent injuries and therefore deliver more personalised classes
- [#18 Request a Substitute](https://github.com/Agnieszka-21/namaste-django/issues/18) - so that teachers can alert one another and the admin to any changes needed in their teaching schedule
- [#17 Log out of the Teacher Account](https://github.com/Agnieszka-21/namaste-django/issues/17)


## Testing

### Testing Overview

...
Continuous testing was an integral part of the development process. I used numerous print statements, which were removed as specific features reached their desired shape and functionality. The statements helped me understand which exact details were accessed via API in the online dictionary, how my functions influenced one another, and what information I had to gather in order to print clear messages for the user. Testing multiple word inputs, as well as the behavior of the application in response to them was an important step in the development of a refined and reliable input validation process. While there is still potential for further enhancements, I ensured to handle any and all errors that I encountered, and took great care to handle various word inputs in a way that prevents mistakes as much as possible, at the same time allowing for a lot of variety without restricting the user in their choice of word inputs. Tests were conducted mainly in my development environment, and once results were positive, they were re-checked within the live application after it was deployed to Heroku.

### Manual Testing

While testing every single functionality as I was creating and refining it was essential to progressing with this project, I also applied a more structured approach to testing once everything seemed to work correctly in order to double-check the code's behavior and ensure that I handled any possible scenarios to avoid any issues. The table below documents this more structured approach, where I tested any and all possible functionalities as well as likely user inputs in [the live version of the app](link...).


| Functionality being tested | Expected Outcome | Actual Outcome | Result (pass/fail) |
| :------------------- | :--------------- | :------------- | :-------------------- |



### Validator Testing

In order to check any html files
I utilized the Code Institute's [Python Linter](https://pep8ci.herokuapp.com/) in order to check my Python files. No errors were reported - screenshots are linked here:
- [name of the file](link to the screenshot)

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

This program was developed using a [template from the Code Institute](https://github.com/Code-Institute-Org/ci-full-template).

UPDATE CONFIG VARS!!!
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
- The function ... is based on the code from an article on the forum [geeksforgeeks.org](https://www.geeksforgeeks.org/clear-screen-python/).


### Content

- [Yoga Dublin's website](https://www.yogadublin.com/) was an inspiration to build a functional, aesthetically pleasing webpage that could be used by a real-world yoga studio. Descriptions of yoga styles as well as teachers' bios were copied from the Yoga Dublin's website and adapted for the needs of this projects (e.g. shortened, paraphrased, and any names have been changed).
- Several free-licence images from [Pexels](https://www.pexels.com/) were used in the project. Yan Krukau's photos of yoga classes were particularly helpful, allowing me to use a suite of matching images that contributed to the website's consistent design and branding.
- [Font Awesome](https://docs.fontawesome.com/) was used for several icons used in the navigation menu, in the footer (social media icons), on the Schedule page (calendar icons), and in the modals (close icon).
- This [favicon converter](https://favicon.io/favicon-converter/) was used to create favicons based on the brand element "Namaste" in the navigation bar.
- [Google Fonts](https://fonts.google.com/) page was used to access the fonts used throughout the website.
- [Google Maps](https://www.google.ie/maps/) page was used to embed the small map with the studio's location as an iframe on the homepage.
- [Cloudinary](https://cloudinary.com/) was used to store profile images uploaded by users, as well as photos for the schedule detail pages uploaded in the admin panel by an admin.


## Acknowledgements

I would like to express my sincere gratitude to my mentor, Matt Bodden, whose suggestions and practical advice have been invaluable. I am also grateful for the help of the team of tutors who supported me when I felt stuck and whose insights and tips ensured I could progress with the project.
