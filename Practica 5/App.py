from flask import Flask, render_template, request
#inicialisacion del servidor flask
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_BD']="bdflask"



#Declaramos una rutas

# Ruta Index https://localhost:5000/
@app.route('/') # Declaras una ruta ('nombre')
def index(): #def y dentro del def la logica 
    return render_template('index.html')



@app.route('/guardar', methods=['POST']) 
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo,artista,anio)
    

    return "La informacion del Album llego a su ruta :)"

@app.route('/eliminar') 
def eliminar(): 
    return "Se elimino el album de la BD"

# Ejecutan el servidor 
if __name__=='__main__':
    app.run(port= 5000, debug=True) #debug=true activaactualizacion 
