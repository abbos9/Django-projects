# import
from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect
from django.views.generic import (TemplateView, CreateView, ListView)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
# models 
from blogs.models import CategoryModel, InstragramModel, LikedModel, PostModel, TagsModel
from pages.forms import contactForm
from pages.models import (ContactModel, GalleryModel, MenuModel,
TestimonialsModel, BannerModel,)
# forms

# Create your views here.

class PageIndexView(ListView):
    template_name = 'index.html'
    model = MenuModel
    context_object_name = 'menus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specials'] = MenuModel.objects.all()[:2]
        context['testimols'] =TestimonialsModel.objects.filter(is_active=True)
        context['instagrams'] =InstragramModel.objects.all()[:4]
        context['banners'] =BannerModel.objects.filter(is_active=True)
        return context


class PageAboutView(ListView):
    template_name = 'about.html'
    model = GalleryModel
    context_object_name = 'galleries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specials'] = InstragramModel.objects.all()[:4]
        context['testimols'] =TestimonialsModel.objects.filter(is_active=True)
        return context
    def get_queryset(self):
        product = super().get_queryset()
        return product


class PageContactView(CreateView):
    template_name = 'contact.html'
    model = ContactModel
    form_class = contactForm
    success_url = reverse_lazy("pages:contact")

class PageElementView(TemplateView):
    template_name = 'elements.html'

class PageMainView(TemplateView):
    template_name = 'main.html'

class PageMenuView(ListView):
    template_name = 'menu.html'
    model =  MenuModel
    context_object_name = 'menus'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instagrams'] =InstragramModel.objects.all()[:4]
        context['specials'] = MenuModel.objects.all()[:2]
        context['testimols'] =TestimonialsModel.objects.filter(is_active=True)
        return context


class LikedView(ListView):
    template_name = 'liked.html'
    model = LikedModel
    context_object_name = 'likes'
    paginate_by = 2

    def get_queryset(self):
        liked = super().get_queryset()
        liked = LikedModel.objects.filter(user__id=self.request.user.pk)
        return liked
