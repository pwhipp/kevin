from step_game.forms import ActorSearchForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from step_game.models import Movie, Actor

class SearchFormMixin(object):
    """Mixin behaviour for the search form"""
    form_class = ActorSearchForm
    def get_context_data(self, **kwargs):
        """Specialisation to add actor_search_form to context"""
        context = super(SearchFormMixin, self).get_context_data(**kwargs)
        context['actor_search_form'] = ActorSearchForm(self.request.POST)
        return context

    def post(self, request, *args, **kwargs):
        """Specialisation to redirect to result using valid form data"""
        form = ActorSearchForm(request.POST)
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        if form.is_valid():
            try:
                actor = Actor.objects.get(last_name=last_name, first_name=first_name)
                return redirect('result', last_name=last_name, first_name=first_name)
            except Actor.DoesNotExist:
                pass

        msg = "Sorry: '{0}', '{1}' is not a known actor.".format(last_name, first_name)
        messages.add_message(request, messages.WARNING, msg)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
            
    
class MainView(SearchFormMixin, TemplateView):
    template_name = 'step_game/main.html'


class ResultView(SearchFormMixin, ListView):
    template_name = 'step_game/result.html'
    model = Movie
    context_object_name = "movie_list"
    paginate_by = 10


    def get_queryset(self):
        """Specialisation to just get the movies starring our actor"""
        self.bacon = Actor.objects.get(last_name='Bacon', first_name='Kevin')
        self.actor = get_object_or_404(Actor,
                                       last_name=self.kwargs['last_name'],
                                       first_name=self.kwargs['first_name'])
        all_movies = super(ResultView, self).get_queryset()

        # Add in the shared movies - Django optimises this!
        self.shared_movies = Movie.objects.filter(role__actor=self.actor)
        self.shared_movies = self.shared_movies.filter(role__actor=self.bacon)
        
        return all_movies.filter(role__actor=self.actor)

    def get_context_data(self, **kwargs):
        """Specialisation to add actor and shared movies to context."""
        context = super(ResultView, self).get_context_data(**kwargs)

        context['actor'] = self.actor
        context['shared_movie_list'] = self.shared_movies
        return context
    

