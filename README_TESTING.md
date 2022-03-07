#[![David's GitHub Banner](/documents/assets/logos/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# Leannes Learners - Tests

This is the documentation section regarding the testing of the Leanne's Learners website.

<!--TODO CONTENTS HERE-->

## Testing

### Code Validation

### HTML

The W3C Markup Validation Service was used to validate the HTML page of the project.
To use this service, I opened each page and viewed the source code, copied and pasted in to the W3C Markup Validation Service, minor errors were corrected, issues and problems have been noted below.

* **Home Page** - No Errors

* **About Us** - No Errors

* **Pass Plus** - No Errors

* **Prices** - No Errors

* **Posts - individual detail view** - No Errors  
(initially I had errors from the comment section, I had used a comment form for the replies which used the same id for each reply button and comment form. I added the reply to comment reference to each reply button and copied the form element from the code and replaced the ```comment.form | crispy``` with

~~~~ html
<div id="div_id_comment{{ comment.id }}" class="form-group"> <label
        for="id_comment{{ comment.id }}" class="requiredField">
        Your comment</label>
       <div> <textarea name="comment" cols="40" rows="10" class="textarea form-control" required=""
         id="id_comment{{ comment.id }}"></textarea> </div>
      </div> 
~~~~  

using the ```{{ comment.id }}``` gave each comment reply its own unique id

* **Blog Categories** - No Errors
(fixed an error with regard to empty spaces in the categories passed to the url. Fixed by creating a slug of the name and passing this through as the url)

* **Contact us** -
Error: ```Bad value mailto:leanne@leanneslearners.com?subject=Website%20Contact%20Details%Page%Link for attribute href on element a:
Percentage ("%") is not followed by two hexadecimal digits.
<a href="mailto:leanne@leanneslearners.com?subject=Website%20Contact%20Details%Page%Link”>```

    *This is code injected from the Django Summernotes form widget. The form has been tested and does submit the email, sending copies to both admin and the user*

* **Local_traffic** - No Errors

* **edit_user_details** - No Errors

* **edit_profile** - No Errors

* **Create a Blog Post** - code injected from the Django Summernotes form widget showed as having errors.

    *It does create the post and goes directly to the new posts page*.

* **Edit a Blog Post**  - code injected from the Django Summernotes form widget showed as having errors.

    *It does edit the post successfully goes returns to the posts page*.

* **Delete a Post** - No Errors

### CSS

The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.

* **styles.css** - No Errors (used for the frontend)
* **admin_color.css** - No Errors (used for the backend admin area)

### Python

The PEP8 Online Check was used to validate all Python code. No errors or warnings to show
### Blog

* **admin.py** -  No Errors
* **apps.py** -  No Errors
* **forms.py** -  No Errors
* **models.py** -  No Errors
* **urls.py** -  No Errors
* **views.py** -  No Errors

### leannes_learners_data  

* **admin.py** -  No Errors
* **apps.py** -  No Errors
* **forms.py** -  No Errors
* **models.py** -  No Errors
* **urls.py** -  No Errors
* **views.py** -  No Errors  

### users  

* **admin.py** -  No Errors
* **apps.py** -  No Errors
* **forms.py** -  No Errors
* **models.py** -  No Errors
* **urls.py** -  No Errors
* **views.py** -  No Errors  

### Different Screen Size

The site is optimized for all screen sizes and tested with an ipad, iPhone 10 and Chrome developer.
I use media queries to make everything look and feel good as the screen size increases.

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
<https://www.sitepoint.com/django-send-email/>
