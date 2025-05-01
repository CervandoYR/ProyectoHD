# myproject/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LogoutRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == reverse('empleados'):
            return redirect('login')
        response = self.get_response(request)
        return response
