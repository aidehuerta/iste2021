from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Book Motion Kids Administración')
admin.site.site_title = _('Book Motion Kids Portal de Administración')
admin.site.index_title = _('Bienvenido al portal de Book Motion Kids')

urlpatterns = [
    path('', include('common.urls')),
    path('account/', include('account.urls')),
    path('content/', include('content.urls')),
    path('grade/', include('grade.urls')),
    path('session/', include('session.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('therapist/', include('therapist.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
