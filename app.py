from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Lab Pipeline DevOps 9ASO G41 - versão final!"

if __name__ == '__main__':
    app.run()