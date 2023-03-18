# Manual testing

[Back to README](README.md)

# Home page

## [Introduction](https://github.com/EmelieMarkkanen/make-it-sew/issues/1)
- The website features an informative text on the homepage, explaining the purpose and idea of the site.

## [Navbar and footer](https://github.com/EmelieMarkkanen/make-it-sew/issues/2) 
- The website feature a navbar and footer that are present on all pages throughout. 
- The links in the navbar change depending on whether a user is logged in or not, showing different features.
- The links are informative and lead to the correct respective pages.
- The navbar and footer are responsive to different screen sizes. 
- The footer links open in new tabs.

## [Featured patterns](https://github.com/EmelieMarkkanen/make-it-sew/issues/5) 
- The home page features cards with featured patterns with an image, excerpt, author and heading. Card heading link to corresponding pattern.
- The home page features a button visible to logged out users, referring the user to sign in to be able to view all patterns. 

# Detailed pattern page

## [Detailed pattern description](https://github.com/EmelieMarkkanen/make-it-sew/issues/6)
- The detailed pattern page feature the title, author and description of the pattern post.

## [Pattern difficulty](https://github.com/EmelieMarkkanen/make-it-sew/issues/15)
- The detailed pattern page feature the difficulty setting of the posted pattern.

## [Suggested fabrics](https://github.com/EmelieMarkkanen/make-it-sew/issues/16)
- The detailed pattern page feature the suggested fabrics for the posted pattern. 

## [Edit pattern button](https://github.com/EmelieMarkkanen/make-it-sew/issues/46)
- For a signed in user that is the author of the pattern post an Edit button is visible.
- When clicked, the button redirects the user to the edit pattern page.
- The edit button is only available to a user who is logged in AND the author of a pattern post. 

## [Delete pattern button](https://github.com/EmelieMarkkanen/make-it-sew/issues/30)
- For a signed in user that is the author of the pattern post a Delete button is visible.
- When clicked the button triggers defensive programming, asking if the user really want to delete the pattern.
- If the user clicks the Delete button in the triggered modal the pattern is deleted and the user is redirected to the My patterns page.
- If the user clicks Cancel in the triggered modal it is closed. 
- The delete button is only available to a user who is logged in AND the author of a pattern post. 

