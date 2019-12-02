from django.views import generic
from django.db.models import Q

from .models import Meibo
from .forms import SearchFormSet

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'meibo_list'
    keywords: str = "^$"

    def get_queryset(self):
        q = self.__get_where__()
        return Meibo.objects.filter(q).order_by('simei_kana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchFormSet(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        fms = SearchFormSet(request.POST or None)
        fms.is_valid()
        for fm in fms:
            self.keywords = fm.cleaned_data.get('keywords')
        return self.get(request, *args, **kwargs)

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

