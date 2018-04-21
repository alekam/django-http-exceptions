# coding: utf-8


class HttpException(Exception):
    status_code = 500


class HttpExceptionBadRequest(HttpException):
    status_code = 400


class HttpExceptionUnauthorized(HttpException):
    status_code = 401


class HttpExceptionForbidden(HttpException):
    status_code = 403


class HttpExceptionNotFound(HttpException):
    status_code = 404


class HttpExceptionNotAllowed(HttpException):
    status_code = 405


class HttpExceptionGone(HttpException):
    status_code = 410


class HttpExceptionServerError(HttpException):
    status_code = 500


# class HttpExceptionRedirect(HttpExceptionRedirectBase):
#     status_code = 302
#
#
# class HttpExceptionPermanentRedirect(HttpExceptionRedirectBase):
#     status_code = 301
#
#
# class HttpExceptionNotModified(HttpException):
#     status_code = 304
