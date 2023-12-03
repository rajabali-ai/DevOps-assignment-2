from django.contrib import admin

from .models import User, tanslated_video, uploaded_video

admin.site.register(User)
admin.site.register(uploaded_video)
admin.site.register(tanslated_video)
