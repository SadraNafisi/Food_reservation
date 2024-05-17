from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
def unauthenticated_user(get_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return get_func(request, *args, **kwargs)

    return wrapper_func

def allowed_user(allowed_groups=[]):
    def decorator(get_func):
        def wrapper_func(request,*args,**kwargs):
            group=None

            if(request.user.groups.exists()):
                group=request.user.groups.all()[0].name
            if group in allowed_groups:
                return get_func(request,*args,**kwargs)
            else:
                messages.warning(request,'you are not authorized to access that view.')
                return redirect('index')
        return wrapper_func
    return decorator

# def UserAdmin_Only(get_func):
#     def wrapper_func(request,*args,**kwargs):
#         if()

