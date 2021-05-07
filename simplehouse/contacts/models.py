from django.db import models


# Create your models here.
class Contact(models.Model):

  name = models.CharField('nome', max_length=30, unique=True)
  email = models.EmailField('email')
  message = models.TextField('mensagem')
  created_at = models.DateTimeField("Criado em", auto_now_add=True)

  class Meta:
    ordering = ('-created_at', )
    verbose_name = "Contato"
    verbose_name_plural = "Contatos"

  def __str__(self):
    return self.name