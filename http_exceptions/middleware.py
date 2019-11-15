# coding: utf-8

import traceback

from django.conf import settings
from django.http.response import JsonResponse, Http404
from django.utils.deprecation import MiddlewareMixin


class ErrorHandlingMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        if not isinstance(exception, Exception):
            return

        if not request.is_ajax() or not request.GET.get('format') == 'json':
            return

        data = {
            'status': False,
            'exception': exception.__class__.__name__,
            'message': unicode(exception),
        }

#         try:
#             data['message'] = formatters.render_formatted_error(request, exception)
#         except Exception, e:
#             # TODO: log to sentry
#             data.update({
#                 'message': u'No message. Error During Error Processing'
#             })
#             return JsonResponse(data, status_code=500)

        if settings.DEBUG:
            data.update({
                'traceback': traceback.format_exc()
            })

        if hasattr(exception, 'status_code'):
            status_code = exception.status_code
        elif isinstance(exception, Http404):
            status_code = 404
        else:
            status_code = 500

        return JsonResponse(data, status=status_code)
