from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
import datetime
from django.template.defaultfilters import slugify


# Create your models here.


class Library(models.Model):
    library_name  = models.CharField(max_length=100, null=False, help_text="Enter Library Name")
    slug = models.SlugField(max_length=100, unique=True, default=None)

    def __unicode__(self):
        return self.library_name

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def save(self):
        super(Library, self).save()
        date = datetime.date.today()
        self.slug = '%s' % (
            slugify(self.library_name)
        )
        super(Library, self).save()



class Book(models.Model):
    book_name = models.CharField(max_length=100, null=False, help_text="Enter Book Name")
    library = models.ForeignKey(Library, null=False ,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.book_name
