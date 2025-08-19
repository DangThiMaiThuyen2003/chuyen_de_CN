import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import PersonShirt

p = PersonShirt(name="Fred Flintstone", shirt_size="L")
p.save()
print(p.shirt_size)              # 'L'
print(p.get_shirt_size_display()) # 'Large'

