# Third Milestone Project / Grubhub
____

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

Branding - the logo should be heavily emphasized and unique. I want to establish a font as well as a colour scheme.

Media content – The recipes will be displayed in a card format. Each card will have an image so the users can easily see what recipe 
                they would like to choose.

Social media –  to further promote the site across other social media platforms.

### Scope

#### What does the client need?
* A brand name to help make the site more recognisable and create a sense of familiarity.
* A mobile first website approach
* A catalogue page displaying any recipes added by users, including a brief outline of what each recipe is.
* A catalogue page displaying all of the recipes added by a user. 
* A registration page
* A login page
* Links to their social media pages

#### What else can we provide for the client?
* A news section that will update fans with any new products that are being released, or any new updates or bug fixes for current products
* A contact section to leave feedback about games, or for any potential collaborations with other people or businesses in the industry.

#### User scenarios
**Scenario:**
A user would like to view a recipe ---  
**Requirement:**
The ability to click on a recipe and be redirected to a page where they can view all of the details of that recipe.

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

### Structure

#### Information Architecture
For this project I will be using a standard tree structure. To achieve this, the header of each page will 
consist of a navigation bar that contains the logo of the business and the main navigational links for each page in the website. 

### Skeleton

#### Wireframe
[A link to my Mobile wireframe]()
[A link to my Desktop wireframe]()

## Features

### Existing Features
* Feature 1 - A subscribe bar at th very top of the page that allows th user to subscribe for updates and notifications by submitting their email address 
                 in a pop up modal.

* Feature 2 - A games catalogue that take the form of cards allows the user to hover over the card and click it which will take them to the playstore/appstore
                to download the game.  

* Feature 3 - A slideshow allows the user to viewport screenshots and covers for the different gsmes so they have abetter understanding of what each game is about.

* Feature 4 - A contact page allows the user to get in touch with the company about working on projects together in the future, or to leave feedback about games.

* Feature 5 - Social media links allow users to view the companies social media pages to view and share content.

* Feature 6 - A return to top button allows the user to navigate back to the top of the page when they click it.

* Feature 7 - Hover effects help users to identify buttons by changing color and size (navbar). 
 

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
* [Gitpod](https://github.com/gitpod-io/gitpod) - The is the IDE used to write and test the code for this project.
* [Git](https://git-scm.com/) - Git is a tool that is used to track and store changes to your codes as you work. It stores your code in a local repository.
* [Github](https://github.com/) - Github is a remote repository used to store all of the code for this project.
* [Python 3](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language. In this project it was
                                        used to manage the back end development of the project.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is a micro-framework which depends on Jinja and Werkzeug to manange html templates
                                                         and create and render views for each page in the project.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - Heroku is used to deploy this project.

## Testing
In order to ensure the website functioned as expected, all of the testing for this project was done using the browser web developer tools. This was a very 
important tool for me through the creative process as it helped me to isolate where the problems were in my code. The issues that this helped me resolve 
include:

* Test my python application
The very first thing to test in this project was my python application setup.
1. Create a root view that renders a simple <h1> tag with the content "Hello World".
2. Run the application via the terminal.
3. Check to see that the element is rendered.

* Test a template:
The second thing to test in this project was the templates.
1. Create a base template
2. Create an index template containing a <h1> tag with the content "index template"
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
1. Click each link on the main page to verify they work.
2. Navigate to each page from the index page

* Registration form:
1. Try to submit form with empty fields
2. 

* Login/ Modal:
⋅⋅1. Click "login" button.
⋅⋅2. Try to submit without any information and verify that an error message about the required fields appears.
⋅⋅3. Try t submit an invalid email address and and verify that a relevant error message appears.
⋅⋅4. Verify that a successful message appears by submitting a valid email address.

* Grid system:
⋅⋅1. Open bwoser developer tools. 
⋅⋅2. Display device toolbar. 
⋅⋅3. Select iPhone 5SE.
⋅⋅4. Review layout for small screen widths.
⋅⋅5. Select Ipad in the device toolbar.
⋅⋅6. Review layout for medium screen widths.
⋅⋅7. Select Laptop in the device toolbar.
⋅⋅8. Review layout for large screen sizes.
⋅⋅9. Make any necessary changes. 

* Layout - mostly padding and margins, to ensure adequate spacing between elements as well as sizing for elements.

* Media queries - certain elements that might overflow such as titles, on very small screen sizes. Viweing the change of elements with screen sizes allowed
  me to make the necessary changes so that elemnts were proportional across differnet screen widths. 

I used a *code validator* on [W3 Markup Validation Service](https://validator.w3.org/#validate_by_input) to checks for any errors that needed to be 
fixed in my code. 

Finally, I posted my project in the peer-code-review channel on Slack and received some very helpful criticism to help me fix some mistakes that 
slipped under the rader.

## Deployment 
1. The project was written and developed in the Gitpod IDE.
2. A local repository was intialized using Git. Regular changes were commited to the local repository.
3. Github was used as a remote repository, and at the end of each development session, all local commits were pushed to ()
4. The project’s source file was published from GitHub repository to GitHub pages using GitHub default settings via the master branch.
5. GitHub Pages was then enabled to publish the site from the master branch following this path:
.. 1. GitHub repository settings page.
.. 2. Scrolling down to the GitHub Pages Repository box, the master branch was selected from the dropdown menu.
.. 3. The action was saved by clicking the save button.

6. The Project’s source file is now published as a site on GitHub Pages at [Astirian-Rae Games](https://martycistudent.github.io/First-milestone-project/)

## Credits
### Media 
The full width background image on the index page of the website was taken from a stock image website called [shutterstock](https://www.shutterstock.com/search/food+background) 

### Acknowledgements 
#### Front End
For the main layout of this project I took inspiration from [Jamie Oliver's cooking website](https://www.jamieoliver.com/) and [BBC goodfood](https://www.bbcgoodfood.com/).
This is also where I found most of the recipes to populate the website. 

#### Back End
To complete this project I relied on additional reasearch in order to get the reistration and login features of the page fully functional.

