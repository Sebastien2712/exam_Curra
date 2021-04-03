from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)

    with app.app_context():
       pass
    return app

app = create_app()

@app.route('/',methods=['GET'])
@cross_origin()
def home():
	return {"starting": "Hola, Mundo!", "name": "EXAM"}

@app.route('/login',methods=['GET'])
@cross_origin()
def login():
	from login import login
	return login()

@app.route('/colonia',methods=['GET'])
@cross_origin()
def colonia():
	from colonia import colonia
	return colonia()

@app.route('/get/colonia',methods=['GET'])
@cross_origin()
def getColonia():
	from getColonia import getColonia
	return getColonia()

@app.route('/get/estado',methods=['GET'])
@cross_origin()
def getEstado():
	from getEstado import getEstado
	return getEstado()

@app.route('/get/municipio',methods=['GET'])
@cross_origin()
def getMunicipio():
	from getMunicipio import getMunicipio
	return getMunicipio()

@app.route('/upload/colonia',methods=['POST'])
@cross_origin()
def uploadColonia():
	from seed import uploadColonia
	return uploadColonia()

@app.route('/upload/estado',methods=['POST'])
@cross_origin()
def uploadEstado():
	from seed import uploadEstado
	return uploadEstado()

@app.route('/upload/municipio',methods=['POST'])
@cross_origin()
def uploadMunicpio():
	from seed import uploadMunicpio
	return uploadMunicpio()

if __name__ == '__main__':
	app.run("0.0.0.0",port=5003,debug=True)