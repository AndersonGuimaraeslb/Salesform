from flask import Flask, Blueprint, request, jsonify, render_template
import requests

app = Flask(__name__)

# Criação do Blueprint
pedidos_route = Blueprint("Pedidos", __name__)

# Função para converter o campo "Quantidade" em número inteiro
def converter_quantidade_para_inteiro(data):
    try:
        data['Quantidade'] = int(data['Quantidade'])
        return data
    except ValueError:
        return None

# Rota para exibir o formulário HTML
@pedidos_route.route('/')
def mostrar_formulario():
    return render_template('index.html')

# Rota para enviar os dados do formulário para o Protheus via JSON
@pedidos_route.route('/', methods=['POST'])
def enviar_formulario():
    # Recebe os dados do formulário
    data = request.json
    
    # Exibe os dados recebidos no terminal
    print("Dados do formulário recebidos:")
    print(data)
    
    # Converte a quantidade para inteiro
    data = converter_quantidade_para_inteiro(data)
    if data is None:
        return jsonify({"status": "error", "message": "A quantidade deve ser um número inteiro."})
    
 
   
    # Envia os dados para o Protheus via JSON
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept-Charset': 'UTF-8'
        }
        response = requests.post('http://localhost:8091/rest/apipv/new', json=data, headers=headers)
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Dados enviados com sucesso para o Protheus!"})
        else:
            return jsonify({"status": "error", "message": "Erro ao enviar os dados para o Protheus. Código de status: " + str(response.status_code)})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Erro ao enviar os dados: {str(e)}"})



if __name__ == "__main__":
    app.run(debug=True)
