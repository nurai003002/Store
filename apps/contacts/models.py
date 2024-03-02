from django.db import models




class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '11) Обратная связь'
        verbose_name_plural = '11) Обратная связь'
        