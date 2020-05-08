from flask import Flask, redirect, url_for, request, render_template
import os
import corescript
from datetime import datetime
import testpy

app = Flask(__name__)

inputt = os.path.join('static', 'input')
app.config['inputt'] = inputt

output = os.path.join('static', 'output')
app.config['output'] = output

@app.route('/')
def index():
    return render_template('index.html', clicked = False)

@app.route('/click', methods =['POST', 'GET'])
def click():
    if request.method == 'POST':

        n = request.form['n']
        if (n == 0) or (n == '') or (n.isnumeric() == False):
            return redirect(url_for('invalidn'))

        file = request.files['nm']
        if file.filename == '':
            return redirect(url_for('nofile'))


        YesNo = request.form['YesNo']
        if(YesNo == ''):
            return redirect(url_for('invalidyesno'))

        if(YesNo == 'Yes'):
            choice = 1
        else:
            choice = 0


        photoid = datetime.now().strftime('%Y%m-%d%H-%M%S')
        square = testpy.tes(5)
        inputfilename = "saved" + photoid + ".jpg"
        filepath = os.path.join(app.config['inputt'],inputfilename)
        file.save(filepath)
        outputfilename = corescript.converter(filepath,int(n), choice,photoid)
        filepath = os.path.join(app.config['output'], outputfilename)
        return render_template("index.html", num = square, idshow =filepath, test = True)


        
        
        #print(filepath)
        
        #print(photoid)
        
        

        

        return render_template("index.html", clicked = True, filelink = filepath)
        
@app.route('/nofile')
def nofile():
    return render_template('index.html', file=False)

@app.route('/invalidn')
def invalidn():
    return render_template('index.html', inputn=False)

    

@app.errorhandler(400)
def incomplete(e):
    return render_template('index.html', inputyesno=False)


