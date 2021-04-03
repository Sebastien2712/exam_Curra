
from .db import db
from random import choice
from flask import request, render_template
import datetime
import urllib.parse
import json
import string
import pymysql


class Main(db):
    
	def __init__(self):
		super().__init__()

	def getUserSession(self,sessionId):
		user = self.getSingleFromTable("user_session","idUser AS ID"," AND active = 1 AND bearerToken = '" + str(sessionId) + "'",1)
		if user != None:
			return user
		else:
			return None
