import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomodel.settings")
django.setup()

from myapp.models import Blog, Author, Entry


def create_sample_data():
    Blog.objects.all().delete()
    Author.objects.all().delete()
    Entry.objects.all().delete()

    # Tạo Blog
    blog1 = Blog.objects.create(name="Tech Blog", tagline="All about tech")
    blog2 = Blog.objects.create(name="Travel Blog", tagline="Adventures worldwide")

    # Tạo Author
    author1 = Author.objects.create(name="Alice", email="alice@example.com")
    author2 = Author.objects.create(name="Bob", email="bob@example.com")
    author3 = Author.objects.create(name="Charlie", email="charlie@example.com")

    # Tạo Entry
    entry1 = Entry.objects.create(
        blog=blog1,
        headline="Django ORM Guide",
        body_text="This is an article about Django ORM.",
        pub_date=date(2024, 5, 1),
        number_of_comments=5,
        rating=4,
    )
    entry1.authors.add(author1, author2)

    entry2 = Entry.objects.create(
        blog=blog1,
        headline="Python Tips",
        body_text="Advanced Python tips.",
        pub_date=date(2024, 6, 15),
        number_of_comments=2,
        rating=5,
    )
    entry2.authors.add(author2)

    entry3 = Entry.objects.create(
        blog=blog2,
        headline="Trip to Japan",
        body_text="My trip to Japan.",
        pub_date=date(2024, 7, 10),
        number_of_comments=8,
        rating=5,
    )
    entry3.authors.add(author1, author3)


def relational_queries():
    print("\n=== Forward ForeignKey (Entry → Blog) ===")
    entry = Entry.objects.get(headline="Django ORM Guide")
    print(f"Entry: {entry}, Blog: {entry.blog}")

    print("\n=== Backward ForeignKey (Blog → Entry set) ===")
    blog = Blog.objects.get(name="Tech Blog")
    print(f"Blog: {blog}")
    for e in blog.entry_set.all():
        print(f" - Entry: {e}")

    print("\n=== Forward ManyToMany (Entry → Authors) ===")
    entry = Entry.objects.get(headline="Trip to Japan")
    print(f"Entry: {entry}")
    for a in entry.authors.all():
        print(f" - Author: {a}")

    print("\n=== Backward ManyToMany (Author → Entries) ===")
    author = Author.objects.get(name="Alice")
    print(f"Author: {author}")
    for e in author.entry_set.all():
        print(f" - Entry: {e}")

    print("\n=== Filtering across relationships ===")
    blogs = Blog.objects.filter(entry__headline__contains="Python")
    print("Blogs with entries containing 'Python':")
    for b in blogs:
        print(f" - {b}")

    authors = Author.objects.filter(entry__headline__contains="Django").distinct()
    print("Authors with entries containing 'Django':")
    for a in authors:
        print(f" - {a}")

    print("\n=== Complex lookups with related fields ===")
    entries = Entry.objects.filter(authors__name="Bob", blog__name="Tech Blog")
    print("Entries written by Bob in Tech Blog:")
    for e in entries:
        print(f" - {e}")


if __name__ == "__main__":
    create_sample_data()
    relational_queries()
