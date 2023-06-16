from flask import Flask
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
    return "Hola Mundo"



@app.route('/guardar') 
def guardar(): 
    return "Se guardo el album en la BD"

@app.route('/eliminar') 
def eliminar(): 
    return "Se elimino el album de la BD"

# Ejecutan el servidor 
if __name__=='__main__':
    app.run(port= 5000, debug=True) #debug=true activaactualizacion 
