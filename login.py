from classes.Main import Main
from flask import request
from random import choice
import datetime
import string

Main = Main()

def login():

	response = {
		"result": 0,
		"error": "",
		"data": ""
	}
	requ = {
		"user": request.args.get("user"),
		"password": request.args.get("password")
	}
	if requ["user"] != None and requ["password"] != None:
		userInfo = Main.getSingleFromTable("user","idUser AS ID,username,password",
			" AND username = '" + str(requ["user"]) + "' AND active = 1",1)
		if userInfo != None:
			userLog = Main.getMultipleFromTable("user_session","*"," AND idUser= " + str(userInfo["ID"]) + " AND active = 1 ORDER BY insertDate ASC",1)
			if len(userLog) >= 3 :
				updateData = {
					"active":"0",
					"logoutDate": str(datetime.datetime.now())
				}				
				updateWhere = {
					"id_user_session":userLog[0]["id_user_session"]
				}
				update = Main.updateTable("user_session",updateData,updateWhere,1)
			if requ["password"] == userInfo["password"]:
				token = ''.join(choice(string.ascii_letters + string.digits) for i in range(64))
				userInsert ={
					"idUser" : str(userInfo["ID"]),
					"bearerToken": token
				}
				login = Main.insertTable("user_session",userInsert,1)
				if login != None:
					response["result"] = 1
					response["data"] = {
                        "username": userInfo["username"]
                    }
				else:
					response["error"] = "User Not Login"
			else:
				response["error"] = "Incorrect Password"
		else:
			response["error"] = "User Not Found"
	else:
		response["error"] = "Parameter"
	return response
