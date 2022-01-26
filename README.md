**Author:** Stina Axelsson

# Project Description
This project is developed as my 4th portfolio project during my course at Code Institute and I call it Utopi'Ally Community.
Utopi'Ally Community is a social media website, where you can register an account, login and create a user profile. You can upload posts with text and images on a feed for others to like and comment. You can follow other users and get along with them in a private chat. It is a small and friendly community for spiritual awaken people that want to find friends with the same interests.
 
# Content
* [Project Description]()
* [UX]()
  * [User Stories]()
  * [Site Owner Goals]()
  * [Structure]()
  * [Wireframes]()
* [Features]()
  * [Existing Features]()
  * [Data storage]()
  * [Features Left To Implement]()
* [Technologies Used]()
  * [Languages]()
  * [Frameworks]()
  * [Other Programmes]()
* [Testing]()
  * [Validator Testing]()
  * [Manually test user storys]()
  * [Bugs]()
* [Deployment]()
* [Credits]()
* [Ackmowledgements]()
# UX
## User Stories
### EPIC 1 Setup
* As a user I can easy and safely register an account so that I can use my account for the websites purpose
* As a user I can use my email or username so that i can login with my account
* As a user I can easy find where to register and create an account so that I can be a member and join the community
* As a user I can see all of the uploaded photos in a feed at the landingpage so that I can follow up what has been uploaded
* As a user I can easy navigate through the site from anywhere I am on the site so that make it easier to use and do what I suppose to
### EPIC 2 Profile
* As a user I can Edit my profile page, add/edit and delete pictures and information so that I can control what to share and make my profile more flexible
* As a user I can Add and change my profile image so that Other users can see who I am
* As a user I can Add information in my biography about myself so that other users get to know me better by my profile page
* As a user I can save all my posts in my page so that it is easy to view what I uploaded and to see what other users have shared on their profiles
* As a user I can choose to upload something from the homepage or from anywhere I am on the site so that I don't have to go back or forward to do that task
* As a user I can like a photo from the feed so that the user who uploaded the post can see that I liked it
* As a user I can make a comment/edit or delete it on a users post so that I can give feedback or discuss what users upload and regret if I want to change or remove it
* As a user I can edit or delete my own uploaded posts so that I can change something in my already uploaded post or delete if I regret uploading it

### EPIC 3 Search users
* As a user I can search after other users by other username, name, location so that I can find other users in my location or find a user that I want to check out their profile page
* As a user I can Add a friend in a friend list, or followlist so that I can see what this person uploads easy and get in touch
* As a user I can unfollow or unfriend a user so that I can regret or if I follow by mistake can undo it

### EPIC 4 Direct Messages
* As a user I can Send a private message to an other user so that Its easy to start a conversation and speak to other users one by one
* As a user I can get private messages from other users in a inbox so that I can sort and see where my messages goes and saves
* As a user I can Delete messages from my inbox so that I easy can clear my inbox and delete those who I don't want to save


## Site owner goals
## Structure
* Landing page/start page for un authentical users.
Showing some information of what the site is about, have an about us file and a login and register form.  
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/landindpage.png)  
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/start%20menu.png)
* Landingpage for logged in users
  * Feed, when user sign up they are provide some information of how to upload, create more information in profile page, this text will dissapere when the user upload their first post or start follow users who have upload posts earlier.  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/landing%20for%20new%20register.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/nav%20bar%20logged%20in.png)
* Profile page
  * Personal page for the user, with fields of information to add about themself
  * Add profile image and edit profile.
  * See how many followers (moon friends) they have and a button to follow or unfollow other users.
  * Uploaded posts that the user have is collected on their own pages.  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/profile%20page.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/edit%20profile.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/all%20post%20on%20profile.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/follow%20button.png)
* Inbox
  * An inbox that collect all active threads
  * Start a new chat and search for user to start chat with
  * The conversation/chat with send and received messages  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/inbox.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/search%20chat.png)
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/conversation%20inbox.png)
* Search
  * search input box on its own template, from the navbar
  * shows all users that include the search query.  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/search.png)
