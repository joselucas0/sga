from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota_prova = models.DecimalField(max_digits=5, decimal_places=2)
    nota_trabalho = models.DecimalField(max_digits=5, decimal_places=2)

    def media(self):
        return (self.nota_prova + self.nota_trabalho) / 2

    def aprovado(self):
        return self.media() >= 6

    def __str__(self):
        return f"Avaliação de {self.aluno.nome}"