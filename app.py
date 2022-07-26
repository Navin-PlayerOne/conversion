from flask import Flask,request,jsonify;
from pdf2docx import Converter
from docx2pdf import convert
import os

app=Flask(__name__)

@app.route('/api',methods=['GET'])
def print_hi():
    d={}
    d['Query']=str(request.args['Query'])
    split_tup = os.path.splitext(d['Query'])
    file_name = split_tup[0]
    file_extension = split_tup[1]
    if file_extension=='.pdf':
        d['Output'] = file_name + '.docx'
        pdf_file = d['Query'];
        docx_file = d['Output']
        cv = Converter(pdf_file)
        cv.convert(docx_file, multiprocessing=True, cpu_count=4)
        cv.close()
    elif file_extension=='.docx':
        d['Output']=file_name+'.pdf'
        convert(d['Query'], d['Output'])
    else:
        d['Output']="";
    return jsonify(d)

if __name__ == '__main__':
    app.debug = True
    app.run()
