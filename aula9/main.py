from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados em memória
usuarios = []

@app.route("/usuarios", methods=["POST"])
def cadastrar():
    # Obtém os dados JSON enviados na requisição
    dados = request.json
    
    # Validação simples: verifica se o nome foi enviado
    if not dados or "nome" not in dados:
        return jsonify({"erro": "Nome é obrigatório"}), 400

    # Cria o dicionário do usuário
    usuario = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        # .get() evita erro se 'email' não for enviado
        "email": dados.get("email", "Sem email") 
    }
    
    # Adiciona à lista
    usuarios.append(usuario)
    
    # Retorna o usuário criado com status 201 (Created)
    return jsonify(usuario), 201

if __name__ == "__main__":
    # Correção aqui: era "__name__" no seu exemplo, o correto é "__main__"
    app.run(debug=True)
