import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xls", ".csv"],
    "executaveis": [".exe", ".bat"],
    "python": [".py"],
    "pdfs": [".pdf"],
    "rar": [".rar"],
    "reg": [".reg"],
}

for arquivo in lista_arquivos:
    # 01. ARquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")