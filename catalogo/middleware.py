from django.shortcuts import redirect
from django.urls import reverse

# Classe reservada para debug de autenticação (script removível)
class DebugAuthMiddleware:
    """Middleware para debug de autenticação"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Logando informações de autenticação
        print(f"\n{'='*60}")
        print(f"URL: {request.path}")
        print(f"Usuario autenticado: {request.user.is_authenticated}")
        print(f"Usuario: {request.user}")
        print(f"Session Key: {request.session.session_key}")
        print(f"{'='*60}\n")
        
        response = self.get_response(request)
        return response
