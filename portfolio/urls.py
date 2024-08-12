from django.urls import path
from .views import home_view,  ContactFormView, TestimonialListView,AboutListView, ContactFormView,ChocolateListView


urlpatterns = [
    path('',home_view,name='index-page'),
    path('about/',AboutListView.as_view(),name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('chocolate/',ChocolateListView.as_view(),name='chocolate-page'),
    path('testimonial/',TestimonialListView.as_view(),name='testimonial-page')
        
]