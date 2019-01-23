from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate
from .forms import CandidateModelForm
from .forms import PositionModelForm

# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)

def create(request):
    context = {}
    form = CandidateModelForm()

    if request.method == "POST":
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request,'create.html', {'form': form})

def createp(request):
    context = {}
    form = PositionModelForm()

    if request.method == "POST":
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request,'createp.html', {'form': form})

def update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate Updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = CandidateModelForm(instance=candidate)
        return render(request, 'update.html', context)

def detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'detail.html', context)
