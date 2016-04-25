from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def CoAadduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect to main view from here (base.html for this project)
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm()

    return render(request, 'adduser.html', {'form': form})
