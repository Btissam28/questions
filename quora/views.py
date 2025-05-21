# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, QuestionForm, AnswerForm
from .models import Question, Answer

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'quora/home.html', {'questions': questions})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'quora/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'quora/login.html', {'form': form})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'quora/ask_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('home')
    else:
        form = AnswerForm()

    return render(request, 'quora/answer_question.html', {'question': question, 'answers': answers, 'form': form})



@login_required
def notification_view(request):
    user_answers = Answer.objects.filter(question__user=request.user).order_by('-created_at')
    return render(request, 'quora/notifications.html', {'user_answers': user_answers})

def contactus(request):
    
    return render(request, 'quora/contactus.html')


