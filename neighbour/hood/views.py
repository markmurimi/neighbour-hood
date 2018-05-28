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

@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Post.objects.filter(user=request.user.id).all()

    except:

        title = f'{current_user.username}'

        pics = Post.objects.filter(user=request.user.id).all()


    return render(request, 'profile.html', {"title": title, "current_user": current_user, "pics": pics})

