# complex_queries.py
"""
Ví dụ đầy đủ Complex lookups with Q objects
theo tài liệu: https://docs.djangoproject.com/en/5.2/topics/db/queries/
Áp dụng cho model Entry (thay Poll/question trong docs).
"""

import os
import django
import datetime
from django.db.models import Q
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import Entry, Blog, Author


def create_sample_data():
    """Tạo dữ liệu mẫu để test Q objects"""

    # Xóa dữ liệu cũ cho sạch
    Entry.objects.all().delete()
    Blog.objects.all().delete()
    Author.objects.all().delete()

    # Tạo blog
    blog = Blog.objects.create(name="Tech Blog", tagline="About Django ORM")

    # Tạo author
    author = Author.objects.create(name="John Doe", email="john@example.com")

    # Tạo entries mẫu
    e1 = Entry.objects.create(
        blog=blog,
        headline="First Post",
        body_text="Example entry",
        pub_date=date(2023, 1, 1),
        mod_date=date(2023, 1, 1),
    )
    e1.authors.add(author)

    e2 = Entry.objects.create(
        blog=blog,
        headline="Second Post",
        body_text="Another entry",
        pub_date=date(2023, 1, 2),
        mod_date=date(2023, 1, 2),
    )
    e2.authors.add(author)

    e3 = Entry.objects.create(
        blog=blog,
        headline="Other Post",
        body_text="Testing Q objects",
        pub_date=date(2024, 5, 1),
        mod_date=date(2024, 5, 1),
    )
    e3.authors.add(author)

    print("Sample data created!\n")


def run():
    print("\n Complex Queries with Q objects\n")

    # Một Q object đơn giản
    q1 = Entry.objects.filter(Q(headline__startswith="First"))
    print("Q object đơn giản (headline bắt đầu bằng 'First'):")
    for e in q1:
        print(f"- {e.headline}")

    # Kết hợp OR
    q2 = Entry.objects.filter(
        Q(headline__startswith="First") | Q(headline__startswith="Second")
    )
    print("\nOR query (headline bắt đầu 'First' OR 'Second'):")
    for e in q2:
        print(f"- {e.headline}")

    # OR và NOT
    q3 = Entry.objects.filter(
        Q(headline__startswith="First") | ~Q(pub_date__year=2023)
    )
    print("\nOR + NOT (headline bắt đầu 'First' OR pub_date KHÔNG phải năm 2023):")
    for e in q3:
        print(f"- {e.headline}, pub_date={e.pub_date}")

    # AND + OR
    q4 = Entry.objects.filter(
        Q(headline__startswith="First"),
        Q(pub_date=date(2023, 1, 1)) | Q(pub_date=date(2023, 1, 2)),
    )
    print(
        "\nAND + OR (headline bắt đầu 'First' AND pub_date = 2023-01-01 OR 2023-01-02):"
    )
    for e in q4:
        print(f"- {e.headline}, pub_date={e.pub_date}")

    # Q object + keyword arg
    q5 = Entry.objects.filter(
        Q(pub_date=date(2023, 1, 1)) | Q(pub_date=date(2023, 1, 2)),
        headline__startswith="First",
    )
    print("\nQ object + keyword arg (valid):")
    for e in q5:
        print(f"- {e.headline}, pub_date={e.pub_date}")

if __name__ == "__main__":
    create_sample_data()  # tạo dữ liệu trước
    run()
