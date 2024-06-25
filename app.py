from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    campo1 = request.form['campo1']
    campo2 = request.form['campo2']
    
    # Aquí podrías realizar acciones con los datos recibidos
    # Por ejemplo, guardarlos en una base de datos o enviarlos por correo electrónico

    return f'Datos recibidos: Campo 1: {campo1}, Campo 2: {campo2}'

if __name__ == '__main__':
    app.run(debug=True)
