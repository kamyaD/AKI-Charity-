from django.shortcuts import render, redirect,get_object_or_404
# from django.http import  HttpResponse
from .models import Contacts, BlogPost,Comment
from .form import CommentForm

# Create your views here.
def index(request):
    return  render(request,'index.html')

def about(request):
    return  render(request,'about.html')

def team(request):
    return render(request,'team.html')

def testimonials(request):
    return render(request,'testimonials.html')

def services(request):
    return render(request,'services.html')

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = Comment.objects.filter(post=post)

    context = {
        'comments': comments,
        'post': post,
    }

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', post_id=post_id)

    return render(request, 'blog-single.html', context)


    



def blog(request):
    posts = BlogPost.objects.all()

    # for post in posts:
    #     print("category===>", post.categories)

    context = {
        'posts': posts,
    }
    return render(request,'blog.html', context)

def contact(request):
    return render(request,'contact.html')

def education(request):
    return render(request,'education.html')

def health(request):
    return render(request,'health.html')

def economic(request):
    return render(request,'economic.html')

def conflict(request):
    return render(request,'conflict.html')

def climate(request):
    return render(request,'climate.html')

def partnerships(request):
    return render(request,'partner.html')

def success(request):
    return render(request,'success.html')

def get_contact_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_instance = Contacts(name = name, email=email, subject=subject, message=message)
        contact_instance.save()

        return redirect('success_page')
    return redirect('contact')

# def get_posts(request):
#     posts = BlogPost.objects.get()
#     print("posts====>", posts)
    # if request.method == 'GET':






