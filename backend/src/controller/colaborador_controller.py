from flask import Blueprint

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

@bp_colaborador.route('pegar-dados')
def pegar_dados():
    dados = [
        {'nome': 'Patrick', 'cargo': 'ceo', 'cracha': '123456'},
        {'nome': 'Lucas', 'cargo': 'dev', 'cracha': '654321'},
        {'nome': 'Gabriel', 'cargo': 'dev', 'cracha': '789012'},
        {'nome': 'Guilherme', 'cargo': 'dev', 'cracha': '345678'},
        {'nome': 'Felipe', 'cargo': 'dev', 'cracha': '901234'}
    ]
    return dados