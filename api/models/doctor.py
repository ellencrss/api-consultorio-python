from sqlalchemy.dialects.postgresql import UUID
from resources import db
from uuid import uuid4

class Doctor(db.Model):
    __tablename__ = 'tb_doctor'
    __table_args__ = {'schema': 'teste_kogui'}
    
    id =  db.Column(UUID(as_uuid=True), primary_key = True, default=uuid4)
    name = db.Column(db.String(255))
    crm = db.Column(db.String(6))
    crm_uf = db.Column(db.String(9))