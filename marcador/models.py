'''
from django.contrib.auth.models import User

from django.db import models
#이건 2버전 3버전 차이 출이라고
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name

class PublicBookmarkManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_queryset()
        return qs.filter(is_public=True)

#Verbose field name
class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)
    #위에 설명 User.Bookmark_set : 자동 생성  Bookmark 테이블 이름 _set으로 가져옴
    #User.bookmarks.all() : related_name

    objects = models.Manager()
    public = PublicBookmarkManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    #save의 overloading
    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)
# Create your models here.

'''
