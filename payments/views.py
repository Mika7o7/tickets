from django.views.generic.base import TemplateView
from .models import Ticket



class HomePageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Query your model to get data
        context['model_data'] = Ticket.objects.all()
        return context

