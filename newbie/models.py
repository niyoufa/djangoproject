#coding=utf-8

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.db import models

#开发者头条独家号
class HeadLineAccount(models.Model):
    owner = models.OneToOneField(User)
    exclusive_number = models.IntegerField()

    def __unicode__(self):
        return self.exclusive_number

    class Meta:
        unique_together = ("exclusive_number",)

class GitAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(_('password'), max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __unicode__(self):
        return self.username

    class Meta:
        unique_together = ("username",)

class Link(models.Model):
    # url + creator.id
    sha1 = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    url = models.URLField()
    creator = models.ManyToManyField(User)
    create_time = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("sha1",)


