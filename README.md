# Third Milestone Project / Grubhub
____
The live site: (https://database-milestone-project.herokuapp.com/)

Grubhub is a site to showcase my skills in my first Full Stack website. The purpose of the website is to allow a user to access the website to
view and search for recipes. The user will also have the option of registering an account on the website. Once they have done this the user
will then also have access to additional features of the website that allows them to create their own recipes and add them to the site. The 
user will also be able to view their own collection of recipes that they've added to the site and edit or delete them.

## UX Design:

### Strategy

#### Who is this for?
This website is available to any user on the web who wishes to find recipes. The site is also for anyone who wishes to 
create an account in order to build and manage their own collection of recipes. 

#### What type of content will be relevant? 
The content on the site will be made up of a collection of recipes built by the site administrator and the users themselves.

Media content – The recipes will be displayed in a card format. Each card will have an image so the users can easily see what
                recipe they would like to choose.

### Scope

#### What does the client need?
* A brand name to help make the site more recognisable and create a sense of familiarity.
* A mobile first website approach
* A "Recipes" page displaying all of the recipes added by users, including a brief outline of what each recipe is.
* A "My Recipes" page for the user to display all of the recipes in their personal collection.
* A registration page for a user to create an account.
* A login page
* An "Add recipe" page
* A "View recipe" page
* An "Edit recipe" page
* A "Delete recipe" button

#### User scenarios
**Scenario:**
A user would like to view a recipe ---  
**Requirement:**
The ability to click on a recipe and be redirected to a page where they can view all of the details of that recipe.

A user would like to view all recipes ---  
**Requirement:**
The ability to click on a recipes navigational link and be redirected to a page where they can view all of the 
recipes onthe website

**Scenario:**
A user wants to view other recipes available on the site ---  
**Requirement:**
The ability to view a collection of recipes added to the site.

**Scenario:**
A user wants to search for a specific recipe ---  
**Requirement:**  
A search bar that allow the user search for a recipe.

**Scenario:**
A user would like to create an account ---  
**Requirement:**  
A registration page that contains a form allowing the user to create their account.

**Scenario:**
A user would like to add a recipe ---  
**Requirement:**  
An add recipe page that contains a form to add a new recipe.

**Scenario:**
A user would like to view all of their own recipes ---  
**Requirement:**  
A "My recipes" page that contains all of the recipes added by that specific user.

**Scenario:**
A user would like to edit one of their own recipes ---  
**Requirement:**  
An edit recipe button and page. The page contain the same form as the add recipe page, pre-populated with the content of that recipe.

**Scenario:**
A user would like to delete one of their own recipes ---  
**Requirement:**  
An delete recipe button that allows the user to delete one of their own recipes.


### Structure

#### Information Architecture
For this project I will be using a standard tree structure. To achieve this, the header of each page will 
consist of a navigation bar that contains the logo of the business and the main navigational links for each page in the website. 


## Features

### Existing Features
* Feature 1 - A "recipes" page that displays all of the recipes in the database in the form of cards.

* Feature 2 - A registration form that allows the user to create an account.

* Feature 3 - A login form that allows the user to log in to their account.

* Feature 4 - An "add recipe" form that allows the user to add a recipe.

* Feature 5 - A "My recipes" page for the user to view their own collection of recipes.

* Feature 6 - An "edit" button. If the user is viewing one of their own recipes they can edit that recipe.

* Feature 7 - An "edit recipe" form that allows the user to edit one of their own recipes. It will render pre-populated 
                with the data contained in the recipe. T

* Feature 8 - A "delete" button that allows the user to delete one of theor own recipes.
 

## Technology's Used:
Information Architecture

For this project I will be using a standard tree structure. To achieve this, the header of each page will 
consist of a navigation bar that contains the logo of the business and the main navigational links for each page in the website. 
* [HTML5](https://www.w3schools.com/html/html5_intro.asp) - A markup language used to create the structure of the webpage.
* [CSS3](https://www.w3schools.com/css/) - Used to style the HTML code. 
* [Bootstrap4](https://getbootstrap.com/) - A front-end component library used to build responsive mobile-first desifn for this webpage.
* [Font Awesome](https://fontawesome.com/) - An icon library and toolkit used to implement various icons and social logos on this webpage.
* [JavaSccript](https://www.javascript.com/) - A high-level, interpreted programming language used to mange the interactivity of the site by
                                                controlling the behaviour of elemetns on the page when a user interacts with them.
* [jQuery](https://jquery.com/) - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling.
* [Gitpod](https://github.com/gitpod-io/gitpod) - The is the IDE used to write and test the code for this project.
* [Git](https://git-scm.com/) - Git is a tool that is used to track and store changes to your codes as you work. It stores your code in a local repository.
* [Github](https://github.com/) - Github is a remote repository used to store all of the code for this project.
* [Python 3](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language. In this project it was
                                        used to manage the back end development of the project.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is a micro-framework which depends on Jinja and Werkzeug to manange html templates
                                                         and create and render views for each page in the project.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform as a service. Heroku is used to deploy this project.
* [MongoDB](https://www.mongodb.com/cloud/atlas) -a NoSQL document-oriented database program that uses JSON like documents with schema

## Testing
In order to ensure the website functioned as expected, all of the testing for this project was done using the browser web developer tools. This was a very 
important tool for me through the creative process as it helped me to isolate where the problems were in my code. The issues that this helped me resolve 
include:

* Test my python application
  The very first thing to test in this project was my python application setup.
1. Create a root view that renders a simple h1 tag with the content "Hello World".
2. Run the application via the terminal.
3. Check to see that the element is rendered.

* Test a template:
  The second thing to test in this project was the templates.
1. Create a base template
2. Create an index template containing a h1 tag with the content "index template"
3. Run the application via the terminal.
4. Check to see that index.html is rendered.

* Connection to the database:
  Next I tested the connection to my MongoDB database.
1. Create a sample recipe in the database.
2. Create a function in the index view to return everything from the database.
3. Add the html to return everything from the document into an unordered list
4. Run the application through the terminal and verify that the contents of the document
   are displayed and the connection to the database secure.

* Navigation bar links:
1. Click each link and check to that each page is rendered.

* Registration form - databse connection:
1. Fill out the form and click the submit button to see if I am redirected back to the home page.
2. Check the database to see if the document has been submitted.

* Registration form - empty/partially filled form:
1. Try to submit form with empty fields
2. Partially fill out the form.
3. Try to submit a partially filled form and check for the required field messages.

* Registration form - password field:
1. Start typing
2. Check to see password message is displayed when the user starts typing.
3. Type a password 8 characters long.
4. Check to see the password message disappears.
5. Delete some characters so the password is less than 8 characters long. 
6. Check to see that the password message reappears.
7. Type in a password less than 8 characters.
8. Click out of the password input field.
9. Check to see that the password message remains if the password entered is less than 8 characters.

* Registration form - repeat password field:
1. Start typing a the repeat password.
2. Check to see that the repeat password message appears.
3. Check that the submit button is disabled if the passwords do not match.
3. Type the same password and check to see that the message changes accordingly when the passwords match.
4. Click the submit button to verify that the submit button has been re-enabled.

* Registration form - username field:
1. Type in a username that exists in the database.
2. Fill out the form.
3. Submit the form.
4. Check to see that the flash message is displayed when the user tries to enter a username that already exists.

* Login form:
1. Create an account.
2. Enter the username of the account in the login form.
3. Enter an invalid username and click login.
4. Check to see that the invalid username message is displayed.
5. Enter the correct username and click login to check that the user is redirected to the index page.
6. Check for the welcome message in the navbar.
7. Login again with the correct username.
8. Enter an incorrect password and click login.
9. Check to see that the invalid password messaage is displayed.

* Add Recipe Feature:
1. Login and navigate to the Add recipe page
2. Fill out the form and click submit
3. Check to see that the user is redirected to the index page and the recipe has been added to the recipes page.

* Edit Recipe Feature: 
1. Login and navigate to "My recipes"
2. Click a recipe to view and navigat to the "view recipe" page.
3. Click on on the edit button and navigate to the "edit recipe" page
4. Check to see that the form is pre-populated.
5. Change something in the recipe and click submit.
6. Check to see that the user is redirected to the "view recipe" page and the recipe has been updated accordingly.

* Delete Recipe Feature:
1. Login and navigate to "My recipes".
2. Click a recipe to view and navigate to the "view recipe" page.
3. Click the delete button and check to see that the user is redirected to the "recipes" page and the recipe has been deleted.

I used a *code validator* on [W3 Markup Validation Service](https://validator.w3.org/#validate_by_input) to checks for any errors that needed to be 
fixed in my code. 

Finally, I posted my project in the peer-code-review channel on Slack and received some very helpful criticism to help me fix some mistakes that 
slipped under the rader.

## Features Left to implement
The only feature in the project I could not get working was the search bar functionality. The search bar does not yield
any results at the moment. 

## Deployment 
1. The project was written and developed in the Gitpod IDE.
2. A local repository was intialized using Git. Regular changes were commited to the local repository.
3. Github was used as a remote repository, and at the end of each development session, all local commits were pushed to (https://github.com/martycistudent/milestone-project3)
4. The project’s source file was published from GitHub repository to GitHub pages using GitHub default settings via the master branch.
5. The project was linked to Heroku for deployment, a requirements.txt file and a Procfile were created to deploy the project on Heroku.
6. Configuration variables had to be set in order to get the project running. These had to be set in both the Gitpod IDE and on Heroku.
These included, PORT, IP, Mongo URI and a SECRET KEY.
5. The Project’s source file is now published as a site on Heroku at [Grubhub](https://database-milestone-project.herokuapp.com/)

## Credits
### Media 
The full width background image on the index page of the website was taken from a stock image website called [shutterstock](https://www.shutterstock.com/search/food+background) 

### Acknowledgements 
#### Front End Design
For the main layout of this project I took inspiration from [Jamie Oliver's cooking website](https://www.jamieoliver.com/) and [BBC goodfood](https://www.bbcgoodfood.com/).
This is also where I found most of the recipes to populate the website. 

#### Back End
To complete this project I relied on additional reasearch in order to get the reistration and login features of the page fully 
functional.

To help me understand the logic required for the registration and login features of my site I watched this video:
* (https://www.youtube.com/watch?v=vVx1737auSE)
In order to create a form that could check whether or not the passwords enterd matched certain criteria I found these pages
that helped me figure out how to access the values being entered, as well as the appropriate event handlers I needed to use.
* (https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518)
* (https://www.w3schools.com/howto/howto_js_password_validation.asp)
To use message flashing I had to read the documentation for the Flask website to help me unserstand how Flask messagin worked.
* (https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)
To get the search bar functioning I relied on the code provided to me by my mentor who helped me to undertsand how it worked
* (https://github.com/5pence/recipeGlut/blob/master/app.py)