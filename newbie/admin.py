from django.contrib import admin

from newbie.models import HeadLineAccount
from newbie.models import GitAccount
from newbie.models import Link

admin.site.register(HeadLineAccount)
admin.site.register(GitAccount)
admin.site.register(Link)

