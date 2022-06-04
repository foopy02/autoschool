from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    first_name = models.CharField(max_length=35,verbose_name="Аты")
    last_name = models.CharField(max_length=35,verbose_name="Тегі")
    patronym = models.CharField(max_length=35,verbose_name="Әкесінің аты")
    phone_number = models.CharField(max_length=200, verbose_name="Ұялы телефон")
    email = models.EmailField(verbose_name="Почтасы")
    
# Create your models here.
class Group(models.Model):
    class Days():
        MONDAY = "Дүйсенбі"
        TUESDAY = "Сейсенбі"
        WEDNESDAY = "Сәрсенбі"
        THURSDAY = "Бейсенбі"
        FRIDAY = "Жұма"
        SATURDAY = "Сенбі"
        SUNDAY = "Жексенбі"
        days = (
            (MONDAY, 'Дүйсенбі'),
            (TUESDAY, 'Сейсенбі'),
            (WEDNESDAY, 'Сәрсенбі'),
            (THURSDAY, 'Бейсенбі'),
            (FRIDAY, 'Жұма'),
            (SATURDAY, 'Сенбі'),
            (SUNDAY, 'Жексенбі'),
        )

    class Hours():
        o_clock_08__00 = "08:00"
        o_clock_09__00 = "09:00"
        o_clock_10__00 = "10:00"
        o_clock_11__00 = "11:00"
        o_clock_12__00 = "12:00"
        o_clock_13__00 = "13:00"
        o_clock_14__00 = "14:00"
        o_clock_15__00 = "15:00"
        o_clock_16__00 = "16:00"
        o_clock_17__00 = "17:00"
        o_clock_18__00 = "18:00"
        o_clock_19__00 = "19:00"
        o_clock_20__00 = "20:00"
        hours = (
            (o_clock_08__00, "08:00"),
            (o_clock_09__00, "09:00"),
            (o_clock_10__00, "10:00"),
            (o_clock_11__00, "11:00"),
            (o_clock_12__00, "12:00"),
            (o_clock_13__00, "13:00"),
            (o_clock_14__00, "14:00"),
            (o_clock_15__00, "15:00"),
            (o_clock_16__00, "16:00"),
            (o_clock_17__00, "17:00"),
            (o_clock_18__00, "18:00"),
            (o_clock_19__00, "19:00"),
            (o_clock_20__00, "20:00"),
        )
    name = models.CharField(max_length=255,verbose_name="Топтың аты")
    description = models.TextField(null=True, blank=True,verbose_name="Топтың қысқаша")
    day = models.CharField(choices=Days.days,max_length=255,verbose_name="Күн")
    hours = models.CharField(choices=Hours.hours,max_length=255,verbose_name="Сағат")
    filled = models.IntegerField(default=0,verbose_name="Неше оқушы бар")
    max_available = models.IntegerField(default=30,verbose_name="Максималды оқушылар саны")
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Құрылған уақыты")
    users = models.ManyToManyField(User,verbose_name="Оқушылар")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE,verbose_name="Қолданушы")
    dateofbirth = models.DateField(verbose_name="Туған күні")
    city = models.CharField(max_length=255, null=True, blank=True,verbose_name="Қала")
    IIN = models.CharField(max_length=20,verbose_name="ЖСН")
    patronym = models.CharField(max_length=35,verbose_name="Әкесінің аты")
    def __str__(self):
        return self.user.username
