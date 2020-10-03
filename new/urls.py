from django.contrib import admin
from django.urls import include, path
from newApp import alumniView as alumni
from newApp import collegeView as college
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
        ),
    path(
        '',
        include('newApp.urls')
    ),
    path(
        'accounts/',
        include('django.contrib.auth.urls')
        ),
    path(
        'accounts/signup/alumni/',
        alumni.SignupView.as_view(),
        name='alumni_signup'
        ),
    path(
        'accounts/signup/college/',
        college.SignupView.as_view(),
        name='college_signup'
        )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
