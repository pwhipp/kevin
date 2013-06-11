from step_game.forms import ActorForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from step_game.models import Movies

class MainView(FormView):
    template_name = 'step_game/main.html'
    form_class = ActorForm

    def form_valid(self, form):
        """create /result/<last_name>/<first_name>/"""
        self.success_url = "/result/Affleck/Casey/"
        return super(MainView, self).form_valid(form)

class ResultView(ListView):
    template_name = 'step_game/result.html'
    model = Movies
    context_object_name = "movie_list"
    paginate_by = 10
    # If actor not found redirect to 404
    

