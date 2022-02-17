[![David's GitHub Banner](/documents/assets/logos/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# Leannes Learners

This is the documentation regarding the creation of the Leanne's Learners website.
This is my 4th Portfolio Project for the Code Institute's Diploma in Full Stack Development.  
The projects purpose:
To build a Full-Stack site based on business logic used to control a centrally-owned dataset. Including an authentication mechanism and providing role-based access to the site's data or other activities based on the dataset.

<!--TODO CONTENTS HERE-->

## UX (User Experience)

### User Stories

* As a user
  * I want to know where Leanne's Learners operate
  * I want to see the service's Leanne's Learners offer.
  * I want to be able to see the prices.
  * I want to know about the company.
  * I want to be able to contact the company.
  * I want to be able to easily book my lessons.
  * I want to be able to easily cancel my lessons.
  * I want to get a confirmation email with my appointment time.

### Site Owner Goals

* As a site owner
  * I want to show where Leanne's Learners operate.
  * I want to show the prices.
  * I want to let people see the services we offer
  * I want to let people easily contact us either by email or phone.
  * I want to make it easy for pupils to book lessons.
  * I want to get an email when a pupil requests to make or cancel a lesson.
  * I want to be able to confirm a pupils requests to make or cancel a lesson.
  * I want to be able to cancel pupils lessons.
  * I want to be able to get email from site users through a contact form

## User Persona Summary ![User Persona Summary](/documents/assets/UserPersonaSummary.jpg)

## Project Board

I Used Github's Project board to plan the project and Github Issue's for User Stories and Tasks [here](https://github.com/users/dkitley1975/projects/9)  

*Project Board listed by Status*
![Project Board listed by Status](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_List_By_Status.png)  

*Project Board listed by Milestone*
![Project Board listed by Milestone](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_List_By_Milestones.png)  

*First Milestone with Tasks added*
![Milestone with tasks added](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_Milestone_Description_And_Adding_Tasks.png)

*User Story with Tasks added*
![User Story with tasks added](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_User_Story_and_Added_Tasks.png)  

*Project Board Kanban, with Automation*
![Project Board Kanban, with Automation](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board.png)  

### Site Creation Path Project Board

In addition to User Stories and Tasks Project board I also created a Site Creation Path Board Used Github's Project board again to plan the projects creation path.

*Site Creation Path Board List View*
![Site Creation Path Board List View](/documents/assets/screenshots/GitHub_Site_Creation_Project_Path_Screen_Shots/GitHub_Site_Creation_Project_Path_Screen_Shots_list_view.png)

*Site Creation Path Board Table View*
![Site Creation Path Board Table View](/documents/assets/screenshots/GitHub_Site_Creation_Project_Path_Screen_Shots/GitHub_Site_Creation_Project_Path_Screen_Shots_table_view.png)

*Site Creation Path Board Indiviual Item View*
![Site Creation Path Board Indiviual Item View](/documents/assets/screenshots/GitHub_Site_Creation_Project_Path_Screen_Shots/GitHub_Site_Creation_Project_Path_Screen_Shots_item.png)

## Design

### Fonts

### Colors

### Wireframe

#### Desktop

![WEB](/documents/assets/Holding_Image.png)

#### Mobile

![MOBILE](/documents/assets/Wireframes/wireframe-mobile.png)

## Technologies

### Languages

* HTML
* CSS
* Python
* Django

### Frameworks and Tools

* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [Postgres](https://www.postgresql.org/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [http://pep8online.com/](http://pep8online.com/)
* [Am I responsive](http://ami.responsivedesign.is/)
* [WebAim](https://webaim.org/resources/contrastchecker/)

### Contrast Checker

![image](/documents/assets/Holding_Image.png)

## Features

The website has the following features:

### Navigation bar

![image](/documents/assets/Holding_Image.png)

### Home

![image](/documents/assets/Holding_Image.png)

### Services

![image](/documents/assets/Holding_Image.png)

### Contact us


### Login

![image](/documents/assets/Holding_Image.png)

### Admin

![image](/documents/assets/Holding_Image.png)

### Registration/Login

![image](/documents/assets/Holding_Image.png)

### User/Logout

![image](/documents/assets/Holding_Image.png)

#### Contact Form
This is the contact form filled in
![image](/documents/assets/screenshots/contactform/contact-form.png)
After submission:   
the user is redirected to this page
![image](/documents/assets/screenshots/contactform/contact-success.png)
and receives an email
![image](/documents/assets/screenshots/contactform/contact-result-email-for-originator.png)
the owner reveives this email
![image](/documents/assets/screenshots/contactform/contact-result-email-for-staff.png)
During debug:   
the contact test results are shown in the console:
![image](/documents/assets/screenshots/contactform/contact-test-result-email-for-staff.png)
![image](/documents/assets/screenshots/contactform/contact-test-result-email-for-originator.png)

## Testing

### Code Validation

### HTML

The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.

#### Home Page

#### Service Page

#### Contact-Us Page

#### Appointment Page

#### Manage-Appointment Page

### CSS

The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.

### Python

The PEP8 Online Check was used to validate all Python code. No errors or warnings to show

### Different Screen Size

The site is optimized for all screen sizes and tested with a Macbook Pro 13" and iPhone 13 Pro.
I use media queries to make everything look and feel good on mobile devices.

### Issues found during site development and their Solutions

1. When adding the localhost as an ALLOWEDHOST in the settings page, I continued to receive an Django error indicating the host needed to be added to the allowed host settings.

    * As this was being developed locally in VS Code. I tried editing the hosts file via -

      ```bash
      sudo nano /private/etc/hosts
      ```

      Saving the changes by pressing ```ctrl + O```, then exiting by pressing ```ctrl + X```  

    This error continues - but if ```http://localhost:8000/``` or ```http://127.0.0.1:8000/``` are used in the address bar the site works, just not directly from the link in the output message in the terminal.

1. My initial thought was to just use the base comment feature as demonstrated in the I think therefore I blog walkthrough, with the following code:

```HTML
<div class="card-body">
  {% if commented %}
  <div class="alert alert-success" role="alert">
    Your comment is awaiting approval
  </div>
  {% else %}
  {% if user.is_authenticated %}
  <h3>Leave a comment:</h3>
  <hr>
  <p>Posting as: {{ user.username }}</p>
  <form method="post" style="margin-top: 1.3em;">
    {% csrf_token %}
    {{ comment_form | crispy }}
    <button type="submit" class="btn btn-signup btn-lg">Submit</button>
  </form>
  {% else %}
  <h3>Leave a comment:</h3>
  <hr>
  <p class="mt-4 mb-2 fw-bolder fst-italic">If you would like a comment.</p>
  <p>Please login to your account or register and join our community </p>
  {% endif %}
  {% endif %}
</div>
```

```python
def post(self, request, slug, *args, **kwargs):
  queryset = Post.objects.filter(status=1)
  post = get_object_or_404(queryset, slug=slug)
  comments = post.comments.filter(approved=True).order_by("-created_at")
  liked = False
  if post.likes.filter(id=self.request.user.id).exists():
      liked = True

  comment_form = CommentForm(data=request.POST)
  if comment_form.is_valid():
      comment_form.instance.email = request.user.email
      comment_form.instance.name = request.user.username
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
  else:
      comment_form = CommentForm()
```
This refreshed the page and displayed a 'Your comment is awaiting approval message' If like me the user would then hit refresh to see if the message was refreshed, or leave the page open and hit refresh the message would send again repeating the message.
To solve this easily I looked at removing the fact the message needs to be approved by the admin before being posted, which then made me think about nesting comments, comments on comments etc and so I rethought the entire commenting section, replacing it with its own app.

1. NEXT ISSUE 


## Deployment

1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser

The program is set to be deployed automatically after each push from gitpod.

I also set up a Postgres database with Heroku.

1. Click on Resources in your Heroku app.
2. In the add-ons field search for Heroku Postgres and press submit.

### Cloning

How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

## Credits
Email sending: Using Forms and Class based views instead of Function based views
https://www.sitepoint.com/django-send-email/