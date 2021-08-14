import requests
from django.shortcuts import render
from django.views.generic import TemplateView


class TesteView(TemplateView):
    template_name = 'base/tabela.html'

    def get(self, request):
        url = 'http://127.0.0.1:4000/api-teste/get_infos/'
        response = requests.get(url, data={'tabela1__in': []}).json()
        return render(request, self.template_name, {'response': response})
