from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from usefulModels.models import ReadingBook, QuesModel

#Tạo render cho HOME
def homePage(request):
    object_list = ReadingBook.objects.all()
    return render(
        request,
        'homePage.html',
        {'object_list':object_list,}
        )

#Tạo render cho READING    
def readingSite(request):
    object_view = ReadingBook.objects.all()
    object_view1 = ReadingBook.objects.filter(category__name = 'Funny Story')
    object_view2 = ReadingBook.objects.filter(category__name = 'Jokes')
    object_view3 = ReadingBook.objects.filter(category__name = 'Children Story')
    return render (
        request,
        'readingSite.html',{
        'object_view': object_view,
        'object_view1' : object_view1,
        'object_view2' :object_view2,
        'object_view3' :object_view3,
        }
    ) 

#Tạo render cho READPAGE
def readPageSite(request, id):

    if request.method == 'POST':
        print(request.POST)
        object_views = ReadingBook.objects.get(id = id) 
        questions=QuesModel.objects.filter()

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
        return render(request,'', context)
    else:
        object_views = ReadingBook.objects.get(id = id)
        questions=QuesModel.objects.filter()
        
        context = {
            'questions':questions,
            'object_views': object_views,
        }
        return render(request,'readPageSite.html', context)