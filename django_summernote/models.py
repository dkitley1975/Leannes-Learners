from django.db import models
from django_summernote.utils import get_attachment_storage, get_attachment_upload_to
from django.utils.safestring import mark_safe



__all__ = ['AbstractAttachment', 'Attachment', ]


class AbstractAttachment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text="Defaults to filename, if left blank")
    file = models.FileField(
        upload_to=get_attachment_upload_to(),
        storage=get_attachment_storage()
    )
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        super().save(*args, **kwargs)

    def image_thumb(self):
        """
        This creates a thumbnail image of the current uploaded image
        """
        return mark_safe('<img src="{}" width="100" height="auto">'.format(
            self.file.url))
    image_thumb.short_discription = "image"
    file.allow_tags = True

    class Meta:
        abstract = True


class Attachment(AbstractAttachment):
    pass

