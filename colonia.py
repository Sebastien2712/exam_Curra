from classes.Main import Main
from flask import request
from werkzeug.utils import secure_filename
import datetime

Main = Main()

def colonia():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    requ=request.get_json()
    if request.headers.get('Authorization'):
        if request.method == "GET":
            if request.args.get("cp"):
                colonia = Main.getSingleFromTable("colonia","d_asenta AS colonia"," AND d_codigo= '" + str(request.args.get("cp")) + "'",1)
                if colonia != []:
                    response["data"] = colonia
                    response["result"] = 1
                else:
                    response["error"] = "No existe esta colonia"
            else:
                response["error"] = "Se busca por Codigo Postal"
        else:
            response["error"] = "Tiene que ser un GET"
    else:
        response["error"] = "No tienes Authorization"
    return response
    