from flask import Flask, request, render_template_string

app = Flask(__name__)

# Formulaire HTML
form_html = '''
    <h1>Bienvenue sur ma page web statique !</h1>
    <p>Ceci est le contenu de ma page web, oui je sais c'est un petit peu vide.</p>
'''

@app.route('/')
def index():
    return form_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

