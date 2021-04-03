from classes.Main import Main
from flask import request
from werkzeug.utils import secure_filename
import datetime
import os
import csv

 # web service for upload lleads with csv 
ALLOWED_EXTENSIONS = set(['csv'])
Main = Main()

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploadColonia():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    if request.method == "POST":
        PATH_FILE = 'csvs/'
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                if file and allowed_file(file.filename):
                    if not os.path.exists(PATH_FILE):
                        os.makedirs(PATH_FILE)
                    extension = "."+file.filename.rsplit('.', 1)[1].lower()
                    filename = extension
                    r_save = file.save(os.path.join(PATH_FILE, filename))
                    with  open(PATH_FILE+filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        lista = []
                        aux1 = []
                        cont = 0
                        for row in reader:
                            lista.append(row)
                        for row in lista:
                            if row.keys() >= {"d_codigo","d_asenta","d_tipo_asenta","D_mnpio","d_estado","d_ciudad","d_CP","c_estado","c_oficina","c_CP","c_tipo_asenta","c_mnpio","id_asenta_cpcons","d_zona","c_cve_ciudad"}:
                                insertData = {
                                    "d_codigo": row["d_codigo"],
                                    "d_asenta": row["d_asenta"],
                                    "d_tipo_asenta": row["d_tipo_asenta"],
                                    "D_mnpio":  row["D_mnpio"],
                                    "d_estado": row["d_estado"],
                                    "d_ciudad": row["d_ciudad"],
                                    "d_CP": row["d_CP"],
                                    "c_estado": row["c_estado"],
                                    "c_oficina": row["c_oficina"],
                                    "c_CP": row["c_CP"],
                                    "c_tipo_asenta": row["c_tipo_asenta"],
                                    "c_mnpio": row["c_mnpio"],
                                    "id_asenta_cpcons": row["id_asenta_cpcons"],
                                    "d_zona": row["d_zona"],
                                    "c_cve_ciudad": row["c_cve_ciudad"]
                                }
                                insert = Main.insertTable("colonia",insertData,1)
                                if insert != None:
                                    response["data"] = insert
                                else:
                                    response["error"] = "Hay campos vacios"
                            else:
                                response["error"] = "Error Not Parameters Found"
                else:
                    response["error"] = "Error filename" 
            else:
                response["error"] = "Error filename vacio"
        else:
            response["error"] = "Error file"
    else:
        reponse["error"] = "Es un POST"
    return response

def uploadEstado():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    if request.method == "POST":
        PATH_FILE = 'csvs/'
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                if file and allowed_file(file.filename):
                    if not os.path.exists(PATH_FILE):
                        os.makedirs(PATH_FILE)
                    extension = "."+file.filename.rsplit('.', 1)[1].lower()
                    filename = extension
                    r_save = file.save(os.path.join(PATH_FILE, filename))
                    with  open(PATH_FILE+filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        lista = []
                        aux1 = []
                        cont = 0
                        for row in reader:
                            lista.append(row)
                        for row in lista:
                            if row.keys() >= {"c_estado","d_estado"}:
                                insertData = {
                                    "c_estado": row["c_estado"],
                                    "d_estado": row["d_estado"]
                                }
                                insert = Main.insertTable("estado",insertData,1)
                                if insert != None:
                                    response["data"] = insert
                                else:
                                    response["error"] = "Hay campos vacios"
                            else:
                                response["error"] = "Error Not Parameters Found"
                else:
                    response["error"] = "Error filename" 
            else:
                response["error"] = "Error filename vacio"
        else:
            response["error"] = "Error file"
    else:
        reponse["error"] = "Es un POST"
    return response

def uploadMunicpio():
    response = {
        "result":0,
        "error":"",
        "data":""
    }
    if request.method == "POST":
        PATH_FILE = 'csvs/'
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                if file and allowed_file(file.filename):
                    if not os.path.exists(PATH_FILE):
                        os.makedirs(PATH_FILE)
                    extension = "."+file.filename.rsplit('.', 1)[1].lower()
                    filename = extension
                    r_save = file.save(os.path.join(PATH_FILE, filename))
                    with  open(PATH_FILE+filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        lista = []
                        aux1 = []
                        cont = 0
                        for row in reader:
                            lista.append(row)
                        for row in lista:
                            if row.keys() >= {"c_estado","d_municipio","c_mnpio"}:
                                insertData = {
                                    "c_estado": row["c_estado"],
                                    "d_municipio": row["d_municipio"],
                                    "c_mnpio": row["c_mnpio"]
                                }
                                insert = Main.insertTable("municipio",insertData,1)
                                if insert != None:
                                    response["data"] = insert
                                else:
                                    response["error"] = "Hay campos vacios"
                            else:
                                response["error"] = "Error Not Parameters Found"
                else:
                    response["error"] = "Error filename" 
            else:
                response["error"] = "Error filename vacio"
        else:
            response["error"] = "Error file"
    else:
        reponse["error"] = "Es un POST"
    return response

def remove_char(s):
    return s[ 1:len(s) - 1]

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['csv']