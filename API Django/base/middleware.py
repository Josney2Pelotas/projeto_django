from django.http import JsonResponse
import requests


class AuthMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'token' in request.headers:
            if request.headers['token'] != '1234':
                return JsonResponse({'erro': 'token incorreto'})
            else:
                request.session['middleware'] = 'teste middleware'
                return
        else:
            return JsonResponse({'erro': 'sem token no header'})

