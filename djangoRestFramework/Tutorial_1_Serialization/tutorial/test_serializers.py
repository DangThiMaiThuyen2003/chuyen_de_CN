# test_serializers.py
import io
import django
import os

# Cấu hình Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Tạo 2 snippet để test
s1 = Snippet(code='foo = "bar"\n')
s1.save()
s2 = Snippet(code='print("hello, world")\n')
s2.save()

print("==> Danh sách Snippet trong DB:")
print(Snippet.objects.all())

# Serialize 1 instance
serializer = SnippetSerializer(s2)
print("\n==> Serializer Data (Python dict):")
print(serializer.data)

# Render JSON
content = JSONRenderer().render(serializer.data)
print("\n==> JSON Output:")
print(content)

# Deserialize lại từ JSON
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
print("\n==> Parsed JSON (Python dict):")
print(data)

serializer2 = SnippetSerializer(data=data)
print("\n==> is_valid:", serializer2.is_valid())
print("Validated Data:", serializer2.validated_data)
obj = serializer2.save()
print("==> Save object:", obj)

# Serialize queryset
serializer3 = SnippetSerializer(Snippet.objects.all(), many=True)
print("\n==> Serialize toàn bộ queryset:")
print(serializer3.data)