* Upload
  * From navbar users can upload a post/image that uploads in the feed (and profile page)  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/upload.png)
* post detail
  * When user want to comment or like, you have to click on the post to get more details and show comments.
  * From post detail you can edit or delete your own posts and delete comments that user have made.  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/post%20detail.png)
* Footer
  * contains links to site owners social media  
  ![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/footer.png)
## Design Choises
### Fonts
I have two main fonts from Google Fonts. 
'Handlee' and 'Dancing script' that meet up my thoughts of how i want a first time user want to feel when they visit. Soft and friendly and kind of playful. Using this in the Logo and as rubric. And Handlee is using as rubrics and bread-text.
### Colours
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/colours.png)
Main colour is white, with details as in navbar and footer with the gradiant mix of #A6BFFF and #A4EAC0 and for all the buttons on the page. The #F7BAF0 is used for smaller details and some hover colours and the receivers chat bubble. The colours combine is soft, beautifyl and gives the impression that i seeking for in the theme of the site.
## Wireframes
I have been following the structure from the wireframes, with some changes for message and the notifications that i chose to not go with on this project for the lack of time and knowledge for that.
* [Desktop](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/wireframes/browser%20wireframes.pdf)
* [Tablet](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/wireframes/Tablet%20wireframes.pdf)
* [Mobile](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/wireframes/Mobile%20wireframes.pdf)
# Features
## Data storage
### Post model
| Title      	| Key in Database   	| Form Validaton 	| Data Type       	|
|------------	|-------------------	|----------------	|-----------------	|
| body       	| body         	| max_length=500 	| TextField       	|
| created_on 	| created_on 	| None           	| DateTimeField    	|
| author     	| author              	| None           	| ForeignKey      	|
| upload     	| upload             	| image          	| CloudinaryField 	|
| likes      	| likes             	| None           	| ManytoManyField 	|
### Comment model
| Title      	| Key in Database   	| Form Validaton 	| Data Type     	|
|------------	|-------------------	|----------------	|---------------	|
| comment    	| comment           	| max_length=500 	| TextField     	|
| created_on 	| created_on 	| None           	| DateTimeField 	|
| author     	| author              	| None           	| ForeignKey    	|
| post       	| post              	| None           	| ForeignKey    	|
### Users (profile)
| Title     	| Key in Database   	| Form Validaton          	| Data Type       	|
|-----------	|-------------------	|-------------------------	|-----------------	|
| username      	| user 	| None                    	| OnetoOneField   	|
| name      	| name              	| max_length=50           	| CharField       	|
| profile picture   	| picture             	| None                    	| CloudinaryField 	|
| birthday  	| birthday          	| blank=True              	| DateField       	|
| gender    	| gender  	| default=Gender.other.id 	| IntegerField    	|
| location  	| location          	| max_length=100          	| CharField       	|
| bio       	| bio               	| max_length=500          	| TextField       	|
| followers 	| followers         	| User, blank=True        	| ManyToManyField 	|
## Existing features
* Create an account
* Login as existing user
* Add information on an profile page
* Upload texts and images saved on the profile page
* Share posts with other users 
* Follow or unfollow other users 
* Edit profile page
* Like and comment other posts 
* Edit or delete posts
* Delete comments
* Send private messages to other users
* Delete threads from inbox
* search for other users by username
* Visit other users profile pages

