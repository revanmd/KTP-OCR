from flask import Blueprint,request, jsonify, session, Response,render_template
from flask import current_app as app
from werkzeug.utils import secure_filename
from .model.ocr import OCR
from .model.pretext import Pretext
from .model.result import Result
from .model.person import Person
from .model.correction import Correction
import os
import uuid

api = Blueprint('v1',__name__)
Correction = Correction()

@api.route('',methods=['GET'])
def index_html():
	return render_template('index.html')
	
@api.route('convert',methods=['GET'])
def convert_handler():
	#get_image
    try:
        path = "app/ktp_gege.jpeg"
        ocr_result = OCR.image_to_string(path)
        person = Result.prepare_result(ocr_result)
        person.nama = Pretext.get_nama(person.nama)
        person.nik = Pretext.get_nik(person.nik)
        person.tgl_lahir = Pretext.get_tgl_lahir(person.tgl_lahir)
        person.tempat = Pretext.get_tempat(person.tempat)
        person.kec = Pretext.get_kec(person.kec)
        person.kel = Pretext.get_kel(person.kel) 
        #Correction
        person.tempat = Correction.correct('tempat',person.tempat)
        person.kec = Correction.correct('kec',person.kec)
        return jsonify(person.to_dict())
    except:
        return jsonify({'status': "404"})

@api.route('upload',methods=['GET'])
def upload_handler():
	return render_template('upload.html')

@api.route('process',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "tidak ada file"

        file = request.files['file']

        if file.filename == '':
            return 'tidak ada file'

        if file:
            try:
                extension = file.filename.split('.')[1]
                filename = uuid.uuid1()
                file.save(os.path.join('app/static/upload', str(filename)+'.'+extension))
                path = os.path.join('app/static/upload', str(filename)+'.'+extension)
                ocr_result = OCR.image_to_string(path)
                person = Result.prepare_result(ocr_result)
                person.nama = Pretext.get_nama(person.nama)
                person.nik = Pretext.get_nik(person.nik)
                person.tgl_lahir = Pretext.get_tgl_lahir(person.tgl_lahir)
                person.tempat = Correction.correct('tempat',Pretext.get_tempat(person.tempat))
                person.kec = Correction.correct('kec',Pretext.get_kec(person.kec))
                person.kel = Pretext.get_kel(person.kel)
                return jsonify({'data':person.to_dict(),'raw':ocr_result})
            except:
                return jsonify({'status': "404"})
    return 'gagal upload'
	