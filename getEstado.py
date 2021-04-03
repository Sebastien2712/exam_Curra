from classes.Main import Main
from flask import request
from werkzeug.utils import secure_filename
import datetime

Main = Main()

def getEstado():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    requ=request.get_json()
    if request.headers.get('Authorization'):
        if request.method == "GET":
            if request.args.get("nombre"):
                estado = Main.getSingleFromTable("estado","d_estado AS estado"," AND d_estado= '" + str(request.args.get("nombre")) + "'",1)
                if estado != []:
                    response["data"] = estado
                    response["result"] = 1
                else:
                    response["error"] = "No existe este estado"
            else:
                response["error"] = "Se busca por nombre completo"
        else:
            response["error"] = "Tiene que ser un GET"
    else:
        response["error"] = "No tienes Authorization"
    return response
    