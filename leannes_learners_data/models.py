from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    """
    The About model. This model is used to store the about us information.
    @param short_description - the short description of the about us page.
    @param about_us - the long description of the about us page.
    @param updated_at - the date the about us page was last updated.
    @param created_at - the date the about us page was created.
    @param status - the status of the about us page.
    """

    short_description = models.CharField(max_length=80, unique=True)
    about_us = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        """
        Return a string representation of the object.
        @returns the string representation of the object.
        """
        return self.short_description


class Carousel(models.Model):
    """
    Create a model for the carousel.
    @param slide_identifying_name - the name of the slide
    @param slide_text_headline - the headline of the slide
    @param slide_text_description - the description of the slide
    @param slide_image - the image of the slide
    """

    slide_identifying_name = models.CharField(max_length=80, unique=True)
    slide_text_headline = models.CharField(
        max_length=80, unique=False, blank=True)
    slide_text_description = models.TextField(max_length=200, blank=True)
    slide_image = CloudinaryField(
        folder="leannes_learners/caurosel_images/",
        transformation={"width": "1240", "height": "700", "crop": "fill"},
        default="placeholder",
    )

    alt_tag = models.CharField(
        max_length=200, blank=True, verbose_name="image alternative text"
    )
    include_in_carousel = models.BooleanField(default=False)

    class Meta:
        ordering = ["-include_in_carousel", "-slide_identifying_name"]
        verbose_name = "Carousel on Home Page"
        verbose_name_plural = "Carousel on Home Page"

    def __str__(self):
        """
        Return the slide headline for the slide.
        @return The slide headline for the slide.
        """
        return self.slide_text_headline

    def image_thumb(self):
        """
        Create a thumbnail for the image.
        @returns the thumbnail
        """
        return mark_safe(
            '<img src="{}" width="100" height="auto">'.format(
                self.slide_image.url)
        )

    image_thumb.short_discription = "image"
    slide_image.allow_tags = True


