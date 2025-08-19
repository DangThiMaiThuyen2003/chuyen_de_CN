from django.db import migrations

def forwards_func(apps, schema_editor):
    Blog = apps.get_model("myapp", "Blog")
    db_alias = schema_editor.connection.alias
    Blog.objects.using(db_alias).bulk_create(
        [
            Blog(name="Tech Blog", tagline="All about technology and innovation"),
            Blog(name="Food Blog", tagline="Recipes and culinary adventures"),
        ]
    )

def reverse_func(apps, schema_editor):
    Blog = apps.get_model("myapp", "Blog")
    db_alias = schema_editor.connection.alias
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