import os
import django
from datetime import date

# Cấu hình Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import Person, Group, Membership

# Xóa dữ liệu cũ để chạy lại nhiều lần
Membership.objects.all().delete()
Group.objects.all().delete()
Person.objects.all().delete()

# Tạo Person
ringo = Person.objects.create(name="Ringo Starr")
paul = Person.objects.create(name="Paul McCartney")

# Tạo Group
beatles = Group.objects.create(name="The Beatles")

# Tạo Membership
m1 = Membership.objects.create(
    person=ringo,
    group=beatles,
    date_joined=date(1962, 8, 16),
    invite_reason="Needed a new drummer.",
)

m2 = Membership.objects.create(
    person=paul,
    group=beatles,
    date_joined=date(1960, 8, 1),
    invite_reason="Wanted to form a band.",
)

print("== Thành viên Beatles ==")
for member in beatles.members.all():
    print(member.name)

# Truy vấn Membership cụ thể
ringos_membership = Membership.objects.get(group=beatles, person=ringo)
print("\nThông tin Membership của Ringo:")
print("Ngày tham gia:", ringos_membership.date_joined)
print("Lý do:", ringos_membership.invite_reason)

# Query nâng cao
after_1961 = Person.objects.filter(
    group__name="The Beatles", membership__date_joined__gt=date(1961, 1, 1)
)
print("\nThành viên Beatles tham gia sau 1/1/1961:")
for p in after_1961:
    print(p.name)
