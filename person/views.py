from django.shortcuts import render
from main.models import Service
from posts.models import Post
from .models import Resume, About, Partner, Projects
from main.forms import GetInTouchForm


def index(request):
    resumes = Resume.objects.all()
    about = About.objects.all()
    partners = Partner.objects.all()
    posts = Post.objects.all()
    services = Service.objects.all()
    projects = Projects.objects.all()
    form = GetInTouchForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
    tags = request.GET.get('tags')
    cat = request.GET.get('cat')
    search = request.GET.get('search')
    if search:
        posts = posts.filter(title__icontains=search)
    if tags:
        posts = posts.filter(tag__tag=tags)
    if cat:
        posts = posts.filter(category__category=cat)
    context = {
        'resumes': resumes,
        'about': about,
        'form': form,
        'partners': partners,
        'posts': posts,
        'services': services,
        'projects': projects,
    }
    return render(request, 'index.html', context)

