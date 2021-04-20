class ViewFuncWrapper:
    def __init__(self, func, description="", auth=None, query=None, body=None, responses=None, tags=None):
        self.func = func
        self.description = description
        self.auth = auth
        self.query = query
        self.body = body
        self.responses = responses
        self.tags = tags
        self.__name__ = func.__name__
        if query:
            pass
        if body:
            pass

    def __call__(self, **view_args):
        # 权限验证
        if self.auth:
            # 验证登陆
            # 验证接口使用权限
            pass
        # url参数验证
        if self.query:
            pass
        # body参数验证
        if self.body:
            pass
        # 调用方法
        self.func(**view_args)
        # 序列化返回值
        if self.response:
            pass

    def auth(self):
        pass
