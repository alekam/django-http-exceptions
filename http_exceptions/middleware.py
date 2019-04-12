# coding: utf-8

import traceback

from django.conf import settings
from django.http.response import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ErrorHandlingMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        if not isinstance(exception, Exception):
            return

        data = {
            'status': False,
            'exception': exception.__class__.__name__,
        }

        if exception.message:
            data['message'] = exception.message

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
        else:
            status_code = 500

        return JsonResponse(data, status=status_code)
