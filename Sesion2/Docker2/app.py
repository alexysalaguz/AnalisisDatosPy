from flask import Flask

#crear una instancia de la clase flask y con el nombre name del modulo
app = Flask(__name__)

#ruta1
@app.route('/api/hello')
def hello():
    return 'Hola Mundo desde Docker'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)