from models import Doctor
from marshmallow import Schema, fields
from resources import db, marsh

class DoctorSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    crm = fields.Str(required=True, allow_none=False)
    crm_uf = fields.Str(required=True, allow_none=False)

class DoctorSchemaAlteracao(Schema):
    name = fields.Str(required=False, allow_none=True)
    crm = fields.Str(required=False, allow_none=True)
    crm_uf = fields.Str(required=False, allow_none=True)