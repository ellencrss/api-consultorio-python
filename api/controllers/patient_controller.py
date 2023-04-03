from flask_restful import Resource
from flask import request
from models import Patient
from schemas import PatientSchema
from resources import db, validate_pattern_cpf
import re

class CadastraPaciente(Resource):
    def post(self):
        patient_schema = PatientSchema()  
        patient_request = patient_schema.load(request.json)
        patient_entity = Patient()
        patient_entity.name = patient_request["name"]
        patient_entity.birth_date = patient_request["birth_date"]  
        patient_entity.cpf = patient_request["cpf"]  
        patient_entity.id_doctor = patient_request["id_doctor"]  

        if(not(bool(re.match(validate_pattern_cpf, patient_entity.cpf)))):
           return { "message": "Campo CPF inválido" }, 405
        
        if(Patient.query.filter(Patient.cpf == patient_entity.cpf).first() != None):
            return { "message": "Campo CPF inválido. CPF já existe na base" }, 405
        
        db.session.add(patient_entity)
        db.session.flush()
        db.session.commit()
        
        return { "message": "Incluído com êxito" }, 201 ## Created

class GetPacientPorId(Resource):
    def get(self, id):
        patient_schema = PatientSchema()
        patient = Patient.query.filter(Patient.id == id).first()
        return {
            'Patient': patient_schema.dump(patient)
        }
    
    def delete(self, id):
        patient = Patient.query.filter(Patient.id == id).first()

        if(patient == None):
            return { "message": "Paciente inválido." }, 404
        
        db.session.delete(patient)
        db.session.commit()
        return { "message": "Excluído com êxito" }, 202 ## OK
    
class GetListaPacientes(Resource):
    def get(self):
        patient_schema = PatientSchema()  
        patients = Patient.query.all()
        return {
            "Pacientes": [ patient_schema.dump(patient) for patient in patients ]
        }, 200

class GetListaPacientesPorMedico(Resource):
    def get(self, id_doctor):
        if(id_doctor == None):
            return { "message": "Erro. Parâmetro obrigatório não informado: idMedico"}, 405
        
        patient_schema = PatientSchema()  
        patients = Patient.query.filter(Patient.id_doctor == id_doctor)
        return {
            "Pacientes": [ patient_schema.dump(patient) for patient in patients ]
        }, 200
