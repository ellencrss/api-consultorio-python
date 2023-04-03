from sqlalchemy.dialects.postgresql import UUID
from resources import db
from uuid import uuid4

class Patient(db.Model):
    __tablename__ = 'tb_patient'
    __table_args__ = {'schema': 'teste_kogui'}
    
    id =  db.Column(UUID(as_uuid=True), primary_key = True, default=uuid4)
    name = db.Column(db.String(255))
    birth_date = db.Column(db.DateTime(8))
    cpf = db.Column(db.String(11))
    id_doctor = db.Column(UUID(as_uuid=True))
