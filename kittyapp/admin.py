from django.contrib import admin
from kittyapp.models import *
from kittyapp.models import Datastore
# Register your models here.

class DatastoreAdmin(admin.ModelAdmin):
    list_display=('name','desc','datafile')

class PatreonAdmin(admin.ModelAdmin):
    list_display=('user','amount','order_id','razorpayment_id','paid')

admin.site.register(Customer)
admin.site.register(Improve)
admin.site.register(Survey)
admin.site.register(Patreon,PatreonAdmin)
admin.site.register(Datastore,DatastoreAdmin)

admin.site.site_header = 'Hello Kitty'
admin.site.site_title = 'My Admin'
admin.site.index_title = 'Welcome to Hello Kitty Admin Page'