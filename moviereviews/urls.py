from django.contrib import admin
from django.urls import path
from movie import views as movieViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', movieViews.home, name='home'),
    path('about/', movieViews.about, name='about'),
    path('movies/', movieViews.movies, name='movies'),
    path('movies/<int:id>/', movieViews.movie_detail, name='movie_detail'),

    path('review/delete/<int:id>/', movieViews.delete_review, name='delete_review'),

    # AUTH
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),

    path('signup/', movieViews.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
