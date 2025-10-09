from django.http import HttpResponse
from django.shortcuts import redirect

def unauthorized_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def if_is_admin(admin=False):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == "admin" and admin:        
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Go Away, You are not forbidden to view this page!")
        return wrapper
    return decorator

