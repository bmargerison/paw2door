# Paw2Door - An aggregator for Pet Rescues 
  The goal of this project was to create an aggregator for pet rescues to make it easier for people to adopt a pet.  
  This project was done as part of the Makers Academy final engineering project.

### How to run

Run the backend (from root directory):
```
pip install -r requirements.txt
python3 manage.py runserver
```

Run the frontend (from paw2door/frontend):
```
npm i
npm start
```

### User Stories

The user stories we followed when creating the project.

```
As a shelter
I want to be able to add a pet profile
So that a potential adopter see what pets we have

As a site visitor
I want to be able to see a list of all available pets for adoption
So that I can know which pets are available

As a site visitor
I want to filter the list of pets to my requirments
So that I can find a good fit for my needs

As a shelter
I want to be able to register my shelter
So that my shelter can be part of the site's listings

As a shelter
I want to add a photo to my pet profile
So that a potential adopter can see what the pet looks like

As a shelter
I want to be able to log in and log out
So that I can have control over my shelter

```

### Technologies 

This application was built using a tech stack of:
 - SQLite
 - Django
 - Django REST Framework
 - ReactJS (Reactstrap)

We chose these technologies because we needed to create a full stack application, and as part of our learning - we wanted to take on new technologies.

Django was chosen because the team wanted to learn python and we found Django to be one of the more popular backend solutions with built in SQLite support to handle the database.

React was chosen because we wanted a JS frontend which allowed for asynchronou functions so that our application could be a dynamic SPA. 

### Reflections

Using a new tech stack for the whole team was definitely a challenge, and a tech stack that I would describe as not the most beginner friendly. In some instances the team took the appraoch to getting a feature deployed as quickly as possible, even if later it could cause issues to build upon. 

The most significant issue was with login and token authentication. The team decided to split into 2 groups to try and come up with a solution, and then come together a couple of days later to choose the solution to go forward with. This is a credit to the team; we were adaptable and open to different ways of working, and also able to choose and discuss issues based on their merits to decide on a course of action.

From a personal perspective I also made great progress in my understanding of how React works, which is evidenced by the 'ShowPets.js' React hook. Having in the past used what I would describe as 'non React ways of doing things', getting user input in the correct way this opened a lot of doors and allowed me to iterate and build on top of this Hook.

### Improvements

* The main selling point of the app is the ability to locate pets close to the user. Our initial preference was to have a map with pins for each shelter, but after research we decided with our time frame this would not be possible.
* Providing the ability for someone looking to adopt to create an account would open the door to a lot of features, such as commenting, messaging etc.
* The pets could be further filtered, for example indoor/outdoor cats, certain medical conditions, gender etc.

### Known bugs and issues

* There is an inconsistent bug where after you have just logged in the filepath to the 'My Shelter' page won't be completed with the correct number, or directs to '/shelter/null'. I believe this is due to our quick fixes to the login solution resulting from erroneous component trees.
* When creating an account there is validation on the password field to ensure the password is unique enough, and that the email is unique. There are however no user prompts to inform that the account creation was not successful if they do not satisfy the criteria.
