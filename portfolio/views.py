from django.shortcuts import render

# Create your views here.
def home_view(request):
 return render(request=request,template_name='index.html')

def about_view(request):
 return render(request=request,template_name='about.html')


def chocolate_view(request):
 return render(request=request,template_name='chocolate.html')



def testimonial_view(request):
 return render(request=request,template_name='testimonial.html')


def contact_view(request):
 return render(request=request,template_name='contact.html')
