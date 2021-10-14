from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "CONSEGUI FINALIZAR O EXERCICIO, QUE ORGULHO !!"

if __name__ == '__main__':
    app.run(debug=True)