class Instructors(models.Model):
    """
    The instructor model.
    @param name - the name of the instructor
    @param instructor_image - the image of the instructor
    @returns the instructor model
    """

    name = models.CharField(max_length=80, unique=True)
    instructor_image = CloudinaryField(
        folder="leannes_learners/instructor_images/",
        transformation={
            "width": "600",
            "height": "800",
            "crop": "fill",
            "gravity": "face",
            "zoom": "0.5",
        },
        default="placeholder",
    )
    alt_tag = models.CharField(
        max_length=200, blank=True, verbose_name="image alternative text"
    )
    about = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        Return the image thumbnail for the instructor.
        @returns the image thumbnail
        """

        return mark_safe(
            '<img src="{}" width="100" height="auto">'.format(
                self.instructor_image.url)
        )

    image_thumb.short_discription = "image"
    instructor_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Driving Instructor"
        verbose_name_plural = "Driving Instructors"

    def __str__(self):
        """
        Return the name.
        @return the name.
        """
        return self.name


class Service(models.Model):
    """
    The service model.
    @param service_name - the name of the service
    @param service_description - the description of the service
    @param service_duration - the duration of the service
    @param price - the price of the service
    @param created_at - the date the service was created
    @param featured - whether the service is featured
    @return The service model.
    """

    service_name = models.CharField(max_length=80, unique=True)
    service_description = models.CharField(max_length=200, blank=True)
    service_duration = models.CharField(max_length=80, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    featured_order = models.IntegerField(
        verbose_name="Featured Price Order results display 1,2,3"
    )

    class Meta:
        ordering = ["-featured", "service_duration"]
        verbose_name = "Service Description"
        verbose_name_plural = "Service Descriptions"

    def __str__(self):
        """
        Return the service name.
        @return The service name.
        """
        return self.service_name


class Passplus(models.Model):
    """
    The Passplus model is a custom model for the Pass Plus website.
    It is a subclass of Django's Model class.
    It has a short description, a background image, a lead content,
    a main content, and a focus image.
    """

    short_description = models.CharField(max_length=80, unique=True)
    lead_content = models.TextField(
        verbose_name="Lead content - more prominent than the rest."
    )
    main_content = models.TextField(verbose_name="Main content of the page.")
    focus_image = CloudinaryField(
        folder="leannes_learners/pass_plus/focus_images/",
        transformation={
            "width": "800",
            "height": "800",
            "crop": "fill",
            "gravity": "face",
            "zoom": "0.5",
        },
        default="placeholder",
    )
    alt_tag = models.CharField(
        max_length=200, blank=True, verbose_name="image alternative text"
    )
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Pass Plus Page"
        verbose_name_plural = "Pass Plus Page"

    def __str__(self):
        """
        Return a string representation of the object.
        @returns a string representation of the object.
        """
        return self.short_description


class Terms(models.Model):
    """
    The Terms and Conditions page.
    """

    lead_content = models.TextField(
        verbose_name="Lead content - The explanation.")
    main_content = models.TextField(verbose_name="The Terms and Conditions.")
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Terms and Conditions Page"
        verbose_name_plural = "Terms and Conditions Page"

    def __str__(self):
        """
        returns the terms and conditions.
        """
        return "Terms and Conditions"


class Testimonial(models.Model):
    """
    The testimonial model.
    @param name - the name of the testimonial.
    @param testimonial_image - the testimonial image.
    """

    name = models.CharField(max_length=80, unique=True)
    testimonial_image = CloudinaryField(
        folder="leannes_learners/testimonial_images/",
        transformation={
            "width": "600",
            "height": "800",
            "crop": "fill",
            "gravity": "face",
            "zoom": "0.5",
        },
        default="placeholder",
    )
    alt_tag = models.CharField(
        max_length=200, blank=True, verbose_name="image alternative text"
    )
    testimonial = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def image_thumb(self):
        """
        Create a thumbnail for the testimonial image.
        @returns the thumbnail
        """
        return mark_safe(
            '<img src="{}" width="100" height="auto">'.format(
                self.testimonial_image.url
            )
        )

    image_thumb.short_discription = "image"
    testimonial_image.allow_tags = True

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        """
        Return the name.
        @return The name.
        """
        return self.name


class CompanyDetails(models.Model):
    """
    Return the contact details of the company.
    @returns the contact details of the company.
    """

    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    social_media_name = models.CharField(max_length=80, blank=True)
    social_media_link = models.CharField(max_length=200, blank=True)
    social_media_image = CloudinaryField(
        folder="leannes_learners/contact_page/social_images/",
        transformation={"width": "auto", "height": "50", "crop": "fill"},
        default="placeholder",
    )
    social_media_name_2 = models.CharField(max_length=80, blank=True)
    social_media_link_2 = models.CharField(max_length=200, blank=True)
    social_media_image_2 = CloudinaryField(
        folder="leannes_learners/contact_page/social_images/",
        transformation={"width": "auto", "height": "50", "crop": "fill"},
        default="placeholder",
    )
    social_media_name_3 = models.CharField(max_length=80, blank=True)
    social_media_link_3 = models.CharField(max_length=200, blank=True)
    social_media_image_3 = CloudinaryField(
        folder="leannes_learners/contact_page/social_images/",
        transformation={"width": "auto", "height": "50", "crop": "fill"},
        default="placeholder",
    )
    social_media_name_4 = models.CharField(max_length=80, blank=True)
    social_media_link_4 = models.CharField(max_length=200, blank=True)
    social_media_image_4 = CloudinaryField(
        folder="leannes_learners/contact_page/social_images/",
        transformation={"width": "auto", "height": "50", "crop": "fill"},
        default="placeholder",
    )

    class Meta:
        # ordering = ["-id"]
        verbose_name = "Company Contact/Social Information"
        verbose_name_plural = "Company Contact/Social Information"

    def __str__(self):
        """
        Return the phone number of the user.
        @returns the phone number of the user.
        """
        return self.phone


class TeachingHours(models.Model):
    """
    The model for the teaching hours.
    This is a simple model that stores the day, start time, and finish time.
    @param day - the day of the week
    @param start_time - the start time
    @param finish_time - the finish time
    """

    day = models.CharField(max_length=9, unique=True)
    start_time = models.CharField(max_length=6)
    finish_time = models.CharField(max_length=6, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Teaching Hours"
        verbose_name_plural = "Teaching Hours"
