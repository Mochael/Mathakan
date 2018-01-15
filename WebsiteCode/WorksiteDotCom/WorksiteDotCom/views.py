from django.shortcuts import render
from django.views.generic.base import View

class Home(View):
    def get(self, request):
        context = {}
        posts = Post.objects.all()
        context["posts"] = posts
        return render(request,"home.html", context)

