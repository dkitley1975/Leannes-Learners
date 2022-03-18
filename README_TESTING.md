[![David's GitHub Banner](/documents/assets/logos/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara) <!-- omit in toc -->

# Leannes Learners - Tests <!-- omit in toc -->

This is the documentation section regarding the testing of the Leanne's Learners website.

## Contents <!-- omit in toc -->

- [Testing](#testing)
  - [Code Validation](#code-validation)
  - [Unittest](#unittest)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
- [Blog](#blog)
  - [leannes_learners_data](#leannes_learners_data)
  - [users](#users)
- [Different Screen Size](#different-screen-size)
- [Issues found and worth metioning during site development and their Solutions](#issues-found-and-worth-metioning-during-site-development-and-their-solutions)
- [Lighthouse](#lighthouse)
- [Contrast Checking](#contrast-checking)

## Testing

### Code Validation

### Unittest

Unit test were performed on the python files.
  
[The results are here](/htmlcov/index.html)

|                                                                         | coverage report |      |       |
|-------------------------------------------------------------------------|-----------------|------|-------|
| Name                                                                    | Stmts           | Miss | Cover |
|----------------------------------------------------|-----------------|------|-------|---|
| blog/admin.py                                                           | 23              | 0    | 100%  |
| blog/apps.py                                                            | 5               | 0    | 100%  |
| blog/forms.py                                                           | 12              | 0    | 100%  |
| blog/models.py                                                          | 72              | 7    | 90%   |
| blog/urls.py                                                            | 8               | 0    | 100%  |
| blog/views.py                                                           | 114             | 55   | 52%   |
| leannes_learners/urls.py                                                | 12              | 0    | 100%  |
| leannes_learners/views.py                                               | 10              | 4    | 60%   |
| leannes_learners_data/admin.py                                          | 88              | 10   | 89%   |
| leannes_learners_data/apps.py                                           | 5               | 0    | 100%  |
| leannes_learners_data/models.py                                         | 139             | 11   | 92%   |
| leannes_learners_data/templatetags/auth_extras.py                       | 7               | 2    | 71%   |
| leannes_learners_data/urls.py                                           | 5               | 0    | 100%  |
| leannes_learners_data/views.py                                          | 67              | 4    | 94%   |
| users/admin.py                                                          | 11              | 1    | 91%   |
| users/apps.py                                                           | 4               | 0    | 100%  |
| users/forms.py                                                          | 31              | 0    | 100%  |
| users/models.py                                                         | 24              | 2    | 92%   |
| users/urls.py                                                           | 4               | 0    | 100%  |
| users/views.py                                                          | 40              | 9    | 78%   |
|                                                                         | _______________ | ____ | _____ |
| TOTAL                                                                   | 681             | 105  | 85%   |

### HTML

The W3C Markup Validation Service was used to validate the HTML page of the project.
To use this service, I opened each page and viewed the source code, copied and pasted in to the W3C Markup Validation Service, minor errors were corrected, issues and problems have been noted below.

- **Home Page** - No Errors

- **About Us** - No Errors

- **Pass Plus** - No Errors

- **Prices** - No Errors

- **Posts - individual detail view** - No Errors  
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

- **Blog Categories** - No Errors
(fixed an error with regard to empty spaces in the categories passed to the url. Fixed by creating a slug of the name and passing this through as the url)

- **Contact us** -
Error: ```Bad value mailto:leanne@leanneslearners.com?subject=Website%20Contact%20Details%Page%Link for attribute href on element a:
Percentage ("%") is not followed by two hexadecimal digits.
<a href="mailto:leanne@leanneslearners.com?subject=Website%20Contact%20Details%Page%Link”>```

    *This is code injected from the Django Summernotes form widget. The form has been tested and does submit the email, sending copies to both admin and the user*

- **Local_traffic** - No Errors

- **edit_user_details** - No Errors

- **edit_profile** - No Errors

- **Create a Blog Post** - code injected from the Django Summernotes form widget showed as having errors.

    *It does create the post and goes directly to the new posts page*.

- **Edit a Blog Post**  - code injected from the Django Summernotes form widget showed as having errors.

    *It does edit the post successfully goes returns to the posts page*.

- **Delete a Post** - No Errors

- **Reset a Password** - No Errors
  
- **Reset a Password - Email sent Confirmation** - No Errors

- **Reset a Password - Change Password** - One warning regarding the default change password form. Does not effect the functunality of the form or page.
  
- **Reset a Password - Completion message** - No Errors.
  
### CSS

The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.

- **styles.css** - No Errors (used for the frontend)
- **admin_color.css** - No Errors (used for the backend admin area)

### Python

The PEP8 Online Check was used to validate all Python code. No errors or warnings to show

## Blog

- **admin.py** -  No Errors
- **apps.py** -  No Errors
- **forms.py** -  No Errors
- **models.py** -  No Errors
- **urls.py** -  No Errors
- **views.py** -  No Errors

### leannes_learners_data  

- **admin.py** -  No Errors
- **apps.py** -  No Errors
- **forms.py** -  No Errors
- **models.py** -  No Errors
- **urls.py** -  No Errors
- **views.py** -  No Errors  

### users  

- **admin.py** -  No Errors
- **apps.py** -  No Errors
- **forms.py** -  No Errors
- **models.py** -  No Errors
- **urls.py** -  No Errors
- **views.py** -  No Errors  

## Different Screen Size

The site is optimized for all screen sizes and tested with an ipad, iPhone 10 and Chrome developer.
I use media queries to make everything look and feel good as the screen size increases.

## Issues found and worth metioning during site development and their Solutions

1. When adding the localhost as an ALLOWEDHOST in the settings page, I continued to receive an Django error indicating the host needed to be added to the allowed host settings.

    - As this was being developed locally in VS Code. I tried editing the hosts file via -

      `
      sudo nano /private/etc/hosts
      `
      Saving the changes by pressing ctrl + O, then exiting by pressing ctrl + X  

      This error continues - but if `http://localhost:8000/` or `http://127.0.0.1:8000/` are used in the address bar the site works, just not directly from the link in the output message in the terminal.

2. Refreshing the page after commenting resubmitted the page.
My initial thought was to just use the base comment feature as demonstrated in the I think therefore I blog walkthrough, with the following code:
After submitting the message this would refreshed the page and displayed a 'Your comment is awaiting approval message',  
But if the user would then hit refresh the page the message would send again repeating the message.
To solve this easily I removed the message needing to be approved by the admin before being posted.
The commenting code was later extracted and added to a modal.

3. The replys to comments all had the same html reference id's, causing a reply to a previous comment to always be associated with the latest comment.
This was fixed by adding the comment.id reference to the html id reference.  

4. I initially had placed login, logout and register elements within insividual forms in the Navigation bar. Whilst testing manually on the live site on smaller screens, the forms were hidden beneath the footer and the page wouldn't scroll to reveal the rest of the forms.
This was fixed within the CSS, further testing with the the W3C Markup Validation Service flagged the forms as errors, indicating that forms were not allowed with in `<ul>` elements.
I rethought the approach and added the login and register elements as modals instead.  

5. Page Meta Descriptions and Title. I had added the page title to each page using this method:  

      ~~~~ html
      {% block title %}
      <title>Leannes Learner's Home Page</title>
      {% endblock %}
      ~~~~  

    I then added the Page Meta Description with:  

      ~~~~ html
      {% block metadescription %} 
      <meta name="keywords"
        content="Driving School, Driving Lessons, Learn to Drive, Huddersfield, HD4, Female Driving School, Female Driving Instructor, Blog"> 
      <meta name="description"
      content="Welcome to Leannes Learners, we are a Huddersfield based Driving School, here you can find links to our latest blog posts and testimonials">
      <title>Leannes Learner's Home Page</title>
      {% endblock %}
      ~~~~

    It is a future revision to have this information pulled from the database but this has alluded me so far.
    To add dynamic content for the page meta description for the individual blog pages I added the page description using this:

      ~~~~html
      {% block metadescription %} 
      <meta name="keywords" content="Driving School, Driving Lessons, Learn to Drive, Huddersfield, HD4, Female Driving School, Female Driving Instructor, Blog"> 
      <meta name="description"
      content="{{post.title|safe|truncatechars:50 }} - {{post.content|striptags|safe|truncatechars:100 }}">
      <title>Post - {{post.title}}</title>
      {% endblock %}
      ~~~~

    This will add dynamocally add the post title and some content to the page description within google searches.
    This did add an error within the W3C Markup Validation Service. As the Post content allowed html elements these appeared within the description, but didn't always close.
    This would show as unclosed tags in the source code.
    I added the ```|striptags``` to remove the html markup from the page description content to resolve this error.  

6. On the ipad the like and comment icons for a post distributed over two lines even when there was enough room to display, this displayed fine on Desktop Safari and Chrome, I amended the code using flex and moved the icons to the right.  

## Lighthouse

![image](/documents/assets/screenshots/tests/lighthouse_home.png)
![image](/documents/assets/screenshots/tests/lighthouse_blog.png)
Any performace issues appear to be related to the time the content can be retrived from cloudinary.

## Contrast Checking

I used [color.a11y.com](https://color.a11y.com/Contrast/) to check the sites colour contrast for each page. No issues detected.

![image](/documents/assets/screenshots/tests/color_contrast_report.png)
