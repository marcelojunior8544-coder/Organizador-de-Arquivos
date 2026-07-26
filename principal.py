import os
import shutil

origem = '%userprofile%/Downloads'
regras = {
    'imagens':['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documentos':['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'compactados': ['.zip', '.rar', '.7z', '.tar'],
    'instaladores': ['.exe', '.msi']
}

def organizar(pasta):
    if not os.path.exists(origem):
        print('O caminho especificado não existe')
        return

    for arquivo in os.listdir(origem):
        caminho = os.path.join(origem, arquivo)

        if os.path.isdir(caminho):
            continue

        _, ext = os.path.splitext(arquivo)
        ext = ext.lower()

        destino = 'Outros'
        for pasta, extensoes in regras.items():
            if ext in extensoes:
                destino = pasta
                break

        pasta_destino = os.path.join(origem, destino)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        novo_caminho = os.path.join(pasta_destino, arquivo)
        shutil.move(caminho, novo_caminho)
        print(f'Movido: {arquivo} -> {destino}/')


if __name__ == '__main__':
    print('Iniciando organizador')
    organizar(origem)
    print('Pasta organizada')
