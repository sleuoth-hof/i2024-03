from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/get_price/'):
            ip = request.META['REMOTE_ADDR']
            key = f'rate-limit-{ip}'
            count = cache.get(key, 0)
            if count >= 60:
                return JsonResponse({'error': 'Rate limit exceeded. Try again later.'}, status=429)
            cache.set(key, count + 1, timeout=60)