from flask import Blueprint, current_app, jsonify
from marshmallow import ValidationError
from flask_restful import Api
from controllers import CadastraMedico, GetMedicoPorId, GetListaMedicos, CadastraPaciente, GetPacientPorId, GetListaPacientes, GetListaPacientesPorMedico

blueprint = Blueprint("api-teste-kogui", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(CadastraMedico, "/doctor/new", endpoint="includeNewDoctor")
api.add_resource(GetMedicoPorId, "/doctor/<uuid:id>", endpoint="getDoctorById")
api.add_resource(GetListaMedicos, "/doctors", endpoint="getDoctorsList")

api.add_resource(CadastraPaciente, "/patient/new", endpoint="includeNewPatient")
api.add_resource(GetPacientPorId, "/patient/<uuid:id>", endpoint="getPatientById")
api.add_resource(GetListaPacientes, "/patients", endpoint="getPatientsList")
api.add_resource(GetListaPacientesPorMedico, "/patients/<uuid:id_doctor>", endpoint="getPatientsListByDoctor")
