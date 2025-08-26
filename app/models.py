from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Reklama'
        verbose_name_plural = 'Reklamalar'
        ordering = ['title']

    def __str__(self):
        return self.title


class Announcement(models.Model):
    name = models.CharField(max_length=250, verbose_name="Malumot Nomi")
    description = models.TextField(verbose_name="Malumot qo‘shing")
    views = models.IntegerField(default=0, null=True, blank=True, verbose_name="Ko‘rishlar soni")
    image = models.ImageField(upload_to="image/", null=True, blank=True, verbose_name="Surat kiriting")
    video = models.FileField(upload_to="video/", null=True, blank=True, verbose_name="Video kiriting")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo‘yilgan vaqti")
    update_at = models.DateTimeField(auto_now=True, verbose_name="O‘zgartirilgan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarilsinmi?")
    author = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name="Bo‘limlar")

    class Meta:
        verbose_name = 'Elon'
        verbose_name_plural = 'Elonlar'
        ordering = ['-create_at']

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Izoh matni")
    film = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Film')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Foydalanuvchi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user} - {self.text[:30]}"
