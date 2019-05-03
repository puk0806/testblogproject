from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects    # 쿼리셋 # 메소드
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id) :
    details = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog': details})

# new.html 띄어주는 함수
def new (request):

    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()     # 객체.deleate() 삭제
    return redirect('/blog/'+str(blog.id))   # redirect : 위에 상황을 처리한훈 해당 URL이동