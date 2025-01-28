from rest_framework.exceptions import APIException
from .error_message import get_error_message


class CustomAPIException(APIException):
    def __init__(self, enum_code, message: str = None, ok=False):
        result = get_error_message(enum_code.value)
        error_message = message if message else result.get('result')
        self.status_code = result.get('http_status')
        self.time = None
        self.detail = {
            'detail': error_message,
            'ok': ok,
            'result': '',
            'error_code': enum_code.value,
        }
