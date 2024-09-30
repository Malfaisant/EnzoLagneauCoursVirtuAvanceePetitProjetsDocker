from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Formulaire HTML
form_html = '''
    <form action="/submit" method="post">
        <label for="name">Nom:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Valider">
    </form>
'''

@app.route('/')
def index():
    return form_html

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    try:
        response = requests.post('http://app2:5001/process', json={'name': name})
        return f"Réponse d'app2: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Une erreur est survenue: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

