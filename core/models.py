from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    delecao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=50)
    qtEstoque = models.IntegerField('Quantidade em Estoque')

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
