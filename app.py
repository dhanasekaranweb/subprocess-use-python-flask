__author__ = "DOTK"
import os
from flask import (Flask, request, render_template, redirect, session, json, Response)
import sys
import pickle
import subprocess

app = Flask(__name__)


@app.route("/test",methods=['GET'])
def test():
	try:

		#the subprocess will create unique job for every request
		pass_input = { "message": "Hey welcome note from subprocess"}
		#input keyword used to pass the input object/array to subprocess file 
		result = subprocess.run(['python3','subprocess.py'], input=pickle.dumps(pass_input), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stdout keyword used to capture the output
		#stderr keyword used to capture the error message
		if result.stderr:
			return json.dumps({"status":False,"message":str(result.stderr)})

		df = pickle.loads(result.stdout)

		return ({"status":True,"message":df})

	except Exception as e:
		return json.dumps({"status":False, "message":str(e)})


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)