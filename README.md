# Django News Site Project

Heroku Deployment: https://still-hamlet-62827.herokuapp.com/news/

# Features Implemented
● Order the stories by date 

● Style the form for adding new stories - styled

● Add a field to the NewsStory model for an image url and use this image url rather than the default
images provided in the starter

● Functional login/logout buttons

● Account view so authors can see their profile information - Profile Information Page, shows username

● Create Account functionality, so a new user can sign up to be an author

● View stories by a particular author - when clicking the name of an author of a story, redirects to a page solely of that author's stories. 

● Show/Hide the relevant information and buttons based on whether the user is logged in/out (e.g.
should only be able to see the button to create a new story if I am logged in) - Write Story button displays only whilst logged in, Welcome message displays only when logged in, Log Out option displays only when logged in, Username on navbar only displays once logged in.

● Enable/Disable the relevant features based on whether the user is logged in/out (e.g. should only be
able to create a new story if I am logged in) - Write Story functionality only available when logged in, Delete and Edit of a story only available if the author ID is equal to the User ID (i.e owner of the story), only able to view User Information is logged in.

# Additional Features
● Add the ability to update and delete stories - options to edit/delete only shown for the owner of that post.

Additional Info:
- Links to Sign up and Login in Pages when user is logged out and trying to access a logged-in piece of functionality (edit/delete story/user profile page)
- Upon clicking author title and redirecting to stories by that author page, clicking the article again redirects to that single article page.
- Change the title of each page, so that the story title displays on the browser tab.
