import os
import datetime
import subprocess
import schedule
import time

# Caminho do repositório local
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

# Conteúdo do arquivo de contribuição
CONTENT = "Contribuição automática em " + str(datetime.date.today())

# Nome do arquivo a ser criado
FILENAME = f"contrib_{datetime.date.today()}.txt"

def adicionar_e_enviar_arquivo():
    # Navegar até o repositório
    os.chdir(REPO_PATH)

    # Criar um novo arquivo com conteúdo
    with open(FILENAME, "w") as file:
        file.write(CONTENT)

    # Adicionar o arquivo ao controle de versão
    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "commit", "-m", f"Adicionado {FILENAME}"])
    subprocess.run(["git", "push"])

    print(f"Arquivo {FILENAME} adicionado e enviado ao repositório!")

# Agendar a execução para começar às 9:00 e repetir a cada 2 horas
schedule.every().day.at("09:00").do(adicionar_e_enviar_arquivo)
schedule.every(2).hours.do(adicionar_e_enviar_arquivo)  # Executa a cada 2 horas

while True:
    schedule.run_pending()  # Verifica se há tarefas pendentes
    time.sleep(1)  # Atraso de 1 segundo para evitar uso excessivo da CPU
