import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import Person

# Tạo dữ liệu
p1 = Person(first_name="John", last_name="Doe")
p1.save()

# Lấy dữ liệu
people = Person.objects.all()
for person in people:
    print(person.id, person.first_name, person.last_name)
