from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length =30)
    neighbourhood_location = models.CharField(max_length = 30)
    occupants_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        '''Method to create a neighbourhood'''
        self.create()

    def delete_neighbourhood(self):
        '''Method to delete a neighbourhood'''
        self.delete()

class Profile(models.Model):
    name = models.CharField(max_length =20)
    neighbourhood = models.ForeignKey('Neighbourhood')
    email = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to='occupants/')
    occupant_id = models.IntegerField(unique = True)
    location = models.CharField(max_length= 30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length =30)
    post = models.ImageField(upload_to= 'posts/')
    profile = models.ForeignKey('Profile')
    post_caption = models.TextField()
    neighbourhood = models.ForeignKey('Neighbourhood')
    date =models.CharField(max_length= 30)
    business = models.ForeignKey('Business')

    def __str__(self):
        return self.name
        
    @classmethod
    def get_posts(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            get_posts : list of image post objects from the database
        ''' 
        images = Post.objects.all ()
        return images

class Business(models.Model):
    name = models.CharField(max_length =20)
    b_email = models.CharField(max_length= 40)
    neighbourhood = models.ForeignKey('Neighbourhood')
    profile = models.ForeignKey('Profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def create_business(self):
        '''Method to create a business'''
        self.create()

    def delete_business(self):
        '''Method to delete a certain business'''
        self.delete()

    