from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import  NewsStory
from .forms import StoryForm, StoryFormUpdate
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = stories[:3]
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


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    def delete_data(request, story_id):
        post_to_delete=NewsStory.objects.get(id=story_id)
        post_to_delete.delete()

    
class AuthorsListView(generic.ListView):
    form_class = StoryForm
    context_object_name = 'author_list'
    template_name = 'news/author.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(AuthorsListView, self).get_context_data(**kwargs)
        context['author'] = NewsStory.objects.all()
        return context

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return NewsStory.objects.filter(author = author_id,)
