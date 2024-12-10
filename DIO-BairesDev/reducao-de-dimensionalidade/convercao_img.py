from PIL import Image

def ppm_to_png_jpg(ppm_file, png_file, jpg_file):
    """Converte uma imagem PPM para PNG e JPG usando Pillow."""
    # Abrir a imagem PPM com Pillow
    with open(ppm_file, 'rb') as f:
        img = Image.open(f)
        img = img.convert('RGB')  # Garantir que está no formato RGB
    
    # Salvar como PNG
    img.save(png_file, 'PNG')
    print(f"Imagem salva como PNG: {png_file}")
    
    # Salvar como JPG
    img.save(jpg_file, 'JPEG')
    print(f"Imagem salva como JPG: {jpg_file}")

# Exemplo de uso
gray_ppm = "imagem_gray.ppm"
bw_ppm = "imagem_bw.ppm"

# Convertendo tons de cinza
ppm_to_png_jpg(gray_ppm, "imagem_gray.png", "imagem_gray.jpg")

# Convertendo preto e branco
ppm_to_png_jpg(bw_ppm, "imagem_bw.png", "imagem_bw.jpg")
