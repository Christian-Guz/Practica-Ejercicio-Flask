from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo='Inicio')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html', titulo='Contactos')

@app.route('/catalogos')
def catalogos():
    return render_template('catalogos.html', titulo='Catálogos')


if __name__ == '__main__':
    app.run(debug=True, port = 5010)