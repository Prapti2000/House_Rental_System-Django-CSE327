from django.contrib import admin
from .models import *

class HotelAdmin(admin.ModelAdmin):
    list_display = ['house_description','banner_image','house_rent','no_of_bedrooms']


admin.site.register(RentalAdvertisement)
admin.site.register(AdvertisementImage)
admin.site.register(Amenities)
admin.site.register(Division)
admin.site.register(City)
admin.site.register(AreaName)
admin.site.register(Block)
admin.site.register(HouseAddress)
admin.site.register(House,HotelAdmin)
admin.site.register(HouseImage)


