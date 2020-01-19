from django.views import generic
from django.db.models import Q

from .models import Meibo
from .forms import SearchForm
from pure_pagination.mixins import PaginationMixin

class IndexView(PaginationMixin, generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'meibo_list'
    keywords: str = "^$"
    paginate_by = 8

    def get_queryset(self):
        q = self.__get_where__()
        return Meibo.objects.filter(q).order_by('simei_kana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)
        return context

    def get(self, request, *args, **kwargs):
        fm = SearchForm(request.GET or None)
        if fm.is_valid():
            self.keywords = request.GET['keywords']
        return super().get(request, *args, **kwargs)

    def __get_where__(self):
        str = self.keywords
        q = Q(simei__regex = "^$")
        if str:
            q = Q()
            for s in str.replace('\u3000',' ').split(' '):
                q &= self.__get_q__(s)
        return q

    def __get_q__(self, str):
        q = Q(simei__regex = str)
        q |= Q(simei_kana__regex = str)
        q |= Q(seibetu__regex = str)
        q |= Q(blood_gata__regex = str)
        q |= Q(chiiki__regex = str)
        return q

