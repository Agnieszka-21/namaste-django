# Namaste Yoga Studio


## Introduction

Namaste Yoga Studio is a web application for a fictional yoga studio in Dublin. Anyone can access information regarding opening hours, the studio's location, class schedule, a detailed description of each class as well as each teacher's bio. Moreover, users interested in taking classes at the studio can sign up for an accout that allows them to book classes, manage their bookings (update and cancel), and also manage their user profile while logged in.

This is the fourth Portfolio Project for the Code Institute's Diploma Course in Full Stack Software Development (E-commerce Applications). The application is built in Django using Python, HTML, CSS, and JavaScript. It provides role-based permissions for users to interact with data in a PostgreSQL database. It includes user authentication, email validation, and CRUD functionality for User Profiles and Bookings.

[View the live website here](https://namaste-yoga-studio-d494d1aeeada.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![Screenshot of the application on multiple devices](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/amiresponsive.png)


## Table of Contents

- [Namaste Yoga Studio](#namaste-yoga-studio)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [The Strategy Plane](#the-strategy-plane)
      - [The Site's Ideal User](#the-site's-ideal-user)
      - [Site Goals](#site-goals)
      - [Iterations (GitHub Milestones)](#iterations-(github-milestones))
      - [Epics](#epics)
      - [User Stories](#user-stories)
      - [Story Points](#story-points)
      - [MoSCoW Prioritization](#moscow-prioritization)
    - [The Scope Plane](#the-scope-plane)
    - [The Structure Plane](#the-structure-plane)
      - [View class schedule](#view-class-schedule)
      - [View a specific class in detail](#view-a-specific-class-in-detail)
      - [View teacher's bio](#view-teacher's-bio)
      - [View the studio's location](#view-the-studio's-location)
      - [View the studio's opening hours](#view-the-studio's-opening-hours)
      - [View the studio's social media accounts](#view-the-studio's-social-media-accounts)
      - [Create a User (Client) account](#create-a-user-(client)-account)
      - [Log in to the User account](#log-in-to-the-user-account)
      - [Log out of the User account](#log-out-of-the-user-account)
      - [Manage the User (Client) account](#manage-the-user-(client)-account)
      - [Book a class](#book-a-class)
      - [View personal bookings](#view-personal-bookings)
      - [Cancel a booked class](#cancel-a-booked-class)
      - [Add a profile photo in My Account](#add-a-profile-photo-in-my-account)
      - [Class cannot be booked because it is already full](#class-cannot-be-booked-because-it-is-already-full)
      - [Edit a future booking (change date)](#edit-a-future-booking-(change-date))
      - [Ensure each client signs a waiver](#ensure-each-client-signs-a-waiver)
      - [Opportunities arising from User Stories](#opportunities-arising-from-user-stories)
    - [The Skeleton Plane](#the-skeleton-plane)
      - [Wireframe mock-ups](#wireframe-mock-ups)
      - [Database schema](#database-schema)
    - [The Surface Plane](#the-surface-plane)
      - [Design](#design)
      - [Typography](#typography)
      - [Images](#images)
  - [Features](#features)
    - [Homepage](#homepage)
    - [Schedule page](#schedule-page)
    - [Schedule detail pages](#schedule-detail-pages)
    - [Book class page](#book-class-page)
    - [My profile page](#my-profile-page)
    - [Edit profile page](#edit-profile-page)
    - [My bookings page](#my-bookings-page)
    - [Edit booking page](#edit-booking-page)
    - [Cancel booking page](#cancel-booking-page)
    - [Sign up page](#sign-up-page)
    - [Log in page](#log-in-page)
    - [Log out page](#log-out-page)
  - [Future Enhancements](#future-enhancements)
  - [Testing](#testing)
    - [Testing Overview](#testing-overview)
    - [Manual Testing](#manual-testing)
    - [Validator Testing](#validator-testing)
    - [Lighthouse and Webaim Wave Testing](#lighthouse-and-webaim-wave-testing)
    - [Responsiveness (tested with Chrome Dev Tools)](#responsiveness-(tested-with-chrome-dev-tools))
    - [Browser compatibility testing](#browser-compatibility-testing)
    - [Automated tests](#automated-tests)
    - [Notable Bugs](#notable-bugs)
  - [Technologies Used](#technologies-used)
    - [Django](#django)
    - [Django AllAuth](#django-allauth)
    - [django-eventtools](#django-eventtools)
    - [django-render-partial](#django-render-partial)
    - [DTL/Jinja](#dtl/jinja)
    - [Crispy forms](#crispy-forms)
    - [Heroku](#heroku)
    - [PostgreSQL](#postgresql)
    - [JavaScript](#javascript)
    - [Bootstrap 5](#bootstrap-5)
    - [Font Awesome](#font-awesome)
    - [CSS](#css)
    - [HTML](#html)
    - [Packages Used](#packages-used)
    - [Resources Used](#resources-used)
  - [Deployment](#deployment)
  - [Cloning and forking the repository](#cloning-and-forking-the-repository)
  - [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
  - [Acknowledgements](#acknowledgements)


## UX

### The Strategy Plane

Namaste Yoga Studio is a web application for a fictional yoga studio in Dublin offering group classes in various styles of yoga. Any user can access the most important information about the studio - its location, opening hours, weekly class schedule, as well as a detailed description of each class which includes a teacher's bio, characteristics of the yoga style taught in the class, and who it is suitable for. Users interested in reserving their spot in a class can sign up in order to create an account, and after logging in they are able to book any classes. They can also see their upcoming booked classes, update or cancel their bookings, as well as update their personal profile by adding/changing/removing a profile picture, their date of birth, and information on recent or chronic injuries.


#### The Site's Ideal User
- People who want to attend in-studio yoga classes, whether they are new to yoga or seasoned practicioners
- People who are interested in trying yoga for the first time, whether to de-stress, improve their mobility and flexibility, or as a workout routine
- Elderly people who are looking for gentle full-body workouts
- Expectant mothers and new mothers who want to be healthier


#### Site Goals
- To inform users about the studio's offerings, class schedule and different styles of yoga
- To provide an easy way for users to book a class up to 4 weeks in advance so that they can plan ahead and ensure their spot in a class where the number of participants is limited
- To give users the possibility of cancelling their booking or changing the date of their booked class easily and quickly
- To provide users with the opportunity to create a personal profile and submit information on their chronic or recent injuries (if applicable), so that yoga teachers at the studio can deliver classes that satisfy clients


#### Iterations (GitHub Milestones)
Since the project was created using the Agile approach, both planning and prioritizing accordingly was essential.

The work on this project has been divided into 3 iterations, where the 1st and 3rd iteration lasted for close to 4 weeks, and the 2nd iteration exactly 3 weeks. This made the entire process easier to manage and helped track progress as well as decide on the priorities at each stage.

- Iteration 1 - ended on Aug 25, 2024
- Iteration 2 - ended on Sept 15, 2024
- Iteration 3 - ended on Oct 11, 2024

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
- [#9 Delete a User (Client) account](https://github.com/Agnieszka-21/namaste-django/issues/9) - see [Future Enhancements](#future-enhancements)
- [#41 Sign in to the User account with a social media login](https://github.com/Agnieszka-21/namaste-django/issues/41) - see [Future Enhancements](#future-enhancements)

4. Create and Manage a Class Schedule
- [#23 Create a class schedule](https://github.com/Agnieszka-21/namaste-django/issues/23)
- [#25 Manage a class schedule](https://github.com/Agnieszka-21/namaste-django/issues/25) 
- [#24 View all data related to classes and bookings](https://github.com/Agnieszka-21/namaste-django/issues/24)

5. Book Classes, View and Manage Bookings
- [#10 Book a class](https://github.com/Agnieszka-21/namaste-django/issues/10)
- [#11 Cancel a booked class](https://github.com/Agnieszka-21/namaste-django/issues/11)
- [#12 Join a waitlist](https://github.com/Agnieszka-21/namaste-django/issues/12) - see [Future Enhancements](#future-enhancements)
- [#13 Add a profile photo in My Account](https://github.com/Agnieszka-21/namaste-django/issues/13)
- [#28 Class cannot be booked because it is already full](https://github.com/Agnieszka-21/namaste-django/issues/28)
- [#33 View personal bookings](https://github.com/Agnieszka-21/namaste-django/issues/33)
- [#45 Edit a future booking (change date)](https://github.com/Agnieszka-21/namaste-django/issues/45)

6. Inform, Ask, and Listen to the Clients
- [#22 Ensure each client signs a waiver](https://github.com/Agnieszka-21/namaste-django/issues/22)
- [#40 Ask client for a review of a class they attended](https://github.com/Agnieszka-21/namaste-django/issues/40) - [Future Enhancements](#future-enhancements)

7. Create, Manage, and Delete Staff Accounts - see the user stories under [Future Enhancements](#future-enhancements)

8. Use a Staff Account to Teach with Ease and Clarity - see the user stories under [Future Enhancements](#future-enhancements)

9. Ensure the Code is Ready for Production
- [#46 Create automated tests to ensure the code is working as expected](https://github.com/Agnieszka-21/namaste-django/issues/46)
- [#48 Create a comprehensive README.md file](https://github.com/Agnieszka-21/namaste-django/issues/48)
- [#49 Deploy the final version of the application to Heroku](https://github.com/Agnieszka-21/namaste-django/issues/49)
- [#50 Run manual tests on the deployed app](https://github.com/Agnieszka-21/namaste-django/issues/50)

#### Story Points
Each User Story was given a label that specifies the number of story points in order to measure/estimate in a predictive way how much time is needed for completing the User Stories as compared to one another. The simplest User Stories were given just 1 story point, the ones that needed a little more attention 2 story points, then 4 points for the ones that required more time to be completed, and 8 for the most complex features and functionalities.

Altogether, user stories completed in this project take up 74 story points. The user stories that have not been handled here (potential future features) have a total of 50 points, leading to 124 points being 100% of all points and 74 points (completed user stories) being 59%, so below 60% as recommended.

#### MoSCoW Prioritization

Each User Story has been marked with one of these labels:
- must-have,
- should-have,
- could-have,
- won't have.

Using these labels allowed for a clear understanding of what needs to be prioritized in terms of necessary features, and what is simply optional or can be added later as a nice-to-have functionality.


### The Scope Plane

__Features planned include:__
- User Profile - Create, Read, Update and Delete
- Bookings - Users can create, read, update and delete bookings
- Users can log in to their account
- Users can log out of their account
- Users can reset their password if they forget it
- Users need to be logged in to book scheduled classes, access their user account, see their bookings (upcoming classes only), update and cancel their bookings, as well as view and/or update their user profile (additional information like the date of birth, chronic/recent injuries, a profile image).
  

### The Structure Plane

---

#### View class schedule

[User story #2:  ](https://github.com/Agnieszka-21/namaste-django/issues/2)
As a User (Client), I would like to view the studio's class schedule, so that I can check if I am interested in and able to attend any classes offered.

__Acceptance Criteria__
- Given that I am a User (Client), when I navigate to the studio's schedule page, then I can see the current schedule without having to register or log in.

__Implementation__
- Create models YogaStyle, StyleDescription, and GroupClass
- In the admin panel, set up data related to these models as needed to create GroupClass objects
- Create a view which lists all group classes, and a template for Schedule page which extends base.html

---

#### View a specific class in detail

[User story #3:  ](https://github.com/Agnieszka-21/namaste-django/issues/3)
As a User (Client), I would like to view each class in the schedule in more detail, so that I can make an informed decision regarding which class to choose

__Acceptance Criteria__
- Given that I am a User (Client), when I navigate to the schedule page and click on a specific class that caught my attention, then I can see all relevant details (class type, duration, time, location, instructor, who it is for, who it is not for) without having to register or log in.

__Implementation__
- Create a view that can access a specific group class from the database
- Create a template for "Schedule detail" page that shows relevant information related to the chosen group class

---

#### View teacher's bio

[User story #4:  ](https://github.com/Agnieszka-21/namaste-django/issues/4)
As a User (Client), I would like to read each teacher's short bio, so that I can choose a class and an instructor that is the best fit for me.

__Acceptance Criteria__
- Given that I am a User (Client), when I navigate to the "Schedule detail" page, then I can read a short bio for the particular teacher without having to register or log in.

__Implementation__
- Add a teacher_bio field with relevant choices in the GroupClass model
- Add a modal to the template
- Use CSS and JavaScript to hide the modal by default, and to handle opening/closing it, as well as trapping focus in the modal for keyboard accessibility

---

#### View the studio's location

[User story #30:  ](https://github.com/Agnieszka-21/namaste-django/issues/30)
As a User (Client), I would like to be able to see where the studio is located, so that I can decide whether I am interested in the services it offers.

__Acceptance Criteria__
- Given that I am a User (Client or Potential Client), when I navigate to the homepage, then I can view the location of the studio (address, map).

__Implementation__
- Add an iframe for Google maps with a pin for the studio's address in the index.html template
- Add an address section in the same template

---

#### View the studio's opening hours 

[User story #42:  ](https://github.com/Agnieszka-21/namaste-django/issues/42)
As a User (Client), I would like to check the yoga studio's opening hours, so that I have the basic information I need to decide whether I am interested in their offer.

__Acceptance Criteria__
- Given that I am a client or potential client, when I navigate to the homepage, then I can view the studio's opening hours.

__Implementation__
- In the index.html template create a section with the studio's opening hours

---

#### View the studio's social media accounts

[User story #43:  ](https://github.com/Agnieszka-21/namaste-django/issues/43)
As a User (Client), I would like to check out the studio's social media accounts, so that I can find more information regarding their culture, community, events etc.

__Acceptance Criteria__
- Given that I am a client or potential client, when I navigate to the studio's website, then I can easily find there links to their social media accounts.
- Given that I am a client or potential client, when I navigate to the website and click any of the social icons in the footer, then I am automatically taken to the particular account in a new tab.

__Implementation__
- Add anchor elements in the footer that open in a new tab each (base.html template)

---

#### Create a User (Client) account

[User story #5:  ](https://github.com/Agnieszka-21/namaste-django/issues/5)
As a User (Client), I would like to create an account, so that I can book classes online.

__Acceptance Criteria__
- Given that I am an unregistered User (Client), when I choose the "Sign Up" option, then I can create my account with an email address and a password.
- Given that I am an unregistered User (Client), when I choose the "Sign Up" option, then I am sent an email that allows me to verify my email and confirm that I want to sign up for an account.

__Implementation__
- Use Django AllAuth to set up authentication
- Adjust the AllAuth templates so that they extend the base.html template
- Set up email verification

---

#### Log in to the User account

[User story #6:  ](https://github.com/Agnieszka-21/namaste-django/issues/6)
As a User (Client), I would like to be able to log in to my account, so that I can access the advantages of having an account.

__Acceptance Criteria__
- Given that I am a registered user, when I navigate to the login page, then I can enter my details to login to my account
- Given that I am a registered user, when I navigate to the login page and enter my details and I click login, then I am logged into my account and I am able to see a visual confirmation that I am now logged in.
- Given that I am a registered user and I try to log in to my account, when I enter the wrong information, then the site informs me that the information was incorrect and prevents my logging in.
- Given that I am a registered user and I try to log in to my account, when I forget my password, then I can click a "Forgot password" link that takes me to a page that helps me reset my password.

__Implementation__
- Ensure the login page is easily accessible in the navbar
- Show a confirmation message when a User logs into their account successfully
- Make sure the User is notified if they try to log in with a wrong email or password
- Ensure that "Forget password" is shown on the log in page so that the User can reset their password if they forgot it

---

#### Log out of the User account

[User story #7:  ](https://github.com/Agnieszka-21/namaste-django/issues/7)
As a User (Client), I would like to be able to log out of my account, so that I can make sure my account details are safe.

__Acceptance Criteria__
- Given that I am a logged in user, when I click the "log out" button, then I am redirected to the homepage and a confirmation message is shown

__Implementation__
- In settings.py, set LOGOUT_REDIRECT_URL to the homepage
- Ensure a confirmation message is shown after the User logged out of their account

---

#### Manage the User (Client) account

[User story #8:  ](https://github.com/Agnieszka-21/namaste-django/issues/8)
As a User (Client), I would like to be able to add a profile image and edit my account details, so that they stay up to date and I am in charge of my profile.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to my Account page, then I can add/edit/delete suitable profile data.
- Given that I am a logged in user, when I add/edit/delete my profile data, then get a notification that confirms my changes.
- Given that I am a logged in user, when there is an issue with adding/editing/deleting my profile data, then the site informs me that my changes were not saved.

__Implementation__
- Create the Profile view and a matching template with the option "Edit profile"
- Create an "Edit profile" view for updating the profile (profile form), and a matching template
- Create messages to be shown upon form submission that let the user know whether their data was updated successfully (or not)
- Redirect user to the Profile page, so that they can see their updated profile right away

---

#### Book a class

[User story #10:  ](https://github.com/Agnieszka-21/namaste-django/issues/10)
As a User (Client), I would like to book a class, so that I can attend it.

__Acceptance Criteria__
- Given that I am an unregistered user, when I navigate to the Schedule, choose a class and click the "Book now" button, then I am prompted to create a user account.
- Given that I am a registered user, when I navigate to the Schedule page, choose a class and click he "Book now" button, then I am asked to sign in.
- Given that I am a logged in user, when I navigate to the Schedule, choose a class and click the "Book now" button, then the site prompts me to fill a suitable form.
- Given that I am a logged in user, when submit a valid booking form for a specific class, then a suitable notification is shown on the page to confirm a successful booking.

__Implementation__
- Create a "Book class" page (a suitable view, form, and template)
- On the "Schedule detail" page, show a "Book class" button (for a logged in user only - if the user is not logged in, add a link to the Log In page and the information that they have to log in to book a class)
- Create a Booking model to store informtion like who made the booking, which group class they chose etc.
- Create dates and times for the next 3 occurrences of each group class so that the user can choose one of them from a list of available dates

---

#### View personal bookings

[User story #33:  ](https://github.com/Agnieszka-21/namaste-django/issues/33)
As a User (Client), I would like to view an up-to-date list of all classes I have booked, so that I can see my upcoming classes, making it easy for me to be in charge of my schedule.

__Acceptance Criteria__
- Given that I am a logged in User (Client), when I navigate to my account, then I can view a list of all upcoming classes I have booked.

__Implementation__
- Create "My bookings" page (suitable view that lists a specific user's bookings and a template that goes with it)

---

#### Cancel a booked class

[User story #11:  ](https://github.com/Agnieszka-21/namaste-django/issues/11)
As a User (Client), I would like to be able to cancel a class I booked, so that I can avoid blocking a place that someone else could use.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to the Account page, then I see my bookings and have the cancellation option next to the ones that can be cancelled (future classes)
- Given that I am a logged in user, when I navigate to the Account page and click "Cancel" next to one of my booked classes, then I am asked whether I would like to cancel that particular class.
- Given that I am a logged in user, when I click "Cancel" next to a class in my Account and confirm it, then the site informs me that the class has been successfully cancelled.

__Implementation__
- Ensure only future classes are shown so that the user does not cancel a class that has already happened
- Add to that page a "Cancel booking" button next to each class, to take the user to the "Cancel booking" page
- Create "Cancel booking" page (view, form, template)
- In the Booking model, add fields "cancelled" (boolean), and "cancellation reason" with 2 choices: "client's decision" or "class full"
- Upon cancellation, update these 2 fields accordingly in the backend for the specific Booking object
- Ensure that a confirmation (success) message is shown upon cancellation

---

#### Add a profile photo in My Account

[User story #13:  ](https://github.com/Agnieszka-21/namaste-django/issues/13)
As a User (Client), I would like to be able to add my profile picture, so that my user account feels personalized and truly mine.

__Acceptance Criteria__
- Given that I am a logged in user (client), when I am on My Account page, then I can upload a profile picture and save it in my profile.

__Implementation__
- Ensure the form for editing the profile has a field for an image upload to Cloudinary
- Set up Cloudinary

---

#### Class cannot be booked because it is already full

[User story #28:  ](https://github.com/Agnieszka-21/namaste-django/issues/28)
As a User (Client), I would like to be able to know when a class is booked out, so that I am not booking a spot in a class that is already full.

__Acceptance Criteria__
- Given that I am a logged in User (Client), when I try to book a specific class on a specific date that is already full, then I am informed that there are no more spots left and encouraged to choose a different date.
- Given that I am a logged in User (Client), when I try to book a class that turns out to be full, then I am given a chance to book this class on a different date instead (different week).

__Implementation__
- Upon the submission of the booking form, show the message information that the class is already fully booked and encourage the user to choose a different date, or a different group class
- In the backend, cancel the booking immediately, adding the following cancellation reason: "class full". This allows an admin to see how many people were actually interested in booking a specific class, which can be helpful when making business decisions regarding the schedule and class offer

---

#### Edit a future booking (change date)

[User story #45:  ](https://github.com/Agnieszka-21/namaste-django/issues/45)
As a User (Client), I would like to be able to choose a different date for my upcoming booking, so that I can feel in charge of my schedule and have the flexibility I need to change my bookings according to my personal needs.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to the My Bookings page, then I can see the Edit option next to my upcoming bookings.
- Given that I am a logged in user, when I click "Edit booking", then I can choose one of available dates for this class.
- Given that I am a logged in user changing my booking, when I choose a different date and confirm it, then it is updated in my account and I can see a notification on the website that confirms the change.

__Implementation__
- Add an "Edit booking" button for each class listed on the "My bookings" page
- Take the user to the "Edit booking" page where they can choose one of 3 available dates for this group class (same as on the "Book class" page)
- Create a suitable view and template for that page
- Take care of all possible scenarios, including when the class on the new date is already full or the user already has a booking for that class
- Depending on the outcome of the update, show a suitable message to inform the user what has been done
- Upon a successful update, redirect the user back to the "My bookings" page

---

#### Ensure each client signs a waiver

[User story #22:  ](https://github.com/Agnieszka-21/namaste-django/issues/22)
As an Admin, I would like *to ensure that each client signs a waiver when booking a class, so that I can protect the business and my employees from unforeseen issues.

__Acceptance Criteria__
- Given that I am an Admin, when I check clients' booking data, then I can see that the waiver has been signed for each and every booking.

__Implementation__
- Add a "waiver signed" checkbox in the booking form and make it required
- Add a suitable label that explains what the checkbox is for rather than just using the default field name
- Add a span "Read the waiver here" that opens a modal (hidden by default) with the content of the liabiliy waiver. 
- Add JavaScript to handle interactions between the user and the modal, trap focus in the modal when open, and make it accesible to keyboard users as well.

---

#### Opportunities arising from User Stories

| Opportunity | Importance | Viability/Feasibility |
| :---------- | :--------- | :------------- |
| Provide users the ability to access the website on any device | 5 | 5 |
| Provide users the ability to access the general, informative part of the application without having to log in or register | 5 | 5 |
| Provide users the ability to create an account | 5 | 5 |
| Provide users the ability to view their profile when logged in | 5 | 5 |
| Provide users the ability to update their profile when logged in | 5  | 5 |
| Provide users the ability to delete data from their profile when logged in | 5 | 5 |
| Provide users the ability to book a class when logged in | 5 | 5 |
| Provide users the ability to view their upcoming booked classes when logged in | 5 | 5 |
| Provide users the ability to update their bookings | 5 | 5 |
| Provide users the ability to cancel their bookings | 5 | 5 |
| Provide users the ability to view the studio's liability waiver when booking a class | 4 | 4 |
| Provide users the ability to view a teacher's bio for each group class | 3 | 4 |


### The Skeleton Plane

#### Wireframe mock-ups

__Home page__

The home page provides the user with a clear understanding as to the purpose of the site. There is a clear call to action for the user to check out the studio's class schedule, with a button in the center of the hero section that links directly to the Schedule page. The hero section also includes a photograph of a yoga studio space and a welcome message, creating a friendly, inviting mood for the website. Underneath the hero section, there is a Google map, the studio's address, and its opening hours. The welcome message is clearly visible to the user when they first arrive at the site regardless of the device they are using. There is also a navigation bar at the top of the page with the menu, and a footer including social media links - these 2 elements are visible on all pages.

![Wireframe of the homepage - large screen](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/dsktp_home.png)

__Schedule page__

The schedule page contains a banner image, a call to action heading, and a list of all weekly group classes offered by the studio. Each listed class is shown as a card, presenting the most important information. The title of each class is a clickable link that leads to a detail page for that specific class, should the user be interested in booking the class or simply finding out more.

![Wireframe of the Schedule page - large screen](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/dsktp_schedule.png)

__Schedule detail pages__

Each class listed on the schedule page leads to its own page where user can find a detailed description of the yoga style taught in the class, recommendations regarding who this class is suitable or not suitable for, as well as information regarding the location (which room in the studio), start time, weekday, and duration. Next to the teacher's name, there is also a "Show bio" link which opens a modal with the teacher's bio. 

![Wireframe of the Schedule detail page - large screen](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/dsktp_schedule_detail.png)

__My profile__

This page can be accessed only if user is logged in. Each user can see here the information they provided when signing up (first name, last name, email address), a profile image (default or their own), and their profile information. There is also an "Edit profile" button which leads to another page which contains a form, allowing the user to update their profile data.

![Wireframe of the My profile page - large screen](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/dsktp_my_profile.png)

__My bookings__

This page can be accessed only if user is logged in. It lists the user's booked classes, but only the ones that have not started yet. The reason for this is that each booking can be updated or cancelled up to the moment of the start of each specific class booked by the user. Each booking is shown as a card that lists the most important details that help clearly identify the booked class, with 2 buttons: "Edit booking" and "Cancel booking". These buttons lead to a new page each where the user can take action as they wish.

![Wireframe of the My bookings page - large screen](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/dsktp_my_bookings.png)

If the user has no upcoming classes booked, the page shows a button with a call to action - "Book your next class", redirecting the user to the Schedule page.

__Wireframes for mobile devices__

Wireframes were also produced for each major page for mobile devices since the intention was to make the site fully responsive so that regardless of the user's device size, it will display accordingly. These wireframes were created before the ones for large screens (because of the mobile-first approach to design) and therefore depict an earlier version of the project, which evolved with time as the development process was progressing.

See the mobile wireframes below:

| Homepage | Schedule page | Schedule - class list |
| :------------------- | :--------------- | :------------- |
| ![Homepage mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_homepage.png) | ![Schedule page mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_schedule_page.png) | ![Schedule page continuation - class list mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_schedule_list.png) |

| Schedule detail | User profile page | My bookings page |
| :------------------- | :--------------- | :--------------- |
| ![Class detail mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_class_detail.png) | ![User profile mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_user_account.png) | ![My bookings mobile wireframe](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/wireframes/wireframe_my_bookings.png) |


#### Database schema

A few custom models were predicted to be required when building the site. Built-in Django AllAuth with its User model was applied for the user authentication system, removing the need to build a custom User model. However, a custom Profile model was required in order to gather and maintain additional information like a profile image uploaded by the user, as well as information on their date of birth and recent or chronic injuries - if they wished to add these. These 2 models were used throughout the User Profiles app.

In the Schedule app, there are more custom models, some of them linked to the User model. The Yoga Styles and Style Description are simple models which define options to choose from for the Group Class model that stores information on the weekly group classes. The "title" column uses the Yoga Style model as its Foreign Key, while the "description" column has the same relationship to the Style Description model. Further details are declared as choices for a CharField or an IntField, or as a direct input in a form or within the admin panel (e.g. for the datetime field - "first class" column, or the "image" column - CloudinaryField upload).

The next two models, Repeated Event and Event Occurrence, are a result of using the Django-Eventtools library, which was applied to create specific datetimes for each weekly class, needed for the Booking model and the Specific Group Class model.

The Booking model utilises Group Class and User models as its Foreign Keys (for the "chosen class" column, and the "client" column). It gathers and maintains information regarding each specific booking, including whether or not it was cancelled, and storing a cancellation reason based on how the booking was cancelled.

The Specific Group Class model is directly connected only to the User model (many-to-many relationship to store a list of participants' names for each specific class). However, through the use of suitable logic in views, it "inherits" indirectly information regarding the "specific title" column from the Group Class, and for the "specific datetime" column from the Django-Eventtools models (datetime chosen by user on the book class page).

You can see the models and the relationships between them in the following database schema, created using the [drawSQL app](https://drawsql.app/).

![Database schema](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/drawSQL-image-export-2024-10-06.png)


### The Surface Plane

#### Design
The design of the website is simple, minimalistic, and coherent. It is supposed to convey ease, simplicity, and make the end-user feel both grounded and welcome.

The color palatte is based on earthy and neutral tones.

The main color - walnut brown - has been used throughout the page in the navbar and footer, and also on hover/select for elements like buttons and links to emphasise their active state. It is a neutral shade often associated with earth and nature, which can convey the message of the studio: we are here to help you feel calm, relaxed, and grounded.

The main background color of the page is an off-white color #f7f7f7. Since most of the text is pure black (#000), it provides a good contrast while being gentler on the eyes and matching the natural theme of the color palette.

There is also pure white color (#fff) used as background for cards on the Schedule page and My bookings page, so that the cards are clearly discernible from the off-white background but without creating too much contrast, which could result in distraction and overwhelm.

Elements that are links or made to look like links use the eye-catching "office-green" color (#008000), and the font-weight is bold to ensure plenty of contrast with the background since these are elements that the end-user will interact with.

The following table created with [Contrast Grid](https://contrast-grid.eightshapes.com/) shows the color palette utilised in this project.

![Contrast Grid color palette](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/contrast_grid.png)


#### Typography
Two types of Google fonts have been used in this project.
For the brand name shown in the top left corner of each page, "Namaste", the Nova Mono font was used to provide an eye-catching design. Since this is a monospace font, monospace was also declared as a fallback font-family in style.css.

Lato font-family was used for all remaining text, in various weights ranging from 400 to 800. This is a sans-serif font, easily readable, light and simple, which matches the website's overall feel of being easy to navigate, minimalistic, and accessible for anyone. 


#### Images
Images of yoga classes used on this website are free-licence images from Pexels. Most of them come from the same suite of images by Yan Krukau, providing a coherent feel and look, and conveying to the end-user the real character of the yoga studio, giving them insights into the environment and the community of yoga practicioners. The hero image was also the starting point for creating the color palette for the website, with the walnut brown found directly in the image through a color picker tool.


## Features

### Homepage

__Navigation bar__

The navigation bar is shown in 2 versions, depending on whether the user is logged in or not. For a user who is not logged in, it lists Home, Schedule, Sign up, and Log in.

![Navbar - user not logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/navbar_not_logged_in.png)

For a logged in user, it shows the following options: Home, Schedule, My profile, My bookings, and Log out.

![Navbar - user logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/navbar_logged_in.png)

__Hero section__

The hero section consists of a responsive full-width background image, a black semi-transparent overlay for optimal contrast, and white text "Welcome to the friendliest yoga studio in Dublin" followed by a button with the call to action "See our class schedule", which redirects the user to the Schedule page. This way the purpose of the page is clear right away - to invite user to check out the offer of yoga classes so they can book the ones that they find interesting.

![Hero section](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/home_hero.png)

__Embedded Google maps__

Underneath the hero section, the user can find general information about the studio, including an embedded Google map with a pin showing the exact location of the studio.

![Google maps, address, and opening hours](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/home_map_info.png)

__Address and opening hours__

Next to the map (or below on tablet and phone screens), there is information on the studio's address and its opening hours - easily accessible to anyone visiting the page. See the previous screenshot.

__Footer with social icons__

The footer includes links to social media pages of the studio, which open in a new tab each. It also has a copyright section at the very bottom.

![Footer](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/footer.png)


### Schedule page

__Banner image and call-to-action heading__

An image depicting a group of people practising yoga in a class, and below the heading with a call to action: "Find the perfect class for you!".

![Schedule page banner and heading](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_banner_heading.png)

__List of all weekly classes (cards)__

The classes are listed grouped by weekday, starting with Monday, and ordered according to their start time. A calendar icon from Font Awesome and a short name of each weekday visually divide the list for enhanced user experience and clarity. Each class is shown as a card which presents the most important details, and the class title is a link that leads directly to the detail page for the class. Class titles are also tabbable, ensuring that the entire website is accessible for keyboard users.

![Schedule list](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_list.png)


### Schedule detail pages

__Image__

For added visual interest, there is an image of a yoga class. The images differ depending on the style of yoga taught in the class to give the user an idea of what is done in the class or who it is for. The images can be uploaded to Cloudinary through the admin panel when creating/updating a group class.

![Schedule detail page - user not logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_det_not_logged_in.png)

__Class details__

Title, instructor, description, weekday, start time, and duration are all shown next to the class image. They are visually coherent yet separate from one another to ensure that the user finds the information they need the most without feeling overwhelmed by details (see the previous screenshot).

__Show bio link and modal__

Next to the instructor's name, there is a "Show bio" span that can be selected (by a mouseclick or with Tab key) to open a modal that houses a short bio of the instructor. In the modal, there is also a "close" button - if you click the button (or anywhere outside of the modal), the modal will be closed. To ensure that the page is fully accessible, JavaScript was used to handle the modal functionality, including trapping focus in the modal when it is open.

![Teacher bio modal](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/teacher_bio_modal.png)

__Book now button__

Shown only for logged in users, when selected, it takes the user to the "Book class" page. For users who are not logged in or do not have an account yet, there is a link to the log in page instead.

![Schedule detail page - user logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_det_logged_in.png)


### Book class page

__User form__

Pre-filled and uneditable. Contains the following details: the logged-in user's first name, last name, and email address.

![Book class page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_page.png)

__Booking form__

Contains a dropdown with available dates - the next 3 available occurrences of the weekly group class to choose from.
It also has a checkbox to "sign" the studio's liability waiver, which is required so that the class can be booked.

![Waiver not signed](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/waiver_signed_required.png)

If the booking is successful, the user is redirected to the Schedule page (to encourage the user to check out other classes) and shown a success message.

![Booking successful](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/booking_success.png)

Should the chosen class be already fully booked, the following message is shown:

![Booking failed - class already full](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_fail_full.png)

In the event when the user tries to book the exact same class that they have already booked (same group class on the same date and time), they are informed that they have already booked a place in this class and prevented from making a duplicate booking (each user is allowed to book a class only for themselves, so they receive exactly one spot in each class they book).

![Booking failed - duplicate exists](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_already_booked.png)

__"Read the waiver here" link and modal__

Under the checkbox, there is a span "Read the waiver here" that opens a modal with the studio's liability waiver. In the modal, there is also a "close" button - if you click the button (or anywhere outside of the modal), the modal will be closed. To ensure that the page is fully accessible, JavaScript was used to handle the modal functionality, including trapping focus in the modal when it is open.

![Waiver modal](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/waiver_modal.png)


### My profile page

This page shows the following information: a profile image (either one uploaded by the user, or the default image), the user's full name and email address, and then their additional information like date of birth and chronic/recent injuries. There is also a button "Edit profile" that brings the user to the Edit profile page.

![My profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_profile_page.png)


### Edit profile page

![Edit profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_profile_page.png)

This page contains a profile form where the user can update the following details: their date of birth, their information about injuries, and their profile image. All these elements are optional and can be left blank (a default picture is used as a profile image in this case). At the bottom of the form, there are 2 buttons: "Save profile" and "Discard changes". The latter simply redirects the user back to their profile page. The "Save profile" button saves the changes, redirects the user to the profile page, and shows the following success message:

![Edit profile - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_profile_success.png)


### My bookings page

The user can see here a list of their booked classes, but only the ones that are upcoming in the future to ensure that no changes are made to the classes that are in the past or taking place in that exact moment. Each class is shown as a card with 2 buttons - Edit booking, and Cancel booking.

![My bookings page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_bookings.png)

If the user has no upcoming bookings, the page informs them about that and a button with the call to action "Book your next class" is shown that redirects the user to the Schedule page so that they can choose and book their next class easily.

![My bookings page with no upcoming classes](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_bookings_page_empty.png)


### Edit booking page

The user can change here the date of their class. A dropdown like the one on the "Book class" page is shown, with the next 3 dates of the weekly class. There are also 2 buttons: "Save changes" which leads to the outcomes described below, and "Discard changes" which simply redirects the user to their "My bookings" page.

![Edit booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_page.png)

If the user could be added to the specific class on the new date they chose, a success message is shown and they are redirected to the "My bookings" page.

![Edit booking - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_success.png)

If the specific class on the new date chosen by the user is already fully booked, they are informed that their booking could not be updated for that reason. The user can still choose a different date from the dropdown and try again.

![Edit booking - class already full](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_fail_full.png)

If the specific class on the new date chosen by the user is already one of that user's booked classes, they are informed about that, redirected to their "My bookings" page, and prevented from creating a duplicate booking.

![Edit booking - class already booked](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_duplicate_found.png)


### Cancel booking page

The user can cancel here their upcoming class. The page re-confirms that the user wants to cancel their booking. There are 2 buttons, similarly to the "Edit booking" page: "Yes, cancel my booking" and "No, I changed my mind". 

![Cancel booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/cancel_booking_page.png)

If the latter is seleted, the user is simply redirected back to their "My bookings" page. If the user does go ahead with the cancellation, they are shown a success message and are redirected to the "My bookings" page.

![Cancel booking - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/cancel_booking_success.png)


### Sign up page
The Sign Up option in the navigation menu is shown when user is not logged in. This page presents a sign up form, allowing the user to create an account and therefore access further features.

![Sign up page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/sign_up_page.png)


### Log in page
The Log In option in the navigation menu is shown when user is not logged in. This page presents a log in  form, allowing the user to log into their account and access further features.

![Log in page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/log_in_page.png)
![Log in success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/log_in_success.png)


### Log out page
The Log Out option in the navigation menu is shown when user is logged in. This page asks for a log out confirmation, allowing the user to log out of their account and keep their personal data safe.

![Log out page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/log_out_page.png)
![Log out success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/log_out_success.png)


## Future Enhancements

While the following User Stories have not been completed as they have been deemed unnecessary for an MVP, they present a wide range of potential enhancements that could be added to the project in the future.

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

Another possible enhancement could be a time limit on editing/cancelling upcoming bookings as well as booking classes - for example ending the period where any changes are allowed 15 minutes before a class. This is a common practice in many studios and fitness centers that allows for better user experience by avoiding any last-minute changes to the classes offered in the studio.


## Testing

### Testing Overview

Continuous testing was an integral part of the development process. I used numerous print statements, which were removed as specific features reached their desired shape and functionality. The statements helped me follow what is happening, especially in the more complex scenarios where multiple things were affected by just one change (e.g. when booking a class, cancelling, or updating a booking) and where multiple functions worked together, calling one another and handling a wide range of scenarios. 

While there is still a significant potential for further enhancements in a project as complex as this one, I ensured to handle any and all errors that I encountered, and took great care to minimise the risk of any errors occurring on submission of forms. Validation was often handled at the earliest stages while developing the forms, limiting the end-users' access to information that can be handled in the backend, in a more secure way (e.g. date input in the booking and update booking forms, name and email not editable by the end-user after the user signs up for an account, or the "waiver signed" field in the booking form being required and a simple checkbox).

Manual tests were conducted mainly in my development environment, and once results were positive, they were re-checked within the live application after it was deployed to Heroku. 

Automated tests were also written to confirm that each view renders the correct template, to ensure that views restricted to logged-in users only redirect the user to the log in page, and many more.


### Manual Testing

While testing every single functionality as I was creating and refining it was essential to progressing with this project, I also applied a more structured approach to testing once everything seemed to work correctly in order to double-check the code's behavior and ensure that I handled any possible scenarios to avoid any issues. The table below documents this more structured approach, where I tested all possible functionalities as well as likely user inputs in [the live version of the app](https://namaste-yoga-studio-d494d1aeeada.herokuapp.com/).


| Functionality being tested | Expected Outcome | Actual Outcome | Result (pass/fail) |
| :------------------------- | :--------------- | :------------- | :-------------------- |
| Logo "Namaste" | takes the user to the homepage when selected on any page | as expected | pass |
| Navbar link "Sign up" | takes the user to the Sign up page | as expected | pass |
| Navbar link "Log in" | takes the user to the Log in page | as expected | pass |
| Navbar link "Schedule" | takes the user to the Schedule page | as expected | pass |
| Navbar link "My profile" | takes a logged-in user to their profile page | as expected | pass |
| Navbar link "My bookings" | takes a logged-in user to their bookings | as expected | pass |
| Navbar link "Log out" | takes a logged-in user to the log out page | as expected | pass |
| Footer: Facebook icon | opens Facebook in a new tab | as expected | pass |
| Footer: Instagram icon | opens Instagram in a new tab| as expected | pass |
| Footer: YouTube icon | opens YouTube in a new tab | as expected | pass |
| Sign up page: "Sign up" button | creates a user account & profile, sends a verification email, redirects the user to the homepage and shows a suitable message | as expected | pass |
| Sign up page: "log in" link | redirects the user to the Log in page | as expected | pass |
| Log in page: "sign up" link | redirects the user to the Sign up page | as expected | pass |
| Log in page: "Log in" button | logs the user into their account, redirects them to the homepage, shows a success message | as expected | pass |
| Log in page: "Forgot password" link | redirects the user to the Password Reset page | as expected | pass |
| Log out page: "Log out" button | logs the user out of their account, redirects them to the homepage, shows a success message | as expected | pass |
| Home: "See our schedule" button | redirects user to the Schedule page | as expected | pass |
| Schedule: class title links | redirect the user to a Schedule detail page for the chosen class | as expected | pass |
| Schedule detail: "Show bio" underlined text | opens the modal containing a particular instructor's bio | as expected | pass |
| Schedule detail: close icon inside the modal | closes the modal | as expected | pass |
| Schedule detail: "Log in to book the class" link | redirects user to the log in page | as expected | pass |
| Schedule detail: "Book class" button | redirects a logged-in user to the Book class page | as expected | pass |
| Book class page: "Read the waiver here" underlined text | opens the modal containing the studio's liability waiver | as expected | pass |
| Book class page: close icon inside the modal | closes the modal | as expected | pass |
| Book class page: "Available dates" dropdown | shows the next 3 dates for the chosen class | as expected | pass |
| Book class page: "Book class" button | if successful: creates a booking, redirects the user to the Schedule page, shows a success message; if not successful: shows a suitable message | as expected | pass | 
| My bookings: "Book your next class" button (shown only if there are no upcoming bookings) | redirects the user to the Schedule page | as expected | pass |
| My bookings: "Edit booking" | redirects the user to the Edit booking page | as expected | pass |
| My bookings: "Cancel booking" | redirects the user to the Cancel booking page | as expected | pass |
| Edit booking page: "Available dates" dropdown | shows the next 3 dates for the chosen class | as expected | pass |
| Edit booking page: "Save changes" button | if successful: updates the chosen booking, redirects the user to My bookings page, shows a success message; if class full: shows an error message; if class already booked on the new date: redirects to My bookings and shows an info message | as expected | pass |
| Edit booking page: "Discard changes" button | redirects the user to My bookings page | as expected | pass |
| Cancel booking page: "Yes, cancel my booking" button | cancels the chosen booking, redirects the user to My bookings, shows a success message | as expected | pass |
| Cancel booking page: "No, I changed my mind" button | redirects the user to My bookings | as expected | pass |
| My profile: "Edit profile" button | redirects the user to the Edit profile page | as expected | pass |
| Edit profile page: "Choose file" for the "Profile image" field | opens the File Explorer on the user's device | as expected | pass |
| Edit profile page: "Clear" checkbox for the "Profile image" field | when checked, on submission it removed the user's current profile image if they uploaded one earlier | as expected | pass | 
| Edit profile page: "Save profile" button | saves changes, redirects the user to My profile page, shows a success message | as expected | pass |
| Edit profile page: "Discard changes" button | redirects the user to My profile | as expected | pass |


### Validator Testing

__HTML__

The [W3C Markup Validation Service](https://validator.w3.org/) was used to check any html files containing custom code. All files are passed the validation test without errors - you can see relevant screenshots below:
- [home page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_home.png)
- [schedule page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_schedule.png)
- [schedule detail page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_schedule_detail.png)
- [signup page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_signup.png)
- [login page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_login.png)
- [logout page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_logout.png)
- [profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_profile.png)
- [edit profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_edit_profile.png)
- [my bookings page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_my_bookings.png)
- [edit booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_edit_booking.png)
- [cancel booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_cancel_booking.png)

__CSS__

The style.css file containing custom styling for the application has been checked in the [W3C CSS Validation Service Jigsaw](https://jigsaw.w3.org/css-validator/) and has no errors - see the screenshot below:

![CSS validator test](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/css_no_errors.png)

__JavaScript__

[JSHint](https://jshint.com/) has been used to validate the two JavaScript files in the application. Both files returned no errors.
- [waiver.js - validattion result](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/js_waiver_validator.png)
- [bio.js - validation result](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/js_bio_validator.png)

__Python__

All Python files containing custom code have been run through the [Code Institute's Python linter](https://pep8ci.herokuapp.com/#) in order to ensure that they meet the PEP8 requirements/recommendations. No errors were found - you can find relevenat screenshots in [this folder](https://github.com/Agnieszka-21/namaste-django/tree/main/assets/python_linter).


### Lighthouse and Webaim Wave Testing

The deployed website has been tested using both Lighthouse and WebaAim WAVE in order to ensure that it performs well and meets accessibility criteria. A vast majority of Lighthouse scores is in the optimal green range. However, it is worth noting that using Google maps on the homepage, images uploaded to Cloudinary on other pages, as well as applying Bootstrap and Google Fonts has led to Best Practices scores being slightly lower. From the perspective of a business using this web application it made more sense to keep the map and Cloudinary storage rather than trying to get the best score and missing out on those valuable resources, so the decision was simple. 

In order to keep accessibility scores in the optimal range, I ensured to make the website fully-operational for keyboard users, including trapping focus in each modal while it is open (waiver.js and bio.js files) and adding tabindex to card titles on the Schedule page.

You can find screenshots with relevant results [here](https://github.com/Agnieszka-21/namaste-django/tree/main/assets/lighthouse_wave).


### Responsiveness (tested with Chrome Dev Tools)

| Device tested | Site responsive >=700px |	Site Responsive <699px |Renders as expected |
| :------------ | :---------------------- | :--------------------- | :----------------- |
|Galaxy Fold | N/A | yes | yes |
|iPhone SE | N/A | yes | yes |
|iPhone 12Pro | N/A | yes | yes |
|Samsung Galaxy S8+	| N/A | yes	| yes |
|iPad Air | yes	| N/A | yes |
|Surface Pro 7 | yes | N/A | yes |
|Laptop 1440px | yes | N/A | yes |
|4K - 2560px | yes | N/A | yes |


### Browser compatibility testing

| Browser being tested | Section tested | Intended appearance | Intended responsiveness |
| :------------------- | :------------- | :------------------ | :------------------ |
| Chrome | Navbar | good | good |
| Chrome | Footer | good | good |
| Chrome | Home - hero section | good | good |
| Chrome | Home - map, address, opening hours | good | good |
| Chrome | Schedule - banner image and heading  | good | good |
| Chrome | Schedule - list of classes grouped by weekday | good | good |
| Chrome | Schedule detail - class image | good | good |
| Chrome | Schedule detail - text and "Book class" button | good | good |
| Chrome | Book class page - booking form | good | good |
| Chrome | My profile page | good | good |
| Chrome | Edit profile - profile form | good | good |
| Chrome | My bookings - list of upcoming bookings | good | good |
| Chrome | My bookings - no upcoming classes | good | good |
| Chrome | Edit booking page | good | good |
| Chrome | Cancel booking page | good | good |
| Chrome | Sign up page | good | good |
| Chrome | Log in page | good | good |
| Chrome | Log out page | good | good |
| Firefox | Navbar | good | good |
| Firefoc | Footer | good | good |
| Firefox | Home - hero section | good | good |
| Firefox | Home - map, address, opening hours | good | good |
| Firefox | Schedule - banner image and heading  | good | good |
| Firefox | Schedule - list of classes grouped by weekday | good | good |
| Firefox | Schedule detail - class image | good | good |
| Firefox | Schedule detail - text and "Book class" button | good | good |
| Firefox | Book class page - booking form | good | good |
| Firefox | My profile page | good | good |
| Firefox | Edit profile - profile form | good | good |
| Firefox | My bookings - list of upcoming bookings | good | good |
| Firefox | My bookings - no upcoming classes | good | good |
| Firefox | Edit booking page | good | good |
| Firefox | Cancel booking page | good | good |
| Firefox | Sign up page | good | good |
| Firefox | Log in page | good | good |
| Firefox | Log out page | good | good |
| Edge | Navbar | good | good |
| Edge | Footer | good | good |
| Edge | Home - hero section | good | good |
| Edge | Home - map, address, opening hours | good | good |
| Edge | Schedule - banner image and heading  | good | good |
| Edge | Schedule - list of classes grouped by weekday | good | good |
| Edge | Schedule detail - class image | good | good |
| Edge | Schedule detail - text and "Book class" button | good | good |
| Edge | Book class page - booking form | good | good |
| Edge | My profile page | good | good |
| Edge | Edit profile - profile form | good | good |
| Edge | My bookings - list of upcoming bookings | good | good |
| Edge | My bookings - no upcoming classes | good | good |
| Edge | Edit booking page | good | good |
| Edge | Cancel booking page | good | good |
| Edge | Sign up page | good | good |
| Edge | Log in page | good | good |
| Edge | Log out page | good | good |


### Automated tests

Automated testing was done for both apps - Schedule, and User Profiles. In total, 81 tests were made - 55 tests for the Schedule app, and 26 for the User Profile app. 

__Schedule app testing__

1. test_models.py

26 tests ran successfully, checking the following:
- field labels, 
- max_length of CharFields, 
- default value of a field, 
- ForeignKey relationship between models, 
- string representation, 
- verbose name plural (for the models where it was set explicitly), 
- and ordering (if set in class Meta).

![Test results - models](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_s_models.png)

2. test_forms.py

10 tests ran successfully, checking:
- whether specific fields are required, or uneditable, 
- whether form field labels are shown correctly, 
- whether a field widget is a checkbox as expected, 
- and finally also whether a form is valid when specific criteria are met.

![Test results - forms](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_s_forms.png)

3. test_views.py

19 tests ran successfully, checking the following:
- whether views render correct templates,
- whether views restricted to logged-in users only redirect anyone who is not logged in,
- whether views can be accessed by their name,
- whether generic.ListView views actually show all items they should list,
- whether the url of a view exists at the expected location,
- whether listed objects are filtered as expected,
- whether listed objects are shown in the correct order,
- whether views redirect the user upon a successful interaction (e.g. upon cancellation of a booking),
- whether views handling the number and list of participants update data as expected.

![Test results - views](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_s_views.png)

__User Profiles__

1. test_models.py

2 tests ran successfully, checking:
- the maximum length of a CharField, 
- and the string representation of the Profile model. 

Since the only other model in the User Profiles app is the Django User model, I did not create additional tests here.

![Test results - models](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_up_models.png)

2. test_forms.py

13 tests ran successfully, checking the following criteria:
- max_length of certain fields,
- field labels,
- whether a field is required/not required,
- the placeholder value in one of the fields (date of birth - shown in the form for optimal user experience).

![Test results - forms](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_up_forms.png)

3. test_views.py

11 tests ran successfully, checking the following criteria:
- whether the url related to a view exists at a desired location,
- whether the url related to a view can be accessed by its name,
- whether the correct template is rendered,
- whether views restricted to logged-in users only redirect anyone who is not logged in,
- whether a view redirects the user after a successful interaction (e.g. updating a user profile).

![Test results - views](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/automated_tests/test_up_views.png)


### Notable Bugs

There are currently no notable bugs within the project. While I did encounter a few stubborn issues - especially around some views containing forms, and around creating specific dates for each weekly class - continuous manual testing during the development process as well as running automated tests to confirm that everything works as expected has led me to believe that all problems that have arised in the current form of this application have been resolved.


## Technologies Used

### Django
Django was used as the main framework for this project.

### Django AllAuth
Django Allauth was utilised to handle authentication and authorization and therefore manage user permissions.

### django-eventtools
A library utilised to create weekly occurrences of each weekly group class. 

### django-render-partial
A library used to embed a partial template (dates.html in the Schedule app) into another template (book_class.html). The dates.html template is connected to a specific view which ensures that 3 dates are created for the next 3 occurrences of a chosen class and shown in the booking form as a select (dropdown) field, so that the user can choose the best option from the available ones.

### DTL/Jinja
Jinja/Django templating language was used to insert data from the database into templates and to perform queries on specific datasets.

### Crispy forms
Django-crispy-forms was utilised to improve styling and ensure consistent design in any forms in the project

### Heroku
A cloud-based platform for deploying the site.

### PostgreSQL
PostgreSQL was used as the database for this project during both development and in production.

### JavaScript
JavaScript has been utilised to handle interactions with the waiver modal on the "Book class" page and the teacher bio modal on each "Schedule detail" page.

### Bootstrap 5
Bootsrap was utilised for creating a responsive layout.

### Font Awesome
It was used to access the calendar icons on the Schedule page.

### CSS
style.css file was created to handle custom styling beyond Bootstrap and introduce media queries for improved responsive design.

### HTML
HTML was utilised to create templates for each page.

### Packages Used

- Gitpod was used to develop the site
- GitHub was utilised for storing the files for this project
- Heroku was used to deploy the site
- Balsamiq was used to develop initial wireframes for the site (mobile version)
- DrawSQL.app was utilised to develop the database schema during development

### Resources Used

- [UUID generator](https://www.uuidgenerator.net/version4) utilised for automated tests
- [Favicon generator](https://favicon.io/favicon-generator/) used to create the website's favicons
- [Django secret key generator](https://djecrety.ir/) was utilised for creating a secret key for deployment on Heroku (SECRET_KEY config var)


## Deployment

The application has been deployed via Heroku and the live page can be found [here](https://namaste-yoga-studio-d494d1aeeada.herokuapp.com/).

This program was developed using [this particular template from the Code Institute](https://github.com/Code-Institute-Org/ci-full-template).

In order to deploy the application to Heroku I followed the following steps:
- Sign up or log in to Heroku.
- On the main Heroku dashboard page select "Create new app".
- Give the project a unique name, select a suitable region, and click "Create app". This will create the app in Heroku and bring you to the Deploy tab.
- Switch to the Settings tab. 
- In the "Config Vars" section click the "reveal config vars" button.
- Add the following key: DISABLE_COLLECTSTATIC, with the value 1 to prevent Heroku from uploading static files during the build.This key-value pair must be removed before final deployment.
- In the next KEY input field enter "SECRET_KEY" (all capitals), in the VALUE field next to it enter your secret key - you can create yours using [this Django secret key generator](https://djecrety.ir/). Then click the "Add" button to the right.
- Add another config var, with the KEY "DATABASE_URL" and the VALUE that is your PostgreSQL database's URL. Click "Add".
- The next config var, with the KEY "CLOUDINARY_URL" and the VALUE of your Cloudinary account's URL, allows you to use Cloudinary to upload and store images. Click "Add".
- Add also your "CLOUDINARY_NAME" as the next config var to ensure there are no issues with communication between the program and Cloudinary.
- To handle email authentication, add also these config vars:
  - EMAIL_HOST_PASSWORD, where the value is a 16-digit app password from a Gmail account to which you would like to connect the program - see more detailed information on that [here](https://support.google.com/mail/answer/185833?hl=en).
  - EMAIL_HOST_USER, where the value is the email address of the Gmail account with the app passcode.
- In the section "Buildpacks" click the "Add buildpack" button and select "python". Confirm by clicking the button "Add buildpack".
- Prepare the code for deployment in your local environment: use  pip install -r requirements.txt to install the libraries and packages needed to run the program (including gunicorn)
- In the Procfile add the following code:
web: gunicorn codestar.wsgi
- Make sure DEBUG = False in the settings.py file
- Also in settings.py, add '.herokuapp.com' to the list of ALLOWED_HOSTS
- Git commit and push the changes to your GitHub repository.
- Go back to your Heroku account, choose the Deploy tab at the top. 
- In the "Deployment Method" section choose the "GitHub" button. Follow the next steps (if any) as prompted to connect your GitHub account. In the "Connect to GitHub" section that appears, choose your account, enter the name of your repository, and select "Search".
-  Once your GitHub repo is connected to the Heroku app, scroll down to the section "Manual deploys".
-  Confirm that the correct branch of the repo is selected in the drop-down box, and select "Deploy Branch".
-  Heroku will now build the app for you. Once the process is completed, you will see the message "Your app was successfully deployed", and a link to the app where you can visit the live site.
  

## Cloning and forking the repository

In order to clone the GitHub repository use the following link:
- [https://github.com/Agnieszka-21/namaste-django.git](https://github.com/Agnieszka-21/namaste-django.git)

In order to fork the GitHub repository:
- Go to this [namaste-django repository](https://github.com/Agnieszka-21/namaste-django)
- In the menu at the top choose the option "Fork"
- You should now have your own repository inside your GitHub account.


## Credits

The following tutorials, articles, documentation and media were used to create this web application.

### Code

- [Django documentation](https://docs.djangoproject.com/en/4.2/) has been used extensively for this project
- Further helpful documentation was related to the libraries installed:
  - [django-render-partial](https://pypi.org/project/django-render-partial/) utilised for embedding a partial html template with dates for weekly classes into the book_class.html template
  - [django-eventtools](https://pypi.org/project/django-eventtools/) utilised for creating dates and times for 3 upcoming instances of each chosen group class
- [Cloudinary documentation](https://cloudinary.com/documentation) was used to set up the configuration between Django and the Cloudinary account
- The hero section of the homepage is loosely based on [this article](https://mdbootstrap.com/docs/standard/extended/hero/)
- Templates profile.html and profile_form.html are loosely based on this [User profile template](https://bbbootstrap.com/snippets/bootstrap-5-myprofile-90806631#) in regards to layout and styling.
- HTML and CSS code used to handle messages has been copied from [this article](https://www.brntn.me/blog/how-i-use-djangos-messages-framework/) by Brenton Cleeland.
- The footer has been adapted from [this tutorial](https://mdbootstrap.com/docs/standard/extended/social-media-icons-footer/).
- Navigation bar is loosely based on the CI walkthrough blog project and [this w3schools article](https://www.w3schools.com/bootstrap4/bootstrap_navbar.asp).
- The JavaScript code for trapping focus in a modal has been adapted from the [following article](https://hidde.blog/using-javascript-to-trap-focus-in-an-element/).
- The automatic creation of a profile when a User object is created was done with Django signals - code was copied (and slightly adapted) from the Code Institute's walkthrough project [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/profiles/models.py).

Please note that any code that has been copied or adapted from an external source has been also marked in the program files (comments were added with links to the sources and more exact information where applicable).


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
