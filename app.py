from flask import Flask 

app = Flask("Meu APP")

posts = [
    {
    "titulo": "minha primeira postagem",
    'texto': "teste"

    },
    {
    "titulo": "minha segundo postagem",
    'texto': "outro teste" 
    }



]

@app.route('/')
def exibir_entradas():
    entradas = posts #mock das postagens
    return str(entradas)


