from django.urls import path
from .views import home_view, about_view, testimonial_view, contact_view,chocolate_view


urlpatterns = [
    path('',home_view,name='index-page'),
    path('about/',about_view,name='about-page'),
    path('contact /',contact_view,name='contact-page'),
    path('chocolate/',chocolate_view,name='chocolate-page'),
    path('testimonial/',testimonial_view,name='testimonial-page')
]