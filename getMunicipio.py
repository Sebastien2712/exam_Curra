from classes.Main import Main
from flask import request
from werkzeug.utils import secure_filename
import datetime

Main = Main()

def getMunicipio():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    requ=request.get_json()
    if request.headers.get('Authorization'):
        if request.method == "GET":
            if request.args.get("nombre"):
                municipio = Main.getSingleFromTable("municipio","d_municipio AS municipio"," AND d_municipio= '" + str(request.args.get("nombre")) + "'",1)
                if municipio != None:
                    response["data"] = municipio
                    response["result"] = 1
                else:
                    response["error"] = "No existe este municipio"
            else:
                response["error"] = "Se busca por nombre completo"
        else:
            response["error"] = "Tiene que ser un GET"
    else:
        response["error"] = "No tienes Authorization"
    return response
    