import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import Runner
r = Runner(name="Usain Bolt", medal=Runner.MedalType.GOLD)
r.save()
print(r.medal)                # 'GOLD'
print(r.get_medal_display())  # 'Gold Medal'
