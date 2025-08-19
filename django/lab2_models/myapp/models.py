from django.db import models

from datetime import date


class PersonProfile(models.Model):   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100, default="Unknown")  

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.name})"
 
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
    
class PersonShirt(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return f"{self.name} ({self.get_shirt_size_display()})"
    
class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = "GOLD", "Gold Medal"
        SILVER = "SILVER", "Silver Medal"
        BRONZE = "BRONZE", "Bronze Medal"

    name = models.CharField(max_length=60)
    medal = models.CharField(
        max_length=10,
        choices=MedalType.choices,
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.medal}"
    
class Fruit(models.Model):
     # name sẽ làm primary key, Django sẽ KHÔNG tạo cột id
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

# Verbose name = tên hiển thị “dễ đọc hơn” cho field (ví dụ khi dùng trong Admin hoặc form).
class PersonVerbose(models.Model):
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField("person's last name", max_length=30)

class Poll(models.Model):
    question = models.CharField(max_length=200)

class Vote(models.Model):
    poll = models.ForeignKey(
        Poll, 
        on_delete=models.CASCADE, 
        verbose_name="the related poll"
    )
    
# Many-to-one relationship (ForeignKey)
# Khi một Manufacturer bị xóa, tất cả Car liên quan cũng bị xóa (on_delete=models.CASCADE).
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} - {self.model_name}"
    
# Many-to-many relationship (ManyToManyField)
# Ví dụ: Một Pizza có nhiều Topping, một Topping có thể nằm trên nhiều Pizza.
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

# One-to-one relationship (OneToOneField)
# Ví dụ: Một Place có đúng một Restaurant
# OneToOneField tương tự ForeignKey(unique=True)
class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place, 
        on_delete=models.CASCADE, 
        verbose_name="related place"
    )
    serves_hot_dogs = models.BooleanField(default=False)

    def __str__(self):
        return f"Restaurant at {self.place}"
    

# --------------------
class Person(models.Model):
    name = models.CharField(max_length=128, default="Unknown")
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField("Person", through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["person", "group"], name="unique_person_group"
            )
        ]

    def __str__(self):
        return f"{self.person} in {self.group}"
    
    


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline






