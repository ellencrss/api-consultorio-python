from sqlalchemy.dialects import postgresql
import sqlalchemy as db
import uuid

engine = db.create_engine('postgresql://postgres:root@localhost:5432/postgres', echo=True)
metadata_obj = db.MetaData(schema="teste_kogui")

### Patient
tb_patient = db.Table(
    'tb_patient',
    metadata_obj,
    db.Column('id', postgresql.UUID, default=uuid.uuid4, primary_key=True),
    db.Column('name', db.String, nullable=False),
    db.Column('birth_date', db.Date, nullable=False),
    db.Column('cpf', db.String, nullable=False, unique=True),
    db.Column('id_doctor', postgresql.UUID, nullable=False)
)

metadata_obj.create_all(engine)

