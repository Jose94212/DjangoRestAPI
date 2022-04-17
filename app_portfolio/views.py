import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from app_portfolio.forms import PostForm
from app_portfolio.models import Post


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    html = '''<html><body>Portfolio\n</body></html>
            <html><body><br>It is now %s.</body></html>''' % now
    return HttpResponse(html)

def view_company_name(request,company_name):
    html='<html><body>Company name:%s</body></html>'% company_name
    return HttpResponse(html)


def view_apple(request):
    return HttpResponse('this is apple!!!')

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
