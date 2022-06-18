from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import TemplateView
from news.views import StoryForm, NewsStory, AuthorsListView

from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    
#     form_class = StoryForm
#     context_object_name = 'author_list'
#     template_name = 'users/profile.html'
#     paginate_by = 50

#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         context['author'] = NewsStory.objects.all()
#         return context

#     def get_queryset(self):
#         author_id = self.kwargs['pk']
#         return NewsStory.objects.filter(author = author_id,)
