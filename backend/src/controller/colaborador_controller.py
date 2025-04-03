from src.database.db import dados
from flask import Blueprint, request, jsonify

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

@bp_colaborador.route('/pegar-dados', methods=['GET'])
def pegar_dados():
    
    return dados;

@bp_colaborador.route('/cadastrar', methods=['POST'])
def cadastrar_novo_colaborador():
    dados_requisicao = request.get_json()
    
    # Verificado de campos obrigatorios
    if dados_requisicao['nome'] == '' or dados_requisicao['cargo'] == '' or dados_requisicao['cracha'] == '':
        return jsonify({'mensagem': 'Todos os campos são obrigatorios!'}), 400;
    
    # Loop para verificar se o crachá já existe
    for colaborador in dados:
        if colaborador['cracha'] == dados_requisicao['cracha']:
            return jsonify({'mensagem': 'Colaborador já cadastrado!'}), 400;
            break;

    
    novo_colaborador = {
        'id': len(dados) + 1,
        'nome': dados_requisicao['nome'],
        'cargo': dados_requisicao['cargo'],
        'cracha': dados_requisicao['cracha'],
    }
    dados.append(novo_colaborador)
    return jsonify({'mensagem': 'Colaborador cadastrado com sucesso!'}), 201;

# @bp_atualizar_colaborador.rout('/atualizar/<int>:id_colaborador',methods=['PUT'])
#     def atualizar_dados_colaborador(id_colaborador):
        

