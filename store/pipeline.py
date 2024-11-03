# wedding/pipeline.py
from django.contrib.auth import get_user_model
from social_core.exceptions import AuthForbidden

User = get_user_model()

def validate_user(backend, strategy, details, response, *args, **kwargs):
    if backend.name == 'google':
        email = details.get('email')
        if email:
            if not User.objects.filter(email=email).exists():
                raise AuthForbidden('social_core.backends.google.GoogleOpenIdConnect')
