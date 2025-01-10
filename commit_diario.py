import os
import datetime
import subprocess
import schedule
import time
import random

REPO_PATH = os.path.dirname(os.path.abspath(__file__))

CONTENT = "Contribuição automática em " + str(datetime.date.today())

FILENAME = f"contrib_{datetime.date.today()}.txt"

LOG_FILE = "commit_diario.log"

def log_event(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

def adicionar_e_enviar_arquivo():
    os.chdir(REPO_PATH)

    with open(FILENAME, "w") as file:
        file.write(CONTENT)

    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "add", LOG_FILE])
    subprocess.run(["git", "commit", "-m", f"Adicionado {FILENAME} e atualizado log"])
    subprocess.run(["git", "push"])

    log_event(f"Arquivo {FILENAME} adicionado e enviado ao repositório!")

log_event("Início do script.")

def tarefa_aleatoria():
    if random.random() > 0.25:
        adicionar_e_enviar_arquivo()

schedule.every().day.at("09:07").do(tarefa_aleatoria)
schedule.every(2).hours.do(tarefa_aleatoria)

while True:
    schedule.run_pending()
    time.sleep(1)
