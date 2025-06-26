# Biblioteca para realizar requisições HTTP. Simples e intuitiva
import requests # type: ignore
from .log import log 

def check_health(url):
    '''
    Função principal que executa a requisição http para validar a integridade das URLs
    '''
    # Tratar comportamentos
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            msg = f"[✔] A comunicação com {url} está online e integra"
        else:
            msg = "[✖]A comunicação com {url} falhou. Código do erro: {response.status_code}."
    except requests.exceptions.RequestException as error:
        msg = f"[✖] Erro ao tentar acessar a url {url}: {error}"

    print (msg)
    log(msg)

