from django.shortcuts import render, redirect
from .models import Aluno, Avaliacao
from .forms import AlunoForm, AvaliacaoForm

def home(request):
    return render(request, 'alunos/home.html')

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastro_aluno.html', {'form': form})

def cadastro_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AvaliacaoForm()
    return render(request, 'alunos/cadastro_avaliacao.html', {'form': form})

def relatorio(request):
    alunos = Aluno.objects.all()
    dados = []
    for aluno in alunos:
        avaliacoes = Avaliacao.objects.filter(aluno=aluno)
        media = sum([av.media() for av in avaliacoes]) / len(avaliacoes) if avaliacoes else 0
        dados.append({
            'aluno': aluno,
            'media': media,
            'aprovado': media >= 6
        })
    return render(request, 'alunos/relatorio.html', {'dados': dados})