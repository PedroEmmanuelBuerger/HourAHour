import os
import datetime
import subprocess

# Caminho do repositório local
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

# Conteúdo do arquivo de contribuição
CONTENT = "Contribuição automática em " + str(datetime.date.today())

# Nome do arquivo a ser criado
FILENAME = f"contrib_{datetime.date.today()}.txt"

def main():
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

if __name__ == "__main__":
    main()
