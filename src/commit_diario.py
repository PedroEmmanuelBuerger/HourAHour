import os
import datetime
import subprocess
import requests

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
LOGS_PATH = os.path.join(REPO_PATH, "../logs")
os.makedirs(LOGS_PATH, exist_ok=True)

FILENAME = os.path.join(LOGS_PATH, f"clima_blumenau_{datetime.date.today()}.txt")
LOG_FILE = os.path.join(REPO_PATH, "commit_diario.log")

def log_event(message):
    """Registra eventos no arquivo de log."""
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

def obter_clima():
    """Obtém as informações do clima de Blumenau."""
    try:
        response = requests.get("https://wttr.in/Blumenau?format=%l:+%c+%t")
        response.raise_for_status()
        return f"Local e Clima: {response.text.strip()}\nHora: {datetime.datetime.now()}\n"
    except requests.RequestException as e:
        error_message = f"Erro ao obter clima: {e}\nTimestamp: {datetime.datetime.now()}\n"
        log_event(error_message)
        return error_message

def adicionar_e_enviar_arquivo():
    """Adiciona o arquivo ao Git, faz o commit e envia ao repositório."""
    if datetime.datetime.now().weekday() in [5, 6]:
        log_event("Script não executado porque hoje é fim de semana.")
        return

    os.chdir(REPO_PATH)
    clima_info = obter_clima()

    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(clima_info)
    subprocess.run(["git", "pull", "--rebase"])
    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "add", LOG_FILE])
    subprocess.run(["git", "commit", "-m", f"Adicionado {os.path.basename(FILENAME)} com condições climáticas de Blumenau"])
    subprocess.run(["git", "push"])

    log_event(f"Arquivo {os.path.basename(FILENAME)} adicionado e enviado ao repositório!")

if __name__ == "__main__":
    log_event("Execução do script iniciada.")
    adicionar_e_enviar_arquivo()
