from django.conf import settings
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import ugettext_lazy as _


class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'lang' in request.GET:
            language = request.GET.get('lang', 'es')
            if language in dict(settings.LANGUAGES).keys():
                request.session['_language'] = language

        language = request.session.get('_language', 'es')
        translation.activate(language)
