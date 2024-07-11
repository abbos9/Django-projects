# imports
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from blogs.models import CategoryModel, CommentModel, LikedModel, PostModel, TagsModel

# Create your views here.

class PageBlogDetailtView(DetailView):
    template_name = 'single-blog.html'
    model = PostModel
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['recent_posts'] = PostModel.objects.all().order_by("-created_at")
        context['tags'] = TagsModel.objects.all()
        context['comments'] = CommentModel.objects.filter(post__id=self.object.id) 
        return context

    def get_queryset(self):
        post=super().get_queryset()
        tag= self.request.GET.get('tag')
        category= self.request.GET.get('category')
        q = self.request.GET.get('q')
        if q:
            post = PostModel.objects.filter(headline__icontains=q)
        elif category:
            post = PostModel.objects.filter(category__name=category)
        elif tag:
            post = PostModel.objects.filter(tags__name=tag)
        return post


@login_required
def add_to_like(request, product_pk):
    post = get_object_or_404(PostModel, pk=product_pk)
    try:
        LikedModel.objects.create(user=request.user, post=post)
    except IntegrityError:
        LikedModel.objects.filter(user=request.user, post=post).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse_lazy('blog:blog')))


def CommentView(request, pk):
    post = PostModel.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("comment")
        website = request.POST.get("website")
        CommentModel.objects.create(
            name=name, email=email,
            comment=text, website=website,
            post=post
        )
    return redirect('blog:blog_detail', pk=pk)

class PageBLogView(ListView):
    template_name = 'blog.html'
    model = PostModel
    context_object_name = 'posts'
    paginate_by = 1
    page_kwarg = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['recent_posts'] = PostModel.objects.all().order_by("-created_at")
        context['tags'] = TagsModel.objects.all()
        return context
    
    def get_queryset(self):
        post=super().get_queryset()
        tag= self.request.GET.get('tag')
        category= self.request.GET.get('category')
        q = self.request.GET.get('q')
        if q:
            post = PostModel.objects.filter(headline__icontains=q)
        elif category:
            post = PostModel.objects.filter(category__name=category)
        elif tag:
            post = PostModel.objects.filter(tags__name=tag)
        return post