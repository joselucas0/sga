from django import forms
from .models import Aluno, Avaliacao

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'endereco']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['aluno', 'nota_prova', 'nota_trabalho']