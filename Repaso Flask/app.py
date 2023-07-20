from flask import Flask, render_template, request, redirect,url_for,flash
# redirect,url_for se hace un redireccionamineto 
from flask_mysqldb import MySQL

#inicialisacion del servidor flask
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="DB_Fruteria"

app.secret_key = 'mysecretkey'
mysql = MySQL (app)

@app.route('/')
def index(): 


    return render_template('index.html')


@app.route('/Guardar', methods=['POST'])
def Guardar():
    if request.method == 'POST':
        Vfruta = request.form['txtFruta']
        VTemp = request.form['txtTemporada']
        Vpre = request.form['txtPrecio']
        vst = request.form['txtStock']
        cs = mysql.connection.cursor()
        cs.execute('insert into tbFrutas(fruta, temporada, precio, stock) values (%s,%s,%s,%s)', (Vfruta,VTemp,Vpre,vst))
        mysql.connection.commit()
    flash('Guardado correctamente')
    return redirect(url_for('index'))

@app.route('/consultar')
def consultar():

    return render_template('consultar.html')




if __name__=='__main__':
    app.run(port= 5001, debug=True) #debug=true activaactualizacion 
