from django.shortcuts import render, HttpResponse
from school.forms import ContactForm, ContactModelForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    form = ContactForm()
    return render(request, 'home.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactModelForm()
    return render(request, 'contact_us.html', {
        'form': form
    })
