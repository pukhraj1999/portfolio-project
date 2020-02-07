from django.shortcuts import render,get_object_or_404
# awesome function
from blog.models import Blog

# Create your views here.
def Blogs(request):
    blog=Blog.objects
    return render(request,'blog/blog.html',{'blog':blog})

def detail(request,blog_id):
    detail_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detail_blog})