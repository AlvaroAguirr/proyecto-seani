from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .forms import CandidateForm
from .models import Exam

@login_required
def home(request) :
    user= request.user
    if user.is_superuser:
            return redirect('admin:index')
    return render(request, 'exam/home.html',{"user": user})

@login_required
def question(request, m_id, q_id =1):

    exam= request.user.exam

    if(q_id <1):
        return redirect('exam:home')


    if request.method =='POST':
        questions= exam.breakdown_set.filter(question__module_id=m_id)
        question= questions[q_id-1]
        question.answer = request.POST['answer']
        question.save()
        return redirect('exam:question', m_id, q_id +1)
    try:
        questions = exam.breakdown_set.filter(question__module_id= m_id)
        question= questions[q_id-1].question
        answer= questions[q_id-1].answer
        return render(request, 'exam/question.html',
                    {
                        "question": question,
                        "m_id":m_id,
                        "q_id":q_id,
                        "answer":answer
                        })
    except IndexError:
        return redirect('exam:home')

@login_required
def add_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            stage = form.cleaned_data['stage']
            career = form.cleaned_data['career']



            # crear usuario
            user= User.objects.create_user(username,email,password)
            # editar usuario
            user.first_name = first_name
            user.last_name =last_name
            user.save()

            # crear examen
            exam= Exam.objects.create(user=user, stage=stage, career=career)
            exam.set_modules()
            exam.set_question()
            html = """

            return HttpResponse("usuario y examen create ")
        
        <h1>Agregar Aspirantes UwU</h1>
            <a href="/exam/add/">Agregar otro</a>
            """
            return HttpResponse(html)


            # llenar examen
    form =CandidateForm()
    return render(request, 'exam/add_candidate.html',{"form": form})