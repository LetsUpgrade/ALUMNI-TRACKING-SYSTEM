from django.urls import path
from . import views, alumniView, collegeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        '',
        views.home,
        name='home'
        ),    
    path(
        'collegeprofile/<int:pk>/',
        collegeView.profile,
        name="college-profile"
        ),
    path(
        'alumniprofile/<int:pk>/',
        alumniView.profile,
        name="alumni-profile"
        ),
    path(
        'showalumni/',
        views.AlumniListView,
        name="show-alumni"
        ),
    path(
        'showcolleges/',
        views.CollegeListView,
        name='show-college'
        ),
    path(
        'college/<int:pk>/',
        views.CollegeDetailView.as_view(),
        name='college-detail'
        ),
    path(
        'alumni/<int:pk>/',
        views.AlumniDetailView.as_view(),
        name="alumni-detail"
         ),
    path(
        'college/query/',
        collegeView.PendingQueryView.as_view(),
        name="pending-query"
        ),
    path(
        'authenticate/<int:pk>/',
        collegeView.AlumniAuthenticationView.as_view(),
        name="alumni-authentication"
        )
]+static(settings.MEDIA_URL, document_root=settings. MEDIA_ROOT)
