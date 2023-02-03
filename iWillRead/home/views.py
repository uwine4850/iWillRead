from django.views.generic import ListView
# from iWillRead.section_page.models import SectionModel
from section_page.models import SectionModel


class SectionView(ListView):
    model = SectionModel
    context_object_name = 'sections'
    template_name = 'home/home.html'


# def test(request):
#     return render(request, 'home/home.html')


