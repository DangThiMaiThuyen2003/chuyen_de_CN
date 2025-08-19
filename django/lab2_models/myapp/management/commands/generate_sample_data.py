from django.core.management.base import BaseCommand, CommandError
from myapp.models import Blog, Author, Entry
from datetime import date

class Command(BaseCommand):
    help = 'Generates sample data for Blog, Author, and Entry models'

    def add_arguments(self, parser):
        # Positional argument: number of records to generate
        parser.add_argument('count', type=int, help='Number of records to generate for each model')
        # Optional argument: delete existing data
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete existing data before generating new data',
        )

    def handle(self, *args, **options):
        count = options['count']
        if count <= 0:
            raise CommandError('Count must be a positive integer')

        try:
            # Delete existing data if --delete is specified
            if options['delete']:
                Entry.objects.all().delete()
                Author.objects.all().delete()
                Blog.objects.all().delete()
                self.stdout.write(self.style.SUCCESS('Successfully deleted existing data'))

            # Generate sample data
            for i in range(count):
                # Create Blog
                blog = Blog.objects.create(
                    name=f"Blog {i+1}",
                    tagline=f"Tagline for Blog {i+1}"
                )

                # Create Author
                author = Author.objects.create(
                    name=f"Author {i+1}",
                    email=f"author{i+1}@example.com"
                )

                # Create Entry
                entry = Entry.objects.create(
                    blog=blog,
                    headline=f"Post {i+1}",
                    body_text=f"Content of post {i+1}.",
                    pub_date=date(2025, 8, 20),
                    mod_date=date(2025, 8, 20),
                    number_of_comments=i + 1,
                    number_of_pingbacks=i,
                    rating=5 + (i % 5)  # Vary rating between 5 and 9
                )

                # Link Author to Entry
                entry.authors.add(author)

                self.stdout.write(self.style.SUCCESS(f'Successfully created Blog {i+1}, Author {i+1}, and Post {i+1}'))

        except Exception as e:
            raise CommandError(f'Error generating sample data: {str(e)}')