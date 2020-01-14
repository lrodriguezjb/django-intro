from django.views.generic import TemplateView

# def homepage(request):
#     return HttpResponse('Nice!')

class HomePageView(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

