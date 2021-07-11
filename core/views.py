from django.shortcuts import render, HttpResponseRedirect
from .models import Messages
from .forms import MessageForm
from django.contrib.auth.models import User

# Create your views here.


def send(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                form = MessageForm()
        else:
            form = MessageForm()
        message = Messages.objects.all()
        return render(request, 'core/index.html', {'form': form, 'message': message})
    else:
        return HttpResponseRedirect('/login/')


def users(request):
    u = User.objects.all()
    return render(request, 'core/users.html', {'users': u})
