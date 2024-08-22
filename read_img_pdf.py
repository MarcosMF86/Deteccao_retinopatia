import fitz  # PyMuPDF
import io
from PIL import Image
import os

def extrair_imagens_de_pdf(pdf_path, output_folder):
    # Abrir o arquivo PDF
    documento = fitz.open(pdf_path)
    # Iterar pelas páginas do PDF
    for numero_pagina in range(len(documento)):
        pagina = documento.load_page(numero_pagina)
        imagens = pagina.get_images(full=True)

        # Iterar sobre todas as imagens encontradas
        for i, img in enumerate(imagens):
            xref = img[0]
            # Extrair o objeto de imagem
            base_image = documento.extract_image(xref)
            imagem_bytes = base_image["image"]

            # Nome do arquivo de saída
            #nome_imagem = f"pagina_{numero_pagina+1}_imagem_{i+1}.{base_image['ext']}"
            nome_imagem = 

            caminho_completo = f"{output_folder}/{nome_imagem}"

            # Salvar a imagem extraída
            with open(caminho_completo, "wb") as img_file:
                img_file.write(imagem_bytes)

            print(f"Imagem salva em: {caminho_completo}")

    documento.close()

# Exemplo de uso
pdf_path = "seu_arquivo.pdf"  # Substitua pelo caminho do seu arquivo PDF
output_folder = "imagens_extraidas"  # Pasta onde as imagens serão salvas
extrair_imagens_de_pdf(pdf_path, output_folder)
