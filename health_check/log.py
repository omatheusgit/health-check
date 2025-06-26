from datetime import datetime

def log(msg):
    '''Função criada para gerar entradas de log das verificações'''
    
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} {msg}\n")