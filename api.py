from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.crud
collection = db.usuarios

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = []
    for usuario in collection.find():
        usuario['_id'] = str(usuario['_id'])
        usuarios.append(usuario)
    return jsonify({'usuarios': usuarios})

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({'message': 'Usuario criado com sucesso!'})

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    usuario = collection.find_one({'_id': ObjectId(id)})
    usuario['_id'] = str(usuario['_id'])
    return jsonify({'usuario': usuario})

@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Usuario atualizado com sucesso!'})

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Usuario deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)