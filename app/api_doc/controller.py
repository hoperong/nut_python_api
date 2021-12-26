import os

from flask import current_app
from openapi_schema_pydantic import OpenAPI
from openapi_schema_pydantic.util import (
    PydanticSchema,
    construct_open_api_with_schema_class,
)
from flask import render_template
from pydantic import BaseModel
from pydantic.schema import schema

from app.core.api import ViewFuncWrapper

"""
openapi 规范 https://github.com/OAI/OpenAPI-Specification/
"""


def get_open_api(app):
    api_obj = {"info": {"title": "xx开放平台接口文档", "version": "v0.0.1"}, "paths": {}}
    for url in app.url_map.iter_rules():
        print(url)
        func = app.view_functions[url.endpoint]
        if not isinstance(func, ViewFuncWrapper):
            continue
        item = {}
        for method in url.methods:
            print(method)
            method = method.lower()
            if method not in ["get", "post", "put", "delete", "patch"]:
                continue
            item[method] = {}
            item[method]["description"] = func.description
            item[method]["summary"] = func.summary
            if hasattr(func, "tags") and func.tags:
                item[method]["tags"] = func.tags
            # url上的参数
            item[method]["parameters"] = []
            for arg in url.arguments:
                arg_obj = {
                    "name": arg,
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                }
                item[method]["parameters"].append(arg_obj)
            # get参数
            if hasattr(func, "query") and func.query:
                sc = schema(models=[func.query])
                obj_sc = sc.get("definitions", {})
                obj_sc = obj_sc[list(obj_sc.keys())[0]] if len(sc.keys()) > 0 else {}
                prop_list = obj_sc.get("properties", [])
                required_list = obj_sc.get("required", [])
                for key, value in prop_list.items():
                    required = key in required_list
                    prop = {
                        "name": key,
                        "in": "query",
                        "required": required,
                        "description": value.get("description", ""),
                        "schema": value,
                    }
                    item[method]["parameters"].append(prop)
            if hasattr(func, "body") and func.body:
                item[method]["requestBody"] = {
                    "content": {
                        "application/json": {
                            "schema": PydanticSchema(schema_class=func.body)
                        }
                    }
                }
            item[method]["responses"] = {}
            if hasattr(func, "responses") and func.responses:
                for key, value in func.responses.items():
                    item[method]["responses"][key] = {
                        "description": value.get("description", ""),
                        "content": {
                            "application/json": {
                                "schema": PydanticSchema(
                                    schema_class=value.get("schema", BaseModel)
                                )
                            }
                        },
                    }
        if url.rule not in api_obj["paths"]:
            api_obj["paths"][url.rule] = {}
        api_obj["paths"][url.rule].update(item)
    return OpenAPI.parse_obj(api_obj)


def get_api_doc_view():
    open_api = get_open_api(current_app)
    open_api = construct_open_api_with_schema_class(open_api)
    return open_api.json(by_alias=True, exclude_none=True, indent=2), 200


def get_api_doc_html_view():
    return render_template(os.path.join("api_doc.html"))
