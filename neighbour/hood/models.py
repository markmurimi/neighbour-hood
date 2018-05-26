from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length =30)
    neighbourhood_location = models.CharField(max_length = 30)
    occupants_count = models.IntegerField()
    user = models.ForeignKey('Occupant')

    def create_neighbourhood(self):
        '''Method to create a neighbourhood'''
        self.create()

    def delete_neighbourhood(self):
        '''Method to delete a neighbourhood'''
        self.delete()

class Occupant(models.Model):
    name = models.CharField(max_length =20)
    user_id = models.IntegerField()
    neighourhood = models.ForeignKey('Neighbourhood')
    email = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to='occupants/')


class Post(models.Model):
    post = models.ImageField(upload_to= 'posts/')
    occupant = models.ForeignKey('Occupant')
    neighbourhood = models.ForeignKey('Neighbourhood')


class Business(models.Model):
    name = models.CharField(max_length =20)
    b_email = models.CharField(max_length= 40)
    neighbourhood = models.ForeignKey('Neighbourhood')
    occupant = models.ForeignKey('Occupant')

    def create_business(self):
        '''Method to create a business'''
        self.create()

    def delete_business(self):
        '''Method to delete a certain business'''
        self.delete()

    