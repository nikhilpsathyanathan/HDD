from flask import Flask, render_template, request , send_file
import os                    
import test_preprocess as tp  # for preprocessing 
import prediction   # for prediction 
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")   #load the index file 

@app.route("/csv", methods=["POST"])       #Receive CSV file from the user
def data():
    model = request.form['model']

    try:
        f = request.files["csvfile"]
    except:
        return render_template('error.html', error = "Please select any file")  # redirect to error page incase user did't select any file
    f.save(f.filename.replace(" ", "_"))
    file_name=f.filename.replace(" ", "_")
    tp.test_process(file_name)                       #preprocess the data 
    if model=='all':
        fail=prediction.predict_all()
    else:
        fail=prediction.predict_new(file_name,model)    

    return render_template('result_fail.html', fail_count = fail)


@app.route('/price')               # pricing page
def price():
    return render_template('price.html')
    


@app.route('/download')         # return the file to download
def download():
    return send_file('./static/result.csv',
                     mimetype='text/csv',
                     attachment_filename='result.csv',
                     as_attachment=True)
                   

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8888)
