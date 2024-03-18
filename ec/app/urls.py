from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from . views import CustomerRegistrationView
from .forms import  MyPasswordResetForm
from .views import MyPasswordResetForm





urlpatterns = [
    path("", views.home),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name="contact"),  # Added a trailing slash and a comma
    path("category/<slug:val>/", views.CategoryView.as_view(), name="category"),  # Added a trailing slash
    path("category.title/<val>/", views.CategoryView.as_view(), name="category-title"),  # Added a trailing slash
    path("product-detail/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),  # Added a trailing slash
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'), 
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.ProfileView.as_view(), name='address'),


    # Login authentication
    path('registeration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('account/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('password-reset/',auth_views.PasswordResetView.as_view (template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

         
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
