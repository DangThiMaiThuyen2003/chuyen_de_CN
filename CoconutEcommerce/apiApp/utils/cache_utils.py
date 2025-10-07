from django.core.cache import cache
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

def cache_response(timeout=settings.CACHE_TTL):
    """
    Decorator for caching API views
    """
    def decorator(view_func):
        @method_decorator(cache_page(timeout))
        @method_decorator(vary_on_cookie)
        def _wrapped_view(view_instance, *args, **kwargs):
            return view_func(view_instance, *args, **kwargs)
        return _wrapped_view
    return decorator
