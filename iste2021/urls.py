from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

from session.views import SetButton, GetButton

admin.site.site_header = _('Administración de Bookmotion Kids')
admin.site.site_title = _('Portal de Administración de Bookmotion Kids')
admin.site.index_title = _('Bienvenido al portal de Bookmotion Kids')

urlpatterns = [
    path('', include('common.urls')),
    path('account/', include('account.urls')),
    path('content/', include('content.urls')),
    path('diagnosis/', include('diagnosis.urls')),
    path('group/', include('group.urls')),
    path('session/', include('session.urls')),
    path('student/', include('student.urls')),

    path('admin/', admin.site.urls),

    path('api/set_button/', SetButton.as_view(),
         name='api_set_button'),
    path('api/get_button/<int:session_id>/', GetButton.as_view(),
         name='api_get_button'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
