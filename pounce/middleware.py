from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

RESOURCE_TYPES = frozenset(('img', 'script', 'link'))

class InvalidAssetException(Exception):
    pass

class PounceMiddleware(MiddlewareMixin):
    """Enables pushing resources using HTTP2 Link header"""

    def __init__(self, get_response):
        self.get_response = get_response
        self._link_header = None

        try:
            resources = settings.POUNCE_RESOURCES
        except AttributeError:
            raise MiddlewareNotUsed("No resources to preload specified")

        try:
            self._validate_resources(resources)
        except InvalidAssetException as e:
            if settings.DEBUG:
                raise e
            return

        self._link_header = self._generate_link_header(resources)

    def __call__(self, request):
        response = self.get_response(request)
        if self._link_header:
            response['Link'] = self._link_header
        return response

    def _validate_resources(self, resources):
        for resource in resources:
            if len(resource) != 2:
                raise InvalidAssetException("Resource must contain URL and type")

            if type(resource[0]) != str:
                raise InvalidAssetException("%s is not a string" % resource[0])

            if resource[1] not in RESOURCE_TYPES:
                raise InvalidAssetException("%s is not registered as a resource type" % resource[1])

    def _generate_link_header(self, resources):
        header = ''

        for i, resource in enumerate(resources):
            if i > 0:
                header += ','
            header += '<%s>; rel=preload; as=%s; nopush' % resource

        return header

