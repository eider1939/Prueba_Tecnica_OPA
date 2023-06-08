import os
from flask import Flask
from flask import render_template, request, redirect, session
from flask import send_from_directory
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template('Sitio/index.html')

@app.route('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join('/Templates/Sitio/css/'),archivocss)

if __name__=='__main__':
    app.run(debug=True)