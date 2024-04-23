from flask import Blueprint, jsonify, make_response, request
from models.rol import Rol
from models.persona import Persona
from models.censo_persona import Censo_persona
from models.censo import Censo
from models.censador import Censador
from models.motivo_censo import Motivo_censo
from models.motivo import Motivo




api = Blueprint('api', __name__)

@api.route('/')
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200}), 
        200
    )

#esto es sin post
@api.route('/suma/<a>/<b>')
def suma(a, b):
    c = float(a) + float(b)
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "data":{"suma es: ": c}}), 
        200
    )


#primer post
@api.route('/sumar', methods = ["POST"])
def suma_post():
    data = request.json
    #print(data["a"])
    c = float(data["a"]) + float(data["b"])
    #c = 0
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "data":{"suma es: ": c}}), 
        200
    )

