from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# nuestra ruta de índice manejará la representación de nuestro formulari

# Sesion
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def index():
    if session.get('intentos') is None:
        session['intentos'] = 1
    else:
        session['intentos'] += 1
    
    return render_template("index.html")


@app.route('/sesion')
def redirecto():
    return redirect('/')

@app.route('/cierre_sesion')
def cierre_sesion():
    session.clear()
    return redirect('/')

@app.route('/mas_dos')
def mas_dos():
    session['intentos']+=1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

