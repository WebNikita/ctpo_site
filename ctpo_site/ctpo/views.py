from django.shortcuts import render, get_object_or_404
from .models import Post, Training_programs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main_page(request):
    posts = Post.published.filter(status='published')
    programs = Training_programs.object.all()
    robotech = programs[0]
    IoT = programs[1]
    return render(request, 'ctpo/news/main.html', {'posts': posts, 'robotech': robotech, 'IoT': IoT})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,
    publish__month=month,publish__day=day)
    return render(request,'ctpo/news/detail.html',{'post': post})

def all_news(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'ctpo/news/list.html', {'page': page,'posts': posts})