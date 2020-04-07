from django.shortcuts import render, get_object_or_404,redirect 
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView)
from blog.models import Post, Comment
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CommentForm


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


class PostList(ListView):
    template_name = "blog/post_list.html"
    queryset = Post.objects.all()
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #context = super().get_context_data(**kwargs)
    #context['now'] = timezone.now()
    # return context

class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'
    Model = Post
    def get_object(self):
        slug= self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug)



def post_detail(request, slug, *args, **kwargs):
    posts = Post.objects.all()[:5]
    post = get_object_or_404(Post, slug=slug)
    
    comments = post.comments.filter(active=True)
    new_comment=None
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    context ={
        'post':post,
        'posts':posts,
        'comments':comments,
        'new_comment':new_comment,        
        'comment_form':comment_form,
    }
    
    
    return render(request, "blog/post_detail.html", context)
                                        

def search(request, *args, **kwargs):
    query = request.GET.get('q', '')

    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(body__icontains=query)
    )
    context = {
        'results': results,
        'query': query

    }
    return render(request, 'blog/search.html', context)


def aboutPage(request):
    context={}
    return render(request, 'blog/about.html', context)

def contactPage(request):
    context={}
    return render(request, 'blog/contact.html', context)
