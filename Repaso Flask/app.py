from flask import Flask, render_template, request, redirect,url_for,flash
# redirect,url_for se hace un redireccionamineto 
from flask_mysqldb import MySQL

#inicialisacion del servidor flask
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="rpf"

app.secret_key = 'mysecretkey'
mysql = MySQL (app)

@app.route('/')
def index():

    return render_template('index.html')

#consultar
@app.route('/consultar')
def consultar():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from fruta')
    #creamos la variable consulta para crear la lista que se va a desplegar en vista
    consulta=curSelect.fetchall() #fetchall para jalar la lista completa de registros
    #print(consulta)

    return render_template('consultar.html', fruta=consulta)

#actualizar 

@app.route('/actualizar')
def actualizar():

    return render_template('Actual.html')

#eliminar

@app.route('/eliminar')
def eliminar():

    return render_template('eliminar.html')

#guardar 

@app.route('/guardar',methods=['POST']) ##Una segunda ruta o más ya pueden tener otros nombres.
def guardar(): 
    if request.method == 'POST':
        Vfruta=request.form['txtFruta']
        Vtemp=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstoc=request.form['txtStock']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into fruta(nombre,temporada,precio,stock) values (%s,%s,%s,%s)',(Vfruta,Vtemp,Vprecio,Vstoc))
        mysql.connection.commit()
        
    flash('Articulo agregado correctamente')
    return redirect(url_for('index'))

#actualizar

@app.route('/actualizarr', methods=['POST'])
def actualizarr():
    if request.method == 'POST':
        Vfruta = request.form['txtFruta']
        Vtemp = request.form['txtTemporada']
        Vprecio = request.form['txtPrecio']
        Vstoc = request.form['txtStock']

        try:
            cursor = mysql.connection.cursor()

            # Consultar si la fruta existe antes de actualizar
            consulta_existe = 'SELECT COUNT(*) FROM fruta WHERE nombre = %s'
            cursor.execute(consulta_existe, (Vfruta,))
            existe_fruta = cursor.fetchone()[0]

            if existe_fruta:
                # Actualizar los datos de la fruta
                query = 'UPDATE fruta SET temporada=%s, precio=%s, stock=%s WHERE nombre=%s'
                values = (Vtemp, Vprecio, Vstoc, Vfruta)
                cursor.execute(query, values)
                mysql.connection.commit()
                flash('Datos actualizados correctamente')
            else:
                flash('La fruta no existe')

            cursor.close()

        except Exception as e:
            print("Error:", e)
            mysql.connection.rollback()

    return redirect(url_for('consultar'))


#elimminar 

@app.route('/eliminarr', methods=['GET', 'POST'])
def eliminarr():
    if request.method == 'POST':
        Vfruta = request.form['txtFruta']

        try:
            cursor = mysql.connection.cursor()

            # Consultar si la fruta existe antes de eliminar
            consulta_existe = 'SELECT COUNT(*) FROM fruta WHERE nombre = %s'
            cursor.execute(consulta_existe, (Vfruta,))
            existe_fruta = cursor.fetchone()[0]

            if existe_fruta:
                # Eliminar la fruta
                query = 'DELETE FROM fruta WHERE nombre = %s'
                cursor.execute(query, (Vfruta,))
                mysql.connection.commit()
                flash('Fruta eliminada correctamente')
            else:
                flash('La fruta no existe')

            cursor.close()

        except Exception as e:
            print("Error:", e)
            mysql.connection.rollback()

    return redirect(url_for('consultar'))




if __name__=='__main__':
    app.run(port= 5001, debug=True) #debug=true activaactualizacion 
