import os
from dotenv import load_dotenv

from health_check.utils import check_health

def main():
    '''
    Função foi criada para ler as URLs no arquivo .env e validar se existe valor, e posteriormente armazenar em uma lista.
    '''
    load_dotenv()
    urls_env = os.getenv("URLS")

    if not urls_env:
        print("Nenhuma URL foi encontrada no arquivo .env")
    
    urls = urls_env.split(",")

    for i in urls:
        check_health(i)


# Chamada do arquivo como principal para execução
if __name__ == "__main__":
    main()
