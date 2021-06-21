from flask import Flask, redirect, url_for, session,render_template,request
from werkzeug.utils import secure_filename
import os
from flask.json import jsonify
import textstat
import json

app = Flask(__name__)

app.secret_key = "dhutrr"

@app.route('/')
def hello_world():
    return render_template("test.html")

@app.route('/main',methods=['POST','GET'])
def main():
    info=[]
    if request.method=='POST':
        f = request.files['myfile']
        f.save(secure_filename(f.filename))
        session["filename"]=secure_filename(f.filename)
        test_data=open(session["filename"],"r").read()
        my_path=os.path.dirname(__file__)
        os.remove(os.path.join(my_path, session["filename"]))
    data1 = json.dumps([{"Input text":test_data},
                    {"flesch_reading_ease ":textstat.flesch_reading_ease(test_data)},
                    {"smog_index ":textstat.smog_index(test_data)},
                    {"flesch_kincaid_grade ":textstat.flesch_kincaid_grade(test_data)},
                    {"coleman_liau_index ":textstat.coleman_liau_index(test_data)},
                    {"automated_readability_index ":textstat.automated_readability_index(test_data)},
                    {"dale_chall_readability_score ":textstat.dale_chall_readability_score(test_data)},
                    {"difficult_words ":textstat.difficult_words(test_data)},
                    {"linsear_write_formula ":textstat.linsear_write_formula(test_data)},
                    {"gunning_fog ":textstat.gunning_fog(test_data)},
                    {"text_standard ":textstat.text_standard(test_data)},
                    {"fernandez_huerta ":textstat.fernandez_huerta(test_data)},
                    {"szigriszt_pazos ":textstat.szigriszt_pazos(test_data)},
                    {"gutierrez_polini ":textstat.gutierrez_polini(test_data)},
                    {"crawford ":textstat.crawford(test_data)}],intents=2)
    return data1
if __name__ == '__main__':
    app.run(debug=True)
