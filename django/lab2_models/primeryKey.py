import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()


from myapp.models import Fruit
fruit = Fruit.objects.create(name="Apple")
fruit.name = "Pear"
fruit.save()
print(Fruit.objects.values_list("name", flat=True))  
# ['Apple', 'Pear']
