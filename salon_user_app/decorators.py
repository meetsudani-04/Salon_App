from functools import wraps

from django.shortcuts import redirect


def session_login_required(function=None, session_key='customer_id'):
    def decorator(view_func):
        @wraps(view_func)
        def f(request, *args, **kwargs):
            if session_key in request.session:
                return view_func(request, *args, **kwargs)
            return redirect('user_login_view')
        return f
    if function is not None:
        return decorator(function)
    return decorator