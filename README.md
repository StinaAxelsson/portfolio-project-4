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
* Landingpage for logged in users
  * Feed, when user sign up they are provide some information of how to upload, create more information in profile page, this text will dissapere when the user upload their first post or start follow users who have upload posts earlier.
* Profile page
  * Personal page for the user, with fields of information to add about themself
  * Add profile image and edit profile.
  * See how many followers (moon friends) they have and a button to follow or unfollow other users.
  * Uploaded posts that the user have is collected on their own pages.
* Inbox
  * An inbox that collect all active threads
  * Start a new chat and search for user to start chat with
  * The conversation/chat with send and received messages
* Search
  * search input box in the navbar to easy search users
  * shows all users that include the search query.
* Upload
  * From navbar users can upload a post/image that uploads in the feed (and profile page)
* post detail
  * When user want to comment or like, you have to click on the post to get more details and show comments.
  * From post detail you can edit or delete your own posts and delete comments that user have made.
* Footer
  * contains links to site owners social media
## Design Choises
### Fonts
I have two main fonts from Google Fonts. 
'Handlee' and 'Dancing script' that meet up my thoughts of how i want a first time user want to feel when they visit. Soft and friendly and kind of playful. Using this in the Logo and as rubric. And Handlee is using as rubrics and bread-text.
### Colours
![](https://github.com/StinaAxelsson/portfolio-project-4/blob/main/media/imagesReadme/colours.png)
Main colour is white, with details as in navbar and footer with the gradiant mix of #A6BFFF and #A4EAC0 and for all the buttons on the page. The #F7BAF0 is used for smaller details and some hover colours and the receivers chat bubble. The colours combine is soft, beautifyl and gives the impression that i seeking for in the theme of the site.
## Wireframes
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
## Features left to implement
# Technologies used
## Languages
* HTML5
* CSS
* Javascript
* Python
## Frameworks
* Django
* Bootstrap
## Other programmes
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
## Bugs
During the development of this project, I got alot of bugs and errors. Some of them was easy to fix by just read what the error message that telling me what is wrong. Small errors like indent problems, forgot to import something from views, models or urls, spelling errors in the variables etc.
Then I got bigger issues and errors that I had more problem to solve. some of them I solved after searching through the entire internet and found good answers in eg stackoverflow and similar forums. Some problems I had to get help from tutor support who has helped me solve some of the biggest bugs during the project.

One of the bigger issues I got was to get the private messages function to work. I got alot of problem with both the templates, views and urls. From the beginning I wantet the inbox, search for user to chat with, and the messages thread to be all at the same template, like a e-mail structure. But that caused so many problem and it did'nt want to work well. I asked for help from the tutor team and they got me on the right track, and then I got alot of help from my mentor. But I finally manage to fix the problem by just add two more templates and divide the code into three parts, so you have the inbox for its own, then the search part on its own and then the chat box on its own, and it looked much better in on both desktop view and above all the phone view. And it worked fine!

Another bug that has given me problems is the search field. I first had them as a separate file and search from the template, but did not manage to hide the search result before I tried to search. So I changed so that I had the search box up in the navbar and then it worked well! On the other hand, I wanted them in my own template as my first plan was and therefore I redid them and had to use javascript to make it work the way I wanted. I received good help from the tutor team to lead me in the right direction on this too.

Other bugs was to write right variables in the templates and then to fix the static files to show when deployed the project to Heroku and realised that i had to change debug=true til False!

# Deployment
# Credits
# Acknowledgements
