from step_game.forms import ActorForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from step_game.models import Movie, Actor

class MainView(FormView):
    template_name = 'step_game/main.html'
    form_class = ActorForm

    def form_valid(self, form):
        """create /result/<last_name>/<first_name>/"""
        self.success_url = "/result/Affleck/Casey/"
        return super(MainView, self).form_valid(form)

class ResultView(ListView):
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
    

