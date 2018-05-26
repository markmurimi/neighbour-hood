from django.contrib import admin
from .models import Occupant,Business,Neighbourhood,Post
# Register your models here.
admin.site.register(Occupant)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Post)