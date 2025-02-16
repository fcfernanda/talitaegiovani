from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de presentes (simulando um banco de dados)
presentes = [
    {"id": 1, "nome": "Conjunto de facas de cozinha", "dado_por": None},
    {"id": 2, "nome": "Espátulas de silicone", "dado_por": None},
    {"id": 3, "nome": "Colheres de pau e silicone", "dado_por": None},
    {"id": 4, "nome": "Conjunto de medidores", "dado_por": None},
    {"id": 5, "nome": "Abridor de garrafas e latas", "dado_por": None},
    {"id": 6, "nome": "Ralador", "dado_por": None},
    {"id": 7, "nome": "Escorredor de macarrão", "dado_por": None},
    {"id": 8, "nome": "Pegador de massa e de salada", "dado_por": None},
    {"id": 9, "nome": "Pinça de cozinha", "dado_por": None},
    {"id": 10, "nome": "Tábua de cortar", "dado_por": None},
    {"id": 11, "nome": "Colher de servir e concha", "dado_por": None},
    {"id": 12, "nome": "Batedor de arame (fouet)", "dado_por": None},
    {"id": 13, "nome": "Liquidificador", "dado_por": None},
    {"id": 14, "nome": "Processador de alimentos", "dado_por": None},
    {"id": 15, "nome": "Grill ou sanduicheira", "dado_por": None},
    {"id": 16, "nome": "Espremedor de frutas", "dado_por": None},
    {"id": 17, "nome": "Conjunto de pratos", "dado_por": None},
    {"id": 18, "nome": "Copo", "dado_por": None},
    {"id": 19, "nome": "Talheres", "dado_por": None},
    {"id": 20, "nome": "Jogo de taças para sobremesa", "dado_por": None},
    {"id": 21, "nome": "Jogo de pratos", "dado_por": None},
    {"id": 22, "nome": "Porta-guardanapos", "dado_por": None},
    {"id": 23, "nome": "Jogo americano", "dado_por": None},
    {"id": 24, "nome": "Sousplats (base para pratos)", "dado_por": None},
    {"id": 25, "nome": "Travessas para servir", "dado_por": None},
    {"id": 26, "nome": "Potes herméticos", "dado_por": None},
    {"id": 27, "nome": "Frigideira", "dado_por": None},
    {"id": 28, "nome": "Jarras para bebidas", "dado_por": None},
    {"id": 29, "nome": "Toalhas de banho, rosto ou de piso", "dado_por": None},
    {"id": 30, "nome": "Jogos de lençóis", "dado_por": None},
    {"id": 31, "nome": "Kit de vassoura, pá e rodinho", "dado_por": None},
    {"id": 32, "nome": "Balde", "dado_por": None},
    {"id": 33, "nome": "Panos de limpeza", "dado_por": None},
    {"id": 34, "nome": "Escova para roupas", "dado_por": None},
    {"id": 35, "nome": "Lixeira", "dado_por": None},
    {"id": 36, "nome": "Cestos para roupas sujas", "dado_por": None},
    {"id": 37, "nome": "Cesta de frutas", "dado_por": None},
    {"id": 38, "nome": "Jogo de xícaras", "dado_por": None},
    {"id": 39, "nome": "Relógio de parede", "dado_por": None},
    {"id": 40, "nome": "Cortinas", "dado_por": None},
    {"id": 41, "nome": "Tapetes para cozinha e banheiro", "dado_por": None},
    {"id": 42, "nome": "Panos de prato", "dado_por": None},
    {"id": 43, "nome": "Jogo de formas", "dado_por": None},
    {"id": 44, "nome": "Assadeira para pizza", "dado_por": None},
    {"id": 45, "nome": "Porta-gelo", "dado_por": None},
    {"id": 46, "nome": "Garrafa térmica", "dado_por": None},
    {"id": 47, "nome": "Porta-copos", "dado_por": None},
    {"id": 48, "nome": "Kit churrasco", "dado_por": None},
    {"id": 49, "nome": "Tábua de frios e faca de queijo", "dado_por": None},
    {"id": 50, "nome": "Termômetro", "dado_por": None},
    {"id": 51, "nome": "Suporte papel toalha", "dado_por": None},
    {"id": 52, "nome": "Organizador para tampas de panelas", "dado_por": None},
]

@app.route('/')
def index():
    return render_template('index.html', presentes=presentes)

@app.route('/reservar/<int:presente_id>', methods=['POST'])
def reservar(presente_id):
    nome = request.form.get("nome")
    
    # Atualiza a lista de presentes marcando como reservado
    for presente in presentes:
        if presente["id"] == presente_id and presente["dado_por"] is None:
            presente["dado_por"] = nome
            break

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)
