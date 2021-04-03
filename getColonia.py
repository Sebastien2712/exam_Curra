from classes.Main import Main
from flask import request
from werkzeug.utils import secure_filename
import datetime

Main = Main()

def getColonia():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    requ=request.get_json()
    if request.headers.get('Authorization'):
        if request.method == "GET":
            if request.args.get("nombre"):
                colonia = Main.getSingleFromTable("colonia","d_asenta AS colonia"," AND d_asenta= '" + str(request.args.get("nombre")) + "'",1)
                if colonia != None:
                    response["data"] = colonia
                    response["result"] = 1
                else:
                    response["error"] = "No existe esta colonia"
            else:
                response["error"] = "Se busca por nombre completo"
        else:
            response["error"] = "Tiene que ser un GET"
    else:
        response["error"] = "No tienes Authorization"
    return response
    