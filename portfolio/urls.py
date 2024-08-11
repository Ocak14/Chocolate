from django.urls import path
from .views import home_view,  ContactFormView, testimonial_view,about_view, ContactFormView,chocolate_view


urlpatterns = [
    path('',home_view,name='index-page'),
    path('about/',about_view,name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('chocolate/',chocolate_view,name='chocolate-page'),
    path('testimonial/',testimonial_view,name='testimonial-page')
        
]