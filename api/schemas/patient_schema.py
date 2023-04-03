from models import Patient
from marshmallow import Schema, fields
from resources import db, marsh

class PatientSchema(Schema):
    name = fields.Str()
    birth_date = fields.Date()
    cpf = fields.Str()
    id_doctor = fields.Str()