
from django.contrib.auth.forms import AuthenticationForm
from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render
from Reading.models import QuesModel, ReadingBook
from Reading.forms import createuserform
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *




#Tạo render cho HOME
def home_view(request):
    object_list = ReadingBook.objects.all()

    return render(
        request,
        'dashboard.html',{
            'object_list':object_list,
        }
    )

#Tạo render cho ABOUT
def about_view(request):
    return render(
        request,
        'about.html',{}
    )


#Tạo render cho READ-PAGE
def read_page_view(request, id):

    if request.method == 'POST':
        print(request.POST)
        object_views = ReadingBook.objects.get(id = id) 
        questions=QuesModel.objects.filter(name_read__name = id)
        
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'object_views': object_views,
            
        }
        return render(request,'Test/result.html', context)
    else:
        object_views = ReadingBook.objects.get(id = id)
        questions=QuesModel.objects.filter()
        
        context = {
            'questions':questions,
            'object_views': object_views,
        }
        return render(request,'read-page.html', context)
#Tạo render cho READING    
def reading_view(request):
    object_view = ReadingBook.objects.all()
    object_view1 = ReadingBook.objects.filter(category__name = 'Funny Story')
    object_view2 = ReadingBook.objects.filter(category__name = 'Jokes')
    object_view3 = ReadingBook.objects.filter(category__name = 'Children Story')
    return render (
        request,
        'reading.html',{
        'object_view': object_view,
        'object_view1' : object_view1,
        'object_view2' :object_view2,
        'object_view3' :object_view3,
        }
    ) 

#Tạo render cho Register
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Sign/register.html',context)

#Tạo render cho LogIn
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=AuthenticationForm(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Sign/login.html',context)


#Tạo render cho LogOut
def logoutPage(request):
    logout(request)
    return redirect('/')