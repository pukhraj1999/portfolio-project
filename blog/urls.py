from django.urls import path
from blog import views

urlpatterns = [
    path('', views.Blogs, name='blog'),
    # Saving int as blog id
    path('<int:blog_id>/',views.detail,name='detail')
]