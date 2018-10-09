# from django.conf import settings
# from django_hosts import patterns, host

# host_patterns = patterns('',
#     host(r'www', settings.ROOT_URLCONF, name='www'),
#     host(r'blog','kirr.hostconf.urls', name = 'blog'),
#     host(r'(?!www).*', 'kirr.hostconf.urls', name='wildcard'),
# )

from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'live', settings.ROOT_URLCONF, name='live'),
    host(r'(?!www).*', 'kirr.hostconf.urls', name='wildcard'),
)
