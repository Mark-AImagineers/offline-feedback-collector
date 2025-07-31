from django.utils import timezone

class SubscriptionMiddleware:
    """
    Downgrade user to Free if their subscription_expires is past.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        if user and user.is_authenticated:
            expires = getattr(user, "subscription_expires", None)
            if expires and timezone.now() > expires:
                user.subscription_level = user.SUBSCRIPTION_FREE
                user.subscription_expires = None
                user.save()

        return self.get_response(request)