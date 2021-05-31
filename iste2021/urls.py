from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('common.urls')),
    path('account/', include('account.urls')),
    path('content/', include('content.urls')),
    # path('course/', include('course.urls')),
    # path('patient/', include('patient.urls')),
    # path('session/', include('session.urls')),
    # path('teacher/', include('teacher.urls')),
    # path('therapist/', include('therapist.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
