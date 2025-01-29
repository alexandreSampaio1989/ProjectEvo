from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now_add=True)
    deletado = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=50)
    qtEstoque = models.IntegerField('Quantidade em Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

#class Pessoa(Base):
#    nome = models.CharField('Nome', max_length=100)
#    telefone = models.CharField('Telefone', max_length=100)
#    celular = models.CharField('Celular', max_length=100)
#    email = models.EmailField('E-Mail', max_length=100)
#
#    class Meta:
#        abstract = True

#class Fornecedor(Pessoa):


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)