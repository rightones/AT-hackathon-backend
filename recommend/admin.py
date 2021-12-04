from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Position)
admin.site.register(Topic)
admin.site.register(AdeptTopicProfile)
admin.site.register(InterestTopicProfile)
admin.site.register(OngoingTopicProfile)