## Features left to implement
Features I want to implement in future for this project is
* Notifications for when users get new followers, likes or comments
and for messages. This feature is something I want to add for expand the users experiance for a social media site!
* To see a list of the users that follows you, or follow other users.
# Technologies used
## Languages
* HTML5
* CSS
* Javascript
* Python
## Frameworks
* Django
* Bootstrap
* Jquery
## Other programmes
* [Heroku](https://id.heroku.com/login) - Deploy my site
* [Pep8](http://pep8online.com/) - Validate python code
* [Gitpod](https://gitpod.io/workspaces) - My workspace 
* [GitHub](https://github.com/) - Make my repository and save my user storys and code.
* [Am I responsive](http://ami.responsivedesign.is/) - Fix the photo for the readme
* [Balsamiq](https://balsamiq.com/) - Make my wireframes
* [Font Awsome](https://fontawesome.com/) - Got all the icons for the site
* [Google Fonts](https://fonts.google.com/) - Got my fonts
* [W3C Validator](https://jigsaw.w3.org/css-validator/validator.html.en) - Validate CSS and HTML
* [JShint](https://jshint.com/)
* [Markdown table generator](https://www.tablesgenerator.com/markdown_tables#) - Help with generate my tables for the readme
* [Color palett generator](https://coolors.co/) - Make my palette of colors
* Chrome Devtools - Fins issues, bugs and errors during the development on the liveserver.
* [Cloudinary](https://cloudinary.com/) - Store all the static images that users upload on the site.
# Testing
I have testing this project with manual testing. I have test i by myself during the development and once it was deployed, I got help by my family to improve and find bugs.
## Manual testing by user storys
### EPIC 1
**Implementations**: As a user I can easy and safely register an account so that I can use my account for the websites purpose.   
**Test**: I test this with first installing allauth, getting urls done and the templates, I try register and the account created, i use receive signals for register users for saving them without errors in database.  
**Result**: This test pass and works fine.  

---
**Implementations**: As a user I can use my email or username so that i can login with my account  
**Test**: Testing this by log in with the created account after logging out, using the chosen username when registerd. Not using Email for this site.
**Result**: This test pass and works how it should.

---
**Implementations**: As a user I can easy find where to register and create an account so that I can be a member and join the community  
**Test**: During the site, there is options on the landingpage and about us page to register and login and in the menu in navbar.  
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can see all of the uploaded photos in a feed at the landingpage so that I can follow up what has been uploaded    
**Test**: When user is logged in, there is a feed page for all the posts, the user have to upload something first or follow other users that have upload posts to see them in their personal feed.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can easy navigate through the site from anywhere I am on the site so that make it easier to use and do what I suppose to.      
**Test**: User have access to the navbar menu from anywhere you are on the site, with options to upload, go to inbox, go to home/feed or search, go to orofile page or logout from the menu.    
**Result**: This test pass and works how it should.   

---
### EPIC 2 Profile
**Implementations**: As a user I can Edit my profile page, add/edit and delete pictures and information so that I can control what to share and make my profile more flexible.      
**Test**: From users profile page you can click on every posts that i as a user have upload and from there delte, or edit a post.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can Add and change my profile image so that Other users can see who I am.      
**Test**: From the profile page the user can edit its personal information and add and change a profile picture from the edit page.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can Add information in my biography about myself so that other users get to know me better by my profile page.      
**Test**: This test is tested as the one abow, from the profile page you can edit your personal information to add a bio or edit/remove it.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can save all my posts in my page so that it is easy to view what I uploaded and to see what other users have shared on their profiles.      
**Test**: When a user has uploaded a post, the post being shared on the feed and saved on the profile page automatic.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can choose to upload something from the homepage or from anywhere I am on the site so that I don't have to go back or forward to do that task.      
**Test**: In the navigation bar on the top, there is a link for upload and you can click on it from anywhere on the site, and takes you to the uploading form and when you submit and upload the post, you get to the feed.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user I can like a photo from the feed so that the user who uploaded the post can see that I liked it.      
**Test**: You can like the photo by click on the post for the detail page, then like it, but there is no notification or any way to see who has liked it.    
**Result**: This test does not really pass, because it doesnt do exactly as the implementations, but it have a like function that works.   

---
**Implementations**: As a user I can make a comment /edit or delete it on a users post so that I can give feedback or discuss what users upload and regret if I want to change or remove it.      
**Test**: As a user you can comment other users or your own posts, from the post detail page when you click on it. You can edit or delete you own comments too.      
**Result**: This test pass.   

---
**Implementations**: As a user I can edit or delete my own uploaded posts so that I can change something in my already uploaded post or delete if I regret uploading it.      
**Test**: As a user i can click on my own post in the feed, or from my profile page so i see it in post detail view, and from there i have an edit button, and a delete button, to make changes in my post or delete it completely.      
**Result**: This test pass.   

---
### EPIC 3 Search User
**Implementations**: As a user I can search after other users by other username, name, location so that I can find other users in my location or find a user that I want to check out their profile page.      
**Test**: As a user I can choose to click on search from navbar and search after other users by their username only, and not location or name.      
**Result**: This test pass but it is not fully functional with all the search choises yet.   

---
**Implementations**: As a user I can Add a friend in a friend list, or followlist so that I can see what this person uploads easy and get in touch.      
**Test**: When i as a user, visit other userse profile page i can choose to follow them by a button, and when i follow someone I can see what that user uploads in my own feed.      
**Result**: This test pass.   

---
**Implementations**: As a user I can unfollow or unfriend a user so that I can regret or if I follow by mistake can undo it.      
**Test**: From a users profile page you can choose to follow or unfollow by a button with no problem.      
**Result**: This test pass.   

---
### EPIC 4 Direct Messages
**Implementations**: As a user I can Send a private message to an other user so that Its easy to start a conversation and speak to other users one by one.      
**Test**: As a user i can go to my inbox, and from there search a user i want to start chat with and send messages to, or if i got an message i can go to that thread from my inbox too.      
**Result**: This test pass.   

---
**Implementations**: As a user I can get private messages from other users in a inbox so that I can sort and see where my messages goes and saves.      
**Test**: All messages that been created from different users, is stored in threads in my inbox.      
**Result**: This test pass.   

---
**Implementations**: As a user I can Delete messages from my inbox so that I easy can clear my inbox and delete those who I don't want to save.      
**Test**: As a user I can delete threads that i have in my inbox, and all the messages that have been sent to that user will be deltet for me.      
**Result**: This test pass.   

---

## Validator testing
### CSS
Css code pass without errors in w3C validator for CSS
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/CSS%20validator.png)

### Javascript
Pass without error in JSHint Validator 
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/JShint%20validate.png)

### HTML
All pages on the deployed site was validate and pass without errors in W3C Validator. Two of the sites (inbox holding threads and profile page) did not pass and gave an 500 error. I got help from tutors team and the reason it gave error was for the information of the page is for logged in users to see and private. The code in general was tested and pass. And the pages works fine in browser too.
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_feed.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_index.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_postdetail.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_search.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_searchchat.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_upload.png)
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/validate_profile.png)

### Python
All python code was tested and validate in PEP8 Validator without errors
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/pep8_mainview.png)

## Bugs
During the development of this project, I got alot of bugs and errors. Some of them was easy to fix by just read what the error message that telling me what is wrong. Small errors like indent problems, forgot to import something from views, models or urls, spelling errors in the variables etc.
Then I got bigger issues and errors that I had more problem to solve. some of them I solved after searching through the entire internet and found good answers in eg stackoverflow and similar forums. Some problems I had to get help from tutor support who has helped me solve some of the biggest bugs during the project.

One of the bigger issues I got was to get the private messages function to work. I got alot of problem with both the templates, views and urls. From the beginning I wantet the inbox, search for user to chat with, and the messages thread to be all at the same template, like a e-mail structure. But that caused so many problem and it did'nt want to work well. I asked for help from the tutor team and they got me on the right track, and then I got alot of help from my mentor. But I finally manage to fix the problem by just add two more templates and divide the code into three parts, so you have the inbox for its own, then the search part on its own and then the chat box on its own, and it looked much better in on both desktop view and above all the phone view. And it worked fine!  
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/inbox%20search%20error.png)

Another bug that has given me problems is the search field. I first had them as a separate file and search from the template, but did not manage to hide the search result before I tried to search. So I changed so that I had the search box up in the navbar and then it worked well! On the other hand, I wanted them in my own template as my first plan was and therefore I redid them and had to use javascript to make it work the way I wanted. I received good help from the tutor team to lead me in the right direction on this too.  
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/search_error3.png)

Other bugs was to write right variables in the templates and then to fix the static files to show when deployed the project to Heroku and realised that i had to change debug=true til False!

# Deployment
When I started this project, I had to use Code Institutes template to be able to deploy it in Heroku and save all files that is secret in an gitignore file that came along the template. 
Then I used Gitpod IDE to bult this project and saved it with **git add**, **git commit** and then pushed it to github with the command **gitpush**. 
For saving code from django, I need to save it by the commands **python3 manage.py makemigrations** and then **python3 manage.py migrate** before I push the code to github and to finally deploy the project to Heroku. And the last step set the Debug to False in my app setting in django to get all the static files to show on the final deployment.

### Project deployment to Heroku
1. Log in to my account at Heroku
2. Select "new" and "Create new app" from the dashboard.
3. Create a unique name for the project
4. Navigate from the deploy tab at the top and select the setting tab.
5. Because I use Code Institute template, I need to add a config var for creating this app. (Not necessary if you do not use the template)
6. Select Reveal config vars button. In KEY field, input PORT with capital letters. In VALUE field, input 8000 and then select add button.
Select Python as yout first bulid pack in buildpacks window and save that.
9. Select the deploy tab again and go to the deployment method section.
10. Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
11. Select your account and enter the name of your repository and then select search.
12. When Heroku has find your repository select connect to connect the repository to the app within Heroku.
13. Below App connected section, I choose to manual deployments options further down.
14. When that is done correctly this will provide me the live link for this programe.
15. Then I choose Automatic Deploys button that will automatically rebuild the app everytime you add, commit and push from GitPod.


# Credits
* [Django Documentation](https://docs.djangoproject.com/en/4.0/) - I used alot of help to understand django and find solutions for my problems from the django documentation for this project!

* I also used very much help from the Django- I Think Therefore I Blog, walkthough project to start the project and fore some ideas how to do with the comments and likes and to start the project, helped me with the basic structure.

* [Receiver/signals](https://www.codeunderscored.com/signals-in-django/) - using receiver when create new users to not get errors.

* [This](https://www.youtube.com/watch?v=dIcCi2SG1CU) tutorial helped me with the search problem and how to implement ajax and jquery for it.

* [Help with how to upload all images and static](https://www.geeksforgeeks.org/python-uploading-images-in-django/)

* [Following system](https://itsvinayak.hashnode.dev/creating-a-follow-and-unfollow-system-in-django) - Using help from this tutorial how to manage the following system.

* [See followers post in feed](https://stackoverflow.com/questions/55675757/django-queryset-for-getting-feeds-from-following-users)

* [One tutorial for messages](https://www.youtube.com/watch?v=j1voZAmVw9I&t=648s)
[Another for private messages](https://www.youtube.com/watch?v=oxrQdZ5KqW0) - Using help from this two tutorials for making the private message function.

* All the images that i used is my own or users uploaded photos.

# Acknowledgements
This project has gone very well to work with. I have seldom encountered the same challenges as in the previous projects. However, the biggest challenge this time was to try to get the time together. This autumn and winter has been full of illnesses and children who have not been able to go to preschool due to the prevailing situation. The last week before the deadline I get covid and a few days the whole family gets it too which was less appropriate as I lost some time. But the positive thing was that my boyfriend got to be home and quarantined, which gave me useful time to put on the project and help taking care of the kids in the end!   
I would also like to thank my mentor Richard Wells and the tutor team at Code Institue for all the help and support.