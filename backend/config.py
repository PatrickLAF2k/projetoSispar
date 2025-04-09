#Armazenar as configurações do ambiente de desenvolvimento
from os import environ

# Carregar as variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

load_dotenv()

class config:
    #Configurações do banco de dados
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False