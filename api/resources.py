from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

## Variaveis
db = SQLAlchemy()
marsh = Marshmallow()
##apispec = APISpecExt()

## Padroes de informacao
validate_pattern_cpf = r"^\d{11}$"
validate_pattern_crm = r"^\d{6}$"   
validate_pattern_crm_uf = r"^\d{6}/[a-zA-Z]{2}$"