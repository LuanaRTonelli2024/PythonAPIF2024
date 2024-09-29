from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient("mongodb+srv://luanartonelli:z6EhuH2MHm8TQAPC@cluster0.fexk2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['LS3FALL2024']
users_collection = db['Users']  # Mova esta linha para fora do bloco if

@app.route('/', methods=['GET'])
def home(): 
    return "HOME"

@app.route('/users', methods=['GET'])
def get_users():
    users = []  # Inicializa a lista de usuários
    try:
        for user in users_collection.find():
            user['_id'] = str(user['_id'])  # Converte ObjectId para string
            users.append(user)  # Adiciona o usuário à lista
    except Exception as e:
        print("Erro ao buscar usuários:", e)  # Imprime o erro no terminal
        return jsonify({"error": str(e)}), 500  # Retorna erro 500 se algo falhar
    return jsonify(users)  # Retorna a lista de usuários como JSON

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o aplicativo Flask




