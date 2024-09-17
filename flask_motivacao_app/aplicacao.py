from flask import Flask
import random

app = Flask(__name__)

# Lista de frases motivacionais
frases = [
    "Acredite em você mesmo!",
    "Nunca desista dos seus sonhos!",
    "Você é capaz de coisas incríveis!",
    "Persistência é o caminho para o sucesso.",
    "A vida é 10% o que acontece com você e 90% como você reage."
]

@app.route('/')
def home():
    frase_aleatoria = random.choice(frases)
    cores = ["blue", "green", "purple"]
    cor_aleatoria = random.choice(cores)
    return f"<h1 style='color:{cor_aleatoria};'>{frase_aleatoria}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
