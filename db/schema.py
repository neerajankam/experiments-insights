import json
from marshmallow import Schema, fields, post_load


class JSONField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        return json.loads(value)


class InsightsSchema(Schema):
    user_name = fields.Str()
    user_insights = JSONField()
