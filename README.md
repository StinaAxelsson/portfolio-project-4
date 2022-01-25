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
| body       	| post-body         	| max_length=500 	| TextField       	|
| created_on 	| auto_now_add=True 	| None           	| DateTimeField    	|
| author     	| User              	| None           	| ForeignKey      	|
| upload     	| image             	| image          	| CloudinaryField 	|
| likes      	| likes             	| None           	| ManytoManyField 	|
### Comment model
| Title      	| Key in Database   	| Form Validaton 	| Data Type     	|
|------------	|-------------------	|----------------	|---------------	|
| comment    	| comment           	| max_length=500 	| TextField     	|
| created_on 	| auto_now_add=True 	| None           	| DateTimeField 	|
| author     	| User              	| None           	| ForeignKey    	|
| post       	| Post              	| None           	| ForeignKey    	|
### Users (profile)
| Title     	| Key in Database   	| Form Validaton          	| Data Type       	|
|-----------	|-------------------	|-------------------------	|-----------------	|
| User      	| User, primary_key 	| None                    	| OnetoOneField   	|
| name      	| name              	| max_length=50           	| CharField       	|
| picture   	| image             	| None                    	| CloudinaryField 	|
| birthday  	| birthday          	| blank=True              	| DateField       	|
| gender    	| choices=Gender()  	| default=Gender.other.id 	| IntegerField    	|
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
  - **As a user I can easy and safely register an account so that I can use my account for the websites purpose** 
    - **Implementations**: Using and installing allauth for users registrations, login and logout, getting all the accounts template for this installing in my project to make sure this is safe and works.
    - **Test**: I test this with first installing allauth, getting urls done and the templates, I try register and the account created, i use receive signals for register users for saving them without errors in database.
    - **Result**: This test pass and works fine.
  - **As a user I can use my email or username so that i can login with my account**
    - **Implementations**: For this site, the users need their username to login.
    - **Test**: Testing this by log in with the created account after logging out.
    - **Result**: This test pass and works how it should.
  - **As a user I can easy find where to register and create an account so that I can be a member and join the community**
    - **Implementations**: From navbar i the header on the landind page you have all the options. And from the button on index file, and about us file. While logged in you can logout from navbar.
    - **Test**: Testing this by put up options so its easy to find
    - **Result**: This test pass and works how it should.

## Validator testing
## Bugs
# Deployment
# Credits
# Acknowledgements
