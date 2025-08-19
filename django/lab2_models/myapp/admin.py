from django.contrib import admin
from .models import Musician, Album, Runner, Fruit, PersonShirt, PersonVerbose, Manufacturer, Car, Topping, Pizza, Place, Restaurant


# Đăng ký model Person để hiển thị trong trang admin
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(PersonShirt)
admin.site.register(Runner)
admin.site.register(Fruit)
admin.site.register(PersonVerbose)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Place)
admin.site.register(Restaurant)