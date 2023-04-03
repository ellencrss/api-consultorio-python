from flask_restful import Resource
from flask import request
from models import Doctor, Patient
from schemas import DoctorSchema, DoctorSchemaAlteracao
from resources import db, validate_pattern_crm, validate_pattern_crm_uf
import re

class CadastraMedico(Resource):
    def post(self):
        doctor_schema = DoctorSchema()  
        doctor_request = doctor_schema.load(request.json)
        doctor_entity = Doctor()
        doctor_entity.name = doctor_request["name"]
        doctor_entity.crm = doctor_request["crm"]
        doctor_entity.crm_uf = doctor_request["crm_uf"] 

        ## Validacoes
        if(not(bool(re.match(validate_pattern_crm, doctor_entity.crm)))):
            return { "message": "Campo CRM inválido" }, 405
        
        if(not(bool(re.match(validate_pattern_crm_uf, doctor_entity.crm_uf)))):
            return { "message": "Campo CRM-UF inválido. Verifique o formato inserido." }, 405
        
        if(Doctor.query.filter(Doctor.crm_uf == doctor_entity.crm_uf).first() != None):
            return { "message": "Campo CRM-UF inválido. CRM-UF já existe na base" }, 405

        db.session.add(doctor_entity)
        db.session.flush()
        db.session.commit()
        
        return { "message": "Incluído com êxito" }, 201

class GetMedicoPorId(Resource):
    def get(self, id):
        doctor_schema = DoctorSchema()
        doctor = Doctor.query.filter(Doctor.id == id).first()
        return {
            'Doctor': doctor_schema.dump(doctor)
        }
    
    def delete(self, id):
        doctor = Doctor.query.filter(Doctor.id == id).first()

        patients = Patient.query.filter(Patient.id_doctor == id).first()

        if(patients != None):
            return { "message": "Erro. Não é possível excluir médicos com pacientes associados"}, 405

        db.session.delete(doctor)
        db.session.commit()
        return { "message": "Excluído com êxito" }, 202 ## OK
    
    def put(self, id):
        doctor_schema = DoctorSchemaAlteracao()
        doctor_request = doctor_schema.load(request.json)
        doctor = Doctor.query.filter(Doctor.id == id).first()

        if(not(doctor != None)):
            return { "message": "Médico não encontrado na base" }, 404

        if "name" in doctor_request.keys():
            doctor.name = doctor_request["name"]

        if "crm" in doctor_request.keys():
            if(not(bool(re.match(validate_pattern_crm, doctor_request["crm"])))):
               return { "message": "Campo CRM inválido" }, 405 
            
            doctor.crm = doctor_request["crm"]
            
        if "crm_uf" in doctor_request.keys():
            if(not(bool(re.match(validate_pattern_crm_uf, doctor_request["crm_uf"] )))):
               return { "message": "Campo CRM-UF inválido. Verifique o formato inserido." }, 405 

            query_doctor = Doctor.query.filter(Doctor.crm_uf == doctor_request["crm_uf"]).first()
            if(query_doctor != None and query_doctor.id != id):
                return { "message": "Campo CRM-UF inválido. CRM-UF já existe na base" }, 405
                        
            doctor.crm_uf = doctor_request["crm_uf"]

        db.session.commit()

        return { "message": "Alterado com êxito" }, 200
    
class GetListaMedicos(Resource):
    def get(self):
        doctor_schema = DoctorSchema()  
        doctors = Doctor.query.all()
        return {
            "Doctors": [ doctor_schema.dump(doctor) for doctor in doctors ]
        }, 200