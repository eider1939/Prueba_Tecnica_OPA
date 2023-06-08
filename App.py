import os
from flask import Flask
from flask import render_template, request, redirect, session
from flask import send_from_directory
from flask_bootstrap import Bootstrap
from Logic.logica import elementosCalcular

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template('Sitio/index.html')

@app.route('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join('/Templates/Sitio/css/'),archivocss)

@app.route('/index/Calcular', methods=['POST'])
def admin_libros_guardar():

    _Calorias=int(request.form['IntCalorias'])
    _Peso=int(request.form['IntPeso'])

    conjunto_respuesta=elementosCalcular(_Calorias,_Peso)
    
    #return redirect('/admin/libros')
    return render_template('/Sitio/Resultados.html',conjunto_respuesta=conjunto_respuesta)


if __name__=='__main__':
    app.run(debug=True)