from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self .first_name

class Readers(models.Model):
    name = models.CharField(max_length=64)
    rid = models.CharField(max_length=32, unique=True)
    sex = models.CharField(max_length=64)
    Contact_number = models.CharField(max_length=64)

    def __str__(self):
        return self .name

class Publisher(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=32)
    state_province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    website = models.URLField()

    def __str__(self):
        return self .name

class Category (models.Model):
    name = models.CharField(max_length=64)
    cid = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self .name

class Book(models.Model):
    STATUS_CHOICES = (
        ('checkout', u'已出版'),
        ('dai', u'待出版'),
        ('status', u'审核中'),
    )
    bname = models.CharField(max_length=64)
    bid = models.CharField(max_length=32, unique=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publisher_date = models.DateField(auto_now_add=True)
    publisher_state = models.CharField(max_length=20, choices=STATUS_CHOICES, default='checkout')

    def __str__(self):
        return self .bname

class Brorrow(models.Model):
    bookname = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookname')
    wid = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='wid')
    name = models.ForeignKey(Readers, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self .bookname

class Returnbook(models.Model):
    BASIC_CHOICES = (
        ('checkout', u'完好'),
        ('status', u'损坏'),
    )
    STATUS_CHOICES = (
        ('checkout', u'未逾期'),
        ('status', u'逾期'),
    )
    tname = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='tname')
    tid = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='tid')
    Damage_situation = models.CharField(max_length=20, choices=BASIC_CHOICES, default='checkout')

    Expired_condition = models.CharField(max_length=20, choices=STATUS_CHOICES, default='checkout')

    def __str__(self):
        return self .tname

class Administrators(models.Model):
    name = models.CharField(max_length=64)
    aid = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self .name

class Loss(models.Model):
    lname = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='lname')
    lid = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='lid')
    penalty_money = models.CharField(max_length=64)

    def __str__(self):
        return self .lname

class Overdue(models.Model):
    reader_id = models.ForeignKey(Readers, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    penalty_money = models.CharField(max_length=64)
    overdue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self .reader_id
