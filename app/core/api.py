import json
from flask import Response, request
from flask.app import Headers, BaseResponse
from pydantic import ValidationError
from flask_babel import gettext

from app.core.exception import BadRequestException


class ViewFuncWrapper:
    def __init__(
        self,
        func,
        summary="",
        description="",
        auth=None,
        query=None,
        body=None,
        responses=None,
        tags=None,
    ):
        self.func = func
        self.__name__ = func.__name__
        self.summary = summary
        if len(description) <= 0:
            self.description = summary
        else:
            self.description = description
        self.auth = auth
        self.query = query
        self.body = body
        self.responses = responses
        self.tags = tags

    def __call__(self, **view_args):
        # 权限验证
        if self.auth:
            # 验证登陆
            # 验证接口使用权限
            pass
        # url参数验证
        if self.query:
            try:
                data_query = self.query(**request.args)
                setattr(request, "bind_query", data_query.dict())
            except ValidationError as e:
                raise BadRequestException(json.dumps(e.json()))
        # body参数验证
        if self.body:
            try:
                data_body = self.body(**request.json)
                setattr(request, "bind_body", data_body.dict())
            except ValidationError as e:
                raise BadRequestException(json.dumps(e.json()))
        # 调用方法
        rv = self.func(**view_args)
        rv = self._auto_serialization(rv)
        return rv

    def _auth(self):
        pass

    def _auto_serialization(self, rv):
        """
        兼容flask返回，
        如果类型是tuple，则可能是(data,code,header) or (data,header) or (data,code)，三种情况
        如果类型不是tuple，则是data
        """
        result = None
        code = 200
        msg = ""
        if isinstance(rv, tuple):
            result = rv[0]
            if len(rv) == 4:
                result = rv[0]
                code = rv[1]
                msg = rv[3]
                rv = (rv[0], rv[1], rv[2])
            # rv=(data,code,msg) or rv=(data,header,msg) or rv=(data,code,header)
            elif len(rv) == 3:
                result = rv[0]
                msg = rv[3]
                # rv=(data,code,msg) or rv=(data,code,header)
                if not isinstance(rv[1], (Headers, dict, tuple, list)):
                    code = rv[1]
                # rv=(data,code,msg) or rv=(data,header,msg)
                if isinstance(rv[2], str):
                    rv = (rv[0], rv[1])
                # rv=(data,code,header)
                else:
                    rv = (rv[0], rv[1], rv[2])
            # rv=(data,code) or rv=(data,header) or rv=(data,msg)
            elif len(rv) == 2:
                result = rv[0]
                # rv=(data,msg)
                if isinstance(rv[1], (str)):
                    rv = rv[0]
                # rv=(data,header)
                elif isinstance(rv[1], (Headers, dict, tuple, list)):
                    pass
                # rv=(data,code)
                else:
                    code = rv[1]
        else:
            result = rv
        # 判断result对象，是否是需要序列化
        if isinstance(result, (str, bytes, bytearray)):
            return rv
        elif isinstance(result, BaseResponse):
            return rv
        # 序列化返回值
        if self.responses:
            if code in self.responses and "schema" in self.responses[code]:
                try:
                    result = (
                        self.responses[code]["schema"].parse_obj(result).dict()
                        if result
                        else {}
                    )
                    result = return_obj(result, code, "", msg)
                except ValidationError as e:
                    raise BadRequestException(json.dumps(e.json()))
        return Response(
            response=json.dumps(result), status=code, mimetype="application/json"
        )


def return_obj(data, code, msg_type, msg):
    if code == 200 and len(msg_type) <= 0:
        msg_type = "success"
    if code == 200 and len(msg) <= 0:
        msg_type = gettext(u"opt success")
    return {"data": data, "code": code, "msg_type": msg_type, "msg": msg}
