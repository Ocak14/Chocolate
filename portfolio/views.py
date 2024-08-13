from django.shortcuts import render
from .models import Contact ,Chocolate,About,Testimonial
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
      full_name = form.cleaned_data.get('full_name')
      phone_number = form.cleaned_data.get('phone_number')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {full_name}\nEmail: {email}\nPhone_number: {phone_number}\ntext: {content}"
      send_message(text)
      Contact.objects.create(
        full_name=full_name,
        email=email,
        content=content
    )
      return super().form_valid(form)



def home_view(request):
 return render(request=request,template_name='index.html')

class AboutListView(ListView):
  model = About
  template_name = 'about.html'
  context_object_name = 'about'



class ChocolateListView(ListView):
  model = Chocolate
  template_name = 'chocolate.html'
  context_object_name = 'chocolate'

class TestimonialListView(ListView):
  model = Testimonial
  template_name ='testimonial.html'
  context_object_name = 'testimonials'