## [View pattern button](https://github.com/EmelieMarkkanen/make-it-sew/issues/20)
- For a signed in user that is not the author of a pattern post a View pattern button is visible.
- When clicked the button open a PDF in a new tab, a facsimile for a PDF pattern. Further comments about this can be read [here](https://github.com/EmelieMarkkanen/make-it-sew/issues/40)
- For a signed out user the button refers the user to the sign in page. 

## [Commentform and submit button](https://github.com/EmelieMarkkanen/make-it-sew/issues/11)
- The detailed pattern page features a comment form and submit button.
- A signed in user can post a comment. 
- After admin approval the comment is visible on the page. 
- For a signed out user the submit button instead refer them to the sign in page. Commenting is only available to signed in users. 

## Like button
- The detailed pattern page features a heartshaped like button. 
- When clicked once the like button increase the amount of likes and change the color of the button icon. 
- When clicked again the amount of likes decrease and the color of the icon change back.
- The like button is only useable by signed in users.  
- A signed out user will only see a heartshaped icon and number of likes, that is not clickable. 

### Notifications
- If a user tries to post an invalid comment form they are notified to fill out required fields. 
- When clicking the like button the user is notified that the pattern have been saved or removed from the Liked pattern page. 

# All patterns

## [All patterns page](https://github.com/EmelieMarkkanen/make-it-sew/issues/19)
- The all patterns page features a list of all patterns posted on the website.
- The page is only available to signed in users. 
- The posts are displayed as cards, linking to the detailed page about each pattern. 
- The page is paginated by 9 items. 

# My patterns

## [My patterns page](https://github.com/EmelieMarkkanen/make-it-sew/issues/18)
- The my patterns page features a list of all patterns posted by the signed in user.
- The page is only available to signed in users. 
- The posts are displayed as cards, linking to the detailed page about each pattern. 
- The page is paginated by 6 items. The pagination is only visible if the user have posted more than 6 items.
- If the user have not posted any patterns a message is displayed instead, with a button referring the user to the Post pattern page.

# Liked patterns

## [Liked patterns page](https://github.com/EmelieMarkkanen/make-it-sew/issues/17)

- The liked patterns page features a list of all patterns liked by the signed in user.
- The page is only available to signed in users. 
- The posts are displayed as cards, linking to the detailed page about each pattern. 
- The page is paginated by 6 items. The pagination is only visible if the user have liked more than 6 items.
- If the user have not liked any patterns a message is displayed instead, with a button referring the user to the All pattern page.

# Post pattern

## [Post pattern form](https://github.com/EmelieMarkkanen/make-it-sew/issues/21)
- The post pattern page features a form for posting a pattern to the website.
- The page is only available to signed in users. 
- The form lets the user add a title, description, pdf, image, set difficulty and suggestion of fabrics. 
- When a valid form is submitted the user is redirected to the Post pattern page again.

### Notifications
- If a user tries to post an invalid pattern form they are notified to fill out required fields.
- When submitting a valid pattern form the user is notified that the pattern will be available after approval from a site administrator. 

# Edit pattern

## [Edit pattern form](https://github.com/EmelieMarkkanen/make-it-sew/issues/46)
- The edit pattern form page features a prepopulated form. 
- The page is only available to signed in users who are the author of the specific pattern. 
- The form lets the user edit the title, description, pdf, image, difficulty setting and fabric suggestions. 
- When a valid form is submitted the user is redirected to the My patterns page. 

### Notifications
- If a user tries to post an invalid edit pattern form they are notified to fill out required fields.
- When submitting a valid edit pattern form the user is notified that the pattern will be available again after approval from a site administrator. 

# [Sign in](https://github.com/EmelieMarkkanen/make-it-sew/issues/13)
- The sign in page features a form with username and password fields. 
- The page features a button to submit the form. 
- The page also features a checkbox to save the users username and password.
- The page also features a link to the sign up page, if the user have not yet registered with Make it Sew.
- When submitting a valid form the user is redirected to the home page as a signed in user. 

### Notifications
- If the user tries to post an invalid sign in form they are notified to fill out the required fields.
- If the user tries to enter an invalid username or password they are notified with the message: `The username and/or password you specified are not correct.`

# [Sign out](https://github.com/EmelieMarkkanen/make-it-sew/issues/14)
- The sign out page features a message asking if the user want to sign out from Make it Sew: `Are you sure you want to sign out?`
- The page features a button, that when clicked redirect the user to the home page as a signed out user.

# [Sign up](https://github.com/EmelieMarkkanen/make-it-sew/issues/12)
- The sign up page features a form with username, password and email (optional) fields. 
- The page features a button to submit the form. 
- The page also features a link to the sign in page, if the user is already registered with Make it Sew. 
- When submitting a valid form the user is redirected to the home page as a signed in user. 

### Notifications
- If the user tries to post an invalid sign in form they are notified to fill out the required fields.
- If the user tries so sign up with a username that already exists in the database they are notified to sign up with a different name: `A user with that username already exists.`
- If a user tries to sign up with an invalid password they are notified and asked to fill out a different password: `The password is too similar to the username.`
- If a user tries to sign up with a too short password they are notified and asked to fill out a different password: `This password is too short. It must contain at least 8 characters.`

# [404](https://github.com/EmelieMarkkanen/make-it-sew/issues/34)
- If a user attempts to access a URL on Make it Sew that doesn't exist, the 404 page will be triggered. 
- The user is notified via a message that the page doesn't exist, and provides a button redirecting them back to the home page. 

# [500](https://github.com/EmelieMarkkanen/make-it-sew/issues/44) 
- A 500 error message is triggered if there is a server-side error preventing the page from loading.
- The user is notified via a message that something went wrong and some possible solutions to the issue, and provides a button redirecting them back to the home page. 

# Django administration

- [A superuser can log in](https://github.com/EmelieMarkkanen/make-it-sew/issues/3) to the administration portal via the link: https://make-it-sew.herokuapp.com/admin
- Once logged in a superuser can administer users, posted patterns and posted comments

    ### Users

    - A superuser can create new users
    - A superuser can delete users 

    ### [Patterns](https://github.com/EmelieMarkkanen/make-it-sew/issues/4)

    - [A superuser can create a new pattern post](https://github.com/EmelieMarkkanen/make-it-sew/issues/9)
    - A superuser can edit a posted pattern
    - [A superuser can delete a posted pattern](https://github.com/EmelieMarkkanen/make-it-sew/issues/10)
    - A superuser can set a pattern as featured
    - A superuser can approve a posted pattern

    ### [Comments](https://github.com/EmelieMarkkanen/make-it-sew/issues/4)

    - [A superuser can create new comments](https://github.com/EmelieMarkkanen/make-it-sew/issues/24)
    - A superuser can edit comments
    - A superuser can delete comments
    - [A superuser can approve posted comments](https://github.com/EmelieMarkkanen/make-it-sew/issues/8)
    

