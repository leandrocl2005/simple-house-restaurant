from django.db import models


class Category(models.Model):
  name = models.CharField('nome', max_length=100)

  class Meta:
    ordering = ('name', )
    verbose_name = "Categoria"
    verbose_name_plural = "Categorias"

  def __str__(self):
    return self.name


class Food(models.Model):

  name = models.CharField('nome', max_length=100, unique=True)
  description = models.TextField('descrição', null=True, blank=True)
  photo = models.ImageField(upload_to='static/img', null=True, blank=True)
  price = models.IntegerField('preço', null=True, blank=True)
  category = models.ForeignKey(Category,
                               related_name='food',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)

  class Meta:
    ordering = ('name', )
    verbose_name = "Comida"
    verbose_name_plural = "Comidas"

  @property
  def formatted_price(self):
    return "R$ {:0.2f}".format(self.price / 100).replace('.', ',')

  def __str__(self):
    return self.name