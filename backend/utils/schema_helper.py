from marshmallow import Schema
from typing import Any
from marshmallow.exceptions import ValidationError
from flask import abort

def serialize(data: Any, schema: Schema) -> str:
    try:
        s = schema.dumps(obj=data)
    except ValidationError as e:
        abort(500, {'message': str(e)})
    return s

def deserialize(data: Any, schema: Schema, cls: Any) -> Any:
    try:
        d = schema.load(data=data)
    except ValidationError as e:
        abort(400, {'message': str(e)})
    return cls(**d)