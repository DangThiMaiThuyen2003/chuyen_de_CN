from django.db import migrations
from datetime import date

def forwards_func(apps, schema_editor):
    Blog = apps.get_model("myapp", "Blog")
    Author = apps.get_model("myapp", "Author")
    Entry = apps.get_model("myapp", "Entry")
    db_alias = schema_editor.connection.alias

    # Tạo 2 bản ghi Blog
    blogs = Blog.objects.using(db_alias).bulk_create([
        Blog(name="Tech Blog", tagline="All about technology and innovation"),
        Blog(name="Food Blog", tagline="Recipes and culinary adventures"),
    ])

    # Tạo 2 bản ghi Author
    authors = Author.objects.using(db_alias).bulk_create([
        Author(name="John Doe", email="john@example.com"),
        Author(name="Jane Smith", email="jane@example.com"),
    ])

    # Tạo 2 bản ghi Entry, liên kết với Blog và Author
    entries = Entry.objects.using(db_alias).bulk_create([
        Entry(
            blog=blogs[0],  # Tech Blog
            headline="Tech Trends 2025",
            body_text="Exploring the latest in AI and tech.",
            pub_date=date(2025, 8, 20),
            mod_date=date(2025, 8, 20),
            number_of_comments=5,
            number_of_pingbacks=1,
            rating=7
        ),
        Entry(
            blog=blogs[1],  # Food Blog
            headline="Easy Pasta Recipe",
            body_text="A quick and delicious pasta dish.",
            pub_date=date(2025, 8, 19),
            mod_date=date(2025, 8, 20),
            number_of_comments=3,
            number_of_pingbacks=0,
            rating=8
        ),
    ])

    # Liên kết Authors với Entries qua ManyToMany
    entries[0].authors.add(authors[0])  # John Doe -> Tech Trends 2025
    entries[1].authors.add(authors[1])  # Jane Smith -> Easy Pasta Recipe
    
def reverse_func(apps, schema_editor):
    Blog = apps.get_model("myapp", "Blog")
    Author = apps.get_model("myapp", "Author")
    Entry = apps.get_model("myapp", "Entry")
    db_alias = schema_editor.connection.alias

    # Xóa các bản ghi Entry
    Entry.objects.using(db_alias).filter(
        headline__in=["Tech Trends 2025", "Easy Pasta Recipe"]
    ).delete()
    # Xóa các bản ghi Author
    Author.objects.using(db_alias).filter(
        name__in=["John Doe", "Jane Smith"]
    ).delete()
    # Xóa các bản ghi Blog
    Blog.objects.using(db_alias).filter(
        name__in=["Tech Blog", "Food Blog"]
    ).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0011_author_blog_entry'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]