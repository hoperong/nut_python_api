import json
from flask import Response


class APIException(Exception):
    def __init__(self, code, msg_type="", msg=""):
        self.code = code
        self.msg_type = msg_type
        self.msg = msg

    def get_response(self):
        return Response(
            response=json.dumps(
                {
                    "code": self.code,
                    "data": {},
                    "msg_type": self.msg_type,
                    "msg": self.msg,
                }
            ),
            status=self.code,
            mimetype="application/json",
        )


class BadRequestException(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 400, msg_type="error_bad_request", msg=msg)


class ConflictException(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 409, msg_type="error_already_exists", msg=msg)


class UnAuthenticatedException(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 401, msg_type="error_unauthenticated", msg=msg)


class ForbiddenException(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 403, msg_type="error_permission", msg=msg)


class NotFoundException(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 404, msg_type="error_not_found", msg=msg)


class InternalServerError(APIException):
    def __init__(self, msg=None):
        APIException.__init__(self, 500, msg_type="Internal Server Error", msg=msg)


class HttpApiException(APIException):
    """
    transform werkzeug.exceptions.HTTPException
    """

    def __init__(self, http_exception):
        APIException.__init__(
            self,
            http_exception.code,
            msg_type=http_exception.name,
            msg=getattr(http_exception, "description", http_exception.name),
        )