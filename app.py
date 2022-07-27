from flask import Flask,request,jsonify;
from pdf2docx import Converter
from docx2pdf import convert
import werkzeug
import os

app=Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def print_hi():
    if(request.method=="POST"):
        file=request.files['sendfiles']
        filename=werkzeug.utils.secure_filename(file.filename)
        file.save("./temp"+filename)
        #d['Query']=str(request.args['Query'])
        split_tup = os.path.splitext("./temp"+filename)
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if file_extension=='.pdf':
            pdf_file = "./temp"+filename;
            docx_file = "./temp"+file_name+".doc";
            cv = Converter(pdf_file)
            cv.convert(docx_file, multiprocessing=True, cpu_count=4)
            cv.close()
        elif file_extension=='.docx':
            word_file="./temp"+filename;
            pdf_file="./temp"+file_name+".pdf";
            convert(word_file, pdf_file)
        else:
            return jsonify({
                "status": "Failure",
            })
    return jsonify({
        "status": "Success",
    })

if __name__ == '__main__':
    app.debug=True
    app.run()
