from flask import Flask, render_template, request, redirect,url_for,flash
# redirect,url_for se hace un redireccionamineto 
from flask_mysqldb import MySQL

#inicialisacion del servidor flask
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"

app.secret_key = 'mysecretkey'
mysql = MySQL (app)




#Declaramos una rutas

# Ruta Index https://localhost:5000/
@app.route('/') # Declaras una ruta ('nombre')
def index(): #def y dentro del def la logica 
    #mostrar jalar datos de BD
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta = curSelect.fetchall()
    #print(consulta)

    return render_template('index.html', listAlbums=consulta) # ver en vista



@app.route('/guardar', methods=['POST']) 
def guardar():
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        #print(titulo,artista,anio)
        CS= mysql.connection.cursor() #variable cursosr y coeccion a la bd 
        CS.execute('insert into albums(titulo,artista,anio) values (%s,%s,%s)',(Vtitulo, Vartista, Vanio)) #Se pasan los parametros 
        mysql.connection.commit()
        
    flash('Album Agregado Correctamente') #manda un mensaje junto con la vista 
    return redirect(url_for('index'))

@app.route('/eliminar') 
def eliminar(): 
    return "Se elimino el album de la BD"


@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from albums where id = %s ', (id,))
    consulId= curEditar.fetchone()
    return render_template('EditarAlbum.html', album= consulId)


@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']

        curAct= mysql.connection.cursor()
        curAct.execute('update albums set titulo = %s, artista = %s, anio = %s where id = %s', (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()

    flash('Album Actualizado en la BD') #manda un mensaje junto con la vista 
    return redirect(url_for('index'))


@app.route('/borrar/<id>')
def borrar(id):
    curBorrar = mysql.connection.cursor()
    curBorrar.execute('select * from albums where id = %s ', (id,))
    consultId = curBorrar.fetchone()
    return render_template('Borrar.html', album= consultId)
    

@app.route('/Eliminar/<id>', methods=['POST'])
def Eliminar(id):
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']

        curEli= mysql.connection.cursor()
        curEli.execute('delete albums where id = %s', (id))
        mysql.connection.commit() 

    flash('Album Actualizado en la BD') #manda un mensaje junto con la vista 
    return redirect(url_for('index'))


# Ejecutan el servidor 
if __name__=='__main__':
    app.run(port= 5000, debug=True) #debug=true activaactualizacion 
