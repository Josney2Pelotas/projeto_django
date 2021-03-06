import requests
import re
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import redirect


class GetView(TemplateView):
    template_name = 'base/tabela.html'

    def get(self, request):
        filtro = request.GET.dict()
        lista_ids = []
        if 'select_input' in filtro:
            lista_ids = list(map(int, filtro['select_input'].split(',')))
            # lista_ids = re.findall(r'"([^"]*)"', filtro['ids'])
        url = 'http://127.0.0.1:4000/api-teste/get_infos/'
        response = requests.get(url, data={'tabela1__in': lista_ids}).json()
        return render(request, self.template_name, {'response': response, 'selecionados': lista_ids})


class InsertView(TemplateView):
    template_name = 'base/insert.html'

    def get(self, request):
        url = 'http://127.0.0.1:4000/api-teste/insert_infos/'
        response = requests.get(url).json()
        return render(request, self.template_name, {'response': response})

    def post(self, request):
        valores = request.POST.dict()
        del valores['csrfmiddlewaretoken']
        url = 'http://127.0.0.1:4000/api-teste/insert_infos/'
        requests.post(url, data=valores).json()
        return redirect('tela de inserção')


class UpdateView(TemplateView):
    template_name = 'base/update.html'

    def get(self, request):
        url = 'http://127.0.0.1:4000/api-teste/update_infos/'
        response = requests.get(url).json()
        return render(request, self.template_name, {'response': response})

    def post(self, request):
        valores = request.POST.dict()
        del valores['csrfmiddlewaretoken']
        url = 'http://127.0.0.1:4000/api-teste/update_infos/'
        requests.put(url, data=valores).json()
        return redirect('tela de update')


class DeleteView(TemplateView):
    template_name = 'base/delete.html'

    def get(self, request):
        url = 'http://127.0.0.1:4000/api-teste/delete_infos/'
        response = requests.get(url).json()
        return render(request, self.template_name, {'response': response})

    def post(self, request):
        valores = request.POST.dict()
        del valores['csrfmiddlewaretoken']
        url = 'http://127.0.0.1:4000/api-teste/delete_infos/'
        requests.delete(url, data=valores).json()
        return redirect('tela de delecao')
