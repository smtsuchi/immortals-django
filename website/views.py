from django.shortcuts import redirect, render
from .forms import ApplicationForm
from .models import Application

# Create your views here.
def index(request):
    return render(request, 'website/index.html', context={})

def apply(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print('posted')
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'website/apply.html', context)