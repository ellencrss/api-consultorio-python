from sqlalchemy.dialects import postgresql
import sqlalchemy as db
import uuid

engine = db.create_engine('postgresql://postgres:root@localhost:5432/postgres', echo=True)
metadata_obj = db.MetaData(schema="teste_kogui")

### Doctor
tb_doctor = db.Table(
    'tb_doctor',
    metadata_obj,
    db.Column('id', postgresql.UUID, default=uuid.uuid4, primary_key=True),
    db.Column('name', db.String, nullable=False),
    db.Column('crm', db.String, nullable=False),
    db.Column('crm_uf', db.String, nullable=False, unique=True)
)

metadata_obj.create_all(engine)
