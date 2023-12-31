from datetime import timedelta
from django.utils import timezone
from django.core.cache import cache
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        user_ip = request.META.get('REMOTE_ADDR', None)
        user_identifier = user_ip or request.session.session_key

        key = f'rate_limit:{user_identifier}'
        now = timezone.now()
        last_request_time = cache.get(key)

        try:
            if self.is_potentially_harmful_request():
                if self.handle_is_potentially_harmful_request():
                    # If user exceeds the allowed number of request per specified timeframe, collect information
                    if last_request_time is not None and (now - last_request_time).seconds < 60:
                        gadget_and_user_info = self.collect_gadget_and_user_info(request)
                        return JsonResponse({'error':'Too many requests'}, status=429)
                    cache.set(key, now, 60)
                    return None
                else:
                    return JsonResponse({'error':"Captcha Failed!"}, status=429)
            else:
                if last_request_time is not None and (now - last_request_time).seconds < 60:
                    gadget_and_user_info = self.collect_gadget_and_user_info(request)
                    return JsonResponse({'error':'Too many requests'}, status=429)
                cache.set(key, now, 60)
                return None
        except Exception as e:
            logger.exception("There was an error while running RateLimitMiddleWare: %s", e)

    
    def __call__(self, request):
        response = self.get_response(request)
        return response


    def is_potentially_harmful_request(self):
        # criteria to identify potential harmful request
        # return True
        pass
    
    def handle_is_potentially_harmful_request(self):
        # if is_potentially_harmful_request returns True
        # handle the request by maybe asking user to solve captcha
        # if captcha solved return True
        pass

    def collect_gadget_and_user_info(self):
        collected_gadget_and_user_info = {}
        # collect gadget-specific info
        # for example, extract user-agent, device details, etc
        # return collected_gadget_and_user_info
        user_agent = request.META.get('HTTP_USER_AGENT', None)

        if user_agent is not None:
            collected_gadget_and_user_info['user_agent'] = user_agent
        pass


# from django.contrib.postgres.fields import JsonField
# class DataForUnmatchedFilteredSearch(models.Model):
#     filter_conditions = JsonField()
#     result_count = models.IntegerField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ['filter_conditions']

# result, created = DataForUnmatchedFilteredSearch.objects.get_or_create(
#     filter_conditions = filter_conditions,
#     defaults = {'result_count':1}
# )

# if not created:
#     result.result_count += 1
#     result.save()



class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"

        return response


class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)


        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"

        return response
