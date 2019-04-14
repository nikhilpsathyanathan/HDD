from flask import Flask, render_template, request , send_file
import os
import test_preprocess as tp
import prediction
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/csv", methods=["POST"])
def data():
    model = request.form['model']
    f = request.files["csvfile"]
    f.save(f.filename.replace(" ", "_"))
    file_name=f.filename.replace(" ", "_")
    tp.test_process(file_name)
    if model=='all':
        fail=prediction.predict_all()
    else:
        fail=prediction.predict_new(file_name,model)    

    return render_template('result_fail.html', fail_count = fail)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    model = request.form['model']
    fail=prediction.predict(model)
    return render_template('result.html', score = fail)

@app.route('/price')
def price():
    return render_template('price.html')
    

@app.route('/date')
def date():
    return 'ggcoming soon'
    

@app.route('/download')
def download():
    return send_file('./static/result.csv',
                     mimetype='text/csv',
                     attachment_filename='result.csv',
                     as_attachment=True)

if __name__ == '__main__':
   app.run(debug = True)
