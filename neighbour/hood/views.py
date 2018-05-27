from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from .forms import ProfileForm
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    images = Post.get_posts()
    return render(request, 'home.html', {"images": images})

@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    profiles = Profile.objects.filter(user=current_user).count()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            if profiles == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
            else:
                record = Profile.objects.filter(user=current_user)
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form})