import os
import datetime
import subprocess
import schedule
import time
import requests

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
LOGS_PATH = os.path.join(REPO_PATH, "../logs")
os.makedirs(LOGS_PATH, exist_ok=True)

FILENAME = os.path.join(LOGS_PATH, f"clima_blumenau_{datetime.date.today()}.txt")
LOG_FILE = os.path.join(REPO_PATH, "commit_diario.log")

def log_event(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

def obter_clima():
    try:
        response = requests.get("https://wttr.in/Blumenau?format=%l:+%c+%t")
        response.raise_for_status()
        return f"Local e Clima: {response.text.strip()}\nHora: {datetime.datetime.now()}\n"
    except requests.RequestException as e:
        log_event(f"Erro ao obter clima: {e}")
        return "Erro ao obter informações do clima."

def adicionar_e_enviar_arquivo():
    os.chdir(REPO_PATH)
    clima_info = obter_clima()

    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(clima_info)

    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "add", LOG_FILE])
    subprocess.run(["git", "commit", "-m", f"Adicionado {os.path.basename(FILENAME)} com condições climáticas de Blumenau"])
    subprocess.run(["git", "push"])

    log_event(f"Arquivo {os.path.basename(FILENAME)} adicionado e enviado ao repositório!")

log_event("Início do script.")

def tarefa_aleatoria():
    adicionar_e_enviar_arquivo()

schedule.every().day.at("08:00").do(tarefa_aleatoria)
schedule.every(1).hours.do(tarefa_aleatoria)

while True:
    schedule.run_pending()
    time.sleep(1)
