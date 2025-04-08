from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
