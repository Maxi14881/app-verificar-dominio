from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def verificar_dominio(dominio):
    url = f"https://go-qa.finneg.com/api/1/domains/{dominio}/info"
    response = requests.get(url)
    if response.status_code == 200:
        return "El Dominio está en F4"
    else:
        return "El Dominio está en F3"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        dominio = request.form['dominio'].upper()
        resultado = verificar_dominio(dominio)
        return render_template('result.html', resultado=resultado)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
