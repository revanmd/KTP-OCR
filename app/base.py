from flask import Blueprint,request, jsonify, session, Response,render_template
base = Blueprint('',__name__)

@base.route('',methods=['GET'])
def index_html():
	return render_template('index.html')