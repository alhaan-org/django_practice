from django.http import HttpResponse
from django.shortcuts import redirect

def unauthorized_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper()

def if_is_admin(admin=None):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            
            return view_func(request, *args, **kwargs)
        return wrapper()
    return decorator()