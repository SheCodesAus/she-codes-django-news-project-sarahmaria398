from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm, StoryFormUpdate


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = stories[:4]
        context['all_stories'] = stories
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateStoryView(generic.UpdateView):
    # form_class = StoryFormUpdate
    context_object_name = 'storyForm'
    template_name = 'news/editStory.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('news:index')

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()


# class IndexViewSelected(generic.ListView):
#     template_name = 'news/index.html'

#     def get_queryset(self):
#         '''Return all news stories.'''
#         return NewsStory.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         stories = NewsStory.objects.all().filter('{{user.name}}')
#         # context['latest_stories'] = stories[:4]
#         context['all_stories'] = stories
#         return context